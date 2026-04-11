# YouTube History Channel — "Margins of History"

**Existing channel:** https://studio.youtube.com/channel/UCv8vMc6ZN9Tkc0K5gx53iAA
**Status:** planning complete, first video queued
**Backlog items:** B-012 through B-017
**Created:** 2026-04-11

## What this is
A faceless YouTube channel about obscure, forgotten, or surprisingly consequential moments in history. Written and (eventually) rendered by the Cybertruck Autopilot loop; narrated by Microsoft Edge TTS; illustrated with public domain imagery from Library of Congress, Wikimedia Commons, and Internet Archive. Multiple revenue streams day-1 (Ko-fi, Buy Me a Coffee, crypto tips, Gumroad PDFs).

## Why this will take a while to pay off
Honest: YouTube Partner Program is far off (1,000 subs + 4,000 watch hours), most faceless channels never hit it, and the near-term revenue comes from direct tips — which are rare. See `state/honest-expectations.md`. We are not building this expecting ad revenue tomorrow. We are building it because it has a real ceiling, costs $0, and the production pipeline is automatable.

## Files in this folder
| File | Purpose |
|---|---|
| `README.md` | This file |
| `strategy.md` | Full strategy: niche, name, format, cadence, revenue streams, guardrails, measurement |
| `production-pipeline.md` | End-to-end: topic → script → images → narration → render → upload |
| `video-description-template.md` | The description the agent pastes into every upload |
| `scripts/01-dancing-plague-1518.md` | First video queued (script not yet written — B-012 will write it) |
| `assets/<slug>/` | Per-video assets: images, narration.mp3, storyboard.json, final.mp4, thumbnail.jpg, sources.md |

## Critical non-file assumptions
1. Robert's existing YouTube channel (`UCv8vMc6ZN9Tkc0K5gx53iAA`) will be rebranded as "Margins of History" — channel name, handle, banner, about page. This is a 5-minute YouTube Studio task Robert does once. Or he leaves the channel as-is if he prefers; the brand name is a suggestion.
2. Robert will provide a YouTube Data API v3 OAuth refresh token when ready. Until then, uploads are manual drag-and-drop (~2 min per video). See `human_inbox/0003-youtube-api-setup.md` (to be written by B-012).
3. Ko-fi and Buy Me a Coffee accounts for `bobbyebaby` — both are free signups, ~5 min each. Robert does this once. Linked in every video description. Flagged in `human_inbox/` when convenient.
4. Gumroad link pointing at the Power Prompts pack from B-002 — cross-promotion between experiments. Already flows from other work.
5. Public domain imagery only. No AI-generated illustrations. History credibility depends on real sourcing.

## Human touchpoints (total, forever)
- **Once:** rebrand existing channel (5 min, optional)
- **Once:** create Ko-fi account (5 min)
- **Once:** create BMC account (5 min)
- **Once:** generate YouTube Data API OAuth token (10–15 min) — or skip this and drag-drop uploads (~2 min/video forever)
- **Per episode (new — see "Binding constraints from 06-faceless-youtube refresh" below):** ~15 min for Robert to record a short human-voiced intro/outro + editorial commentary beats against the agent-written script. This is the single largest mitigator against YouTube's Jan 2026 inauthentic-content enforcement wave.
- **Ongoing:** optional spot-checks when weekly review fires

Total one-time: ~25–35 minutes. Ongoing: ~15 min/episode for Robert's voice drop-in + 2 min/video if skipping the API token.

## Binding constraints from 06-faceless-youtube refresh (2026-04-11)
The Jan 2026 YouTube enforcement wave mass-terminated thousands of "faceless AI" channels that matched a recognizable profile: synthetic voiceover with no tonal variation, stock/reused footage with no original editing, templated scripts recycled across uploads, and high publication cadence. As originally designed, this experiment matched **two of those four risk signals** (pure Edge TTS narration + uniform Ken Burns visual treatment). The full research refresh is in `research/markets/06-faceless-youtube.md` (scroll to "Recommendation for the loop"). The binding mitigations now enforced on B-012..B-017:

1. **Narration is no longer pure TTS.** Robert records a short intro + outro + at least 3 editorial commentary beats per episode (~15 min of his time). The agent-written script marks these as `[HUMAN_INTRO]`, `[HUMAN_OUTRO]`, and `[HUMAN_RECORD]` so `tools/narrate.sh` can split the audio into segments and leave human slots as placeholder files for drop-in. If Robert declines the voice work, fall back to having the agent write richer human-sounding editorial commentary and bump visual variety — but the pure-TTS-only path is out.
2. **Visuals must mix treatments.** No more uniform Ken Burns across 20 images. The storyboard manifest must mix: Ken Burns pan/zoom, static-with-text-overlay (primary-source quotes), side-by-side comparisons, and simple map/timeline graphics. `tools/render_video.py` reads a storyboard JSON specifying per-shot treatment.
3. **Cadence hard-capped at 1 episode/week for the first 12 weeks.** Burst publishing is a flagged risk signal. Publications must be spaced ≥3 days apart.
4. **No AI-generated historical visuals, ever.** Public domain only. Already in strategy.md; restated because it's now also an inauthenticity/disclosure risk, not just a credibility one.
5. **Weekly health check for policy notices.** The weekly review must read channel analytics and flag any inactivity warning or policy notice from YouTube immediately.

These constraints slightly reduce the "hands-free automation" ceiling but preserve the channel as a real long-term bet. The earnings upper bound in the niche is unchanged (Simple History ~$60k/yr; Our History ~$27k/yr) — the rules just got sharper about what shape of content clears the filter. Research-driven obscure history with human creative contribution is explicitly on the right side of the line.

## Circuit breaker
If by week 4:
- 0 new subscribers AND
- <20 average views per video AND
- 0 donations across all rails

→ the channel is circuit-broken. Stop shipping new videos. Do a strategic review in the weekly prompt and either pivot the niche, kill it, or diagnose something fixable.

## Decision: niche + channel name were picked without Robert
Per the "minimal interaction" directive, I made the calls:
- Niche: obscure/forgotten history (highest-scoring faceless niche that still has room per 2026 research)
- Name suggestion: "Margins of History"

If Robert disagrees on either, a one-line message pivots the whole thing. No hard dependencies locked in yet — zero videos shipped, all infrastructure is text files.
