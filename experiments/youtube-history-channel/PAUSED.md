---
kind: pause-marker
paused_on: 2026-04-11
paused_by: Robert
---

# PAUSED — YouTube history channel

**Status:** The entire YouTube "Popular Uprisings" experiment is paused indefinitely as of 2026-04-11.

## What "paused" means

**Do not:**
- Write new episode scripts
- Render new videos
- Upload anything new to YouTube
- Add new rebellion/figure/concept wiki pages that exist *only* to support a future episode
- Modify `scripts/daily-remote.md` to work around this pause

**Do:**
- Leave the existing `experiments/youtube-history-channel/` directory completely intact
- Leave existing wiki pages (rebellions, figures, concepts) intact — they have value independent of the channel as a public knowledge base
- Leave the v4 video (`mkFbc00S3ig`) unlisted on YouTube — no deletion
- Continue refreshing existing wiki content when new sources warrant it
- Continue all non-YouTube backlog work normally (browser tools, Gumroad, research, tooling)

## Rule for remote runs

Before picking any backlog task that references this experiment (B-012 through B-018, or anything with "Popular Uprisings" / "youtube-history-channel" in it), check for this file. If it exists, skip the task entirely and pick the next available non-paused task instead. Record the skip in the runlog.

If every non-paused task is also blocked on a human action, append an honest "nothing to do" entry to the runlog and stop — do not invent YouTube busywork to fill the run.

## To resume

Delete this file. The remote agent will pick up YouTube work on the next run.

Recommended resume sequence when the time comes:
1. Delete `experiments/youtube-history-channel/PAUSED.md`
2. Unmark the `[paused]` status on B-012..B-018 in `state/backlog.md` (set to `[pending]` or the appropriate state)
3. Rethink the strategy — the pause itself is useful signal that something about the current approach wasn't working. Don't just restart the pipeline unchanged; revisit `experiments/youtube-history-channel/strategy.md` first.

## Why paused (Robert's call)

Robert decided to pause after reviewing v4 (the Hoch voice clone + clean Popular Uprisings script + parser fix). **Explicit reason:** *"I want to focus on other tasks."* This is a reallocation of effort, not a rejection of the approach. YouTube stays shelved until Robert says resume. In the meantime the rest of the backlog (browser tools, Gumroad, research refreshes, wiki maintenance, other experiments) runs normally.

The v4 video remains unlisted at https://youtu.be/mkFbc00S3ig as a preserved artifact — it's the canonical version if the channel ever resumes.

## Format lock for when we resume (added 2026-04-11)

While paused, Robert decided two format changes to reduce per-episode production cost:

1. **Target length drops from 8–12 min to 3–5 min** (~500–700 words). Ep1 and ep2 (both ~1,650 words / ~11 min) stay as **long-form archive** — do **not** rewrite them. The new short-form format starts at **ep3**.
2. **Pollinations image count drops from 20 to 6–10 per episode** to match the shorter runtime without frantic pacing.
3. **Narrator voice is locked to `en-GB-RyanNeural`** (Edge TTS, UK male, older tone, rate `-15%`, pitch `-2Hz`). See `strategy.md` "Narrator voice (locked 2026-04-11)" section for the full guardrail.

See `experiments/youtube-history-channel/strategy.md` and `production-pipeline.md` for the detailed updates. When PAUSED.md is eventually deleted, the resumer should read those two files before writing a single word of ep3.
