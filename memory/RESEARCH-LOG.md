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

---

## 2026-07-17 — Pre-market Drift Check

### Account
- Equity: $49,624.00
- Cash: $21,381.31
- Buying power: $164,604.77

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO   | 23.8   | 6.977 | 16.823 | yes | no |
| SCHD  | 19.9   | 7.145 | 12.755 | yes | no |
| BTC   | 11.1   | 7.003 | 4.097  | yes | no |
| SGOV  | 9.3    | 7.023 | 2.277  | yes | no |
| QQQM  | 7.8    | 4.869 | 2.931  | yes | no |
| SCHG  | 7.4    | 6.980 | 0.420  | yes | no |
| SPMO  | 5.6    | 5.503 | 0.097  | yes | no |
| VTV   | 2.6    | 2.620 | -0.020 | yes | no (at target) |
| BRK.B | 2.6    | 0     | 2.600  | yes | no (ZERO — spread-skip, retry) |
| MSFT  | 1.7    | 1.743 | -0.043 | no  | — (at target) |
| VGT   | 1.3    | 1.302 | -0.002 | no  | — (at target) |
| ETH   | 1.2    | 1.256 | -0.056 | no  | — (at target) |
| GOOGL | 1.1    | 1.094 | 0.006  | no  | — (at target) |
| VXUS  | 0.9    | 0.886 | 0.014  | no  | — (at target) |
| SOFI  | 0.6    | 0.580 | 0.020  | no  | — (at target) |
| PLTR  | 0.4    | 0.407 | -0.007 | no  | — (at target) |
| GXRP  | 0.3    | 0.296 | 0.004  | no  | — (at target) |
| APLD  | 0.2    | 0.189 | 0.011  | no  | — (at target) |
| IREN  | 0.2    | 0     | 0.200  | no  | — (ZERO — liquidated 07-16, buyback) |
| NBIS  | 0.2    | 0     | 0.200  | no  | — (ZERO — liquidated 07-16, buyback) |
| AMZN  | 0.2    | 0.202 | -0.002 | no  | — (at target) |
| META  | 0.2    | 0.227 | -0.027 | no  | — (at target) |
| IONQ  | 0.1222 | 0.119 | 0.003  | no  | — (at target) |
| RGTI  | 0.1222 | 0     | 0.122  | no  | — (ZERO — liquidated 07-16, buyback) |
| QBTS  | 0.1222 | 0     | 0.122  | no  | — (ZERO — liquidated 07-16, buyback) |
| UNH   | 0.1222 | 0.123 | -0.001 | no  | — (at target) |
| DRAM  | 0.1222 | 0.116 | 0.006  | no  | — (at target) |
| WULF  | 0.1222 | 0.117 | 0.005  | no  | — (at target) |
| CIFR  | 0.1222 | 0.112 | 0.010  | no  | — (at target) |
| GLXY  | 0.1222 | 0.025 | 0.097  | no  | — (remnant — top up to target) |
| RIOT  | 0.1222 | 0     | 0.122  | no  | — (ZERO — liquidated 07-16, buyback) |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **ANOMALY — 5 hold-target positions liquidated after hours 07-16.** IREN,
  NBIS, RGTI, QBTS, RIOT are all at zero. Whole-share slices were
  legitimately stopped out during the 07-16 session (trailing stops fired
  on a broad spec/small-cap down day), BUT the fractional remnants were
  then sold to zero via `close`-style **market SELL orders submitted at
  17:07 ET — after the 16:00 close**, outside any scheduled routine
  (pre-market/market-open/midday all run during market hours;
  daily-summary is read-only). Source of the 17:07 liquidation is
  unexplained. Financial impact is small (~$300 total, all sub-0.2%
  names). Per strategy, all 5 re-enter the buildout queue and rebuy to
  full target at open — but flagging for human review in case a
  rogue/misfiring process is closing hold positions.
- **BRK.B still at zero** — ongoing wide-spread open-skip (not a stop).
  Retry ramp buy at open only if spread has normalized (<~2%); skip again
  otherwise.
- **GLXY remnant** — 0.025% vs 0.1222% target (0.571 sh, sub-1-share,
  scan-only, no trailing stop). Top up to full target at open.
