# Trading Bot

An autonomous Claude Code agent that passively tracks a fixed target
portfolio on Alpaca — no discretionary stock-picking, no benchmark to
beat. There is no separate bot process — Claude itself is the bot, invoked
fresh on a schedule. Git is its only memory between runs (see `memory/`);
the only way it ever touches money is through `scripts/alpaca.sh`.

Paper trading by default. See `env.template` before flipping to live.

## Quickstart (local)

1. `cp env.template .env` and fill in real credentials. `.env` is
   gitignored — never commit it.
2. Sign up for Alpaca (paper is fine to start), Perplexity, and ClickUp.
   Create a ClickUp chat channel for notifications and note its workspace
   ID and channel ID.
3. Open this repo in Claude Code and run `/portfolio`. You should see your
   account and positions print cleanly with no errors.
4. The other local commands — `/pre-market`, `/market-open`, `/midday`,
   `/daily-summary`, `/weekly-review`, `/rebalance`, `/trade` — are in
   `.claude/commands/` for manual/ad-hoc use.

## Safety mechanisms

This repo enforces its hard trading rules in code, not just in prompts:

- **`scripts/alpaca.sh order` validates every BUY before it reaches
  Alpaca** — no options, symbol must be on `memory/TARGET-PORTFOLIO.json`,
  resulting weight can't exceed that symbol's target + tolerance, a ramp
  position (target >= 2%) can't be bought more than 1% of equity in a
  day, cost must not exceed live `buying_power` or cash, and a daily-loss
  circuit breaker (`MAX_DAILY_LOSS_PCT` in `.env`, default 5%) blocks new
  buys after a bad day. Sells/closes are never blocked. The weight-
  tolerance and ramp-cap numbers are hardcoded in the wrapper script
  itself, not `.env`-configurable. A rejected order exits with code 2 and
  a reason on stderr — that's the bot's actual backstop against a bad
  prompt, not the strategy doc.
- **`HALT` file** — commit an empty file named `HALT` to the repo root to
  pause every routine immediately; delete it to resume. See
  `routines/README.md`.
- **Market clock check** — every routine calls `scripts/alpaca.sh clock`
  first and exits without trading if the market is closed (covers
  holidays the cron schedule doesn't know about).
- **Strategy changes require a human** — the weekly-review workflow can
  propose changes to `memory/TRADING-STRATEGY.md` but never edits it
  directly, and the gate math above lives in the wrapper script, not a
  memory file a bad week could talk the bot into loosening. The target
  list itself (`memory/TARGET-PORTFOLIO.json`) is meant to be edited over
  time (e.g. adding GADA once a spot Cardano ETF lists) — that's separate
  from the gate math that enforces it.

See `CLAUDE.md` for the full rule set, `memory/TRADING-STRATEGY.md` for
the strategy, and `memory/TARGET-PORTFOLIO.json` for the target weights.

## Cloud routines (production path)

Six scheduled cloud runs do the actual work: pre-market drift check,
market-open buildout/ramp execution, a midday stop-loss scan, a daily
summary, a Friday weekly health check, and a quarterly rebalance. Setting
these up requires the Claude Code web UI (install the GitHub App, create
six routines, paste in the prompts from `routines/*.md`, set environment
variables on each routine — never a `.env` file in the cloud). Full
instructions: `routines/README.md`.

## Layout

```
CLAUDE.md          Agent rulebook, auto-loaded every session
env.template        Copy to .env locally; never commit .env
.claude/commands/    Local slash commands (manual/ad-hoc use)
routines/            Cloud routine prompts (the production path)
scripts/             alpaca.sh / perplexity.sh / clickup.sh wrappers —
                      the only way this repo touches the outside world
memory/              The bot's persistent state, committed to main,
                      including TARGET-PORTFOLIO.json (the target weights)
                      and REBALANCE-LOG.md (quarterly rebalance history)
```
