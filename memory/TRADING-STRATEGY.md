# Trading Strategy

## Mission
Passively track a fixed target portfolio — not beat the S&P 500, not pick
stocks. Build the Alpaca account toward the weights in
`memory/TARGET-PORTFOLIO.json` and hold them, rebalancing quarterly.

## Capital & Constraints
- Starting capital: $50,000 (reset in the Alpaca dashboard for this
  strategy relaunch — see `memory/TRADE-LOG.md` Day 0)
- Platform: Alpaca (paper trading by default — see env.template)
- Instruments: stocks and ETFs only — no options, ever, no native crypto
  orders (crypto exposure comes entirely through spot-ETF proxies traded
  as normal equities), no real estate

## Source of Truth
`memory/TARGET-PORTFOLIO.json` lists every approved symbol, its target
weight, and whether it's a "ramp" position (target_pct >= 2%). This file
is read by both `scripts/alpaca.sh` (to gate every BUY) and every routine
(to compute drift). A symbol not in this file cannot be bought through the
wrapper, period.

## Core Rules
1. NO OPTIONS — ever. NO native crypto orders — crypto exposure only via
   spot-ETF proxies on the target list (enforced in scripts/alpaca.sh)
2. Only buy symbols on the target-portfolio list (enforced in
   scripts/alpaca.sh — this replaces any notion of a fixed position-count
   cap; you simply can't hold more names than the ~31-symbol list)
3. Resulting position weight may not exceed that symbol's target_pct plus
   a small relative tolerance (enforced in scripts/alpaca.sh — replaces
   the old flat 20%-of-equity cap, which doesn't work when a single target
   like VOO is itself 23.8%)
4. **Buildout / ramp rule** for building toward target from zero (or from
   a gap — see rule 8):
   - Symbols with target_pct < 2%: buy to full target in one order, first
     available session.
   - Symbols with target_pct >= 2% ("ramp" positions): buy up by at most
     1% of account equity per day until reaching target (e.g. VOO's 23.8%
     takes roughly 24 trading days of incremental buys). Enforced in
     scripts/alpaca.sh — a single BUY cannot exceed the day's remaining
     ramp allowance for that symbol.
5. 10% trailing stop GTC on every position, no exceptions — including
   core index/bond ETFs. Tighten to 7% trail at +15% unrealized, to 5%
   trail at +20%. Never move a stop down. Never tighten within 3% of
   current price.
6. Cut losers manually at -7% (same as before) — closing a position this
   way (or via a triggered trailing stop) drops that symbol to zero
   weight; see rule 8.
7. **Quarterly rebalance** (`routines/rebalance.md`) compares actual vs.
   target weight for every symbol and corrects drift in both directions:
   trims overweight names, tops up underweight names. Trims are sells
   (never gated). Underweight buys still go through the normal buildout
   rule (ramp symbols still capped at 1%/day even during a rebalance —
   no bypass).
8. A target-list symbol sitting at zero position (because a stop closed
   it, or it hasn't been bought yet) is not a special case — it re-enters
   the buildout queue and follows rule 4 exactly as if starting fresh.
9. Patience > activity. There is no discretionary trade-idea generation in
   this strategy — every buy either fills a buildout/ramp gap or corrects
   quarterly drift. There is nothing to research or time.

## Retired Rules
"Follow sector momentum" and "exit a sector after 2 failed trades" no
longer apply — those were for discretionary stock-picking, which this bot
no longer does. There is no "entry checklist" — a buy either belongs on
the target list at the right weight, or it doesn't happen.

## Enforcement Note
Rules 1-4 above are validated in code inside `scripts/alpaca.sh` — a BUY
order that breaks one of these is rejected before it reaches Alpaca,
regardless of what any prompt or memory file suggests. The weight-
tolerance and ramp-cap percentages are hardcoded constants in the wrapper
script (not `.env`-configurable) specifically so a bad prompt or a casual
config edit can't loosen them — same protection level the old hardcoded
20%/6-position/8-trades limits had. Changing the target list itself
(`memory/TARGET-PORTFOLIO.json`) is a human, editable action (it's meant
to change — e.g. adding GADA once a spot Cardano ETF lists), but changing
the *gate math* around it requires editing `scripts/alpaca.sh` directly.
See CLAUDE.md "Safety Mechanisms" for the full list.

## Buildout / Ramp Checklist (before any buy)
- Is the symbol on `memory/TARGET-PORTFOLIO.json`? If not, don't buy it.
- Current weight vs. target weight — how big is the gap?
- Is this a ramp symbol (target_pct >= 2%)? If so, has today's 1%
  allowance already been used?
- Is this filling a fresh buildout gap, or a stop-triggered zero-position
  gap? Either way, follow the same ramp/immediate rule.
- Is a trailing stop already queued to be placed immediately after fill?