- Core buildout still ~9 days in and far from target: VOO (gap 16.8%),
  SCHD (12.8%), QQQM (2.9%), SGOV (2.3%), BTC (4.1%) remain the big
  underweights. Cash 43.1% — plenty of dry powder, buildout on schedule.

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $496 each toward target, capped by gap):
  VOO $496, SCHD $496, BTC $496, SGOV $496, QQQM $496, SCHG ~$208 (gap).
  SPMO/VTV within tolerance — skip.
- BRK.B: retry ramp buy up to 1% (~$496) only if spread normalized.
- Buyback liquidated names to full target (all non-ramp, <2%, buy in full):
  IREN ~$99, NBIS ~$99, RGTI ~$61, QBTS ~$61, RIOT ~$61.
- GLXY: top up remnant to full target (~$48 more).
- Set/refresh trailing stops on any position that crosses ≥1 whole share
  after today's ramp buys (market-open routine handles this).
- **Caution flag for market-open**: rebuy the 5 liquidated names per the
  standard buildout rule, but if the 17:07 after-hours liquidation recurs
  tonight, escalate — do not loop rebuy→liquidate indefinitely.

### Decision
BUILDOUT — Core ramp continues (VOO/SCHD/QQQM/SGOV/BTC still deeply
underweight), 6 zero-position names rebuy per buildout rule. One anomaly
flagged: unexplained after-hours liquidation of 5 hold-target positions on
07-16 — surfaced for human review.

---

## 2026-07-22 — Pre-market Drift Check

### Account
- Equity: $50,063.84
- Cash: $13,842.63
- Buying power: $156,600.51

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO   | 23.8   | 9.92  | 13.89  | yes | none (0 fills) |
| SCHD  | 19.9   | 10.02 | 9.88   | yes | none (0 fills) |
| BTC   | 11.1   | 10.30 | 0.80   | yes | none (0 fills) |
| SGOV  | 9.3    | 9.29  | 0.01   | yes | — (at target) |
| QQQM  | 7.8    | 7.80  | 0.00   | yes | — (at target) |
| SCHG  | 7.4    | 7.35  | 0.05   | yes | — (at target) |
| SPMO  | 5.6    | 5.64  | -0.04  | yes | — (at target) |
| VTV   | 2.6    | 2.60  | 0.00   | yes | — (at target) |
| BRK.B | 2.6    | 0     | 2.60   | yes | — (ZERO — still unheld, wide-spread skip) |
| MSFT  | 1.7    | 1.75  | -0.05  | no  | — (at target) |
| VGT   | 1.3    | 1.31  | -0.01  | no  | — (at target) |
| ETH   | 1.2    | 1.31  | -0.11  | no  | — (at target) |
| GOOGL | 1.1    | 1.08  | 0.02   | no  | — (at target) |
| VXUS  | 0.9    | 0.89  | 0.01   | no  | — (at target) |
| SOFI  | 0.6    | 0.59  | 0.01   | no  | — (at target) |
| PLTR  | 0.4    | 0.41  | -0.01  | no  | — (at target) |
| GXRP  | 0.3    | 0.31  | -0.01  | no  | — (at target) |
| APLD  | 0.2    | 0.21  | -0.01  | no  | — (at target) |
| IREN  | 0.2    | 0.001 | 0.199  | no  | — (REMNANT — top up to full target) |
| NBIS  | 0.2    | 0     | 0.200  | no  | — (ZERO — buyback to full target) |
| AMZN  | 0.2    | 0.20  | 0.00   | no  | — (at target) |
| META  | 0.2    | 0.22  | -0.02  | no  | — (at target) |
| IONQ  | 0.1222 | 0.119 | 0.003  | no  | — (at target) |
| RGTI  | 0.1222 | 0.127 | -0.005 | no  | — (at target — recovered) |
| QBTS  | 0.1222 | 0.132 | -0.010 | no  | — (at target — recovered) |
| UNH   | 0.1222 | 0.125 | -0.003 | no  | — (at target) |
| DRAM  | 0.1222 | 0.127 | -0.005 | no  | — (at target) |
| WULF  | 0.1222 | 0.123 | -0.001 | no  | — (at target) |
| CIFR  | 0.1222 | 0.139 | -0.017 | no  | — (at target) |
| GLXY  | 0.1222 | 0.133 | -0.011 | no  | — (at target — remnant filled) |
| RIOT  | 0.1222 | 0.135 | -0.013 | no  | — (at target — recovered) |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **Core ramp still the whole story.** VOO (gap 13.9%) and SCHD (gap
  9.9%) remain deeply underweight — buildout continues at the 1%/day
  ramp cap. BTC nearly there (gap 0.8%). SGOV/QQQM/SCHG/SPMO/VTV all
  within tolerance now.
