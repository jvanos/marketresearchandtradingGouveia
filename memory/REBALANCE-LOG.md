# Rebalance Log

Quarterly rebalance entries appended here by routines/rebalance.md. Each
entry documents the full drift correction for that quarter — trims on
overweight names, top-ups on underweight names, and any stop-loss gaps
filled along the way. Template for each entry:

## YYYY-MM-DD — Quarterly Rebalance

### Pre-Rebalance Weights
| Ticker | Target % | Actual % | Gap |
|---|---|---|---|

### Actions Taken

**Trims (sells, overweight → target):**
| Ticker | Shares/Notional Sold | Price | Realized P&L | New Stop |
|---|---|---|---|---|

**Top-ups (buys, underweight → target or today's ramp allowance):**
| Ticker | Shares/Notional Bought | Price | Ramp? | Still Underweight After? |
|---|---|---|---|---|

**Gap-fills (zero-position symbols, e.g. from a stop-loss trigger):**
| Ticker | Action | Note |
|---|---|---|

### Post-Rebalance Weights
| Ticker | Target % | Actual % | Gap |
|---|---|---|---|

### Ramp Status Summary
- Symbols still ramping toward target: N
- Est. days to full buildout at 1%/day: N

### Notes
- Any trim that touched a stop-protected position must confirm the new
  stop's implied price was not below the old stop's current price before
  the old stop was cancelled (never move a stop down).
