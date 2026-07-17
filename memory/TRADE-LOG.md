# Trade Log

## Day 0 — EOD Snapshot (strategy relaunch baseline)
**Portfolio:** $50,000.00 | **Cash:** $50,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0

Paper account reset to $50,000 / no positions for the new target-portfolio
strategy (see memory/TARGET-PORTFOLIO.json). Prior swing-trading history
has been retired — this is a clean baseline, not a continuation.

## 2026-07-07 — Market-Open Buildout (Day 1)

First buildout day off the Day-0 baseline. 26 of 31 target names bought;
5 skipped at the open on abnormally wide top-of-book spreads (BRK.B, META,
UNH, IONQ, GLXY — opening-auction noise, ~5-6% spread; retry next
buildout). Ramp symbols sized at 1% of equity/day; non-ramp bought to full
target. 6 ramp orders (SCHD, BTC, QQQM, SCHG, SPMO, VTV) first rejected at
$500 when equity dipped a few dollars below $50k after early fills (1% cap
fell under $500) — re-sized to $495 and filled. Stops: 10% GTC trailing
placed on the whole-share (floor) portion of each position (Alpaca rejects
fractional GTC/trailing-stop, 422). AMZN, NBIS, VOO hold <1 whole share so
NO stop could be placed — queued for tomorrow AM (VOO resolves as its ramp
crosses 1 share; AMZN/NBIS at $100 target sit at ~0.4-0.5 sh and may need a
different exit approach). Small fractional remainders on stopped positions
are unprotected (negligible $).

## Open Positions

| Date | Ticker | Side | Shares/Notional | Entry | Stop | Target Weight | Ramp? | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-07-07 | VOO   | buy | $500     | 688.852  | ⚠ NONE (<1 sh)   | 23.8%   | yes | buildout; stop blocked, set tomorrow AM |
| 2026-07-07 | SCHD  | buy | $495     | 32.6886  | 10% trail @29.43  | 19.9%   | yes | buildout ramp; re-sized from $500 (cap) |
| 2026-07-07 | BTC   | buy | $495     | 27.8642  | 10% trail @25.07  | 11.1%   | yes | buildout ramp; GBTC-mini equity ETF; re-sized |
| 2026-07-07 | SGOV  | buy | $500     | 100.46   | 10% trail @90.41  | 9.3%    | yes | buildout ramp |
| 2026-07-07 | QQQM  | buy | $495     | 293.664  | 10% trail @263.73 | 7.8%    | yes | buildout ramp; re-sized from $500 (cap) |
| 2026-07-07 | SCHG  | buy | $495     | 34.4330  | 10% trail @30.96  | 7.4%    | yes | buildout ramp; re-sized from $500 (cap) |
| 2026-07-07 | SPMO  | buy | $495     | 149.18   | 10% trail @133.81 | 5.6%    | yes | buildout ramp; re-sized from $500 (cap) |
| 2026-07-07 | VTV   | buy | $495     | 220.56   | 10% trail @198.47 | 2.6%    | yes | buildout ramp; re-sized from $500 (cap) |
| 2026-07-07 | MSFT  | buy | $850     | 393.58   | 10% trail @354.30 | 1.7%    | no  | buildout full target |
| 2026-07-07 | VGT   | buy | $650     | 114.174  | 10% trail @102.55 | 1.3%    | no  | buildout full target |
| 2026-07-07 | ETH   | buy | $600     | 16.83    | 10% trail @15.14  | 1.2%    | no  | buildout; GETH-mini equity ETF |
| 2026-07-07 | GOOGL | buy | $550     | 368.932  | 10% trail @332.54 | 1.1%    | no  | buildout full target |
| 2026-07-07 | VXUS  | buy | $450     | 85.2816  | 10% trail @76.74  | 0.9%    | no  | buildout full target |
| 2026-07-07 | SOFI  | buy | $300     | 18.5642  | 10% trail @16.69  | 0.6%    | no  | buildout full target |
| 2026-07-07 | PLTR  | buy | $200     | 134.596  | 10% trail @120.33 | 0.4%    | no  | buildout full target |
| 2026-07-07 | GXRP  | buy | $150     | 21.7014  | 10% trail @19.57  | 0.3%    | no  | buildout; XRP proxy ETF |
| 2026-07-07 | APLD  | buy | $100     | 32.7164  | 10% trail @29.43  | 0.2%    | no  | buildout full target |
| 2026-07-07 | IREN  | buy | $100     | 41.94    | 10% trail @37.76  | 0.2%    | no  | buildout full target |
| 2026-07-07 | NBIS  | buy | $100     | 200.766  | ⚠ NONE (<1 sh)   | 0.2%    | no  | buildout; stop blocked, set tomorrow AM |
| 2026-07-07 | AMZN  | buy | $100     | 246.858  | ⚠ NONE (<1 sh)   | 0.2%    | no  | buildout; stop blocked, set tomorrow AM |
| 2026-07-07 | RGTI  | buy | $61.10   | 17.28    | 10% trail @15.48  | 0.1222% | no  | buildout spec basket |
| 2026-07-07 | QBTS  | buy | $61.10   | 21.92    | 10% trail @19.58  | 0.1222% | no  | buildout spec basket |
| 2026-07-07 | DRAM  | buy | $61.10   | 59.608   | 10% trail @53.96  | 0.1222% | no  | buildout spec basket |
| 2026-07-07 | WULF  | buy | $61.10   | 21.30    | 10% trail @19.21  | 0.1222% | no  | buildout spec basket |
| 2026-07-07 | CIFR  | buy | $61.10   | 20.96    | 10% trail @18.80  | 0.1222% | no  | buildout spec basket |
| 2026-07-07 | RIOT  | buy | $61.10   | 22.22    | 10% trail @19.86  | 0.1222% | no  | buildout spec basket |

