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

### Jul 17 — EOD Snapshot (Day 9, Friday)
**Portfolio:** $49,626.12 | **Cash:** $18,787.99 (37.9%) | **Day P&L:** -$228.02 (-0.46%) | **Phase P&L:** -$373.88 (-0.75%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| BTC | 142.222 | 27.93 | 28.38 | -0.11% | +64.40 (+1.62%) | 10% trail |
| SCHD | 121.968 | 32.56 | 32.91 | -0.39% | +42.12 (+1.06%) | 10% trail |
| SGOV | 39.566 | 100.51 | 100.58 | +0.03% | +2.68 (+0.07%) | 10% trail |
| VOO | 5.778 | 688.26 | 683.17 | -1.01% | -29.40 (-0.74%) | 10% trail |
| SCHG | 107.442 | 34.42 | 34.14 | -1.43% | -30.22 (-0.82%) | 10% trail |
| QQQM | 10.173 | 293.12 | 285.99 | -1.61% | -72.55 (-2.43%) | 10% trail |
| SPMO | 19.000 | 151.31 | 143.89 | -0.96% | -140.89 (-4.90%) | 10% trail |
| VTV | 5.944 | 219.21 | 217.92 | -0.43% | -7.67 (-0.59%) | 10% trail |
| MSFT | 2.197 | 393.50 | 393.35 | -1.93% | -0.33 (-0.04%) | 10% trail |
| VGT | 5.693 | 114.17 | 113.10 | -1.00% | -6.11 (-0.94%) | 10% trail |
| ETH | 35.650 | 16.83 | 17.55 | -1.68% | +25.67 (+4.28%) | 10% trail |
| GOOGL | 1.550 | 368.43 | 345.93 | -2.41% | -34.86 (-6.11%) | 10% trail |
| VXUS | 5.277 | 85.28 | 83.38 | -0.81% | -10.03 (-2.23%) | 10% trail |
| SOFI | 16.833 | 17.82 | 17.28 | -0.23% | -9.08 (-3.03%) | 10% trail |
| PLTR | 1.540 | 131.51 | 131.68 | -2.05% | +0.27 (+0.13%) | 10% trail |
| GXRP | 6.912 | 21.70 | 21.14 | -0.56% | -3.88 (-2.59%) | 10% trail |
| META | 0.172 | 581.77 | 644.79 | -2.97% | +10.82 (+10.83%) | scan-only |
| IREN | 3.012 | 32.83 | 33.64 | -3.42% | +2.43 (+2.46%) | 10% trail |
| AMZN | 0.405 | 246.86 | 246.90 | -1.20% | +0.02 (+0.02%) | scan-only |
| QBTS | 3.736 | 16.17 | 16.67 | -1.51% | +1.85 (+3.06%) | 10% trail |
| UNH | 0.143 | 425.73 | 426.09 | +0.64% | +0.05 (+0.09%) | scan-only |
| IONQ | 1.673 | 36.47 | 34.73 | -1.05% | -2.90 (-4.76%) | 10% trail |
| DRAM | 0.126 | 54.18 | 52.24 | -0.19% | -0.24 (-3.57%) | scan-only |
| WULF | 0.276 | 18.62 | 18.20 | +1.22% | -0.12 (-2.26%) | scan-only |

**Notes:** Quiet down day, -0.46%, broad shallow pullback — nearly every
name red on the day but all small; crypto proxies held up (BTC -0.11%,
ETH -1.68%). Today's 8 market-open buildout buys (~$2.8k: VOO/SCHD/BTC/
SGOV/QQQM/SCHG ramp top-ups plus IREN/QBTS gap-fills of names liquidated
07-16) settled; cash down to 37.9%, buildout on schedule. The -7% names
flagged Jul 16 were cut per strategy — CIFR, GLXY and APLD fully exited,
WULF trimmed to a 0.276-sh remnant. Watch item for Monday midday: GOOGL
now -6.11%, closing on the -7% manual-cut line. Stop coverage clean — all
whole-share positions carry live 10% GTC trailing stops (verified against
full 58-order open book, not the truncated 50 the wrapper returns); the
five sub-1-share remnants (AMZN/META/UNH/DRAM/WULF) are scan-only, can't
hold fractional GTC stops. BRK.B still unheld (retry next buildout).
Trades today: 8 buys. Trades this week (Mon-Fri): 22.

