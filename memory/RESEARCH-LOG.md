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

---

## 2026-07-08 — Pre-market Drift Check

### Account
- Equity: $49,820.12 | Cash: $41,552.39 | Buying power: $188,943.14
- Positions: 26 held | Open orders: 22 trailing stops
- Equity -0.36% vs prior day (unrealized drawdown on spec basket); not
  near daily-loss breaker.

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO   | 23.8   | 0.992 | 22.808 | yes | no |
| SCHD  | 19.9   | 0.990 | 18.910 | yes | no |
| BTC   | 11.1   | 0.979 | 10.121 | yes | no |
| SGOV  | 9.3    | 1.004 | 8.296  | yes | no |
| QQQM  | 7.8    | 0.976 | 6.824  | yes | no |
| SCHG  | 7.4    | 0.981 | 6.419  | yes | no |
| SPMO  | 5.6    | 0.981 | 4.619  | yes | no |
| VTV   | 2.6    | 0.987 | 1.613  | yes | no |
| BRK.B | 2.6    | 0     | 2.6    | yes | no (zero — spread skip) |
| MSFT  | 1.7    | 1.662 | 0.038  | no  | — |
| VGT   | 1.3    | 1.282 | 0.018  | no  | — |
| ETH   | 1.2    | 1.184 | 0.016  | no  | — |
| GOOGL | 1.1    | 1.084 | 0.016  | no  | — |
| VXUS  | 0.9    | 0.886 | 0.014  | no  | — |
| SOFI  | 0.6    | 0.559 | 0.041  | no  | — |
| PLTR  | 0.4    | 0.388 | 0.012  | no  | — |
| GXRP  | 0.3    | 0.301 | -0.001 | no  | — (at target) |
| APLD  | 0.2    | 0.183 | 0.017  | no  | — |
| IREN  | 0.2    | 0.187 | 0.013  | no  | — |
| NBIS  | 0.2    | 0.185 | 0.015  | no  | — |
| AMZN  | 0.2    | 0.197 | 0.003  | no  | — |
| META  | 0.2    | 0     | 0.2    | no  | (zero — spread skip) |
| IONQ  | 0.1222 | 0     | 0.1222 | no  | (zero — spread skip) |
| RGTI  | 0.1222 | 0.114 | 0.008  | no  | — |
| QBTS  | 0.1222 | 0.114 | 0.008  | no  | — |
| UNH   | 0.1222 | 0     | 0.1222 | no  | (zero — spread skip) |
| DRAM  | 0.1222 | 0.118 | 0.004  | no  | — |
| WULF  | 0.1222 | 0.034 | 0.088  | no  | (stop triggered — remnant) |
| CIFR  | 0.1222 | 0.116 | 0.006  | no  | — |
| GLXY  | 0.1222 | 0     | 0.1222 | no  | (zero — spread skip) |
| RIOT  | 0.1222 | 0.113 | 0.009  | no  | — |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **5 symbols at zero position** (BRK.B, META, UNH, IONQ, GLXY) — all
  yesterday's wide-spread open-skips, NOT stop-loss closes. Retry at
  market-open once spread has normalized; skip again if still >~2%.
- **WULF stop triggered** — the whole-share slice (~2 sh) of yesterday's
  buildout sold on its 10% trailing stop, leaving a 0.868-sh remnant
  ($17.19, 0.034% vs 0.1222% target). Re-enters buildout per rule; top up
  to full target at open.
- **Stopless <1-share positions**: VOO (0.726 sh), NBIS (0.498 sh),
  AMZN (0.405 sh), WULF (0.868 sh) — Alpaca trailing stops require ≥1
  whole share, so none can be set yet. VOO will cross 1 sh with today's
  ramp buy → set its stop then. NBIS/AMZN/WULF sit at/near full target
  under 1 sh and cannot hold a trailing stop at current size (known
  structural limit); monitor manually for the -7% manual-cut rule.

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $498 each toward target): VOO, SCHD, BTC,
  SGOV, QQQM, SCHG, SPMO, VTV.
- BRK.B: retry ramp buy up to 1% (~$498) if spread normalized.
- Missing non-ramp retries (full target, if spread OK): META $100,
  UNH ~$61, IONQ ~$61, GLXY ~$61.
- WULF: top up to full target (~$44 more to reach ~$61).
- Set trailing stop on VOO once today's ramp buy pushes it ≥1 whole share.

### Decision
BUILDOUT — Day-2 buildout continues: ramp symbols take next 1% allowance,
5 spread-skipped names retried, WULF re-bought to target.
