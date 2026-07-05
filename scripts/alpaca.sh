#!/usr/bin/env bash
# Alpaca API wrapper. All trading API calls go through here.
# Usage: bash scripts/alpaca.sh <subcommand> [args...]
#
# This bot passively tracks a fixed target portfolio (memory/TARGET-
# PORTFOLIO.json) rather than picking its own trades. BUY orders are gated
# in code (not left to the calling prompt): symbol must look like a plain
# equity ticker (no options/derivatives), symbol must be on the approved
# target-portfolio list (memory/TARGET-PORTFOLIO.json -- read fresh on every
# order, fail closed if missing/malformed), resulting position weight must
# not exceed that symbol's target_pct plus a small relative tolerance, ramp
# positions (target_pct >= 2%) are additionally capped to +1% of equity in
# filled buys per calendar day (UTC), cost <= live buying_power, cost <=
# cash, and a daily-loss circuit breaker. The weight-tolerance and ramp-cap
# numbers are hardcoded below (not env-configurable) so a bad prompt or a
# casual .env edit can't loosen them -- only a deliberate edit to this file
# can, same protection level the old hardcoded 20%/6-position/8-trades
# limits had. The PDT day-trade-count rule is being phased out (SEC-approved
# Apr 2026, effective Jun 2026, brokerages have until Oct 2027 to fully
# implement) so this wrapper deliberately checks live `buying_power` instead
# of hardcoding a day-trade formula -- Alpaca computes that field correctly
# under whatever margin rules currently apply.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/.env"
TARGET_FILE="$ROOT/memory/TARGET-PORTFOLIO.json"

# Hardcoded safety constants -- deliberately NOT sourced from .env. See the
# header comment above for why these live here instead of env.template.
RAMP_DAILY_CAP_PCT="1.0"
WEIGHT_TOLERANCE_RELATIVE_PCT="0.10"
WEIGHT_TOLERANCE_FLOOR_PP="0.03"
WEIGHT_TOLERANCE_CEILING_PP="1.0"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

: "${ALPACA_API_KEY:?ALPACA_API_KEY not set in environment}"
: "${ALPACA_SECRET_KEY:?ALPACA_SECRET_KEY not set in environment}"

API="${ALPACA_ENDPOINT:-https://api.alpaca.markets/v2}"
DATA="${ALPACA_DATA_ENDPOINT:-https://data.alpaca.markets/v2}"
MAX_DAILY_LOSS_PCT="${MAX_DAILY_LOSS_PCT:-0.05}"

H_KEY="APCA-API-KEY-ID: $ALPACA_API_KEY"
H_SEC="APCA-API-SECRET-KEY: $ALPACA_SECRET_KEY"

cmd="${1:-}"
shift || true

case "$cmd" in
  account)
    curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/account"
    ;;
  positions)
    curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/positions"
    ;;
  position)
    sym="${1:?usage: position SYM}"
    curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/positions/$sym"
    ;;
  quote)
    sym="${1:?usage: quote SYM}"
    curl -fsS -H "$H_KEY" -H "$H_SEC" "$DATA/stocks/$sym/quotes/latest"
    ;;
  orders)
    status="${1:-open}"
    curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/orders?status=$status"
    ;;
  clock)
    curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/clock"
    ;;
  order)
    body="${1:?usage: order '<json>'}"
    side="$(python3 -c "import json,sys; print(json.loads(sys.argv[1]).get('side',''))" "$body")"
    symbol="$(python3 -c "import json,sys; print(json.loads(sys.argv[1]).get('symbol',''))" "$body")"

    if [[ "$side" == "buy" ]]; then
      # Cheapest check first, no network required: this wrapper has no code
      # path that can construct an options order, so reject anything that
      # isn't a plain equity ticker before making any API calls. Allows an
      # optional single-letter/two-letter share-class suffix (e.g. BRK.B).
      if [[ ! "$symbol" =~ ^[A-Z]{1,5}(\.[A-Z]{1,2})?$ ]]; then
        echo "ORDER REJECTED: symbol '$symbol' does not look like a plain equity ticker -- no options/derivatives through this wrapper" >&2
        exit 2
      fi

      # Fail closed: no target file, or a target file that doesn't parse,
      # means there is no way to validate this order -- refuse rather than
      # fall open. This file is the single source of truth for what this
      # bot is allowed to hold and at what weight.
      if [[ ! -f "$TARGET_FILE" ]]; then
        echo "ORDER REJECTED: memory/TARGET-PORTFOLIO.json not found -- refusing to validate any buy without it" >&2
        exit 2
      fi
      if ! target_json="$(python3 -c "import json,sys; json.load(open(sys.argv[1])); print(open(sys.argv[1]).read())" "$TARGET_FILE" 2>/dev/null)"; then
        echo "ORDER REJECTED: memory/TARGET-PORTFOLIO.json does not parse as JSON -- refusing to validate any buy" >&2
        exit 2
      fi

      account_json="$(curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/account")"
      positions_json="$(curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/positions")"
      today_utc="$(python3 -c "import datetime; print(datetime.datetime.now(datetime.timezone.utc).date().isoformat())")"
      orders_json="$(curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/orders?status=all&symbols=$symbol&after=${today_utc}T00:00:00Z&direction=asc&limit=500")"
      quote_json="$(curl -fsS -H "$H_KEY" -H "$H_SEC" "$DATA/stocks/$symbol/quotes/latest" || echo '{}')"

      gate_result="$(python3 -c "
