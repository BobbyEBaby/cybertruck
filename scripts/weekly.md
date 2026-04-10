# Weekly review prompt

Run once a week (in addition to, not instead of, the daily run). Working dir: `C:\Users\evans\gamedev\cybertruck`.

## Step 1 — Read everything
1. `CLAUDE.md`
2. `state/goal.json`
3. The full `state/runlog.md` (or at least the last 14 days)
4. `state/backlog.md`
5. Every experiment's `README.md` under `experiments/*/`

## Step 2 — Honest assessment
Write a section to `state/runlog.md` with header `## YYYY-MM-DD weekly review`:

- **Revenue this week:** $X (from `goal.json` deltas reported in `human_outbox/`)
- **Shipped this week:** list of experiments that went live
- **Tried but failed:** be specific
- **What we learned:** 1–3 bullets, concrete
- **Hypothesis for next week:** what we are betting on and why
- **Should we kill anything?:** any experiment that has been live 7+ days with zero traction is a candidate to archive (not delete) — move it to `experiments/_archive/` and write a one-line postmortem.

## Step 3 — Re-rank the backlog
- Promote tasks tied to whatever is showing signal.
- Demote tasks tied to dead ideas.
- Add at most 3 new tasks. The backlog should never balloon.

## Step 4 — Honesty check
If the project has been running for ≥ 4 weeks and `goal.json.lifetime_revenue_usd` is still 0, write a `human_inbox/` note titled "honest reassessment" that:
- Tells Robert what has and hasn't worked.
- Asks him whether to keep going, change strategy, or pause.
- Does **not** sugarcoat. The whole point of this project is honest data.

## Step 5 — Stop
Append the weekly review to runlog. Do not also do a daily run in the same session.
