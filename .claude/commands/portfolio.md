---
description: Read-only snapshot of account, positions, open orders, stops, and drift vs target
---

Print a clean ad-hoc snapshot. No state changes, no orders, no file writes.

1. bash scripts/alpaca.sh account
2. bash scripts/alpaca.sh positions
3. bash scripts/alpaca.sh orders
4. Read memory/TARGET-PORTFOLIO.json

Format the output as a single concise summary:

Portfolio — <today's date>
Equity: $X | Cash: $X (X%) | Buying power: $X

Positions:
  SYM | Sh | Entry -> Now | Unrealized P&L | Stop | Target % | Actual % | Gap

Open orders:
  TYPE | SYM | qty | trail/stop | order_id

No commentary unless something is broken: a position without a stop, a
stop below current price, or a held position that isn't on
memory/TARGET-PORTFOLIO.json at all (shouldn't be possible through the
wrapper, but worth flagging if seen — it means something bypassed the
gate).
