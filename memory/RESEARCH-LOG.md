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

---

## 2026-07-28 — Pre-market Drift Check

### Account
- Equity: $49,376.29
- Cash: $9,404.20 (19.05% vs 0.3% target — still underinvested, improving)
- Buying power: $149,207.71

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO | 23.800 | 13.949 | +9.851 | yes | no (fresh) |
| SCHD | 19.900 | 14.458 | +5.442 | yes | no (fresh) |
| BTC | 11.100 | 10.798 | +0.302 | yes | no (fresh) |
| SGOV | 9.300 | 9.425 | -0.125 | yes | no (fresh) |
| QQQM | 7.800 | 7.578 | +0.222 | yes | no (fresh) |
| SCHG | 7.400 | 7.305 | +0.095 | yes | no (fresh) |
| SPMO | 5.600 | 5.499 | +0.101 | yes | no (fresh) |
| VTV | 2.600 | 2.674 | -0.074 | yes | no (fresh) |
| BRK.B | 2.600 | 0.000 | +2.600 | yes | no (fresh) **ZERO** |
| MSFT | 1.700 | 1.749 | -0.049 | no | n/a |
| VGT | 1.300 | 1.284 | +0.016 | no | n/a |
| ETH | 1.200 | 1.292 | -0.092 | no | n/a |
| GOOGL | 1.100 | 1.127 | -0.027 | no | n/a |
| VXUS | 0.900 | 0.891 | +0.009 | no | n/a |
| SOFI | 0.600 | 0.583 | +0.017 | no | n/a |
| PLTR | 0.400 | 0.405 | -0.005 | no | n/a |
| GXRP | 0.300 | 0.296 | +0.004 | no | n/a |
| APLD | 0.200 | 0.195 | +0.005 | no | n/a |
| IREN | 0.200 | 0.186 | +0.014 | no | n/a |
| NBIS | 0.200 | 0.000 | +0.200 | no | n/a **ZERO** |
| AMZN | 0.200 | 0.190 | +0.010 | no | n/a |
| META | 0.200 | 0.207 | -0.007 | no | n/a |
| IONQ | 0.122 | 0.119 | +0.004 | no | n/a |
| RGTI | 0.122 | 0.130 | -0.007 | no | n/a |
| QBTS | 0.122 | 0.124 | -0.001 | no | n/a |
| UNH | 0.122 | 0.122 | +0.000 | no | n/a |
| DRAM | 0.122 | 0.110 | +0.012 | no | n/a |
| WULF | 0.122 | 0.115 | +0.007 | no | n/a |
| CIFR | 0.122 | 0.000 | +0.122 | no | n/a **ZERO** |
| GLXY | 0.122 | 0.030 | +0.092 | no | n/a |
| RIOT | 0.122 | 0.116 | +0.006 | no | n/a |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **Core ramp remains the whole story.** VOO (gap +9.85%) and SCHD (+5.44%)
  still deeply underweight; 1%/day ramp continues. All other ramp cores
  (BTC/SGOV/QQQM/SCHG/SPMO/VTV) are at/within tolerance. Cash 19.05% vs
  0.3% — still heavily underinvested but down from 22.8% Friday as the ramp
  works.
- **Friday's speculative-basket stop-out has been largely rebuilt.** Monday's
  runs restored SOFI, IREN, IONQ, APLD, QBTS, DRAM, WULF, RIOT, PLTR to
  at/within tolerance — the big buyback list is essentially cleared.
- **Remaining zeros / remnants:** BRK.B (2.60%, ramp — persistent wide-spread
  skip), NBIS (0.20%), CIFR (0.122%) all at ZERO; GLXY a 0.030% remnant vs
  0.122%. All rejoin the buildout queue under the normal rule.

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $494 each, gap-capped): VOO $494, SCHD $494.
  BRK.B ramp buy ≈ $494 only if spread has normalized (<~2%); else skip again.
- Buyback / top-up to full target (non-ramp, <2%, buy in full): NBIS ~$99,
  CIFR ~$60, GLXY ~$45 top-up. Total ≈ $1.2k; cash $9.4k covers it easily.
- Set 10% GTC trailing stops on every new buy crossing ≥1 whole share —
  **but see operational flag: order page must be de-duped first to free slots.**