### Skipped this run (wide spread at open — retry next buildout)
| Ticker | Target | Ramp? | Reason |
|---|---|---|---|
| BRK.B | 2.6%    | yes | ~5.9% top-of-book spread at open (thin 40-sh book), not filled |
| META  | 0.2%    | no  | ~5.1% spread at open |
| UNH   | 0.1222% | no  | ~5.9% spread at open |
| IONQ  | 0.1222% | no  | ~5.0% spread at open |
| GLXY  | 0.1222% | no  | ~5.2% spread at open |

## 2026-07-08 — Midday Stop-Loss Scan

Cut 3 losers at the -7% rule (market SELL, wrapper cancelled each symbol's
trailing stop first). No winners at the +15%/+20% tighten tiers. Positions
now zeroed re-enter the buildout queue at the NEXT market-open per the
normal buildout/ramp rule — no rebuy this session (avoid whipsaw).

### Exits (cut at -7% per rule)
| Date | Ticker | Side | Shares | Exit | Realized P&L | Note |
|---|---|---|---|---|---|---|
| 2026-07-08 | APLD | sell | 3.056269113 | $30.27 | -$7.48 (-7.5%)  | cut at -7% per rule; spec/small buildout name, refill next open |
| 2026-07-08 | QBTS | sell | 2.786952554 | $20.30 | -$4.51 (-7.4%)  | cut at -7% per rule; spec basket, refill next open |
| 2026-07-08 | RIOT | sell | 2.749324932 | $20.61 | -$4.43 (-7.3%)  | cut at -7% per rule; spec basket, refill next open |