- **BRK.B still at zero** (2.6% gap) — ongoing wide-spread open-skip, not
  a stop. Retry ramp buy at open only if spread has normalized (<~2%);
  skip again otherwise.
- **NBIS at zero** (0.2% gap) and **IREN remnant** ($0.47, 0.001%) — the
  last two unrecovered names from the 07-16 liquidation. Buy back to full
  target (both non-ramp, buy in full). RGTI/QBTS/RIOT/GLXY from that same
  event are now back at target — no recurrence of the after-hours
  liquidation since.
- **Duplicate trailing-stop accumulation persists** — BTC/QQQM/SCHD/SGOV
  6 stops each, VOO 5, SCHG 5, SPMO 4, CIFR 2. Order book is at the
  50-order return cap, so visibility is truncated. `qty_available` on
  core positions is near-zero (VOO 0.23, SCHD 0.45, SGOV 0.23) because
  stacked stops reserve almost all shares. Not pre-market-actionable, but
  midday scan should audit total stop qty vs holdings and cancel stale
  duplicates before it blocks a rebalance sell.

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $500 each toward target, capped by gap):
  VOO $500, SCHD $500, BTC $500. SGOV/QQQM/SCHG/SPMO/VTV within tolerance
  — skip.
- BRK.B: retry ramp buy up to 1% (~$500) only if spread normalized.
- Buyback/top-up liquidation leftovers to full target (non-ramp, <2%,
  buy in full): NBIS ~$100, IREN ~$100.
- Refresh trailing stops on positions crossing ≥1 whole share after
  today's buys (market-open routine); midday scan to de-duplicate stacked
  stops on core names.

### Decision
BUILDOUT — Core ramp continues (VOO/SCHD still ~14%/10% underweight);
NBIS + IREN buy back per buildout rule; BRK.B conditional on spread. No
new anomalies — the 07-16 after-hours liquidation has not recurred.

---

## 2026-07-23 — Pre-market Drift Check

### Account
- Equity: $49,979.82
- Cash: $12,342.67 (24.7%)
- Buying power: $12,342.67

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO   | 23.8   | 10.92 | 12.89  | yes | no (0/1%) |
| SCHD  | 19.9   | 11.05 | 8.85   | yes | no (0/1%) |
| BTC   | 11.1   | 11.08 | 0.03   | yes | — (at target) |
| SGOV  | 9.3    | 9.31  | -0.01  | yes | — (at target) |
| QQQM  | 7.8    | 7.79  | 0.01   | yes | — (at target) |
| SCHG  | 7.4    | 7.29  | 0.11   | yes | — (within tol) |
| SPMO  | 5.6    | 5.73  | -0.13  | yes | — (at target) |
| VTV   | 2.6    | 2.61  | -0.01  | yes | — (at target) |
| BRK.B | 2.6    | 0     | 2.60   | yes | no — UNHELD (wide-spread skip) |
| MSFT  | 1.7    | 1.71  | -0.01  | no  | — (at target) |
| VGT   | 1.3    | 1.32  | -0.02  | no  | — (at target) |
| ETH   | 1.2    | 1.31  | -0.11  | no  | — (at target) |
| GOOGL | 1.1    | 1.01  | 0.09   | no  | — see Gaps (stop firing at open) |
| VXUS  | 0.9    | 0.89  | 0.01   | no  | — (at target) |
| SOFI  | 0.6    | 0.58  | 0.02   | no  | — (at target) |
| PLTR  | 0.4    | 0.39  | 0.01   | no  | — (at target) |
| GXRP  | 0.3    | 0.31  | -0.01  | no  | — (at target) |
| APLD  | 0.2    | 0.22  | -0.02  | no  | — (at target) |
| IREN  | 0.2    | 0.21  | -0.01  | no  | — (at target — remnant recovered) |
| NBIS  | 0.2    | 0     | 0.20   | no  | — (ZERO — buyback to full target) |
| AMZN  | 0.2    | 0.20  | 0.00   | no  | — (at target) |
| META  | 0.2    | 0.21  | -0.01  | no  | — (at target) |
| IONQ  | 0.1222 | 0.118 | 0.004  | no  | — (at target) |
| RGTI  | 0.1222 | 0.128 | -0.006 | no  | — (at target) |
| QBTS  | 0.1222 | 0.131 | -0.009 | no  | — (at target) |
| UNH   | 0.1222 | 0.123 | -0.001 | no  | — (at target) |
| DRAM  | 0.1222 | 0.133 | -0.011 | no  | — (at target) |
| WULF  | 0.1222 | 0.124 | -0.002 | no  | — (at target) |
| CIFR  | 0.1222 | 0.153 | -0.031 | no  | — (winner +25.8%, drift ok) |
| GLXY  | 0.1222 | 0.133 | -0.011 | no  | — (at target) |
| RIOT  | 0.1222 | 0.152 | -0.030 | no  | — (winner +24.8%, drift ok) |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **Core ramp still the whole story.** VOO (gap 12.9%) and SCHD (gap
  8.85%) remain deeply underweight — buildout continues at the 1%/day
  ramp cap. BTC now at target (gap 0.03%). SGOV/QQQM/SCHG/SPMO/VTV all
  within tolerance.