### Decision
BUILDOUT — VOO/SCHD ramp continues (~10%/5% underweight, 19% idle cash);
small buybacks BRK.B (spread-conditional) / NBIS / CIFR / GLXY. No daily-loss
breaker (equity -0.45% on pre-market marks vs 10% limit).

### STANDING OPERATIONAL FLAG (7 days old — STILL UNRESOLVED, page 50/50)
Order page remains **100% saturated: 50/50 orders, all trailing stops.**
Duplicate stacking on cores persists: SCHD 9, VOO 7, BTC 7, SGOV 5, SCHG 4,
QQQM 4, SPMO 3 (= 39 on 7 symbols); the other 11 are single stops now placed
on small names (SOFI/PLTR/IREN/IONQ/APLD/QBTS/DRAM/WULF/RIOT/RGTI/GOOGL).
Partial healing since Friday (SCHD 10→9, BTC 9→7, SGOV 7→5, QQQM 6→4) but
the page is full again because Monday's buyback stops consumed the freed
slots. Consequences unchanged: (1) 10 held positions have NO visible stop —
AMZN, ETH, GLXY, GXRP, META, MSFT, UNH, VGT, VTV, VXUS (~$4.9k, coverage
unauditable, pushed off the 50-order page); (2) today's fresh buys cannot
register new stops until slots are freed. Market-open/midday MUST de-dupe
(cancel stale duplicates, keep one full-position stop per symbol, honor
never-move-down, then top up uncovered held names) BEFORE placing new stops.
Auto de-dupe has not self-healed for 7 days — needs human attention.

---

## 2026-07-30 — Pre-market Drift Check

### Account
- Equity: $49,253.94
- Cash: $9,045.29 (18.36% vs 0.3% target — still underinvested, ramp continues)
- Buying power: $148,499.26

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO | 23.800 | 15.849 | +7.951 | yes | no (fresh) |
| SCHD | 19.900 | 16.481 | +3.419 | yes | no (fresh) |
| BTC | 11.100 | 11.014 | +0.086 | yes | no (fresh) |
| SGOV | 9.300 | 9.450 | -0.150 | yes | no (fresh) |
| QQQM | 7.800 | 7.515 | +0.285 | yes | no (fresh) |
| SCHG | 7.400 | 7.308 | +0.092 | yes | no (fresh) |
| SPMO | 5.600 | 1.260 | +4.340 | yes | no (fresh) **STOP-TRIGGERED** |
| VTV | 2.600 | 2.656 | -0.056 | yes | no (fresh) |
| BRK.B | 2.600 | 0.998 | +1.602 | yes | no (fresh) |
| MSFT | 1.700 | 1.907 | -0.207 | no | n/a |
| VGT | 1.300 | 1.275 | +0.025 | no | n/a |
| ETH | 1.200 | 1.322 | -0.122 | no | n/a |
| GOOGL | 1.100 | 1.167 | -0.067 | no | n/a |
| VXUS | 0.900 | 0.888 | +0.012 | no | n/a |
| SOFI | 0.600 | 0.609 | -0.009 | no | n/a |
| PLTR | 0.400 | 0.391 | +0.009 | no | n/a |
| GXRP | 0.300 | 0.291 | +0.009 | no | n/a |
| APLD | 0.200 | 0.000 | +0.200 | no | n/a **ZERO** |
| IREN | 0.200 | 0.062 | +0.138 | no | n/a |
| NBIS | 0.200 | 0.193 | +0.007 | no | n/a |
| AMZN | 0.200 | 0.192 | +0.008 | no | n/a |
| META | 0.200 | 0.186 | +0.014 | no | n/a |
| IONQ | 0.122 | 0.120 | +0.002 | no | n/a |
| RGTI | 0.122 | 0.117 | +0.005 | no | n/a |
| QBTS | 0.122 | 0.120 | +0.002 | no | n/a |
| UNH | 0.122 | 0.122 | +0.000 | no | n/a |
| DRAM | 0.122 | 0.117 | +0.005 | no | n/a |
| WULF | 0.122 | 0.022 | +0.100 | no | n/a |
| CIFR | 0.122 | 0.005 | +0.117 | no | n/a **remnant** |
| GLXY | 0.122 | 0.000 | +0.122 | no | n/a **ZERO** |
| RIOT | 0.122 | 0.000 | +0.122 | no | n/a **ZERO** |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **SPMO stop-triggered — dropped 5.50% → 1.26% (+4.34% gap).** Trailing
  stop fired since 07-28 (a fresh trailing_stop still sits on the residual
  ~4 shares). Re-enters ramp buildout under the normal rule — up to 1%/day.