### ⚠ Stop-integrity flag — sub-1-share positions cannot hold a GTC stop
AMZN, NBIS, UNH each hold <1 whole share (0.41 / 0.50 / 0.14 sh). Alpaca
rejects fractional GTC/trailing-stop orders (422 "fractional orders must be
DAY orders"), so a 10% GTC trailing stop is PERMANENTLY impossible at these
target weights (AMZN 0.2% @ ~$242/sh, NBIS 0.2% @ ~$207/sh, UNH 0.1222% @
~$429/sh — none will ever reach 1 whole share). This is structural, not a
"set tomorrow AM" retry. These 3 positions (~$262 total, ~0.5% of equity)
are protected only by the daily -7% manual-cut scan (this routine), not by
a resting stop. Needs a human decision: accept scan-only coverage, or drop
these sub-1-share names from the target list. All other positions retain
their whole-share 10% GTC trailing stops (verified live).

## 2026-07-16 — Market-Open Buildout

Day-N buildout. Ramp symbols took next 1% allowance ($495 each; SPMO $99
to close its small gap). Rebuilt zeroed/remnant non-ramp names to full
target. BRK.B skipped — 3.0% top-of-book spread (ap 500 / bp 485, thin
40-sh book), retry later. Trivial gaps (<$10: VXUS, NBIS, RGTI, QBTS,
RIOT, GXRP, VTV) left as noise. Trailing stops placed for each position's
net-new whole shares (added as fresh 10% GTC layers over existing
partitioned coverage — no existing stop moved). VOO reached 5 whole shares,
now fully covered by its 5 resting qty-1 stops.

| Date | Ticker | Side | Shares/Notional | Entry | Stop | Target Weight | Ramp? | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-07-16 | VOO   | buy | $495     | 691.24  | covered (5 sh, existing stops) | 23.8%   | yes | ramp top-up |
| 2026-07-16 | SCHD  | buy | $495     | 32.84   | 10% trail (+15 sh)  | 19.9%   | yes | ramp top-up |
| 2026-07-16 | BTC   | buy | $495     | 28.43   | 10% trail (+18 sh)  | 11.1%   | yes | ramp top-up |
| 2026-07-16 | SGOV  | buy | $495     | 100.55  | 10% trail (+5 sh)   | 9.3%    | yes | ramp top-up |
| 2026-07-16 | QQQM  | buy | $495     | 292.66  | 10% trail (+2 sh)   | 7.8%    | yes | ramp top-up |
| 2026-07-16 | SCHG  | buy | $495     | 34.74   | 10% trail (+14 sh)  | 7.4%    | yes | ramp top-up |
| 2026-07-16 | SPMO  | buy | $99      | 147.28  | 10% trail (+1 sh)   | 5.6%    | yes | ramp gap-close |
| 2026-07-16 | SOFI  | buy | $297     | 17.81   | 10% trail @16.03    | 0.6%    | no  | rebuild (was remnant) |
| 2026-07-16 | APLD  | buy | $99.90   | 27.78   | 10% trail @25.00    | 0.2%    | no  | gap-fill (was zero) |
| 2026-07-16 | IREN  | buy | $79.80   | 37.05   | 10% trail @33.35    | 0.2%    | no  | top-up (was remnant) |
| 2026-07-16 | IONQ  | buy | $61      | 36.47   | 10% trail @32.82    | 0.1222% | no  | gap-fill (was zero) |
| 2026-07-16 | DRAM  | buy | $61      | 54.19   | 10% trail @48.77    | 0.1222% | no  | gap-fill (was zero) |
| 2026-07-16 | WULF  | buy | $61      | 18.62   | 10% trail @16.76    | 0.1222% | no  | gap-fill (was zero) |
| 2026-07-16 | CIFR  | buy | $60      | 19.08   | 10% trail @17.17    | 0.1222% | no  | rebuild (was remnant) |

### Skipped this run
| Ticker | Target | Reason |
|---|---|---|
| BRK.B | 2.6% | 3.0% top-of-book spread at open (thin 40-sh book) — retry later |

## 2026-07-17 — Market-Open Buildout

Day-N buildout. Ramp symbols took next 1% allowance ($494 each; SCHG $220
gap-capped). Rebuilt two liquidated non-ramp names (IREN, QBTS) to full
target — the other three (NBIS, RGTI, RIOT) and the GLXY remnant skipped on
wide open spreads. BRK.B skipped again (3.0% spread, ap 500 / bp 485).
Trailing stops placed for each position's net-new whole shares (fresh 10%
GTC layers over existing partitioned coverage — no existing stop moved).
VOO already fully covered by its resting qty-1 stops. Note: 07-16 10%
trailing stops on WULF/APLD/CIFR (created 07-16) triggered at today's open
on a down morning — legitimate stop fills, NOT a repeat of the 07-16
after-hours liquidation anomaly.

| Date | Ticker | Side | Shares/Notional | Entry | Stop | Target Weight | Ramp? | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-07-17 | VOO   | buy | $494 / 0.7252 sh   | 681.19  | covered (5 sh, existing stops) | 23.8%   | yes | ramp top-up |
| 2026-07-17 | SCHD  | buy | $494 / 14.884 sh   | 33.19   | 10% trail (+14 sh)  | 19.9%   | yes | ramp top-up |
| 2026-07-17 | BTC   | buy | $494 / 17.830 sh   | 27.705  | 10% trail (+18 sh)  | 11.1%   | yes | ramp top-up |
| 2026-07-17 | SGOV  | buy | $494 / 4.911 sh    | 100.58  | 10% trail (+5 sh)   | 9.3%    | yes | ramp top-up |
| 2026-07-17 | QQQM  | buy | $494 / 1.738 sh    | 284.19  | 10% trail (+2 sh)   | 7.8%    | yes | ramp top-up |
| 2026-07-17 | SCHG  | buy | $220 / 6.462 sh    | 34.044  | 10% trail (+7 sh)   | 7.4%    | yes | ramp gap-close |
| 2026-07-17 | IREN  | buy | $98.89 / 3.012 sh  | 32.833  | 10% trail (+3 sh)   | 0.2%    | no  | gap-fill (was zero, liquidated 07-16) |
| 2026-07-17 | QBTS  | buy | $60.42 / 3.736 sh  | 16.17   | 10% trail (+3 sh)   | 0.1222% | no  | gap-fill (was zero, liquidated 07-16) |

