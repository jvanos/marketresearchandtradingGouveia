---
description: Midday stop-loss scan — cuts losers and tightens stops on winners
---

You are running the midday stop-loss scan workflow (local mode —
credentials come from .env). Resolve today's date via:
DATE=$(date +%Y-%m-%d).

STEP 0 — Safety check: if a file named HALT exists at the repo root, tell
the user — you may still cut losers/close positions if asked explicitly,
but do not open new positions. Run `bash scripts/alpaca.sh clock` — if the
market is closed, tell the user and stop.

STEP 1 — Read memory:
- memory/TARGET-PORTFOLIO.json (target weights)
- memory/TRADING-STRATEGY.md (exit rules)
- tail of memory/TRADE-LOG.md (entries, stops)

STEP 2 — Pull current state:
  bash scripts/alpaca.sh positions
  bash scripts/alpaca.sh orders

STEP 3 — Cut losers immediately. For every position where
unrealized_plpc <= -0.07:
  bash scripts/alpaca.sh close SYM
(the wrapper cancels the symbol's open orders before closing — no separate
cancel step needed.) Log the exit: exit price, realized P&L, "cut at -7%".
Note the resulting zero-position gap for the NEXT market-open to fill —
don't rebuy same session.

STEP 4 — Tighten trailing stops on winners. Cancel the old stop, place a
new one: up >= +20% -> trail_percent "5"; up >= +15% -> trail_percent "7".
Never tighten within 3% of current price. Never move a stop down. Confirm
the replacement was accepted — flag loudly if a position ends up with no
open stop order.

STEP 5 — Stop-integrity check. Every open position should have a live
stop order — if not, place a 10% trailing stop GTC now and flag it
loudly. There's no thesis check in this strategy — a passive holding has
no discretionary thesis to break intraday.

STEP 6 — Notification: only if action was taken.
  bash scripts/clickup.sh "<action summary>"
