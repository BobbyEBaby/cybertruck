# 0005 — Ship the CLAUDE.md Linter (B-010)

**Time estimate:** 10–15 minutes to deploy + 20 minutes across Monday/Tuesday + Saturday to run the distribution push. **Actual attention per day: 3 minutes.**

## What's been built (remote run #16)
`experiments/claude-md-linter/` now contains:
- `index.html` — single-file static tool. Vanilla JS, no deps, no backend, 17 lint rules, client-side only.
- `README.md` — hypothesis, audience, scoring, measurement plan, design decisions.
- `ship.md` — the full distribution playbook (pre-flight → GitHub Pages → HN → Reddit → measurement).

Commit: see the `remote: run #16` commit on `main`.

## Why this one is the next ship
Per the B-004 01-browser-utilities refresh (2026-04-11, remote run #15), candidate #1 in the refined B-010 shortlist was **CLAUDE.md linter** — chosen over the Anthropic tool-def validator, prompt diff viewer, and CLI cheat-sheet because it's the only option that leverages authentic authority from running the Cybertruck Autopilot project itself. The 01 refresh also concluded that every browser tool from B-010 onward needs a **day-1 direct-distribution push** (Show HN + r/SideProject) because AI Overviews have materially killed passive SEO long-tail for small static tools.

## What I need you to do

### 1. Eyeball the tool (2 minutes)
Open `experiments/claude-md-linter/index.html` in a browser. Click **Load sample → Lint**. You should see at least one red **error** badge (the fake Anthropic key in the sample) plus a handful of warnings and info-level findings. If anything looks broken, tell me and I'll fix it before you deploy.

### 2. Deploy to GitHub Pages (5 minutes)
Open a local Claude Code session in `cybertruck/` and say:

> Deploy experiments/claude-md-linter to GitHub Pages.

Or run it yourself:

```bash
cd cybertruck
bash tools/deploy_pages.sh claude-md-linter experiments/claude-md-linter
```

This reads `GITHUB_TOKEN` from `.env` (which the remote agent cannot touch) and creates `BobbyEBaby/claude-md-linter` + enables Pages. After the deploy, load `https://bobbyebaby.github.io/claude-md-linter/` in an incognito window and re-run the sample-lint round-trip.

Add a row to `state/publish-log.md` confirming the deploy.

### 3. Run the distribution push (10 minutes on Mon/Tue + 5 on Saturday)
Exact copy for both posts is in `experiments/claude-md-linter/ship.md` Steps 2a and 2b. In short:

- **Monday or Tuesday, 08:00–10:00 US Eastern: Show HN.** Copy the title and body verbatim from `ship.md` §2a. Post once. Do not reply to comments.
- **Saturday: r/SideProject "Share Your Project Saturday" thread.** Copy from `ship.md` §2b. Do not top-level post outside the thread. Do not reply to comments.
- **Do NOT** post to r/webdev (01 refresh explicitly says r/SideProject is strictly better in 2026).
- **Do NOT** post to more than one Reddit sub in 24h.

Add a `state/publish-log.md` row for each post.

### 4. Report back
Drop `human_outbox/0005-reply.md` with:
```
deployed: yes|no
live_url: <url or "broken">
show_hn_url: <url or "not yet" or "skipped">
reddit_sideproject_url: <url or "not yet" or "skipped">
notes: <anything weird, any bug you noticed, any feedback you got>
```

The next remote run will pick this up, update the backlog, start the 7-day measurement window, and move on to B-011 planning.

## What I'm NOT asking you to do
- Not asking you to spend any money (domain, hosting, ads — none of it).
- Not asking you to reply to any comments on HN or Reddit (CLAUDE.md one-way rule).
- Not asking you to rate the tool's quality — it's either live and working or it isn't.
- Not asking you to port it to a CLI / npm / VS Code extension — that's a post-measurement decision.
- Not asking you to touch `.env` beyond what `tools/deploy_pages.sh` already reads.

## Hard rules (unchanged)
- No spending. Free tier only.
- No replies. One-way posts on HN and Reddit.
- No secrets written anywhere in the repo.
- No multi-account upvoting.
- Honest copy only. The post body in `ship.md` is the final copy — don't embellish it, don't dial up the urgency, don't add emoji-laden hype. The audience can smell astroturf.

## What happens if you don't ship this
The tool sits on `main` and goes nowhere. That's fine — it's reversible and no credentials were burned. The next remote run will notice it's still un-shipped and will NOT build a B-010b or B-011 until this one gets a first measurement.

## What happens if it works
Define of "works" here is **≥ 100 unique visitors + either ≥ 1 tip OR ≥ 5 substantive feedback comments** in the 7-day window. If that fires, the next remote run will:
1. Mark B-010 `[shipped-with-signal]` in the backlog.
2. Draft B-010b (extension rules, Node CLI port, or VS Code extension scoping) based on the specific feedback captured in the README engagement log.
3. Use the validation as the priors update for B-011 candidate selection (a second Gumroad asset aimed at the same AI-tooling developer audience that showed up for this tool).

If it fires zero: we log it as the first of three consecutive browser-tool zeros and the next B-010 candidate becomes the Anthropic tool-definition validator (candidate #2 in the B-010 shortlist).

---

**Written by:** remote run #16 (Sonnet, per the model-switch handoff in `human_inbox/0004-switch-to-sonnet.md`) per `scripts/daily-remote.md`. Build phase for B-010 complete; upload is the only local-required step left.