### Skipped this run (wide spread at open — retry next buildout)
| Ticker | Target | Reason |
|---|---|---|
| BRK.B | 2.6%    | 3.0% spread (ap 500 / bp 485, thin 40-sh book) |
| NBIS  | 0.2%    | 12.4% spread (ap 187.83 / bp 164.50) — was zero, rebuy deferred |
| RGTI  | 0.1222% | 13.3% spread (ap 13.53 / bp 11.73) — was zero, rebuy deferred |
| RIOT  | 0.1222% | 12.6% spread (ap 17.72 / bp 15.48) — was zero, rebuy deferred |
| GLXY  | 0.1222% | 5.3% spread (ap 21.41 / bp 20.28) — remnant top-up deferred |

## Jul 16 — EOD Snapshot (Day 8, Thursday)
**Portfolio:** $49,854.14 | **Cash:** $21,381.33 (42.9%) | **Day P&L:** -$245.36 (-0.49%) | **Phase P&L:** -$145.86 (-0.29%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| SCHD | 107.085 | 32.48 | 33.04 | +2.16% | +60.16 (+1.73%) | $29.74 |
| BTC | 124.392 | 27.96 | 28.41 | -1.08% | +56.10 (+1.61%) | $26.09 |
| SCHG | 100.980 | 34.44 | 34.63 | -0.77% | +19.08 (+0.55%) | $31.43 |
| SGOV | 34.654 | 100.50 | 100.54 | +0.00% | +1.29 (+0.04%) | $90.50 |
| VOO | 5.053 | 689.27 | 689.46 | -0.63% | +0.95 (+0.03%) | $625.00 |
| SPMO | 19.000 | 151.31 | 145.28 | -3.15% | -114.48 (-3.98%) | $139.62 |
| QQQM | 8.435 | 294.96 | 290.39 | -1.75% | -38.55 (-1.55%) | $269.14 |
| VTV | 5.944 | 219.21 | 218.86 | +0.63% | -2.08 (-0.16%) | $198.63 |
| MSFT | 2.197 | 393.50 | 401.42 | +1.46% | +17.41 (+2.01%) | 10% trail |
| VGT | 5.693 | 114.17 | 114.24 | -1.94% | +0.38 (+0.06%) | $106.45 |
| ETH | 35.650 | 16.83 | 17.85 | -2.57% | +36.36 (+6.06%) | 10% trail |
| GOOGL | 1.550 | 368.43 | 355.28 | -4.22% | -20.37 (-3.57%) | 10% trail |
| VXUS | 5.277 | 85.28 | 84.23 | -0.89% | -5.55 (-1.23%) | $76.93 |
| SOFI | 16.833 | 17.82 | 17.37 | -2.80% | -7.56 (-2.52%) | $16.05 |
| PLTR | 1.540 | 131.51 | 133.88 | +0.09% | +3.66 (+1.81%) | $122.23 |
| GXRP | 6.912 | 21.70 | 21.26 | -1.12% | -3.05 (-2.03%) | 10% trail |
| META | 0.172 | 581.77 | 664.50 | -2.47% | +14.21 (+14.22%) | scan-only* |
| AMZN | 0.405 | 246.86 | 249.69 | -2.07% | +1.15 (+1.15%) | scan-only* |
| APLD | 3.596 | 27.78 | 26.55 | -4.43% | -4.42 (-4.43%) | $25.17 |
| UNH | 0.143 | 425.73 | 422.84 | +1.03% | -0.41 (-0.68%) | scan-only* |
| IONQ | 1.673 | 36.47 | 35.33 | -3.12% | -1.90 (-3.12%) | $32.90 |
| WULF | 3.276 | 18.62 | 17.94 | -3.65% | -2.23 (-3.65%) | $16.81 |
| DRAM | 1.126 | 54.18 | 52.17 | -3.71% | -2.26 (-3.71%) | $49.09 |
| CIFR | 3.199 | 19.10 | 17.64 | -11.22% | -4.66 (-7.62%) | $17.23 |
| GLXY | 0.571 | 23.93 | 22.12 | -10.01% | -1.04 (-7.58%) | scan-only* |

**Notes:** Quiet down day, -0.49%, driven by broad small pullback across
crypto proxies (BTC/ETH day -1 to -2.6%) and spec/quantum names; SCHD and
MSFT the only real green. Today's 14 market-open buildout buys ($3.3k
deployed) settled — buildout continues on schedule, cash now 42.9%. Two
names closed past the -7% manual-cut line and warrant a look at tomorrow's
midday scan: CIFR -7.62% (day -11.2%, near its $17.23 stop) and GLXY -7.58%
(sub-1-share, scan-only). *scan-only = sub-1-share position that cannot
hold a GTC trailing stop (Alpaca rejects fractional stops); protected by
the daily -7% manual scan only — pending the human decision flagged Jul 8.
BRK.B still unheld (skipped at open on a 3% spread), retry next buildout.
Trades today: 14. Trades this week (Mon-Thu): 14.
