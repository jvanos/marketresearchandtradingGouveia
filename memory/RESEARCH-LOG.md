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
- Equity: $50,000.00 | Cash: $50,000.00 | Buying power: $200,000.00 (4x margin)
- No open positions, no open orders

### Drift vs. Target
First trading day after 2026-07-05 Day-0 baseline; buildout not yet begun,
so every symbol is fully underweight (gap = target − 0). Today's 1% ramp
allowance unused for all ramp symbols.

| Ticker | Target % | Actual % | Gap | Ramp? | Allowance Used |
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
| MSFT  | 1.7    | 0 | 1.7    | no  | — |
| VGT   | 1.3    | 0 | 1.3    | no  | — |
| ETH   | 1.2    | 0 | 1.2    | no  | — |
| GOOGL | 1.1    | 0 | 1.1    | no  | — |
| VXUS  | 0.9    | 0 | 0.9    | no  | — |
| SOFI  | 0.6    | 0 | 0.6    | no  | — |
| PLTR  | 0.4    | 0 | 0.4    | no  | — |
| GXRP  | 0.3    | 0 | 0.3    | no  | — |
| APLD  | 0.2    | 0 | 0.2    | no  | — |
| IREN  | 0.2    | 0 | 0.2    | no  | — |
| NBIS  | 0.2    | 0 | 0.2    | no  | — |
| AMZN  | 0.2    | 0 | 0.2    | no  | — |
| META  | 0.2    | 0 | 0.2    | no  | — |
| IONQ  | 0.1222 | 0 | 0.1222 | no  | — |
| RGTI  | 0.1222 | 0 | 0.1222 | no  | — |
| QBTS  | 0.1222 | 0 | 0.1222 | no  | — |
| UNH   | 0.1222 | 0 | 0.1222 | no  | — |
| DRAM  | 0.1222 | 0 | 0.1222 | no  | — |
| WULF  | 0.1222 | 0 | 0.1222 | no  | — |
| CIFR  | 0.1222 | 0 | 0.1222 | no  | — |
| GLXY  | 0.1222 | 0 | 0.1222 | no  | — |
| RIOT  | 0.1222 | 0 | 0.1222 | no  | — |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- None from stop-losses (no positions have ever been held). All gaps are
  Day-0 buildout gaps, not corrections.

### Planned Action for Market-Open
- Non-ramp (target < 2%): buy full target in one order each — MSFT $850,
  VGT $650, ETH $600, GOOGL $550, VXUS $450, SOFI $300, PLTR $200,
  GXRP $150, APLD/IREN/NBIS/AMZN/META $100 each, and the 9 speculative
  names (IONQ, RGTI, QBTS, UNH, DRAM, WULF, CIFR, GLXY, RIOT) ~$61 each.
- Ramp (target >= 2%): buy up to 1% of equity ($500) today for each of
  VOO, SCHD, BTC, SGOV, QQQM, SCHG, SPMO, VTV, BRK.B. Continues daily
  until each reaches target.

### Decision
BUILDOUT — begin first buildout at today's market-open per the ramp rule.