- **Core ramp still the main story.** VOO (+7.95%) and SCHD (+3.42%) remain
  underweight; 1%/day ramp continues. BRK.B recovered to 1.00% but still
  +1.60% short. BTC/SGOV/QQQM/SCHG/VTV at/within tolerance. Cash 18.4% vs
  0.3% — heavily underinvested, grinding down as ramp works.
- **Spec-basket zeros/remnants:** APLD, GLXY, RIOT at ZERO; CIFR ($2.46)
  and WULF ($10.82) remnants; IREN ($30.56) underweight. All rejoin the
  buildout queue, buy to full target at open.
- **⚠ OPERATIONAL — 14 positions carry NO trailing stop, incl. the two
  largest: VTV ($1,308) and MSFT ($939); also ETH, VGT, BRK.B, VXUS +8
  smaller (~$4,884 total unprotected).** Violates the 10%-trailing-stop
  hard rule. Root cause is order-page saturation: 50 open orders, 43 of
  them duplicate stale stops stacked on 7 core symbols (SCHD 11, VOO 8,
  BTC 7, SGOV 6, QQQM 5, SCHG 4, SPMO 2) — the market-open routine adds a
  new stop each day without cancelling the prior one, starving uncovered
  positions of order slots. This has worsened since the 07-28 flag.
  **Market-open must de-dup (cancel redundant stops, keep one per symbol)
  before placing new stops.**

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $492 each, gap-capped): VOO ~$492,
  SCHD ~$492, SPMO ~$492 (stop-triggered rebuild), BRK.B ~$492.
- Buyback / top-up to full target (non-ramp, <2%, buy in full): APLD ~$99,
  GLXY ~$60, RIOT ~$60, CIFR ~$58, IREN ~$68, WULF ~$49.
- Total ≈ $2.36k; cash $9.0k covers easily.
- **De-dup the order page first**, then set 10% GTC trailing stops on every
  position/new buy currently lacking one (VTV, MSFT, ETH, VGT, BRK.B, VXUS,
  GXRP, NBIS, AMZN, META, UNH, IREN, WULF, CIFR).

### Decision
BUILDOUT — VOO/SCHD/SPMO/BRK.B ramp continues; spec buybacks; and clear the
stop-coverage gap on the 14 unstopped positions. No daily-loss breaker
(equity -0.35% on pre-market marks vs 10% limit).

---

## 2026-07-31 — Pre-market Drift Check

### Account
- Equity: $49,784.12
- Cash: $6,656.81
- Buying power: $146,850.94 (margin; non-marginable $28,125.32)

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO | 23.80 | 16.94 | +6.86 | yes | no |
| SCHD | 19.90 | 17.20 | +2.70 | yes | no |
| BTC | 11.10 | 10.81 | +0.29 | yes | no |
| SGOV | 9.30 | 9.35 | -0.05 | yes | n/a |
| QQQM | 7.80 | 7.93 | -0.13 | yes | n/a |
| SCHG | 7.40 | 7.43 | -0.03 | yes | n/a |
| SPMO | 5.60 | 2.35 | +3.25 | yes | no |
| VTV | 2.60 | 2.65 | -0.05 | yes | n/a |
| BRK.B | 2.60 | 1.99 | +0.61 | yes | no |
| MSFT | 1.70 | 1.98 | -0.28 | no | n/a |
| VGT | 1.30 | 1.30 | -0.00 | no | n/a |
| ETH | 1.20 | 1.29 | -0.09 | no | n/a |
| GOOGL | 1.10 | 1.16 | -0.06 | no | n/a |
| VXUS | 0.90 | 0.90 | -0.00 | no | n/a |
| SOFI | 0.60 | 0.65 | -0.05 | no | n/a |
| PLTR | 0.40 | 0.39 | +0.01 | no | n/a |
| GXRP | 0.30 | 0.29 | +0.01 | no | n/a |
| APLD | 0.20 | 0.22 | -0.02 | no | n/a |
| IREN | 0.20 | 0.23 | -0.03 | no | n/a |
| NBIS | 0.20 | 0.25 | -0.05 | no | n/a |
| AMZN | 0.20 | 0.21 | -0.01 | no | n/a |
| META | 0.20 | 0.00 | +0.20 | no | no **ZERO** |
| IONQ | 0.12 | 0.13 | -0.01 | no | n/a |
| RGTI | 0.12 | 0.13 | -0.01 | no | n/a |
| QBTS | 0.12 | 0.13 | -0.01 | no | n/a |
| UNH | 0.12 | 0.12 | +0.00 | no | n/a |
| DRAM | 0.12 | 0.14 | -0.02 | no | n/a |
| WULF | 0.12 | 0.03 | +0.10 | no | no **remnant** |
| CIFR | 0.12 | 0.13 | -0.01 | no | n/a |
| GLXY | 0.12 | 0.14 | -0.01 | no | n/a |
| RIOT | 0.12 | 0.13 | -0.01 | no | n/a |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **Core ramp remains the story.** VOO deeply underweight (+6.86% gap,
  ~$3.4k) and SCHD (+2.70%, ~$1.3k) — 1%/day ramp continues. SPMO still
  rebuilding from its 07-28 stop trigger (+3.25%, ~$1.6k). BRK.B +0.61%
  (~$304). BTC within a hair of target (+0.29%). Cash 13.4% vs 0.3% target
  — still overweight cash, grinding down as ramp works. Down from ~18% a
  few sessions ago; buildout is progressing.
