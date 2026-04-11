# YouTube History Channel — "Breaking Points"

**Existing channel:** https://studio.youtube.com/channel/UCv8vMc6ZN9Tkc0K5gx53iAA
**Status:** Episode 1 shipped **unlisted** 2026-04-11 (v1 SFen0WYnBy4 at 15:00 UTC; v2 sBUTZhrbMPU at 15:39 UTC with a UK narrator voice and slower camera pan). Not yet public. Episode 2 queued (B-018 — German Peasants' War 1524–25).
**Backlog items:** B-012..B-017 are all [done 2026-04-11]. B-018 is the active item.
**Created:** 2026-04-11

## What this is
A YouTube channel about **rebellions across history**, analyzed through six recurring themes (economy, royalty, government, wars, environment, debt) on a 0–3 intensity scale. The channel's central thesis — [[../../wiki/concepts/structural-vs-tactical-victory]] — is that rebellions rarely win in their own time but the conditions that cause them almost always win in the century that follows. Scripts are written by the Cybertruck Autopilot loop; narration is Microsoft Edge TTS (currently a UK voice); illustrations are AI-generated via Pollinations.ai (keyless, free) tailored per narration beat; rendered with `tools/render_video.py`; uploaded via `tools/youtube_upload.py`. Multiple revenue streams day-1 (Ko-fi, Buy Me a Coffee, crypto tips, Gumroad PDFs) — pending the accounts in `human_inbox/0003-youtube-api-and-tips-setup.md`.

> **Niche pivot note (2026-04-11):** this channel was originally conceived as "Margins of History — obscure/forgotten history" with Dancing Plague of 1518 as episode 1. Robert pivoted on 2026-04-11 to rebellions-with-thematic-analysis under the name "Breaking Points". The Dancing Plague script + its 22 PD image candidates are archived in `_archive/` rather than deleted. All B-012..B-017 references elsewhere in state describe the post-pivot version.

## Why this will take a while to pay off
Honest: YouTube Partner Program is far off (1,000 subs + 4,000 watch hours), most faceless channels never hit it, and the near-term revenue comes from direct tips — which are rare. See `state/honest-expectations.md`. We are not building this expecting ad revenue tomorrow. We are building it because it has a real ceiling, costs $0, and the production pipeline is automatable.

## Files in this folder
| File | Purpose |
|---|---|
| `README.md` | This file |
| `strategy.md` | Full strategy: niche, name, format, cadence, revenue streams, guardrails, measurement |
| `production-pipeline.md` | End-to-end: topic → script → images → narration → render → upload |
| `video-description-template.md` | The description the agent pastes into every upload |
| `themes.md` | Cross-episode database: every episode's 6-theme intensity ratings. Append-only. |
| `scripts/01-peasants-revolt-1381.md` | Episode 1 — shipped, unlisted. "Why Failed Rebellions Still Win" |
| `assets/peasants-revolt-1381/` | Episode 1 assets: 20 Pollinations images, segment + full narration MP3s, `images.md`, `segments.json` |
| `_archive/` | Pre-pivot Dancing Plague 1518 script + 22 PD source manifest + pre-pivot source_images.py helper |

## Critical non-file assumptions
1. ~~Robert's existing YouTube channel will be rebranded as "Margins of History"~~ — **resolved 2026-04-11**: channel was rebranded to "Breaking Points" (ep1 shipped under that name).
2. ~~Robert will provide a YouTube Data API v3 OAuth refresh token when ready~~ — **resolved 2026-04-11**: token exists in Robert's local `.env` (ep1 uploaded twice via `tools/youtube_upload.py`).
3. Ko-fi and Buy Me a Coffee accounts for `bobbyebaby` — **still pending** per `human_inbox/0003-youtube-api-and-tips-setup.md`. Video description templates currently skip the tip-rail links until the accounts exist. Not blocking.
4. Gumroad link pointing at the Power Prompts pack from B-002 — cross-promotion target exists but is still pending Gumroad upload (B-002 build phase done, upload blocked on Gumroad cred).
5. ~~Public domain imagery only. No AI-generated illustrations.~~ — **changed 2026-04-11 pivot**: episode 1 used 20 AI-generated images via Pollinations.ai, keyless free tier. The PD-only rule was relaxed when Robert pivoted from "obscure history" to "rebellions with thematic analysis" on the grounds that rebellion scenes (crowds, city storming, kings on horseback) are underserved by clean-licensed period imagery and Pollinations with careful per-beat prompts produces better narrative match than recycled Wikimedia stock. The disclosure risk under the Jan 2026 YouTube inauthentic-content filter is real but mitigated by (a) high prompt specificity per narration beat, (b) no text-on-image AI generation, (c) channel name and script are human-written + editorially voiced.

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

## Decision history
**Original (2026-04-11 morning):** agent picked "obscure/forgotten history" niche under the name "Margins of History" per the minimal-interaction directive. First episode queued was Dancing Plague of 1518.

**Pivot (2026-04-11 afternoon):** Robert pivoted the niche to "rebellions across history with 6-theme analysis" under the name "Breaking Points". The six themes are [[../../wiki/themes/economy|Economy]], [[../../wiki/themes/royalty|Royalty]], [[../../wiki/themes/government|Government]], [[../../wiki/themes/wars|Wars]], [[../../wiki/themes/environment|Environment]], [[../../wiki/themes/debt|Debt]]. Every episode rates 0–3 per theme and the running database is in `themes.md`. The channel thesis is [[../../wiki/concepts/structural-vs-tactical-victory]]. Dancing Plague was archived (not deleted) in `_archive/`. Episode 1 was rewritten to the Peasants' Revolt of 1381 (intensity 14/18, outcome `partial_win`) and shipped unlisted the same day.

**Ongoing:** every new episode (B-018 onward) must append a new row to `themes.md`, create a rebellion page in `wiki/rebellions/`, stub any new figures/concepts/themes, and update `wiki/index.md`. This is part of the episode-scripted definition of done.
