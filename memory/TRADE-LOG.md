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
