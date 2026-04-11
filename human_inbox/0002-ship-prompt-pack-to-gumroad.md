# 0002 — Ship the Claude Code Power Prompts pack to Gumroad

**Status:** Built remotely on 2026-04-11 (remote run #1). Ready for a local-run
agent to push it live. You only need to do this once you've finished the
Gumroad half of `human_inbox/0001-setup.md` (account + `GUMROAD_ACCESS_TOKEN`
in `.env`). If that's already done, a local Claude Code session can run
the whole flow end-to-end.

## What was built
`experiments/claude-code-power-prompts/` now contains:
- `claude-code-power-prompts.md` — the product (15 prompts, ~3,500 words)
- `README.md` — hypothesis, pricing rationale, measurement plan
- `ship.md` — exact upload flow for the local-run agent

## What you need to do
**Option A — hands-off (preferred):** open Claude Code locally in the
`cybertruck/` directory and run:

> Read `experiments/claude-code-power-prompts/ship.md` and follow it exactly.
> Don't improvise — if any prerequisite is missing, stop and write a new
> inbox note instead of working around it.

The local agent will check `.env`, convert the markdown to PDF (if pandoc
is available), create a `tools/gumroad_publish.py` helper if it doesn't
exist yet, create the Gumroad listing via API, update `state/publish-log.md`,
mark B-002 done in `state/backlog.md`, and append a runlog entry.

**Option B — you do it manually:** if the Gumroad API path fails, the same
`ship.md` has the listing fields, description copy, pricing (`$5 PWYW`,
`$3 minimum`), tags, and category ready to paste into the Gumroad web UI.

## What NOT to do
- **Do not post any promo yet.** The ship.md explicitly separates
  product-upload from promo-posting. Promo requires Reddit credentials AND
  a confirmed-safe subreddit, which is a separate decision for a later run.
- **Do not create fake reviews or alt accounts.** `CLAUDE.md` forbids this
  and the long game depends on not doing it.
- **Do not pay for anything.** If any step asks for money (e.g. Gumroad
  premium features, a PDF converter), stop and tell me.

## How to report back
After the upload succeeds, drop a file in `human_outbox/` with:
```
product: claude-code-power-prompts
gumroad_url: <the live URL>
listed_price: $5 PWYW ($3 min)
pdf_or_md_uploaded: pdf | md
date_shipped: YYYY-MM-DD
any_issues: <anything weird>
```

The next remote run will read it, update `state/goal.json` if revenue
eventually lands, and start a 14-day measurement window on this experiment.

## Reality check
Expected outcome for this specific product, 14-day window, zero paid promo,
unknown seller, one organic post on one platform: **median 0 sales, realistic
band 0–3 sales, optimistic band 3–10.** See `state/honest-expectations.md`.
This is one shot on goal, not the cybertruck. But it's our first *paid*
shot on goal, which is the point of B-002.

(Built by: remote run #1, commit will be recorded in the runlog entry
appended this run.)
