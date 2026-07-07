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

---

## 2026-07-07 — Pre-market Drift Check

### Account
- Equity: $50,000.00 | Cash: $50,000.00 | Buying power: $200,000.00
- No open positions; no open orders. Account still 100% cash — the Day 0
  (07-05) buildout was planned but never executed (no fills, no orders on
  record).

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO   | 23.8   | 0 | 23.8   | yes | no |
| SCHD  | 19.9   | 0 | 19.9   | yes | no |
| BTC   | 11.1   | 0 | 11.1   | yes | no |
| SGOV  | 9.3    | 0 | 9.3    | yes | no |
| QQQM  | 7.8    | 0 | 7.8    | yes | no |
| SCHG  | 7.4    | 0 | 7.4    | yes | no |
| SPMO  | 5.6    | 0 | 5.6    | yes | no |
| VTV   | 2.6    | 0 | 2.6    | yes | no |
| BRK.B | 2.6    | 0 | 2.6    | yes | no |
| MSFT  | 1.7    | 0 | 1.7    | no  | n/a |
| VGT   | 1.3    | 0 | 1.3    | no  | n/a |
| ETH   | 1.2    | 0 | 1.2    | no  | n/a |
| GOOGL | 1.1    | 0 | 1.1    | no  | n/a |
| VXUS  | 0.9    | 0 | 0.9    | no  | n/a |
| SOFI  | 0.6    | 0 | 0.6    | no  | n/a |
| PLTR  | 0.4    | 0 | 0.4    | no  | n/a |
| GXRP  | 0.3    | 0 | 0.3    | no  | n/a |
| APLD  | 0.2    | 0 | 0.2    | no  | n/a |
| IREN  | 0.2    | 0 | 0.2    | no  | n/a |
| NBIS  | 0.2    | 0 | 0.2    | no  | n/a |
| AMZN  | 0.2    | 0 | 0.2    | no  | n/a |
| META  | 0.2    | 0 | 0.2    | no  | n/a |
| IONQ  | 0.1222 | 0 | 0.1222 | no  | n/a |
| RGTI  | 0.1222 | 0 | 0.1222 | no  | n/a |
| QBTS  | 0.1222 | 0 | 0.1222 | no  | n/a |
| UNH   | 0.1222 | 0 | 0.1222 | no  | n/a |
| DRAM  | 0.1222 | 0 | 0.1222 | no  | n/a |
| WULF  | 0.1222 | 0 | 0.1222 | no  | n/a |
| CIFR  | 0.1222 | 0 | 0.1222 | no  | n/a |
| GLXY  | 0.1222 | 0 | 0.1222 | no  | n/a |
| RIOT  | 0.1222 | 0 | 0.1222 | no  | n/a |

Cash target 0.3% (ADA/GADA placeholder) left uninvested per portfolio note.

### Gaps Needing Attention
- None from stop-losses (nothing has ever been held). Whole portfolio is a
  fresh underweight buildout, not a re-entry.

### Planned Action for Market-Open
- Immediate positions (target < 2%): buy full target in one order each —
  MSFT $850, VGT $650, ETH $600, GOOGL $550, VXUS $450, SOFI $300,
  PLTR $200, GXRP $150, APLD/IREN/NBIS/AMZN/META $100 each, 9 spec-basket
  names ~$61.10 each. (~$4,800 total.)
- Ramp positions (target >= 2%): buy $500 (1% of $50k equity) each —
  VOO, SCHD, BTC, SGOV, QQQM, SCHG, SPMO, VTV, BRK.B. (~$4,500 total.)
- Day-1 buildout ≈ $9,300; ramps continue daily until each hits target.
- Set 10% trailing-stop GTC on each new position at market-open.

### Decision
BUILDOUT — full portfolio buildout at next open per the ramp rule.
