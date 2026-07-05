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

## One-time prerequisites (per the setup guide, Part 7)

1. Install the Claude GitHub App on this repo (or run `/web-setup` to sync
   your `gh` CLI token).
2. On each routine's environment: enable **"Allow unrestricted branch
   pushes"**. Without this, `git push origin main` silently fails with a
   proxy error.
3. At [claude.ai/code/environments](https://claude.ai/code/environments),
   open the environment your routines use and paste these into the
   environment variable field in `.env` format (set once — all routines
   on that environment inherit them automatically; never use a `.env` file
   in the cloud):
   `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_ENDPOINT`,
   `ALPACA_DATA_ENDPOINT`, `MAX_DAILY_LOSS_PCT`, `PERPLEXITY_API_KEY`,
   `PERPLEXITY_MODEL`, `CLICKUP_API_KEY`, `CLICKUP_WORKSPACE_ID`,
   `CLICKUP_CHANNEL_ID`, `GITHUB_TOKEN`.
   The "visible to anyone" warning refers to other members of a shared
   team environment — for a personal account it's just you.
4. Select branch `main`, set the cron + timezone, paste the routine's
   prompt verbatim, save, then click **"Run now"** once to confirm it
   works before trusting the schedule.

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