- **GOOGL gapped through its stop overnight** — now -11.24% unrealized
  (was -6.33% Jul 22). Its 10% trailing stop is LIVE (verified directly),
  but stops only fire in-hours, so it did not trigger overnight. Expect
  the stop to sell GOOGL near the 9:30 open (gap slippage past the
  intended -10%); position then re-enters the buildout queue at zero.
  Auto-handled — no manual pre-market action.
- **Stop coverage confirmed for page-hidden names.** Yesterday's "unverif"
  stops verified live via per-symbol query: GOOGL, VTV(x2), MSFT, VGT,
  ETH, VXUS, GXRP all carry a 10% trailing stop. AMZN/UNH (and META,
  sub-1-share remnants) remain scan-only — no stop, as expected.
- **BRK.B still at zero** (2.6% gap) — ongoing wide-spread open-skip, not
  a stop. Retry ramp buy at open only if spread normalized (<~2%).
- **NBIS at zero** (0.2% gap) — last unrecovered name from the 07-16
  liquidation. Buy back to full target (non-ramp, buy in full). IREN now
  recovered to target — no longer a remnant.
- **Duplicate trailing-stop accumulation persists** — 50-order page still
  saturated (BTC 7, SCHD 7, SGOV 6, QQQM 5, VOO 5, SCHG 4, SPMO 3, CIFR
  2 = 39 dupes). VTV also now double-stopped. `qty_available` near-zero on
  cores (SPMO 0.00, SGOV 0.23, SCHD 0.59, VOO 0.96). Not pre-market
  actionable; midday scan must de-duplicate (keep one per symbol,
  honoring never-move-down) before it blocks a rebalance sell.

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $500 each toward target, capped by gap):
  VOO $500, SCHD $500. BTC/SGOV/QQQM/SCHG/SPMO/VTV within tolerance —
  skip.
- BRK.B: retry ramp buy up to 1% (~$500) only if spread normalized.
- NBIS: buyback to full target (non-ramp, <2%, buy in full) ~$100.
- GOOGL: let the live 10% stop execute at open; re-queue for buildout
  once flat. No manual sell needed pre-market.
- Refresh/de-dupe stops: market-open sets stops on names crossing ≥1
  whole share after buys; midday scan de-duplicates stacked stops on
  cores.

### Decision
BUILDOUT — Core ramp continues (VOO/SCHD still ~13%/9% underweight); NBIS
buy back per buildout rule; BRK.B conditional on spread. One risk event:
GOOGL gapped through its live stop to -11.2% and will auto-sell at open —
covered, not an anomaly. No new liquidation recurrence.

## 2026-07-24 — Pre-market Drift Check

