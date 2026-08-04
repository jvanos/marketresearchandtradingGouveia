# Trade Log

## 2026-07-24 — Market-Open Buildout

Day-14 buildout. Core ramp continues: VOO and SCHD each took the next 1%
allowance ($495; equity $49,555.89 → 1% = $495.56). Both still deeply
underweight (VOO 11.9% → gap, SCHD 12.2% → gap vs targets 23.8%/19.9%).
BTC/SGOV/QQQM/SCHG/SPMO/VTV at/within tolerance — skipped. GOOGL rebought
in full to its 1.1% target ($545) after yesterday's -7% cut — fresh 10%
GTC trailing stop placed (qty 1; new position was zero-stopped, coverage
critical). SCHD's net-new whole shares (+15 sh) covered by a fresh 10%
trail — no existing stop moved. VOO increment was sub-share (+0.7285 sh),
no whole-share stop placeable on the increment alone; rolls into the
midday de-dup consolidation. PLTR and NBIS rebuys and BRK.B ramp all
skipped on wide open-auction spreads (see below).

| Date | Ticker | Side | Shares/Notional | Entry | Stop | Target Weight | Ramp? | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-07-24 | VOO   | buy | $495 / 0.7285 sh  | 679.50  | (incr sub-share; midday consol) | 23.8% | yes | ramp top-up |
| 2026-07-24 | SCHD  | buy | $495 / 15.041 sh  | 32.91   | 10% trail (+15 sh)              | 19.9% | yes | ramp top-up |
| 2026-07-24 | GOOGL | buy | $545 / 1.7034 sh  | 319.948 | 10% trail (qty 1, stop 288.33)  | 1.1%  | no  | gap-fill (buyback after Jul23 cut) |

### Skipped this run (wide spread at open — retry next buildout)
| Ticker | Target | Reason |
|---|---|---|
| BRK.B | 2.6% | ~6.0% spread (ap 516.01 / bp 485) — ongoing open-skip, ramp deferred |
| PLTR  | 0.4% | ~3.8% spread (ap 123.45 / bp 118.75) — was zero, rebuy deferred |
| NBIS  | 0.2% | ~21% spread (ap 232 / bp 183.18) — was zero, rebuy deferred |

### Flag for midday scan
- VOO ramp increment (+0.7285 sh) has no dedicated stop; fold into
  consolidation. VOO position now ~9.42 sh, only ~6 sh covered by stacked
  partial stops — under-covered.
- DUPLICATE/PARTIAL trailing-stop stacking on cores persists (50-order
  page saturated; SCHD 8, BTC 7, VOO 6, SGOV 6, QQQM 5, SCHG 4, SPMO 3).
  Stops are partial-qty and sum to LESS than position on VOO (6/9.4 sh)
  and SCHD (121/197.7 sh) — cores are UNDER-stopped, not just duplicated.
  De-duplicate AND top up to full-position coverage (keep one per symbol,
  honor never-move-down). Now 5 days old — top priority.
- BRK.B/PLTR/NBIS still unheld (wide open spreads), retry next buildout.

