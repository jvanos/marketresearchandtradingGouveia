# Project Context

## Overview
- What: Autonomous passive target-portfolio tracker
- Starting capital: $50,000 (reset for this strategy relaunch)
- Platform: Alpaca (paper trading by default)
- Strategy: Track a fixed target portfolio (memory/TARGET-PORTFOLIO.json)
  by building toward its weights and holding, rebalancing quarterly. No
  options, no native crypto orders, no discretionary stock-picking.

## Rules
- NEVER share API keys, positions, or P&L externally
- NEVER buy a symbol that isn't on memory/TARGET-PORTFOLIO.json. The hard
  limits in scripts/alpaca.sh are the actual backstop against this, not
  this rule alone.
- Every trade must be documented BEFORE execution
- If a file named HALT exists at the repo root, do not trade — see
  CLAUDE.md "Safety Mechanisms" and routines/README.md

## Key Files — Read Every Session
- memory/PROJECT-CONTEXT.md (this file)
- memory/TARGET-PORTFOLIO.json
- memory/TRADING-STRATEGY.md
- Bounded operational-log views from the commands in CLAUDE.md. Never
  open the full TRADE, RESEARCH, WEEKLY-REVIEW, or REBALANCE log during
  routine startup; `memory/archive/` is cold audit history only.