### Account
- Equity: $49,694.58
- Cash: $12,037.58 (24.2%)
- Buying power: $153,377.12 (margin; cash the binding constraint for buys)

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO   | 23.8   | 11.90 | 11.90  | yes | no (0/1%) |
| SCHD  | 19.9   | 12.10 | 7.80   | yes | no (0/1%) |
| BTC   | 11.1   | 11.03 | 0.07   | yes | — (at target) |
| SGOV  | 9.3    | 9.36  | -0.06  | yes | — (at target) |
| QQQM  | 7.8    | 7.72  | 0.08   | yes | — (within tol) |
| SCHG  | 7.4    | 7.25  | 0.15   | yes | — (within tol) |
| SPMO  | 5.6    | 5.73  | -0.13  | yes | — (at target) |
| VTV   | 2.6    | 2.63  | -0.03  | yes | — (at target) |
| BRK.B | 2.6    | 0     | 2.60   | yes | no — UNHELD (buyback if spread ok) |
| MSFT  | 1.7    | 1.71  | -0.01  | no  | — (at target) |
| VGT   | 1.3    | 1.31  | -0.01  | no  | — (at target) |
| ETH   | 1.2    | 1.29  | -0.09  | no  | — (at target) |
| GOOGL | 1.1    | 0     | 1.10   | no  | no — ZERO (cut Jul23, buyback full) |
| VXUS  | 0.9    | 0.89  | 0.01   | no  | — (at target) |
| SOFI  | 0.6    | 0.57  | 0.03   | no  | — (at target; weakest -6.0%) |
| PLTR  | 0.4    | 0     | 0.40   | no  | no — ZERO (cut Jul23, buyback full) |
| GXRP  | 0.3    | 0.30  | 0.00   | no  | — (at target) |
| APLD  | 0.2    | 0.21  | -0.01  | no  | — (at target) |
| IREN  | 0.2    | 0.20  | 0.00   | no  | — (at target) |
| NBIS  | 0.2    | 0     | 0.20   | no  | no — ZERO (buyback to full target) |
| AMZN  | 0.2    | 0.19  | 0.01   | no  | — (at target) |
| META  | 0.2    | 0.21  | -0.01  | no  | — (at target) |
| IONQ  | 0.1222 | 0.116 | 0.006  | no  | — (at target) |
| RGTI  | 0.1222 | 0.126 | -0.004 | no  | — (at target) |
| QBTS  | 0.1222 | 0.129 | -0.007 | no  | — (at target) |
| UNH   | 0.1222 | 0.122 | 0.000  | no  | — (at target) |
| DRAM  | 0.1222 | 0.127 | -0.005 | no  | — (at target) |
| WULF  | 0.1222 | 0.127 | -0.005 | no  | — (at target) |
| CIFR  | 0.1222 | 0.161 | -0.039 | no  | — (winner +31.3%, 5% trail) |
| GLXY  | 0.1222 | 0.132 | -0.010 | no  | — (at target) |
| RIOT  | 0.1222 | 0.153 | -0.031 | no  | — (winner +24.8%, 5% trail) |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **Core ramp still the whole story.** VOO (gap 11.90%) and SCHD (gap
  7.80%) remain deeply underweight — buildout continues at the 1%/day ramp
  cap. Account still 24.2% cash vs 0.3% target: heavily underinvested, keep
  ramping. All other ramp cores (BTC/SGOV/QQQM/SCHG/SPMO/VTV) at/within tol.
- **Four zeroed names in the buyback queue.** GOOGL (1.10% gap) and PLTR
  (0.40%) were cut Jul23 on the -7% manual rule — both non-ramp, buy back in
  full at open. NBIS (0.20%) still unrecovered from the 07-16 liquidation —
  buy back in full. BRK.B (2.60%, ramp) still unheld on wide-spread skip —
  retry ramp buy at open only if spread normalized (<~2%). All standard
  buildout/buyback, no anomaly.
- **SOFI weakest name at -6.0% unrealized** — right under the -7% cut line.
  Midday scan must cut on any further weakness (carried from Jul23 watch).
