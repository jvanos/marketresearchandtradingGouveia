# Research Log (Daily Drift Check)

This bot no longer researches trade catalysts — it passively tracks
memory/TARGET-PORTFOLIO.json. Daily pre-market entries are appended here
as a drift-status check, not a market-research log.

Format each entry:

## YYYY-MM-DD — Pre-market Drift Check

### Account
- Equity: $X
- Cash: $X
- Buying power: $X

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|

### Gaps Needing Attention
- Any target-list symbol at zero position with nonzero target (e.g. from
  a stop-loss trigger) — flag for market-open to buy back per the normal
  buildout/ramp rule.

### Planned Action for Market-Open
- List of symbols to buy today and how much (full target for immediate
  positions still underweight, up to 1% of equity for ramp positions
  still underweight).

### Decision
BUILDOUT / TOP-UP / HOLD (HOLD only once every symbol is within tolerance
of its target)

---

## 2026-07-05 — Pre-market Drift Check (Day 0)

### Account
- Equity: $50,000.00 | Cash: $50,000.00 | Buying power: $50,000.00 (paper
  account reset for strategy relaunch)
- No open positions

### Drift vs. Target
Every symbol on memory/TARGET-PORTFOLIO.json is fully underweight (target
minus zero). See that file for the full list and weights.

### Gaps Needing Attention
None yet — this is Day 0, not a stop-triggered gap.

### Planned Action for Market-Open
- Immediate positions (target_pct < 2%): buy full target in one order
  each — MSFT, VGT, ETH, GOOGL, VXUS, SOFI, PLTR, GXRP, APLD, IREN, NBIS,
  AMZN, META, and the 9 speculative-basket names.
- Ramp positions (target_pct >= 2%): buy up to 1% of equity today for
  each — VOO, SCHD, BTC, SGOV, QQQM, SCHG, SPMO, VTV, BRK.B. Continues
  daily until each reaches target.

### Decision
BUILDOUT — begin today per the ramp rule in memory/TRADING-STRATEGY.md.
