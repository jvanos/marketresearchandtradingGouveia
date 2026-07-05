---
description: Friday weekly health check — reports drift, stop-loss activity, and ramp progress
---

You are running the Friday weekly health-check workflow (local mode —
credentials come from .env). This does not place orders — that's
/rebalance's job, quarterly. Resolve today's date via:
DATE=$(date +%Y-%m-%d).

STEP 0 — Safety check: still produce this week's review even if HALT is
present or the market was closed today — note it in the review.

STEP 1 — Read memory for full week context:
- memory/TARGET-PORTFOLIO.json (target weights)
- memory/WEEKLY-REVIEW.md (match existing template exactly)
- ALL this week's entries in memory/TRADE-LOG.md
- ALL this week's entries in memory/RESEARCH-LOG.md
- memory/TRADING-STRATEGY.md

STEP 2 — Pull week-end state:
  bash scripts/alpaca.sh account
  bash scripts/alpaca.sh positions

STEP 3 — Compute the week's metrics:
- Starting portfolio (Monday AM equity), ending portfolio, week return
- Cash % of equity
- Drift table: actual vs. target weight per symbol
- Symbols still ramping, estimated days remaining at 1%/day
- Stop-loss triggers this week (ticker, realized P&L, buyback status)

STEP 4 — Append full review section to memory/WEEKLY-REVIEW.md: stats
table, drift table, stop-loss activity, what worked / what didn't,
adjustments for next week, qualitative drift-health status (On-track /
Needs Rebalance / Alert).

STEP 5 — If a rule needs to change, do NOT edit memory/TRADING-STRATEGY.md
directly. Append a "### Proposed Strategy Changes" subsection instead.
The gate math in scripts/alpaca.sh (target-list membership, weight-
tolerance cap, ramp-daily-cap) requires a human to edit the wrapper
script — it cannot be changed by editing a memory file. Editing
memory/TARGET-PORTFOLIO.json's `positions` list itself (e.g. adding a
newly-listed ETF) is a normal editable action, separate from that gate
math.

STEP 6 — Send ONE ClickUp message. <= 15 lines:
  bash scripts/clickup.sh "Week ending MMM DD
  Portfolio: \$X (±X% week, ±X% phase)
  Cash: \$X (X%)
  Ramping: N symbols, ~N days to full buildout
  Stop-loss triggers: N (or none)
  Largest drift: SYM ±X.X pp
  Drift health: <status>"