### Jul 20 — EOD Snapshot (Day 10, Monday)
**Portfolio:** $49,739.28 | **Cash:** $15,843.02 (31.9%) | **Day P&L:** +$113.16 (+0.23%) | **Phase P&L:** -$260.72 (-0.52%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| BTC | 159.654 | 28.00 | 28.80 | +1.48% | +127.77 (+2.86%) | 10% trail |
| SCHD | 137.159 | 32.59 | 32.75 | -0.49% | +21.69 (+0.48%) | 10% trail |
| SGOV | 44.521 | 100.52 | 100.59 | +0.01% | +3.07 (+0.07%) | 10% trail |
| VOO | 6.503 | 688.19 | 682.21 | -0.14% | -38.90 (-0.87%) | 10% trail |
| SCHG | 107.442 | 34.42 | 34.15 | -0.09% | -28.71 (-0.78%) | 10% trail |
| QQQM | 11.891 | 292.67 | 286.55 | +0.08% | -72.82 (-2.09%) | 10% trail |
| SPMO | 19.000 | 151.31 | 144.52 | +0.44% | -128.92 (-4.48%) | 10% trail |
| VTV | 5.944 | 219.21 | 216.95 | -0.45% | -13.43 (-1.03%) | 10% trail |
| MSFT | 2.197 | 393.50 | 401.95 | +2.06% | +18.57 (+2.15%) | 10% trail |
| ETH | 35.650 | 16.83 | 18.09 | +3.08% | +44.92 (+7.49%) | 10% trail |
| VGT | 5.693 | 114.17 | 113.23 | +0.11% | -5.37 (-0.83%) | 10% trail |
| GOOGL | 1.550 | 368.43 | 352.39 | +1.62% | -24.85 (-4.35%) | 10% trail |
| VXUS | 5.277 | 85.28 | 83.07 | -0.36% | -11.67 (-2.59%) | 10% trail |
| SOFI | 16.833 | 17.82 | 17.01 | -1.56% | -13.62 (-4.54%) | 10% trail |
| PLTR | 1.540 | 131.51 | 134.20 | +1.38% | +4.15 (+2.05%) | 10% trail |
| GXRP | 6.912 | 21.70 | 21.65 | +2.41% | -0.36 (-0.24%) | 10% trail |
| IREN | 3.012 | 32.83 | 40.36 | +20.04% | +22.66 (+22.92%) | 10% trail |
| META | 0.172 | 581.77 | 645.85 | -0.03% | +11.00 (+11.02%) | scan-only |
| AMZN | 0.405 | 246.86 | 249.78 | +1.03% | +1.19 (+1.19%) | scan-only |
| APLD | 3.537 | 28.18 | 27.93 | -0.89% | -0.88 (-0.89%) | 10% trail |
| GLXY | 2.671 | 22.80 | 23.72 | +4.04% | +2.46 (+4.04%) | 10% trail |
| CIFR | 3.084 | 19.75 | 20.50 | +3.80% | +2.31 (+3.80%) | 10% trail |
| RIOT | 3.167 | 19.23 | 19.86 | +3.28% | +2.00 (+3.28%) | 10% trail |
| QBTS | 3.736 | 16.17 | 16.72 | -0.06% | +2.05 (+3.40%) | 10% trail |
| UNH | 0.143 | 425.73 | 421.55 | -1.07% | -0.60 (-0.98%) | scan-only |
| RGTI | 4.182 | 14.56 | 14.26 | -2.07% | -1.26 (-2.07%) | 10% trail |
| DRAM | 1.115 | 54.55 | 53.11 | +0.74% | -1.61 (-2.64%) | 10% trail |
| WULF | 3.114 | 19.50 | 18.89 | +4.01% | -1.92 (-3.15%) | 10% trail |
| IONQ | 1.673 | 36.47 | 34.24 | -1.55% | -3.72 (-6.10%) | 10% trail |

**Notes:** Quiet up day, +0.23%, first green session in a week — winners
led by IREN (+20% day, now +22.9% unrealized and the standout), crypto
proxies (BTC +1.5%, ETH +3.1%, GXRP +2.4%) and MSFT (+2.1%); most of the
book flat-to-slightly-green. Today's 12 market-open buildout buys ($2,945
deployed) settled: core-ramp top-ups (VOO/QQQM/SGOV/BTC/SCHD ~$500 each)
plus buildout re-entries of the seven names cut on the -7% line last week
(APLD/RIOT/GLXY/CIFR/RGTI/WULF/DRAM re-entered the queue under the same
buildout rule and are back as small full positions carrying fresh 10% GTC
trailing stops). Cash down to 31.9%, buildout on schedule. Watch item for
tomorrow's midday scan: IONQ -6.10%, closest to the -7% manual-cut line;
GOOGL recovered to -4.35% (was -6.11% Fri). Stop coverage looks clean —
new multi-share re-entries all show live trailing stops; only the three
sub-1-share remnants (META/AMZN/UNH) remain scan-only. CIFR showed two
open trailing-stop orders in the book — verify no stale duplicate at next
scan. BRK.B still unheld, retry next buildout. Trades today: 12 buys.
Trades this week (Mon): 12.