- **Duplicate trailing-stop saturation now at 100% of the order page.** The
  50-order list is entirely stacked trailing stops (SCHD 8, BTC 7, VOO 6,
  SGOV 6, QQQM 5, SCHG 4, SPMO 3 = 32 excess dups). qty_available is now
  ~zero on every core (SPMO 0.00, SGOV 0.23, SCHD 0.67, VOO 0.69) — shares
  fully reserved against stacked sells. This is a 5-day-old unaddressed
  operational issue that the midday scan was repeatedly mandated to fix and
  has not; it now hides page-beyond stops (VTV/MSFT/VGT/ETH/VXUS/GXRP) from
  audit and would block any rebalance sell. Not pre-market actionable (buys
  use cash, unaffected), but escalated — see notification.

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $497 each toward target, capped by gap):
  VOO $497, SCHD $497.
- BRK.B: retry ramp buy up to 1% (~$497) only if spread normalized.
- Buyback to full target (non-ramp, <2%, buy in full): GOOGL ~$547,
  PLTR ~$199, NBIS ~$99.
- Set 10% trailing stops on any name crossing ≥1 whole share after buys.
- Midday scan: TOP PRIORITY — de-duplicate stacked stops (keep one per
  symbol, honor never-move-down) to free qty_available and restore audit.

### Decision
BUILDOUT — Core ramp continues (VOO/SCHD ~12%/8% underweight, 24% idle
cash); GOOGL/PLTR/NBIS buy back per buildout rule; BRK.B conditional on
spread. No new risk event. Standing operational flag: duplicate-stop page
saturation (100% of order list, 5 days old) escalated to human — the
automated midday de-dupe is not self-healing.

## 2026-07-27 — Pre-market Drift Check

### Account
- Equity: $49,892.27
- Cash: $11,365.45 (22.8%)
- Buying power: $153,325.99 (4x margin; cash the binding constraint for buys)

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO   | 23.8   | 12.95 | 10.85  | yes | no (0/1%) |
| SCHD  | 19.9   | 13.20 | 6.70   | yes | no (0/1%) |
| BTC   | 11.1   | 11.01 | 0.09   | yes | — (at target) |
| SGOV  | 9.3    | 9.33  | -0.03  | yes | — (at target) |
| QQQM  | 7.8    | 7.71  | 0.09   | yes | — (within tol) |
| SCHG  | 7.4    | 7.29  | 0.11   | yes | — (within tol) |
| SPMO  | 5.6    | 5.68  | -0.08  | yes | — (at target) |
| VTV   | 2.6    | 2.64  | -0.04  | yes | — (at target) |
| BRK.B | 2.6    | 0     | 2.60   | yes | no — UNHELD (buyback if spread ok) |
| MSFT  | 1.7    | 1.70  | 0.00   | no  | — (at target) |
| ETH   | 1.2    | 1.34  | -0.14  | no  | — (over, +11% unreal) |
| VGT   | 1.3    | 1.31  | -0.01  | no  | — (at target) |
| GOOGL | 1.1    | 1.11  | -0.01  | no  | — (rebought Fri, at target) |
| VXUS  | 0.9    | 0.89  | 0.01   | no  | — (at target) |
| SOFI  | 0.6    | 0     | 0.60   | no  | no — ZERO (stopped Fri, buyback full) |
| PLTR  | 0.4    | 0     | 0.40   | no  | no — ZERO (cut Jul23, buyback full) |
| GXRP  | 0.3    | 0.29  | 0.01   | no  | — (at target) |
| APLD  | 0.2    | 0.03  | 0.17   | no  | no — REMNANT (stopped Fri, top to full) |
| IREN  | 0.2    | 0     | 0.20   | no  | no — ZERO (stopped Fri, buyback full) |
| NBIS  | 0.2    | 0     | 0.20   | no  | no — ZERO (buyback to full target) |
| AMZN  | 0.2    | 0.19  | 0.01   | no  | — (at target) |
| META  | 0.2    | 0.21  | -0.01  | no  | — (at target) |
| IONQ  | 0.1222 | 0     | 0.12   | no  | no — ZERO (stopped Fri, buyback full) |
| RGTI  | 0.1222 | 0.125 | -0.003 | no  | — (at target) |
| QBTS  | 0.1222 | 0.024 | 0.098  | no  | no — REMNANT (stopped Fri, top to full) |
| UNH   | 0.1222 | 0.121 | 0.001  | no  | — (at target) |
| DRAM  | 0.1222 | 0.013 | 0.109  | no  | no — REMNANT (stopped Fri, top to full) |
| WULF  | 0.1222 | 0.004 | 0.118  | no  | no — REMNANT (stopped Fri, top to full) |
| CIFR  | 0.1222 | 0.004 | 0.118  | no  | no — REMNANT (winner trailed out Fri, top to full) |
| GLXY  | 0.1222 | 0.032 | 0.090  | no  | no — REMNANT (stopped Fri, top to full) |
| RIOT  | 0.1222 | 0.008 | 0.114  | no  | no — REMNANT (winner trailed out Fri, top to full) |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **Broad Friday-afternoon stop-out swept the speculative/miner basket.**
  Since the Jul-24 EOD snapshot, trailing stops fired across the small
  names: SOFI (0.60%), IREN (0.20%), IONQ (0.12%) fully ZEROED; APLD, QBTS,
  DRAM, WULF, CIFR, GLXY, RIOT reduced to sub-remnants (each now <0.03% vs
  0.12–0.20% targets). CIFR/RIOT were the +31%/+25% winners on 5% trails —
  a single down day trailed them out. Note the crypto-ETF cores were the
  opposite (BTC +1.7%, ETH +5.6% today) — this was name-specific to the
  momo/miner longs, not crypto broadly. All re-enter the buildout queue
  under the normal rule; nothing anomalous, just a large buyback list.
