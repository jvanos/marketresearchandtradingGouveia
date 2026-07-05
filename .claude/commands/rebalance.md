---
description: Quarterly rebalance — trims overweight positions and tops up underweight ones back to target
---

You are running the quarterly rebalance workflow (local mode —
credentials come from .env). This is the only workflow that trims
overweight positions — daily/weekly routines only ever buy toward target.
Resolve today's date via: DATE=$(date +%Y-%m-%d).

STEP 0 — Safety check: if a file named HALT exists at the repo root, tell
the user and do not trim or buy anything — you may still compute and show
the drift report. Run `bash scripts/alpaca.sh clock` — if the market is
closed, tell the user; ask whether to just show the drift report anyway.

STEP 1 — Read memory:
- memory/TARGET-PORTFOLIO.json (target weights, ramp flags)
- memory/TRADING-STRATEGY.md
- memory/REBALANCE-LOG.md (match existing template exactly)
- tail of memory/TRADE-LOG.md

STEP 2 — Pull live state:
  bash scripts/alpaca.sh account
  bash scripts/alpaca.sh positions
  bash scripts/alpaca.sh orders

STEP 3 — Compute pre-rebalance drift for every target symbol (actual %
vs target %, gap), including zero-position symbols with nonzero targets.

STEP 4 — Trim overweight positions FIRST. For each symbol above
target_pct + tolerance: cancel its trailing stop, sell the excess back to
target (qty-based), re-place a trailing stop sized to the new qty —
confirm the new stop isn't looser than the old one before cancelling it
(never move a stop down). Log shares sold, price, realized P&L, new stop.

STEP 5 — Buy underweight positions. Ramp symbols (target >= 2%) buy up to
1% of equity via the normal wrapper call — no bypass of the daily ramp
cap even here; excess catch-up continues on subsequent market-open runs.
Immediate symbols (target < 2%) buy the full remaining gap. Place a 10%
trailing stop GTC after each new fill. Log rejections and move on without
retrying a workaround.

STEP 6 — Re-pull state and compute post-rebalance drift.

STEP 7 — Append the full entry to memory/REBALANCE-LOG.md: pre/post
weights, trims, top-ups, gap-fills, ramp-status summary.

STEP 8 — Notification (always send one — quarterly cadence, silence here
is a bigger flag than on a daily routine):
  bash scripts/clickup.sh "Quarterly rebalance $DATE
  Trimmed: <tickers or none>
  Bought: <tickers or none>
  Still ramping: N symbols
  Largest remaining drift: SYM ±X.X pp"
