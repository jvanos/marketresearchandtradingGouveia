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

### Jul 21 — EOD Snapshot (Day 11, Tuesday)
**Portfolio:** $50,144.23 | **Cash:** $13,842.65 (27.6%) | **Day P&L:** +$404.95 (+0.81%) | **Phase P&L:** +$144.23 (+0.29%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| BTC | 176.657 | 28.14 | 29.38 | +2.01% | +219.93 (+4.42%) | 10% trail |
| SCHD | 152.449 | 32.60 | 32.82 | +0.21% | +33.12 (+0.67%) | 10% trail |
| VOO | 7.232 | 687.92 | 687.58 | +0.79% | -2.47 (-0.05%) | 10% trail |
| SGOV | 46.230 | 100.52 | 100.59 | +0.01% | +3.29 (+0.07%) | 10% trail |
| QQQM | 13.439 | 292.45 | 291.75 | +1.80% | -9.41 (-0.24%) | 10% trail |
| SCHG | 107.442 | 34.42 | 34.27 | +0.35% | -15.81 (-0.43%) | 10% trail |
| SPMO | 19.000 | 151.31 | 149.71 | +3.59% | -30.31 (-1.05%) | 10% trail |
| VTV | 5.944 | 219.21 | 218.63 | +0.77% | -3.45 (-0.26%) | 10% trail |
| MSFT | 2.197 | 393.50 | 397.60 | -1.17% | +9.01 (+1.04%) | 10% trail |
| VGT | 5.693 | 114.17 | 116.01 | +2.46% | +10.45 (+1.61%) | 10% trail |
| ETH | 35.650 | 16.83 | 18.33 | +1.33% | +53.48 (+8.91%) | 10% trail |
| GOOGL | 1.550 | 368.43 | 347.77 | -1.20% | -32.01 (-5.61%) | 10% trail |
| VXUS | 5.277 | 85.28 | 84.45 | +1.66% | -4.39 (-0.97%) | 10% trail |
| SOFI | 16.833 | 17.82 | 17.64 | +3.70% | -3.02 (-1.01%) | 10% trail |
| PLTR | 1.540 | 131.51 | 132.40 | -1.82% | +1.38 (+0.68%) | 10% trail |
| GXRP | 6.912 | 21.70 | 22.39 | +3.42% | +4.76 (+3.17%) | 10% trail |
| META | 0.172 | 581.77 | 642.52 | -0.52% | +10.43 (+10.44%) | scan-only |
| APLD | 3.537 | 28.18 | 30.50 | +9.52% | +8.21 (+8.23%) | 10% trail |
| AMZN | 0.405 | 246.86 | 247.38 | -1.04% | +0.21 (+0.21%) | scan-only |
| CIFR | 3.084 | 19.75 | 22.95 | +11.73% | +9.87 (+16.21%) | 10% trail |
| RIOT | 3.167 | 19.23 | 21.50 | +8.04% | +7.19 (+11.80%) | 10% trail |
| GLXY | 2.671 | 22.80 | 25.44 | +7.52% | +7.05 (+11.58%) | 10% trail |
| QBTS | 3.736 | 16.17 | 17.86 | +6.82% | +6.31 (+10.45%) | 10% trail |
| DRAM | 1.115 | 54.55 | 58.95 | +11.10% | +4.91 (+8.06%) | 10% trail |
| RGTI | 4.182 | 14.56 | 15.36 | +7.79% | +3.34 (+5.49%) | 10% trail |
| UNH | 0.143 | 425.73 | 437.00 | +3.67% | +1.62 (+2.65%) | scan-only |
| WULF | 3.114 | 19.50 | 19.98 | +5.94% | +1.48 (+2.44%) | 10% trail |
| IONQ | 1.673 | 36.47 | 35.72 | +4.32% | -1.25 (-2.05%) | 10% trail |
| IREN | 0.012 | 32.83 | 41.28 | +2.68% | +0.10 (+25.71%) | scan-only |

**Notes:** Strong green session, +$404.95 (+0.81%), second up day in a row
— phase P&L flips positive (+$144.23, +0.29%) for the first time since early
buildout. Broad-based: miners/quantum re-entries led (CIFR +11.7%, DRAM
+11.1%, APLD +9.5%, RIOT +8.0%, RGTI +7.8%, GLXY +7.5%, QBTS +6.8%, WULF
+5.9%), plus crypto proxies (GXRP +3.4%, BTC +2.0%, ETH +1.3%) and SPMO
+3.6%/SOFI +3.7%. IREN's 10% trailing stop TRIGGERED intraday, selling the
3-sh position at $40.53 (booked the +20% winner) — now a 0.012-sh remnant,
scan-only. 5 buildout buys settled (~$2,122): core-ramp top-ups VOO/BTC/SCHD
$500 ea, QQQM $450, SGOV $172; cash down to 27.6%. Watch items for tomorrow:
(1) GOOGL -5.61%, still the weakest name and nearest the -7% manual-cut line
(recovered slightly from -6.11% Fri); (2) duplicate trailing-stop
accumulation is growing across core positions (SGOV/QQQM/BTC/SCHD 6 each,
VOO/SCHG 5, SPMO 4, CIFR 2 in the truncated 50-order book) — buildout adds
appear to be stacking fresh stops rather than replacing; midday scan should
audit total stop qty vs holdings and cancel stale duplicates. IONQ recovered
to -2.05% (was -6.10%). BRK.B still unheld, retry next buildout.
Trades today: 6 (1 stop-triggered sell IREN, 5 buildout buys).
Trades this week (Mon-Tue): 18.

### Jul 22 — EOD Snapshot (Day 12, Wednesday)
**Portfolio:** $50,003.91 | **Cash:** $12,342.67 (24.7%) | **Day P&L:** -$140.32 (-0.28%) | **Phase P&L:** +$3.91 (+0.01%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| BTC | 190.407 | 28.20 | 29.14 | -0.82% | +178.22 (+3.32%) | 10% trail |
| SCHD | 167.591 | 32.64 | 32.88 | +0.18% | +40.13 (+0.73%) | 10% trail |
| VOO | 7.960 | 687.82 | 687.32 | -0.08% | -3.98 (-0.07%) | 10% trail |
| SGOV | 46.230 | 100.52 | 100.61 | +0.01% | +3.87 (+0.08%) | 10% trail |
| QQQM | 13.439 | 292.45 | 290.56 | -0.46% | -25.40 (-0.65%) | 10% trail |
| SCHG | 107.442 | 34.42 | 34.10 | -0.50% | -34.08 (-0.92%) | 10% trail |
| SPMO | 19.000 | 151.31 | 149.76 | +0.04% | -29.36 (-1.02%) | 10% trail |
| VTV | 5.944 | 219.21 | 219.34 | +0.33% | +0.77 (+0.06%) | trail (unverif) |
| MSFT | 2.197 | 393.50 | 390.00 | -1.95% | -7.69 (-0.89%) | trail (unverif) |
| VGT | 5.693 | 114.17 | 115.86 | -0.13% | +9.60 (+1.48%) | trail (unverif) |
| ETH | 35.650 | 16.83 | 18.33 | +0.00% | +53.48 (+8.91%) | trail (unverif) |
| GOOGL | 1.550 | 368.43 | 345.09 | -0.59% | -36.17 (-6.33%) | trail (unverif) |
| VXUS | 5.277 | 85.28 | 84.44 | -0.02% | -4.46 (-0.99%) | trail (unverif) |
| SOFI | 16.833 | 17.82 | 17.08 | -3.17% | -12.45 (-4.15%) | 10% trail |
| PLTR | 1.540 | 131.51 | 124.88 | -5.87% | -10.20 (-5.04%) | 10% trail |
| GXRP | 6.912 | 21.70 | 22.02 | -1.65% | +2.20 (+1.47%) | trail (unverif) |
| META | 0.172 | 581.77 | 625.50 | -2.84% | +7.51 (+7.52%) | scan-only |
| APLD | 3.537 | 28.18 | 29.94 | -0.37% | +6.22 (+6.25%) | 10% trail |
| AMZN | 0.405 | 246.86 | 245.05 | -1.01% | -0.73 (-0.73%) | scan-only |
| CIFR | 3.084 | 19.75 | 24.32 | +6.25% | +14.09 (+23.14%) | 10% trail |
| RIOT | 3.167 | 19.23 | 23.28 | +8.32% | +12.82 (+21.05%) | 10% trail |
| GLXY | 2.671 | 22.80 | 24.56 | -3.35% | +4.70 (+7.72%) | 10% trail |
| QBTS | 3.736 | 16.17 | 17.44 | -2.02% | +4.74 (+7.85%) | 10% trail |
| DRAM | 1.115 | 54.55 | 57.75 | -1.87% | +3.57 (+5.87%) | 10% trail |
| RGTI | 4.182 | 14.56 | 15.20 | -0.52% | +2.67 (+4.39%) | 10% trail |
| UNH | 0.143 | 425.73 | 430.43 | -1.36% | +0.67 (+1.10%) | scan-only |
| WULF | 3.114 | 19.50 | 19.42 | -2.27% | -0.26 (-0.43%) | 10% trail |
| IONQ | 1.673 | 36.47 | 34.74 | -2.17% | -2.89 (-4.73%) | 10% trail |
| IREN | 2.399 | 41.85 | 41.34 | +0.12% | -1.21 (-1.21%) | 10% trail |

**Notes:** Quiet down day, -$140.32 (-0.28%), giving back part of the two-day
bounce; phase P&L still barely green (+$3.91, +0.01%). No trades today — 0
buildout buys ran, cash unchanged at 24.7%. Miner/quantum re-entries held
gains (CIFR +23.1%, RIOT +21.1%, QBTS/GLXY/APLD/DRAM/RGTI all +4-8%); ETH
still +8.9%, BTC +3.3%. Drags: MSFT -2.0% day, SOFI -3.2%, PLTR -5.9% day
(now -5.0% unrealized, next-closest to the -7% cut line after GOOGL). TWO
ACTION ITEMS for tomorrow's midday scan: (1) GOOGL sits at -6.33% unrealized,
right at the -7% manual-cut threshold — cut on any further weakness; still
the single weakest name. (2) STOP-COVERAGE VISIBILITY: duplicate
trailing-stop stacking (flagged Jul 20 & 21, unaddressed) has now SATURATED
the full 50-order API page — 39 of 50 open orders are duplicates on 8 core
symbols (BTC 7, SCHD 7, SGOV 6, QQQM 5, VOO 5, SCHG 4, SPMO 3, CIFR 2). This
pushes the stops for 7 positions (VTV, MSFT, VGT, ETH, GOOGL, VXUS, GXRP,
~$3.7k value) beyond the visible page, so their coverage is UNVERIFIABLE from
the order list — marked "trail (unverif)" above. They almost certainly still
carry live stops (all showed 10% trail yesterday), but the summary cannot
confirm it until duplicates are cancelled. Midday scan MUST cancel stale
duplicate stops (keep one per symbol, honoring never-move-down) so coverage
is auditable again. True scan-only remnants unchanged (META/AMZN/UNH,
sub-1-share). BRK.B still unheld, retry next buildout.
Trades today: none. Trades this week (Mon-Wed): 18.

## 2026-07-23 — Market-Open Buildout

Day-13 buildout. Core ramp continues: VOO and SCHD each took the next 1%
allowance ($497). Both still deeply underweight (VOO 10.9% vs 23.8%, SCHD
11.1% vs 19.9%). BTC/SGOV/QQQM/SCHG/SPMO/VTV all at/within tolerance —
skipped. Fresh 10% GTC trailing stops layered over each name's net-new
whole shares (VOO +1 sh crossing to 8; SCHD +15 sh) — no existing stop
moved. NBIS rebuy and BRK.B ramp both skipped on wide open spreads (see
below). GOOGL note: pre-market expected its live stop to auto-sell at open
(gapped to -11%); as of this run GOOGL is still held at -12.5% with full
qty_available (no reserving stop visible) — flagged for midday scan to
verify/re-establish coverage or cut on the -7% rule.

| Date | Ticker | Side | Shares/Notional | Entry | Stop | Target Weight | Ramp? | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-07-23 | VOO  | buy | $497 / 0.7295 sh  | 681.26 | 10% trail (+1 sh)  | 23.8% | yes | ramp top-up |
| 2026-07-23 | SCHD | buy | $497 / 15.083 sh  | 32.951 | 10% trail (+15 sh) | 19.9% | yes | ramp top-up |

### Skipped this run (wide spread at open — retry next buildout)
| Ticker | Target | Reason |
|---|---|---|
| NBIS  | 0.2% | ~18% spread (ap 225 / bp 188.29) — was zero, rebuy deferred |
| BRK.B | 2.6% | ~10% spread (ap 512.6 / bp 462.98) — ongoing open-skip |

### Flag for midday scan
- GOOGL held at -12.5%, qty_available = full qty (no stop reserving shares).
  Verify/re-establish 10% stop or cut on -7% rule; if flat, re-queues for
  buildout.
- Duplicate trailing-stop stacking on cores persists (50-order page
  saturated). De-duplicate (keep one per symbol, honor never-move-down)
  so coverage is auditable.

### Jul 23 — EOD Snapshot (Day 13, Thursday)
**Portfolio:** $49,608.24 | **Cash:** $12,037.61 (24.3%) | **Day P&L:** -$395.67 (-0.79%) | **Phase P&L:** -$391.76 (-0.78%)

| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
|---|---|---|---|---|---|---|
| SCHD | 182.674 | 32.67 | 32.81 | -0.30% | +24.46 (+0.41%) | 10% trail |
| VOO | 8.690 | 687.27 | 678.61 | -1.23% | -68.77 (-1.15%) | 10% trail |
| BTC | 190.407 | 28.20 | 28.64 | -1.72% | +83.02 (+1.55%) | 10% trail |
| SGOV | 46.230 | 100.52 | 100.60 | +0.00% | +3.52 (+0.08%) | 10% trail |
| QQQM | 13.439 | 292.45 | 285.85 | -1.57% | -88.70 (-2.26%) | 10% trail |
| SCHG | 107.442 | 34.42 | 33.40 | -1.91% | -109.29 (-2.96%) | 10% trail |
| SPMO | 19.000 | 151.31 | 149.83 | -0.16% | -28.03 (-0.98%) | 10% trail |
| VTV | 5.944 | 219.21 | 219.86 | +0.24% | +3.86 (+0.30%) | trail (unverif) |
| MSFT | 2.197 | 393.50 | 381.43 | -2.28% | -26.53 (-3.07%) | trail (unverif) |
| VGT | 5.693 | 114.17 | 114.39 | -1.06% | +1.23 (+0.19%) | trail (unverif) |
| ETH | 35.650 | 16.83 | 17.86 | -2.56% | +36.72 (+6.12%) | trail (unverif) |
| VXUS | 5.277 | 85.28 | 83.67 | -0.94% | -8.50 (-1.89%) | trail (unverif) |
| SOFI | 16.833 | 17.82 | 16.61 | -2.71% | -20.40 (-6.80%) | 10% trail |
| GXRP | 6.912 | 21.70 | 21.40 | -2.82% | -2.08 (-1.39%) | trail (unverif) |
| APLD | 3.537 | 28.18 | 30.13 | +0.16% | +6.89 (+6.91%) | 10% trail |
| META | 0.172 | 581.77 | 605.50 | -3.46% | +4.07 (+4.08%) | scan-only |
| IREN | 2.399 | 41.85 | 40.88 | -0.97% | -2.32 (-2.31%) | 10% trail |
| AMZN | 0.405 | 246.86 | 233.70 | -4.55% | -5.33 (-5.33%) | scan-only |
| CIFR | 3.084 | 19.75 | 25.89 | +5.85% | +18.94 (+31.09%) | 5% trail |
| RIOT | 3.167 | 19.23 | 24.05 | +2.88% | +15.28 (+25.08%) | 5% trail |
| DRAM | 1.115 | 54.55 | 59.03 | +2.18% | +5.00 (+8.21%) | 10% trail |
| GLXY | 2.671 | 22.80 | 24.60 | -0.77% | +4.81 (+7.90%) | 10% trail |
| QBTS | 3.736 | 16.17 | 17.10 | -1.44% | +3.47 (+5.75%) | 10% trail |
| WULF | 3.114 | 19.50 | 20.17 | +3.49% | +2.07 (+3.41%) | 10% trail |
| RGTI | 4.182 | 14.56 | 14.83 | -2.63% | +1.12 (+1.85%) | 10% trail |
| UNH | 0.143 | 425.73 | 423.56 | -1.80% | -0.31 (-0.51%) | scan-only |
| IONQ | 1.673 | 36.47 | 34.28 | -1.14% | -3.65 (-5.99%) | 10% trail |

**Notes:** Down day, -$395.67 (-0.79%), the biggest daily drawdown of the
phase; phase P&L slips back to -$391.76 (-0.78%) after yesterday's brief
green. Broad-market weakness led the drag (VOO -1.23%, QQQM -1.57%, SCHG
-1.91%, MSFT -2.28%) — nothing name-specific. Miner/quantum re-entries kept
their gains (CIFR +31.1%, RIOT +25.1%, DRAM +8.2%, APLD +6.9%, GLXY/QBTS
+5.8-7.9%); ETH still +6.1%, BTC +1.6%. TRADES TODAY (4): market-open ramp
bought VOO +$497 and SCHD +$497 (both still deeply underweight); midday scan
CUT GOOGL and PLTR in full on the -7% manual rule — GOOGL's 1-share trailing
stop filled @324 then the fractional remainder sold @319.93; PLTR's stop
filled @123.14 then remainder @122.19. Both cleared from the book; they
re-enter the buildout queue under the standard rule. NEW WATCH ITEM: with
GOOGL and PLTR gone, SOFI is now the single weakest name at -6.80%
unrealized — right at the -7% cut line. Midday scan tomorrow must cut on any
further weakness. STOP-COVERAGE / DUPLICATE-STOP SATURATION UNRESOLVED AND
WORSENING: the 50-order page is still fully saturated with duplicate
trailing stops on 7 cores (SCHD now 8, BTC 7, VOO 6, SGOV 6, QQQM 5, SCHG 4,
SPMO 3 = 39 dups). The midday scan was explicitly mandated (Jul 20/21/22) to
de-duplicate and did NOT — SCHD dups actually grew 7->8. This pushes the
stops for 6 held positions (VTV, MSFT, VGT, ETH, VXUS, GXRP, ~$3.9k value)
beyond the visible page, so their coverage stays UNVERIFIABLE from the order
list — marked "trail (unverif)". They almost certainly still carry live
stops but the summary cannot confirm it until duplicates are cancelled. This
is now a 4-day-old unaddressed operational issue and the top priority for
tomorrow's midday scan: cancel stale duplicate stops (keep one per symbol,
honor never-move-down) so coverage is auditable again. True scan-only
remnants unchanged (META/AMZN/UNH, sub-1-share). BRK.B/NBIS still unheld
(wide open spreads), retry next buildout.
Trades today: 4 (VOO buy, SCHD buy, GOOGL cut, PLTR cut). Trades this week
(Mon-Thu): 22.

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

## 2026-08-03 — Market-Open Buildout

Day-20 buildout. Equity $49,838.58 (1% ramp allowance = $498.39). Core
ramp continues at the $498 cap: VOO/SCHD/SPMO each took their full 1% day
allowance (all still underweight — VOO 18.1%/SCHD 18.4%/SPMO 3.2% vs
23.8/19.9/5.6% targets). BRK.B (+$288, gap < cap) and BTC (+$97, nearly at
target) topped to remaining gap. Non-ramp remnants bought to full target:
APLD/IREN/CIFR/GLXY. SGOV/QQQM/SCHG/VTV at/over tolerance — skipped.
MSFT/ETH/GOOGL/AMZN/NBIS/META over target — skipped. Total $2,113 filled;
cash $5,135 → ample. APLD/IREN/CIFR crossed 1 whole share for the first
time and now carry their first 10% GTC trailing stops. VOO increment was
sub-share (+0.721 sh) — no dedicated stop placeable on the fractional
increment; its 13 whole shares remain fully covered. No de-dup needed:
order page at 31/50, not saturated — the older stop-stacking backlog has
cleared.

| Date | Ticker | Side | Shares/Notional | Entry | Stop | Target Weight | Ramp? | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-08-03 | VOO   | buy | $498 / 0.7209 sh  | 690.76  | (sub-share incr; 13 sh already covered) | 23.8%   | yes | ramp top-up |
| 2026-08-03 | SCHD  | buy | $498 / 14.7947 sh | 33.66   | 10% trail (+15 sh)  | 19.9%   | yes | ramp top-up |
| 2026-08-03 | SPMO  | buy | $498 / 3.4952 sh  | 142.478 | 10% trail (+3 sh)   | 5.6%    | yes | ramp top-up |
| 2026-08-03 | BRK.B | buy | $288 / 0.5561 sh  | 517.888 | 10% trail (+1 sh)   | 2.6%    | yes | ramp top-up (gap < cap) |
| 2026-08-03 | BTC   | buy | $97 / 3.4966 sh   | 27.739  | 10% trail (+3 sh)   | 11.1%   | yes | ramp top-up (near target) |
| 2026-08-03 | APLD  | buy | $82 / 2.9876 sh   | 27.4435 | 10% trail (+3 sh, first stop) | 0.2% | no | gap-fill (remnant → target) |
| 2026-08-03 | IREN  | buy | $69 / 1.8716 sh   | 36.862  | 10% trail (+2 sh, first stop) | 0.2% | no | gap-fill (remnant → target) |
| 2026-08-03 | CIFR  | buy | $43 / 1.9216 sh   | 22.372  | 10% trail (+2 sh, first stop) | 0.1222% | no | gap-fill (remnant → target) |
| 2026-08-03 | GLXY  | buy | $40 / 1.9171 sh   | 20.86   | 10% trail (+1 sh)   | 0.1222% | no | gap-fill (remnant → target) |

### Skipped this run
| Ticker | Target | Reason |
|---|---|---|
| RIOT | 0.1222% | Remnant ($16.63) below target BUT unrealized -7.72% — past the -7% manual-cut line. Not adding to a name flagged for cutting. Flag for midday scan. |

### Flag for midday scan
- **RIOT -7.72% unrealized** ($16.63, 0.85 sh) — past -7% cut line;
  evaluate for manual cut. Sub-1-share, so no trailing stop; governed by
  manual-cut rule.
- Remaining stopless fractionals (all sub-1sh, Alpaca rejects fractional
  trailing stops): AMZN, META, NBIS, UNH — governed by -7% manual-cut
  rule until they ramp past 1 share. All currently above the cut line.
