# Weekly Review

Friday health checks appended here. This is no longer a win/loss grading
exercise — there are no discrete discretionary trades to grade. It's a
periodic check on drift, stop-loss activity, and buildout/ramp progress.
Template for each entry:

## Week ending YYYY-MM-DD

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $X |
| Ending portfolio | $X |
| Week return | ±$X (±X%) |
| Cash % | X% |
| Symbols still ramping | N of 9 |
| Est. days to full buildout | N |

### Drift Table
| Ticker | Target % | Actual % | Gap |
|---|---|---|---|
(list only names with a meaningful gap — full drift lives in the daily
RESEARCH-LOG entries)

### Stop-Loss Activity This Week
| Ticker | Trigger | Realized P&L | Buyback Status |
|---|---|---|---|
(or "None")

### What Worked / What Didn't
- ...

### Adjustments for Next Week
- ...

### Proposed Strategy Changes
(Optional — see TRADING-STRATEGY.md "Enforcement Note". Propose changes
here for human review; do not edit TRADING-STRATEGY.md or
TARGET-PORTFOLIO.json's gate math directly. Adding/removing a target
symbol in TARGET-PORTFOLIO.json's `positions` list is a normal editable
action, not a hard-rule change — the gate math around it is what requires
a human wrapper edit.)

### Drift Health: On-track / Needs Rebalance / Alert

## Week ending 2026-07-24

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio (Mon AM ≈ Fri 07-17 close) | $49,626.12 |
| Ending portfolio | $49,491.18 |
| Week return | -$134.94 (-0.27%) |
| Cash % | 23.0% |
| Symbols still ramping | 3 of 9 (VOO, SCHD, BRK.B) |
| Est. days to full buildout | ~11 (VOO is long pole) |

Intra-week path: Mon $49,739 → Tue $50,144 (week high) → Wed $50,004 →
Thu $49,608 → Fri $49,491. Two up days, three down; net flat-to-slightly
red on a soft-tape Thu/Fri. Phase P&L (vs $50k Day-0): -$515 (-1.03%).

### Drift Table
| Ticker | Target % | Actual % | Gap (pp) |
|---|---|---|---|
| VOO   | 23.8 | 12.9 | +10.9 |
| SCHD  | 19.9 | 13.3 | +6.6 |
| BRK.B | 2.6  | 0.0  | +2.6 (unheld — wide open spread all week) |
| SOFI  | 0.6  | 0.0  | +0.6 (cut Fri) |
| PLTR  | 0.4  | 0.0  | +0.4 (cut Thu) |
| NBIS  | 0.2  | 0.0  | +0.2 (unheld since 07-16) |
| IREN  | 0.2  | 0.0  | +0.2 (stopped Fri) |
| IONQ  | 0.12 | 0.0  | +0.12 (stopped Fri) |
(All other cores at/within tolerance. VOO+SCHD alone are ~$8.6k of
un-deployed target weight; 23% idle cash vs 0.3% target = still mid-buildout.)

### Stop-Loss Activity This Week
| Ticker | Trigger | Realized P&L | Buyback Status |
|---|---|---|---|
| IREN | Tue: partial trailing stop (3 sh) | ~+$23 (gain) | rebought Wed, then re-stopped Fri |
| GOOGL | Thu: -7% manual cut (full) | ~-$40 | rebought full Fri to 1.1% |
| PLTR | Thu: -7% manual cut (full) | ~-$41 | in buildout queue (unheld) |
| SOFI | Fri: -7% cut (full, 16.83 sh @16.54) | ~-$18 (-6%) | in buildout queue (unheld) |
| IONQ | Fri: trailing stop, gapped (full) | ~-$6 (-9%) | in buildout queue (unheld) |
| IREN | Fri: trailing stop (full ~2.79 sh) | ~flat | in buildout queue (unheld) |
| APLD/CIFR/DRAM/GLXY/QBTS/RIOT/WULF | Fri: **partial** trailing-stop fragments fired (stacked-dup stops) | small each | fractional remnants still held |

### What Worked / What Didn't
- Worked: Core ramp discipline held — VOO/SCHD topped up every session at
  the 1%/day cap; defensives (SGOV, VTV, SCHD) cushioned the soft Thu/Fri
  tape. -7% manual cuts on GOOGL/PLTR fired as designed.
- Didn't: The 5+-day-old stacked/partial trailing-stop saturation stopped
  being just an audit nuisance and did real damage Friday. On the down day,
  the reserved whole-share fragments of the stacked stops triggered across
  7 spec/momo names, selling only partial quantities and leaving orphaned
  fractional remnants (APLD 0.54 sh, CIFR 0.08, DRAM 0.12, GLXY 0.67, QBTS
  0.74, RIOT 0.17, WULF 0.11) — unintended, uneconomic partial exits. The
  midday de-dupe was mandated Jul 20/21/22/23 and never ran/completed.
- Buildout still the whole story: 23% idle cash, VOO/SCHD ~$8.6k short.

### Adjustments for Next Week
- Continue VOO/SCHD ramp at 1%/day (~11 days to full on VOO).
- Rebuy queue: SOFI, PLTR, NBIS, IONQ, IREN back toward target per
  buildout rule; BRK.B ramp only if open spread normalizes (<~2%).
- Reconcile the fractional remnants left by Friday's partial-stop fires
  (either top back to target or let buildout re-enter under the standard rule).

### Proposed Strategy Changes
- **Escalate: stacked/partial trailing-stop reconciliation needs a human
  or a wrapper helper — the automated midday de-dupe has failed 5+
  consecutive sessions and on 07-24 actively caused unintended partial
  liquidations.** This is an operational/tooling defect, not a risk-rule
  loosening (nothing here touches the wrapper's gate math). Recommend a
  human either (a) manually cancel all stacked trailing stops and re-place
  exactly one full-position 10% GTC stop per held symbol (honoring
  never-move-down), or (b) add a `reconcile-stops` helper to scripts/ that
  audits total open-stop qty vs holdings per symbol and collapses
  duplicates. Until fixed, coverage on VTV/MSFT/VGT/ETH/VXUS/GXRP remains
  unauditable (stops pushed beyond the 50-order page) and future down days
  will keep firing partial fragments.

### Drift Health: Needs Rebalance
Core drift itself is normal mid-buildout (expected, on-track for the ramp).
The **operational Alert** is the stop-stacking defect, which Friday
converted from a latent audit gap into real unintended partial fills —
flagged for human action above.