- **META at ZERO (+0.20% gap, ~$100).** Non-ramp — buy to full target at
  open. WULF a remnant ($12.83, +0.10% gap) — top up to full. (Yesterday's
  APLD/GLXY/RIOT/CIFR/IREN zeros/remnants were filled at the 07-30 open and
  now sit at target.)
- **⚠ OPERATIONAL — stop-coverage hard-rule violation persists. 8 held
  positions carry NO trailing stop:** VTV ($1,320), VGT ($649), ETH ($641),
  VXUS ($450), GXRP ($146), NBIS ($126), AMZN ($106), UNH ($60) — ~$3.5k
  unprotected, incl. the 8th-largest position (VTV). Root cause unchanged:
  order page saturated at 50/50, ~36 slots are duplicate stale stops
  stacked on 7 core symbols (SCHD 10, VOO 8, BTC 5, QQQM 4, SGOV 3, SPMO 3,
  SCHG 3), starving uncovered positions of slots. Improved from 14
  unprotected on 07-30 but not cleared. **Market-open must de-dup (cancel
  redundant stops, keep one per symbol, honor never-move-down) BEFORE
  placing the 8 missing 10% GTC trailing stops.**

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $498 each, gap-capped): VOO ~$498,
  SCHD ~$498, SPMO ~$498, BRK.B ~$304, BTC ~$144.
- Buy to full target (non-ramp): META ~$100, WULF ~$50.
- Total ≈ $2.09k; cash $6.66k covers easily.
- **De-dup the order page first**, then set 10% GTC trailing stops on every
  uncovered position/new buy: VTV, VGT, ETH, VXUS, GXRP, NBIS, AMZN, UNH
  (plus stops on any new fills: META, and top-ups).

### Decision
BUILDOUT — VOO/SCHD/SPMO/BRK.B/BTC ramp continues; META buyback + WULF
top-up; clear the 8-position stop-coverage gap. No daily-loss breaker
(equity +0.27% vs prior close on pre-market marks, well within 10% limit).

---

## 2026-08-04 — Pre-market Drift Check

### Account
- Equity: $50,375.14 | Cash: $3,090.98 | Buying power: $53,315.72

