# 0004 — Flip the scheduled trigger from Opus to Sonnet

**Time estimate:** 2 minutes.

**What:** Change the model on the `cybertruck-autopilot-daily` scheduled trigger from `claude-opus-4-6` to `claude-sonnet-4-6`.

**Why:** Your standing rule is Opus for the first 10 runs (early framing matters most — the research refreshes, the first scripts, the backlog rationalization all set the shape the loop repeats later) and Sonnet for the steady-state runs after that (cost). As of 2026-04-11 13:55 UTC remote run, **exactly 10 remote runs have completed on Opus**:

| # | Time (UTC) | Task |
|---|---|---|
| 1 | 06:31 | B-002 — Claude Code Power Prompts pack (build phase) |
| 2 | 06:38 | B-002 collision reconcile + B-001 status fix |
| 3 | 06:49 | B-009 refresh 02-itchio-microgames.md |
| 4 | 06:55 | B-009 refresh 08-open-source-donations.md |
| 5 | 07:11 | B-009 refresh 04-niche-content-sites.md (15→11) |
| 6 | 08:14 | B-009 refresh 06-faceless-youtube.md (13→12 + binding constraints) |
| 7 | 09:23 | B-009 refresh 05-chrome-extensions.md (13→10) |
| 8 | 10:27 | B-009 refresh 07-print-on-demand.md (11→7 — lowest score in set) |
| 9 | 11:42 | B-012 — Dancing Plague 1518 script (~1,342 words) |
| 10 | 13:55 | B-017 — source 22 PD image candidates for episode 1 |

Opus produced: 6 market-research refreshes with cited sources, 2 experiment builds (Gumroad prompt pack + Dancing Plague script), 1 image source list, and the full rationalization of the research landscape into the current backlog ranking. That's the "early framing matters most" investment done. From here the loop is executing a stable plan — exactly what Sonnet is good at.

## How

**Option A — web UI (fastest):**
1. Open https://claude.ai/code/scheduled/
2. Find the trigger named `cybertruck-autopilot-daily`
3. Edit it
4. Change the model field from `claude-opus-4-6` to `claude-sonnet-4-6`
5. Save

**Option B — ask Claude Code locally:**
Open a local Claude Code session in the `cybertruck/` directory and say:
> Flip the `cybertruck-autopilot-daily` scheduled trigger from claude-opus-4-6 to claude-sonnet-4-6.

The local session can run whatever the correct management command is.

## Cost impact

Rough order-of-magnitude: Sonnet is ~5× cheaper per token than Opus. The remote runs are the dominant cost line now that all 10 Opus runs are behind us, so this flip is the single biggest cost reduction available without reducing cadence.

## How to report back

Drop a file at `human_outbox/0004-reply.md` with:
```
switched_to_sonnet: yes | no
notes: <anything weird>
```

Once the next remote run sees that reply, it will:
1. Process and archive the outbox file.
2. Verify this inbox note is resolved.
3. Continue on the post-Opus task queue (recommended next: B-013 — build `tools/source_images.py` and download the 22 PD image candidates identified in `experiments/youtube-history-channel/assets/dancing-plague-1518/sources.md`).

## What happens if you don't flip it

The loop keeps working — Sonnet isn't required, it's just more honest about cost. If you never flip it, the remote runs stay on Opus and the cost line stays ~5× higher than it needs to be for the kind of work the steady-state loop does. No correctness impact either way.

## Hard rules (unchanged)

- The agent will not spend your money.
- The agent will not ask for your seed phrase.
- The agent will not publish to external platforms it cannot reach from the remote sandbox — it writes handoff notes instead.
- The pause switch (`PAUSE` file in repo root) still halts the next run immediately.

---

**Written by:** remote run #10 (Opus, 2026-04-11 13:55 UTC) per `scripts/daily-remote.md` Step 9. This is the last inbox note the Opus model will write in this loop.
