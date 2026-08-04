---
description: Pre-market drift check — computes current vs target weights and today's buildout plan
---

You are running the pre-market drift-check workflow (local mode —
credentials come from .env). Resolve today's date via:
DATE=$(date +%Y-%m-%d).

STEP 0 — Safety check: if a file named HALT exists at the repo root, tell
the user and stop. Run `bash scripts/alpaca.sh clock` — if the market is
closed today (holiday), tell the user; ask whether to proceed anyway
before doing any drift computation (local ad-hoc runs may legitimately
want to check on a closed day).

STEP 1 — Read memory for context:
- memory/TARGET-PORTFOLIO.json (the target weights)
- memory/TRADING-STRATEGY.md
- python3 scripts/memory_log.py recent memory/TRADE-LOG.md --days 5
- python3 scripts/memory_log.py recent memory/RESEARCH-LOG.md --days 5

STEP 2 — Pull live account state:
  bash scripts/alpaca.sh account
  bash scripts/alpaca.sh positions
  bash scripts/alpaca.sh orders

STEP 3 — Compute drift. For every symbol in memory/TARGET-PORTFOLIO.json:
actual %, gap vs target, and (for ramp symbols) whether today's 1%
allowance is already used. Flag any zero-position symbol with a nonzero
target as a gap needing buyback. This is not catalyst research — skip
Perplexity unless something looks genuinely broken (halted symbol,
missing stop) and needs outside context to describe.

STEP 4 — Write a dated entry to memory/RESEARCH-LOG.md (match the
template): account snapshot, drift table, gaps needing attention, planned
action for market-open, decision (BUILDOUT / TOP-UP / HOLD).
Then run:
  python3 scripts/memory_log.py archive memory/RESEARCH-LOG.md --keep-days 5

STEP 5 — Notification: silent unless urgent.
  bash scripts/clickup.sh "<one line>"