### Jul 24 — EOD Snapshot (Day 14, Friday)
**Portfolio:** $49,484.74 | **Cash:** $11,365.47 (23.0%) | **Day P&L:** -$123.50 (-0.25%) | **Phase P&L:** -$515.26 (-1.03%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| SCHD | 197.7 | 32.68 | 33.27 | +1.43% | +115.73 (+1.79%) | 10% trail |
| VOO | 9.418 | 686.67 | 678.72 | +0.02% | -74.86 (-1.16%) | 10% trail |
| BTC | 190.4 | 28.20 | 28.37 | -0.94% | +31.61 (+0.59%) | 10% trail |
| SGOV | 46.23 | 100.52 | 100.64 | +0.03% | +5.26 (+0.11%) | 10% trail |
| QQQM | 13.44 | 292.45 | 281.61 | -1.18% | -145.68 (-3.71%) | 10% trail |
| SCHG | 107.4 | 34.42 | 33.46 | +0.18% | -102.84 (-2.78%) | 10% trail |
| SPMO | 19.0 | 151.31 | 146.51 | -2.22% | -91.11 (-3.17%) | 10% trail |
| VTV | 5.944 | 219.21 | 221.02 | +0.53% | +10.76 (+0.83%) | trail (unverif) |
| MSFT | 2.197 | 393.50 | 381.40 | -0.05% | -26.59 (-3.08%) | trail (unverif) |
| VGT | 5.693 | 114.17 | 113.21 | -1.03% | -5.49 (-0.84%) | trail (unverif) |
| ETH | 35.65 | 16.83 | 17.75 | -0.62% | +32.80 (+5.47%) | trail (unverif) |
| GOOGL | 1.703 | 319.95 | 319.74 | -0.07% | -0.35 (-0.07%) | 10% trail (stop 288.33) |
| VXUS | 5.277 | 85.28 | 83.40 | -0.26% | -9.93 (-2.21%) | trail (unverif) |
| GXRP | 6.912 | 21.70 | 21.07 | -1.54% | -4.36 (-2.91%) | trail (unverif) |
| micro-remnants | — | — | — | — | META/AMZN/UNH/RGTI + 7 sub-$60 momo names | mixed |

**Notes:** Day 14, Friday — quiet down day. Equity $49,484.74, off -$123.50
(-0.25%) vs yesterday's $49,608.24 snapshot; phase -$515.26 (-1.03%) vs the
$50k Day-0 baseline. 3 trades today, all at the market-open buildout (VOO
+$495 ramp, SCHD +$495 ramp, GOOGL $545 full rebuy after Jul-23 cut; fresh
10% GTC trail on GOOGL @288.33). No midday run today. Broad tape soft:
growth-tilted cores led the drag (QQQM -1.18%, SPMO -2.22%, SCHG flat,
BTC -0.94%); SCHD +1.43% and defensives (SGOV, VTV) cushioned. VOO and
SCHD both still deeply underweight vs 23.8%/19.9% targets — ramp continues
Monday. Weekly trades Mon-Fri: 25 (informational; no weekly cap).

**CRITICAL / 5-DAY-OLD OPERATIONAL ISSUE — duplicate + partial trailing-stop
saturation on cores, still unresolved.** 50-order page fully saturated with
stacked trailing stops: SCHD 10, BTC 9, SGOV 7, VOO 7, QQQM 6, SCHG 5,
SPMO 4, GOOGL 1, RGTI 1 = 50. These are partial-qty and on VOO/SCHD sum to
LESS than the position (cores under-stopped, not merely duplicated). The
saturation pushes the stops for 6 held positions (VTV, MSFT, VGT, ETH,
VXUS, GXRP, ~$3.6k value) beyond the visible page — coverage UNVERIFIABLE
from the order list, marked "trail (unverif)". Midday scans on Jul
20/21/22/23 were each mandated to de-duplicate and did not; SCHD dups have
grown 8→10. TOP PRIORITY for Monday's midday scan: cancel stale duplicate
stops (keep one per symbol, top up to full-position coverage, honor
never-move-down) so coverage is auditable again. BRK.B/PLTR/NBIS still
unheld on wide spreads — retry next buildout.

### Jul 29 — EOD Snapshot (Day 17, Wednesday)
**Portfolio:** $48,907.24 | **Cash:** $9,045.31 (18.5%) | **Day P&L:** -$551.97 (-1.12%) | **Phase P&L:** -$1,092.76 (-2.19%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| SCHD | 241.2 | 32.89 | 33.78 | -0.33% | +214.44 (+2.70%) | 10% trail x11 (dup) |
| VOO | 11.58 | 685.61 | 669.00 | -1.76% | -192.38 (-2.42%) | 10% trail x8 (dup, under-covered) |
| BTC | 190.4 | 28.20 | 28.01 | -0.74% | -36.94 (-0.69%) | 10% trail x7 (dup) |
| SGOV | 46.23 | 100.52 | 100.68 | +0.02% | +7.22 (+0.15%) | 10% trail x6 (dup) |
| QQQM | 13.44 | 292.45 | 271.57 | -2.36% | -280.61 (-7.14%) | 10% trail x5 (dup) — PAST -7% cut line |
| SCHG | 107.4 | 34.42 | 33.18 | -1.66% | -132.93 (-3.60%) | 10% trail x4 (dup) |
| VTV | 5.944 | 219.21 | 219.65 | -1.50% | +2.62 (+0.20%) | NO STOP on page |
| MSFT | 2.197 | 393.50 | 399.10 | +1.46% | +12.31 (+1.42%) | NO STOP on page |
| ETH | 35.65 | 16.83 | 17.91 | -2.08% | +38.50 (+6.42%) | NO STOP on page |
| VGT | 5.693 | 114.17 | 108.11 | -2.49% | -34.51 (-5.31%) | NO STOP on page |
| SPMO | 4.509 | 147.21 | 135.42 | -3.92% | -53.16 (-8.01%) | 10% trail x2 (trimmed today) |
| GOOGL | 1.703 | 319.95 | 333.00 | -0.21% | +22.23 (+4.08%) | 10% trail @308.25 |
| BRK.B | 0.967 | 510.84 | 509.24 | -0.31% | -1.55 (-0.31%) | NO STOP on page (rebought today) |
| VXUS | 5.277 | 85.28 | 82.78 | -0.56% | -13.19 (-2.93%) | NO STOP on page |
| SOFI | 19.57 | 15.19 | 15.11 | -9.74% | -1.65 (-0.56%) | 10% trail @14.193 |
| PLTR | 1.586 | 125.61 | 121.23 | -1.86% | -6.95 (-3.49%) | 10% trail @114.55 |
| GXRP | 6.912 | 21.70 | 20.71 | +0.97% | -6.85 (-4.57%) | NO STOP on page |
| micro-remnants | — | — | — | — | AMZN -8.4%, META -9.6%, NBIS -11.4%, UNH -1.3%, QBTS -5.8%, IONQ -5.4%, RGTI -8.1%, DRAM -8.5%, IREN -13.3%, WULF -9.4%, CIFR -10.6% (~$596 total) | QBTS/IONQ/RGTI/DRAM stopped; AMZN/META/NBIS/UNH/IREN/WULF/CIFR NO STOP |

**Notes:** Day 17, Wednesday — busy buildout day, soft tape. Equity
$48,907.24, off -$551.97 (-1.12%) vs Alpaca's Jul-28 close of $49,459.21;
phase -$1,092.76 (-2.19%) vs the $50k Day-0 baseline. (Trade-log gap: no EOD
push landed Jul 27 or Jul 28, so the prior *logged* snapshot is Jul 24
$49,484.74 — Day P&L above uses Alpaca last_equity for a true one-day
figure.) 26 fills today: morning buildout added VOO/SCHD/SPMO ramps plus
full/rebuy buys across small targets (BRK.B, SOFI, PLTR, IREN, NBIS, IONQ,
DRAM, WULF, QBTS, RGTI, RIOT, CIFR); midday trimmed/cut SOFI, SPMO, APLD,
GLXY, RIOT, IREN, CIFR, WULF. All buys on-target. Growth-tilted cores led
the drag (QQQM -2.36% and now -7.14% unrealized — through the -7% manual-cut
line; SPMO -3.92%, SCHG -1.66%, VGT -2.49%); SCHD, SGOV, MSFT, GOOGL held up.
Weekly Mon–today trade count not reconstructable from log (Jul 27/28 pushes
missed); today alone 26 fills. No weekly cap — informational.

**CRITICAL / STOP-COVERAGE BROKEN — worsening, now ~6 days old.** The 50-order
page is 100% consumed by DUPLICATE trailing stops on 6 cores (SCHD 11, VOO 8,
BTC 7, SGOV 6, QQQM 5, SCHG 4 = 41; +SPMO 2, GOOGL/SOFI/PLTR/QBTS/IONQ/RGTI/
DRAM 1 each = 50). Consequence: ~11 HELD positions have NO trailing stop
visible on the page at all — VTV ($1.3k), MSFT ($877), ETH ($638), VGT ($615),
BRK.B ($492), VXUS ($437), GXRP ($143), AMZN, META, NBIS, UNH — i.e. the
strategy's "10% trail on every position, no exceptions" rule is being
violated for real, uncovered dollars. VOO/SCHD dup-stops also still sum to
LESS than the position (under-covered). Midday scans Jul 20–24 + this week
were each mandated to de-duplicate and have not; the situation is now
strictly worse (SCHD dups 10→11, VOO 7→8, and the newly-bought positions
added today got no stop). TOP PRIORITY for the next midday scan: cancel
duplicate stops (keep one per symbol, honor never-move-down), then place a
single full-position 10% trail on every currently-unstopped holding.
QQQM also warrants a manual-cut decision (-7.14%).

### Jul 30 — EOD Snapshot (Day 18, Thursday)
**Portfolio:** $49,675.66 | **Cash:** $6,656.83 (13.4%) | **Day P&L:** +$248.07 (+0.50%) | **Phase P&L:** -$324.34 (-0.65%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| SCHD | 256.019 | 32.92 | 33.38 | -1.34% | +117.26 (+1.39%) | 10% trail x10 (dup) |
| VOO | 12.309 | 685.03 | 682.05 | +1.70% | -36.62 (-0.43%) | 10% trail x7 (dup) |
| BTC | 190.407 | 28.20 | 28.67 | +2.10% | +88.73 (+1.65%) | 10% trail x5 (dup) |
| SGOV | 46.230 | 100.52 | 100.69 | +0.01% | +7.45 (+0.16%) | 10% trail x3 (dup) |
| QQQM | 13.856 | 292.01 | 281.77 | +3.40% | -141.94 (-3.51%) | 10% trail x3 (dup) — recovered above -7% cut |
| SCHG | 108.924 | 34.40 | 33.82 | +1.75% | -63.64 (-1.70%) | 10% trail x2 (dup) |
| VTV | 5.944 | 219.21 | 220.49 | +0.31% | +7.61 (+0.58%) | NO STOP |
| SPMO | 8.009 | 141.89 | 143.47 | +5.21% | +12.69 (+1.12%) | 10% trail x2 (dup) |
| MSFT | 2.197 | 393.50 | 456.45 | +16.88% | +138.33 (+16.00%) | 1 trail — tighten to 7% (+15% tier) |
| BRK.B | 1.943 | 508.11 | 508.46 | -0.14% | +0.70 (+0.07%) | 1 trail |
| ETH | 35.650 | 16.83 | 18.37 | +2.11% | +54.90 (+9.15%) | NO STOP |
| VGT | 5.693 | 114.17 | 113.64 | +5.02% | -3.07 (-0.47%) | NO STOP |
| GOOGL | 1.703 | 319.95 | 334.69 | -0.60% | +25.10 (+4.61%) | 1 trail |
| VXUS | 5.277 | 85.28 | 84.75 | +2.86% | -2.83 (-0.63%) | NO STOP |
| SOFI | 19.566 | 15.19 | 16.42 | +7.67% | +23.98 (+8.07%) | 1 trail |
| PLTR | 1.586 | 125.61 | 122.39 | -0.50% | -5.12 (-2.57%) | 1 trail |
| GXRP | 6.912 | 21.70 | 21.07 | +1.64% | -4.36 (-2.91%) | NO STOP |
| NBIS | 0.612 | 161.71 | 188.68 | +27.30% | +16.50 (+16.68%) | 1 stop (hard) |
| IREN | 2.849 | 34.34 | 37.23 | +27.02% | +8.23 (+8.42%) | 1 trail |
| APLD | 3.685 | 26.76 | 28.09 | +4.99% | +4.92 (+4.99%) | 1 trail |
| AMZN | 0.405 | 246.86 | 239.67 | +5.75% | -2.91 (-2.91%) | 1 stop (hard) |
| DRAM | 1.275 | 47.39 | 51.88 | +15.69% | +5.74 (+9.49%) | 1 trail |
| GLXY | 3.008 | 20.03 | 21.61 | +7.89% | +4.75 (+7.89%) | 1 trail |
| CIFR | 2.839 | 21.15 | 22.66 | +28.07% | +4.28 (+7.12%) | 1 trail |
| IONQ | 1.799 | 33.60 | 35.70 | +11.61% | +3.79 (+6.27%) | 1 trail |
| RIOT | 2.853 | 21.12 | 22.42 | +6.16% | +3.71 (+6.16%) | 1 trail |
| QBTS | 3.558 | 17.11 | 17.97 | +11.06% | +3.08 (+5.05%) | 1 trail |
| RGTI | 4.248 | 14.24 | 14.86 | +12.42% | +2.65 (+4.37%) | 1 trail |
| UNH | 0.143 | 425.73 | 422.98 | +0.57% | -0.39 (-0.65%) | 1 stop (hard) |
| WULF | 0.690 | 16.38 | 17.83 | +18.16% | +1.00 (+8.85%) | 1 stop (hard) |

**Notes:** Day 18, Thursday — firm recovery tape, broad green. Equity
$49,675.66, +$248.07 (+0.50%) vs Alpaca's Jul-29 close of $49,427.59; phase
-$324.34 (-0.65%) vs the $50k Day-0 baseline, best phase reading in over a
week. (Yesterday's *logged* snapshot was $48,907.24, captured mid-afternoon
before the close firmed; comparison vs Alpaca last_equity gives the true
one-day figure per prior convention.) No trades today — EOD summary only.
Growth names that dragged Wed rebounded hard: QQQM +3.40% (unrealized back
to -3.51%, recovered above the -7% manual-cut line), VGT +5.02%, SPMO
+5.21%, SCHG +1.75%; MSFT ripped +16.88% to +16.00% unrealized. Speculative
remnants ran (NBIS +27%, IREN +27%, CIFR +28%, DRAM +16%, WULF +18%).
SCHD was the lone core red (-1.34%). **STOP-COVERAGE — improving but still
broken.** Duplicate trails still consume most of the 50-order page (SCHD 10,
VOO 7, BTC 5, QQQM 3, SGOV 3, SCHG 2, SPMO 2 = 32 dup slots); 5 HELD
positions still carry NO stop — VTV ($1.3k), ETH ($655), VGT ($647), VXUS
($447), GXRP ($146). MSFT hit the +15% tier and should be tightened to a 7%
trail. TOP PRIORITY for next midday scan unchanged: de-dupe (keep one per
symbol, honor never-move-down), then place a single full-position 10% trail
on VTV/ETH/VGT/VXUS/GXRP, and tighten MSFT to 7%.

### 2026-07-31 — Midday stop-loss scan
No cuts (worst open: GXRP -4.98%, BTC -1.60%, RIOT -3.16% — all above the
-7% line). No orders placed by this scan. **STOP-COVERAGE now RESOLVED.**
The prior backlog was cleared by today's market-open run: every position
>=1 whole share carries trailing-stop coverage summing to its full
whole-share qty. The "duplicate" trails are actually complementary lot
stops (older lot + shares added since) that together = full position — not
redundant: BTC 160+36=196, SCHD 240+30=270, SCHG 79+29=108, SGOV 36+10=46,
QQQM 11+2=13, SPMO 10+1=11, VOO 12+1=13, VTV 2+3=5. Previously-uncovered
VTV/ETH/VGT/VXUS/GXRP all now fully covered; MSFT confirmed tightened to 7%
(+17.30%). Remaining stopless = 8 sub-1-share positions (AMZN, APLD, CIFR,
IREN, META, NBIS, RIOT, UNH; ~$470 total) — Alpaca only accepts whole-share
trailing stops here, so none is placeable until the lot ramps past 1 share;
these are governed by the -7% manual-cut rule at each scan meanwhile. Note
NBIS is a +16.3% winner sitting unprotected at 0.61 sh — will get a 7% trail
once it crosses 1 share.

### Jul 31 — EOD Snapshot (Day 19, Friday)
**Portfolio:** $49,610.02 | **Cash:** $5,094.34 (10.3%) | **Day P&L:** -$42.18 (-0.09%) | **Phase P&L:** -$389.98 (-0.78%)
| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
| AMZN | 0.405 | 246.86 | 270.25 | +14.76% | +9.47 (+9.48%) | NO STOP (sub-1sh) |
| APLD | 0.685 | 26.76 | 27.12 | -3.04% | +0.25 (+1.34%) | NO STOP (sub-1sh) |
| BRK.B | 1.943 | 508.11 | 511.88 | +0.43% | +7.33 (+0.74%) | 10% trail |
| BTC | 196.348 | 28.20 | 27.79 | -2.93% | -80.71 (-1.46%) | 2 trails (10%) |
| CIFR | 0.839 | 21.15 | 22.08 | -2.54% | +0.78 (+4.41%) | NO STOP (sub-1sh) |
| DRAM | 1.275 | 47.39 | 49.95 | -4.56% | +3.27 (+5.41%) | 10% trail |
| ETH | 35.650 | 16.83 | 17.76 | -3.06% | +33.13 (+5.52%) | 10% trail |
| GLXY | 3.008 | 20.03 | 21.00 | -2.42% | +2.92 (+4.84%) | 10% trail |
| GOOGL | 1.703 | 319.95 | 354.00 | +6.10% | +58.00 (+10.64%) | 10% trail |
| GXRP | 6.912 | 21.70 | 20.57 | -2.47% | -7.82 (-5.21%) | 10% trail |
| IONQ | 1.799 | 33.60 | 36.23 | +1.29% | +4.73 (+7.83%) | 10% trail |
| IREN | 0.849 | 34.34 | 36.66 | -4.18% | +1.97 (+6.76%) | NO STOP (sub-1sh) |
| META | 0.181 | 549.08 | 555.30 | +3.02% | +1.13 (+1.13%) | NO STOP (sub-1sh) |
| MSFT | 2.197 | 393.50 | 461.46 | +2.30% | +149.34 (+17.27%) | 7% trail |
| NBIS | 0.612 | 161.71 | 187.10 | -0.71% | +15.53 (+15.70%) | NO STOP (sub-1sh) |
| PLTR | 1.586 | 125.61 | 122.70 | +0.36% | -4.62 (-2.32%) | 10% trail |
| QBTS | 3.558 | 17.11 | 17.98 | -0.00% | +3.11 (+5.11%) | 10% trail |
| QQQM | 13.856 | 292.01 | 282.01 | +0.24% | -138.62 (-3.43%) | 2 trails (10%) |
| RGTI | 4.248 | 14.24 | 14.87 | +0.07% | +2.68 (+4.43%) | 10% trail |
| RIOT | 0.853 | 21.12 | 20.07 | -9.26% | -0.89 (-4.96%) | NO STOP (sub-1sh) |
| SCHD | 270.937 | 32.94 | 33.52 | +0.33% | +158.34 (+1.77%) | 2 trails (10%) |
| SCHG | 108.924 | 34.40 | 34.05 | +0.78% | -38.04 (-1.01%) | 2 trails (10%) |
| SGOV | 46.230 | 100.52 | 100.71 | +0.02% | +8.67 (+0.19%) | 2 trails (10%) |
| SOFI | 19.566 | 15.19 | 16.21 | -1.58% | +19.87 (+6.69%) | 10% trail |
| SPMO | 11.397 | 143.22 | 143.58 | +0.11% | +4.08 (+0.25%) | 2 trails (10%) |
| UNH | 0.143 | 425.73 | 414.07 | -1.76% | -1.67 (-2.74%) | NO STOP (sub-1sh) |
| VGT | 5.693 | 114.17 | 112.74 | -0.74% | -8.16 (-1.26%) | 10% trail |
| VOO | 13.034 | 684.99 | 684.79 | +0.44% | -2.60 (-0.03%) | 2 trails (10%) |
| VTV | 5.944 | 219.21 | 219.95 | -0.27% | +4.40 (+0.34%) | 2 trails (10%) |
| VXUS | 5.277 | 85.28 | 84.50 | -0.32% | -4.12 (-0.92%) | 10% trail |
| WULF | 3.322 | 17.85 | 17.65 | -0.95% | -0.65 (-1.10%) | 10% trail |
**Notes:** Day 19, Friday — quiet flat close, essentially unchanged
(-0.09% day vs Alpaca's Jul-30 last_equity of $49,652.20). Phase -0.78% vs
$50k baseline, holding near the recent best. No trades today (EOD summary
only; midday scan placed no orders, no cuts). Modest broad pullback in
speculative/crypto names (BTC -2.93%, ETH -3.06%, DRAM -4.56%, IREN -4.18%)
offset by mega-cap strength (GOOGL +6.10% to +10.64% unrealized, MSFT
holding +17.27%, AMZN +14.76% to +9.48%). RIOT was the day's weakest at
-9.26% but sits -4.96% unrealized, above the -7% manual-cut line. **STOP
COVERAGE: solid.** Every position >=1 whole share carries a full-qty
trailing stop (MSFT at 7% post-+15% tier; all others 10%; "2 trails" =
complementary lot stops = full position). Only remaining stopless names are
8 sub-1-share positions (AMZN, APLD, CIFR, IREN, META, NBIS, RIOT, UNH;
~$450 total) — Alpaca rejects fractional-share trailing stops, so each is
governed by the -7% manual-cut rule until it ramps past 1 share. NBIS
(+15.70%, 0.61sh) still the notable unprotected winner pending a >=1sh ramp.

### 2026-08-03 — Midday stop-loss scan
No cuts (worst opens: GXRP -3.46%, UNH -2.47%, RIOT -1.47% — all above the
-7% line). **Tightened 5 winners** that crossed a stop-ladder tier since
Fri, cancel-then-replace, each new stop verified > old (no stop moved
down), all live post-placement:
- MSFT +24.0% -> +20% tier -> 5% trail (was 7%); stop 456.96 -> 463.86
- IONQ +18.5% -> +15% tier -> 7% (was 10%); stop 36.14 -> 37.08
- GOOGL +17.3% -> +15% tier -> 7% (was 10%); stop 339.02 -> 349.23
- SOFI +16.7% -> +15% tier -> 7% (was 10%); stop 15.97 -> 16.56
- QBTS +16.7% -> +15% tier -> 7% (was 10%); stop 18.12 -> 18.58
**STOP COVERAGE: solid.** Every position >=1 whole share carries full-qty
trailing-stop coverage (re-verified: whole-share qty == summed stop qty for
all 25). Remaining stopless = 6 sub-1-share positions (AMZN, DRAM, META,
NBIS, RIOT, UNH) — Alpaca rejects fractional trailing stops, so each stays
under the -7% manual-cut rule until it ramps past 1 share. Notable
unprotected winners: NBIS +34.1% (0.61sh) and AMZN +15.4% (0.41sh) — both
awaiting a >=1sh ramp before a 5%/7% trail can be placed.

### Aug 03 — EOD Snapshot (Day 20, Monday)
**Portfolio:** $50,299.68 | **Cash:** $3,091.00 (6.1%) | **Day P&L:** +$689.66 (+1.39%) | **Phase P&L:** +$299.68 (+0.60%)
| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
| AMZN | 0.405 | 246.86 | 279.86 | +3.05% | +13.37 (+13.37%) | NO STOP (sub-1sh) |
| APLD | 3.673 | 27.32 | 29.94 | +9.31% | +9.64 (+9.61%) | 10% trail |
| BRK.B | 2.499 | 510.28 | 513.14 | +0.31% | +7.14 (+0.56%) | 2 trails (10%) |
| BTC | 199.845 | 28.19 | 28.05 | +0.86% | -28.59 (-0.51%) | 3 trails (10%) |
| CIFR | 2.761 | 22.03 | 23.94 | +7.26% | +5.28 (+8.68%) | 10% trail |
| DRAM | 0.275 | 47.39 | 51.60 | +2.44% | +1.16 (+8.89%) | NO STOP (sub-1sh) |
| ETH | 35.650 | 16.83 | 17.75 | -0.28% | +32.80 (+5.47%) | 10% trail |
| GLXY | 1.926 | 20.86 | 22.17 | +5.52% | +2.53 (+6.30%) | 10% trail |
| GOOGL | 1.703 | 319.95 | 371.82 | +4.41% | +88.36 (+16.21%) | 7% trail |
| GXRP | 6.912 | 21.70 | 20.94 | +1.80% | -5.26 (-3.51%) | 10% trail |
| IONQ | 1.799 | 33.60 | 39.52 | +8.45% | +10.65 (+17.63%) | 7% trail |
| IREN | 2.720 | 36.28 | 40.15 | +9.12% | +10.55 (+10.69%) | 10% trail |
| META | 0.181 | 549.08 | 589.65 | +5.92% | +7.35 (+7.39%) | NO STOP (sub-1sh) |
| MSFT | 2.197 | 393.50 | 483.46 | +4.03% | +197.68 (+22.86%) | 5% trail |
| NBIS | 0.612 | 161.71 | 216.00 | +13.44% | +33.21 (+33.57%) | NO STOP (sub-1sh) |
| PLTR | 1.586 | 125.61 | 143.01 | +16.21% | +27.60 (+13.85%) | 10% trail |
| QBTS | 3.558 | 17.11 | 20.01 | +10.67% | +10.34 (+16.98%) | 7% trail |
| QQQM | 13.856 | 292.01 | 288.84 | +1.96% | -43.98 (-1.09%) | 2 trails (10%) |
| RGTI | 4.248 | 14.24 | 16.09 | +7.62% | +7.86 (+13.00%) | 10% trail |
| RIOT | 0.853 | 21.12 | 21.50 | +6.59% | +0.32 (+1.80%) | NO STOP (sub-1sh) |
| SCHD | 285.732 | 32.97 | 33.57 | +0.29% | +170.24 (+1.81%) | 3 trails (10%) |
| SCHG | 108.924 | 34.40 | 34.86 | +2.02% | +49.64 (+1.32%) | 2 trails (10%) |
| SGOV | 46.230 | 100.52 | 100.42 | -0.28% | -4.57 (-0.10%) | 2 trails (10%) |
| SOFI | 19.566 | 15.19 | 18.01 | +10.42% | +55.09 (+18.53%) | 7% trail |
| SPMO | 14.892 | 143.05 | 146.00 | +1.51% | +43.90 (+2.06%) | 3 trails (10%) |
| UNH | 0.143 | 425.73 | 414.87 | +0.11% | -1.55 (-2.55%) | NO STOP (sub-1sh) |
| VGT | 5.693 | 114.17 | 115.59 | +2.15% | +8.05 (+1.24%) | 10% trail |
| VOO | 13.755 | 685.29 | 697.05 | +1.52% | +161.73 (+1.72%) | 2 trails (10%) |
| VTV | 5.944 | 219.21 | 221.21 | +0.57% | +11.89 (+0.91%) | 2 trails (10%) |
| VXUS | 5.277 | 85.28 | 85.05 | +0.54% | -1.22 (-0.27%) | 10% trail |
| WULF | 3.322 | 17.85 | 19.04 | +7.81% | +3.97 (+6.69%) | 10% trail |
**Notes:** Day 20, Monday — strong risk-on session, +1.39% day (vs Fri EOD
$49,610.02), new phase high at +0.60% ($50,299.68). Market-open buildout
executed 9 ramp buys totaling ~$2,113 (VOO/SCHD/SPMO $498 ea, BRK.B $288,
BTC $97, APLD $82, IREN $69, CIFR $43, GLXY $40) toward target weights,
each getting a fresh 10% GTC trail; cash drawn to $3,091 (6.1%). Two
trailing stops triggered intraday on brief dips then names rebounded: DRAM
(sold 1 whole sh @48.05, closed 51.60) and GLXY (sold 3 sh @20.51, then
$40 buildout re-buy, closed 22.17) — both re-enter buildout queue per rule.
Broad strength led by high-beta/AI names (PLTR +16.2%, NBIS +13.4%, QBTS
+10.7%, SOFI +10.4%, IREN +9.1%, APLD +9.3%, IONQ +8.5%); mega-caps firm
(MSFT +22.86% unrealized, GOOGL +16.21%). Only laggards SGOV/VXUS flat-red,
BTC -0.51% unrealized. **STOP COVERAGE: solid.** All 27 positions >=1 whole
share carry full-qty trailing coverage (whole-share qty == summed stop qty;
MSFT 5%, GOOGL/IONQ/QBTS/SOFI 7%, rest 10%). Remaining stopless = 6
sub-1-share positions (AMZN, DRAM, META, NBIS, RIOT, UNH; ~$450) — Alpaca
rejects fractional trailing stops, each governed by the -7% manual-cut rule
until it ramps past 1 share. NBIS (+33.57%, 0.61sh) still the notable
unprotected winner pending a >=1sh ramp.