### Drift vs. Target
| Ticker | Target % | Actual % | Gap | Ramp? | Today's Allowance Used |
|---|---|---|---|---|---|
| VOO | 23.80 | 19.06 | +4.75 | yes | no |
| SCHD | 19.90 | 19.05 | +0.85 | yes | no |
| BTC | 11.10 | 11.17 | -0.07 | yes | n/a |
| SGOV | 9.30 | 9.22 | +0.08 | yes | no |
| QQQM | 7.80 | 7.99 | -0.19 | yes | n/a |
| SCHG | 7.40 | 7.55 | -0.15 | yes | n/a |
| SPMO | 5.60 | 4.37 | +1.23 | yes | no |
| VTV | 2.60 | 2.61 | -0.01 | yes | n/a |
| BRK.B | 2.60 | 2.54 | +0.06 | yes | no |
| MSFT | 1.70 | 2.09 | -0.39 | no | n/a |
| VGT | 1.30 | 1.31 | -0.01 | no | n/a |
| ETH | 1.20 | 1.26 | -0.06 | no | n/a |
| GOOGL | 1.10 | 1.24 | -0.14 | no | n/a |
| VXUS | 0.90 | 0.89 | +0.01 | no | n/a |
| SOFI | 0.60 | 0.70 | -0.10 | no | n/a |
| PLTR | 0.40 | 0.46 | -0.06 | no | n/a |
| GXRP | 0.30 | 0.29 | +0.01 | no | n/a |
| APLD | 0.20 | 0.22 | -0.02 | no | n/a |
| IREN | 0.20 | 0.21 | -0.01 | no | n/a |
| NBIS | 0.20 | 0.26 | -0.06 | no | n/a |
| AMZN | 0.20 | 0.22 | -0.02 | no | n/a |
| META | 0.20 | 0.21 | -0.01 | no | n/a |
| IONQ | 0.12 | 0.15 | -0.02 | no | n/a |
| RGTI | 0.12 | 0.14 | -0.02 | no | n/a |
| QBTS | 0.12 | 0.15 | -0.02 | no | n/a |
| UNH | 0.12 | 0.12 | +0.00 | no | n/a |
| DRAM | 0.12 | 0.03 | +0.09 | no | no **remnant** |
| WULF | 0.12 | 0.13 | -0.01 | no | n/a |
| CIFR | 0.12 | 0.12 | -0.00 | no | n/a |
| GLXY | 0.12 | 0.09 | +0.04 | no | no **remnant** |
| RIOT | 0.12 | 0.04 | +0.09 | no | no **remnant** |

(ADA target held as 0.3% cash until GADA lists — see TARGET-PORTFOLIO.json.)

### Gaps Needing Attention
- **Core ramp is the whole story.** VOO deeply underweight (+4.75% gap,
  ~$2.39k) and SPMO (+1.23%, ~$618) — 1%/day ramp continues. SCHD now
  nearly on target (+0.85%, ~$427, fillable in one buy). BRK.B +0.06%
  (~$32), SGOV +0.08% (~$42) trivial. BTC on target (-0.07%). Cash 6.14%
  vs 0.3% — still overweight, grinding down as ramp draws it.
- **Three remnants (non-ramp, buy to full):** DRAM ($14.54, +0.09%, ~$47),
  RIOT ($18.46, +0.09%, ~$43), GLXY ($42.70, +0.04% ~$19). Leftovers from
  prior stop triggers, partially re-bought — top up to full target.
- **No zero-position gaps.** All 31 target symbols hold a position; no
  stop-loss buyback needed.
- **Stop coverage: HEALTHY.** Every whole-share position carries a 10% GTC
  trailing stop to its floor-of-qty (MSFT 5%, GOOGL/IONQ/QBTS/SOFI 7%,
  rest 10%). Only stopless = 6 sub-1-share positions Alpaca can't cover
  with a fractional trailing stop (AMZN, DRAM, META, NBIS, RIOT, UNH;
  ~$482), each under the -7% manual-cut rule until it ramps past 1 share.
  The prior log's "8 uncovered / 50-slot saturation" was cleared at
  Monday's open — order page now at 37, no saturation.

### Planned Action for Market-Open
- Ramp (buy up to 1% equity ≈ $504, gap-capped): VOO ~$504, SPMO ~$504,
  SCHD ~$427, BRK.B ~$32, SGOV ~$42.
- Buy to full target (non-ramp remnants): DRAM ~$47, RIOT ~$43, GLXY ~$19.
- Total ≈ $1.62k; cash $3.09k covers.
- Attach a 10% GTC trailing stop to every new whole-share fill; sub-1-share
  buys stay under the -7% manual rule.

### Decision
BUILDOUT — VOO/SPMO/SCHD/BRK.B/SGOV ramp continues; DRAM/RIOT/GLXY remnant
top-ups. No daily-loss breaker (equity +0.19% vs prior close). Stop
coverage healthy — no operational flag.
