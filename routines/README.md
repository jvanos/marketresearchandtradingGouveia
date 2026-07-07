# Cloud Routines

These six files are pasted **verbatim** into Claude Code cloud routines —
do not paraphrase. The env-var check block, the Step 0 safety check, and
the commit-and-push step are all load-bearing.

| Routine | File | Cron (America/Chicago) |
|---|---|---|
| Pre-market | `pre-market.md` | `0 6 * * 1-5` |
| Market-open | `market-open.md` | `30 8 * * 1-5` |
| Midday | `midday.md` | `0 12 * * 1-5` |
| Daily summary | `daily-summary.md` | `0 15 * * 1-5` |
| Weekly review | `weekly-review.md` | `0 16 * * 5` |
| Quarterly rebalance | `rebalance.md` | `0 16 1-7 1,4,7,10 1` (first Monday of Jan/Apr/Jul/Oct) |

## One-time prerequisites

Routines are managed at [claude.ai/code/routines](https://claude.ai/code/routines)
(there is no separate `/environments` page — "environment" is a
sub-setting reached from inside a routine's own edit form). See the
[official routines docs](https://code.claude.com/docs/en/routines) for
the full reference; this section covers only what's specific to this repo.

1. Make sure GitHub is connected to your claude.ai account (`/web-setup`
   in the CLI, or connect it under claude.ai account settings) so routines
   can clone and push to this repo. The Claude GitHub App install is only
   needed for GitHub-*event* triggers — these six routines are all
   schedule-triggered, so it's not required here.
2. **Per routine**, after creating it: open it for editing (pencil icon),
   go to the **Permissions** tab, and enable **"Allow unrestricted branch
   pushes"** for this repository. Without this, Claude can only push to
   auto-generated `claude/`-prefixed branches — `git push origin main` in
   the routine's Step 8/9 gets silently redirected instead of landing on
   `main`. This is the fix for a routine that appears to run successfully
   but never actually updates `main`.
3. Environment variables: in a routine's edit form, click the environment
   selector (the cloud icon below the Instructions box — shows "Default"
   or a named environment). Hover over the environment in the list and
   click the settings icon that appears, which opens **"Update cloud
   environment"** — add these there:
   `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_ENDPOINT`,
   `ALPACA_DATA_ENDPOINT`, `MAX_DAILY_LOSS_PCT`, `PERPLEXITY_API_KEY`,
   `PERPLEXITY_MODEL`, `CLICKUP_API_KEY`, `CLICKUP_WORKSPACE_ID`,
   `CLICKUP_CHANNEL_ID`, `GITHUB_TOKEN`.
   Use the *same* named environment across all six routines (not each
   left on its own separate "Default") so they all inherit the same
   variables from one place.
4. Create each routine: name it, paste the prompt from the matching
   `routines/*.md` file verbatim into Instructions, select this
   repository, select the shared environment from step 3, and add a
   Schedule trigger. The web form only offers hourly/daily/weekdays/weekly
   presets — for the exact cron expressions in the table above (the
   quarterly rebalance in particular doesn't fit any preset), pick the
   closest preset when creating the routine, then run `/schedule update`
   in the CLI afterward to set the precise cron expression.
5. Click **"Run now"** once per routine and confirm in the run's session
   that a commit actually landed on `main` (not a `claude/...` branch)
   before trusting the schedule.

## The HALT kill switch

Every routine's Step 0 checks for a file named `HALT` at the repo root. If
it exists, the routine exits without trading (daily-summary, weekly-review,
and rebalance still send their recap, noting the halt, so silence never
looks identical to "nothing happened" — a full quarter of silence from
rebalance would be a worse failure mode than a daily skip).

- **To pause all five routines at once:** commit a file named `HALT`
  (empty is fine) to `main` and push.
- **To resume:** delete the `HALT` file and push.

This exists because five independently-scheduled cloud routines can't be
paused in one place from the web UI — a shared file checked by all of them
is the fastest way to stop a stuck or misbehaving run before it fires
again.