- **Core ramp unchanged as the main story.** VOO (gap 10.85%) and SCHD
  (6.70%) still deeply underweight — 1%/day ramp continues. 22.8% cash vs
  0.3% target: still heavily underinvested. Other ramp cores at/within tol.
- **Persistent zeros:** PLTR (cut Jul23) and NBIS (07-16 liquidation) still
  unheld — buy back in full. BRK.B (2.60%, ramp) still unheld on wide-spread
  skip — retry ramp buy at open only if spread normalized (<~2%).

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $499 each toward target, capped by gap):
  VOO $499, SCHD $499. BRK.B $499 only if spread normalized.
- Buyback / top-up to full target (non-ramp, <2%, buy in full):
  SOFI ~$299, PLTR ~$200, IREN ~$100, NBIS ~$100, IONQ ~$61, APLD ~$85,
  and spec top-ups QBTS ~$49 / DRAM ~$55 / WULF ~$59 / CIFR ~$59 /
  GLXY ~$45 / RIOT ~$57 (each to full 0.1222% ≈ $61). Total ≈ $2.7k;
  cash $11.4k covers it.
- Set 10% trailing stops on every name crossing ≥1 whole share after buys.

### Decision
BUILDOUT — Core ramp continues (VOO/SCHD ~11%/7% underweight, 23% idle
cash); large buyback list from Friday's speculative-basket stop-out
(SOFI/IREN/IONQ zeroed + 7 remnants) all rejoin buildout per the standard
rule; PLTR/NBIS persistent zeros; BRK.B conditional on spread. No daily-loss
breaker (equity +0.8% on pre-market marks).

### STANDING OPERATIONAL FLAG (6 days old, ESCALATED — worsening)
Order page is now **100% saturated: 50/50 orders, all stacked duplicate
trailing stops on just 9 core symbols** (SCHD 10, BTC 9, VOO 7, SGOV 7,
QQQM 6, SCHG 5, SPMO 4, GOOGL 1, RGTI 1). SCHD dups grew 8→10 since Jul23.
Consequences: (1) every OTHER held position — VTV, MSFT, VGT, ETH, VXUS,
GXRP + all spec remnants — has NO visible/verifiable stop (pushed beyond
the 50-order page, coverage unauditable); (2) today's fresh buys can't
register new stops until the page is freed; (3) any rebalance sell is
blocked (shares reserved against stacked stops, qty_available ~0 on cores).
The automated midday de-dupe has been mandated Jul20–24 and has NOT
self-healed. Market-open MUST de-dupe (cancel stale duplicates, keep one
full-position stop per symbol, honor never-move-down) BEFORE it can place
stops on today's buys. Needs human attention.