import json, sys, datetime

order, account, positions, orders, quote, target = (json.loads(a) for a in sys.argv[1:7])
max_daily_loss_pct = float(sys.argv[7])
ramp_daily_cap_pct = float(sys.argv[8])
tol_relative = float(sys.argv[9])
tol_floor_pp = float(sys.argv[10])
tol_ceiling_pp = float(sys.argv[11])

symbol = order.get('symbol', '')

def reject(msg):
    print('REJECT: ' + msg)
    sys.exit(0)

by_symbol = {p['symbol']: p for p in target.get('positions', [])}
tgt = by_symbol.get(symbol)
if tgt is None:
    reject(f\"'{symbol}' is not on the approved target-portfolio list \"
           f'(memory/TARGET-PORTFOLIO.json) -- no discretionary buys')

target_pct = float(tgt['target_pct'])
is_ramp = bool(tgt.get('ramp', False))

equity = float(account.get('equity', 0))
cash = float(account.get('cash', 0))
buying_power = float(account.get('buying_power', 0))
last_equity = float(account.get('last_equity', 0))
if equity <= 0:
    reject('could not read a positive account equity')

limit_price = order.get('limit_price')
price = float(limit_price) if limit_price else float(
    quote.get('quote', {}).get('ap', 0) or quote.get('quote', {}).get('bp', 0) or 0)

notional = order.get('notional')
if notional is not None:
    cost = float(notional)
else:
    qty = float(order.get('qty', 0) or 0)
    if price <= 0:
        reject('could not determine a price for cost checks (bad/halted quote)')
    cost = qty * price
if cost <= 0:
    reject('order has no positive cost (bad qty/notional)')

current_mv = next((float(p.get('market_value', 0) or 0)
                    for p in positions if p.get('symbol') == symbol), 0.0)

resulting_pct = (current_mv + cost) / equity * 100.0
tol_pp = min(max(tol_relative * target_pct, tol_floor_pp), tol_ceiling_pp)
cap_pct = target_pct + tol_pp
if resulting_pct > cap_pct:
    reject(f'resulting {symbol} weight ~{resulting_pct:.3f}% would exceed '
           f'target {target_pct:.3f}% + tolerance {tol_pp:.3f}pp (cap {cap_pct:.3f}%)')

if is_ramp:
    today_utc = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    filled_today = sum(
        float(o.get('filled_avg_price') or 0) * float(o.get('filled_qty') or 0)
        for o in orders
        if o.get('symbol') == symbol and o.get('side') == 'buy'
        and o.get('filled_at') and o['filled_at'][:10] == today_utc
    )
    ramp_cap = ramp_daily_cap_pct / 100.0 * equity
    if filled_today + cost > ramp_cap + 1e-9:
        reject(f\"{symbol} is a ramp position: today's filled buys \"
               f'(\${filled_today:.2f}) + this order (\${cost:.2f}) would exceed the '
               f'{ramp_daily_cap_pct:.2f}%/day ramp allowance (\${ramp_cap:.2f})')

if cost > cash:
    reject(f'order cost ~\${cost:.2f} exceeds available cash (\${cash:.2f})')
if cost > buying_power:
    reject(f'order cost ~\${cost:.2f} exceeds live buying_power (\${buying_power:.2f})')

if last_equity > 0:
    loss_pct = (last_equity - equity) / last_equity
    if loss_pct >= max_daily_loss_pct:
        reject(f'daily loss circuit breaker tripped (down {loss_pct:.1%} from last close, threshold {max_daily_loss_pct:.0%}) -- no new buys until tomorrow')

print('OK')
" "$body" "$account_json" "$positions_json" "$orders_json" "$quote_json" "$target_json" \
        "$MAX_DAILY_LOSS_PCT" "$RAMP_DAILY_CAP_PCT" "$WEIGHT_TOLERANCE_RELATIVE_PCT" \
        "$WEIGHT_TOLERANCE_FLOOR_PP" "$WEIGHT_TOLERANCE_CEILING_PP")"

      if [[ "$gate_result" != "OK" ]]; then
        echo "ORDER REJECTED: ${gate_result#REJECT: }" >&2
        exit 2
      fi
    fi

    curl -fsS -H "$H_KEY" -H "$H_SEC" -H "Content-Type: application/json" \
      -X POST -d "$body" "$API/orders"
    ;;
  cancel)
    oid="${1:?usage: cancel ORDER_ID}"
    curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/orders/$oid"
    ;;
  cancel-all)
    curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/orders"
    ;;
  close)
    sym="${1:?usage: close SYM}"
    # Alpaca reserves shares against open sell orders, so cancel the
    # symbol's open orders (e.g. its trailing stop) before closing --
    # closing first and cancelling after gets the close rejected.
    open_orders="$(curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/orders?status=open&symbols=$sym")"
    echo "$open_orders" | python3 -c "
import json, sys
for o in json.load(sys.stdin):
    print(o['id'])
" | while read -r oid; do
      [[ -n "$oid" ]] && curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/orders/$oid" >/dev/null
    done
    curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/positions/$sym"
    ;;
  close-all)
    curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/positions?cancel_orders=true"
    ;;
  *)
    echo "Usage: bash scripts/alpaca.sh <account|positions|position|quote|orders|clock|order|cancel|cancel-all|close|close-all> [args]" >&2
    exit 1
    ;;
esac
echo