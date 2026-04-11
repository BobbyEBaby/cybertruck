# Production Pipeline — YouTube "Breaking Points" Channel (REVISED 2026-04-11)

End-to-end flow for turning a rebellion topic into a published video. Designed for **remote-doable build** with **local-only rendering and upload** where necessary.

## Overview
```
Rebellion topic (from topic queue)
  → Script + thematic analysis + Pollinations prompts + theme intensities
  → Generate 20 images via Pollinations.ai
  → Quality gate (auto or human)
  → Narration via Edge TTS (default) or StyleTTS2 (quality upgrade, local GPU)
  → Storyboard JSON
  → Video render via ffmpeg (Ken Burns pan/zoom, audio mix)
  → Thumbnail
  → Description from template + timestamps + sources
  → [handoff: YouTube API upload OR drag-drop to Studio]
  → Update themes.md with the episode's 6 theme intensity ratings
```

## Step-by-step

### 1. Topic selection (remote, no creds)
Pick the next rebellion from the topic queue, or if none is queued, WebSearch for a candidate that adds **novel theme intensities** to `themes.md`. Criteria:

- Pre-1970 (so the analytical perspective is settled and Pollinations can render it without generating modern people)
- Has at least 3 themes at intensity ≥2 (otherwise it's not actually a *rebellion*, it's something else)
- Has a clean narrative arc (rising tension → climax → aftermath)
- Not already covered by a massive channel (search YouTube, skip if top result has >3M views)
- Adds contrast to the existing themes.md database — if the last 3 episodes were all high-debt rebellions, pick a low-debt high-environment one next

Seed topic queue (suggested order after Peasants' Revolt 1381):
1. ✅ **Peasants' Revolt 1381** (England) — covered by Episode 1, high on Economy/Environment/Government
2. **German Peasants' War 1524–25** — religious + economic, massive scale, Luther's betrayal
3. **Boxer Rebellion 1899–1901** (China) — environment (drought famine) + foreign occupation
4. **Pugachev's Rebellion 1773–75** (Russia) — Cossack + peasant, debt + serfdom
5. **Spartacus 73–71 BC** (Roman Republic) — slavery + military overreach
6. **Taiping Rebellion 1850–64** (China) — most deadly war of 19th century, religion + economy + environment
7. **Bacaudae** (3rd century Gaul) — little-known, Roman imperial decline
8. **Nika Riots 532 AD** (Constantinople) — urban rebellion, sports factions → political
9. **Kett's Rebellion 1549** (England) — direct sequel to Peasants' Revolt
10. **Haitian Revolution 1791–1804** — only successful slave rebellion in modern history

### 2. Research + script (remote, WebSearch)
Before writing a single line, collect:
- 4+ reputable sources (academic, museum, primary chronicle, Wikipedia for summary)
- A list of provable facts with inline citations (as HTML comments in the script file)
- An honest assessment of any disputed points (avoid definitive claims on contested history)

Then write the script following the **Breaking Points structure** (see `strategy.md`):
- Hook (30 sec, vivid climax snippet)
- Context (60 sec)
- Story (4.5 min, three beats)
- **Thematic analysis (2.5 min)** — non-negotiable, this is the channel's differentiator
- Why it matters now (60 sec, non-partisan)
- Outro + CTA (60 sec)

Word count target: **1,500–1,700 words** (at 160 wpm = 9.4–10.6 minutes). The slightly slower pace than generic faceless channels is intentional — gives room for breath and intonation, avoids the "rapid-fire monotone" pattern that YouTube's inauthentic-content classifier flags.

**Every script file MUST end with two sections (not spoken):**

**A. Theme intensities** — the 6 numbers (0–3) with a one-sentence justification each, plus the rebellion's outcome (`crushed | partial_win | full_win | triggered_reform | unclear`). This gets copied to `themes.md` when the episode publishes.

**B. Pollinations prompts** — 20 image prompts matching narration beats, formatted for `tools/generate_images.py`. Each prompt should specify: period, subject, style, color palette, and quality cues. Example:
```
01. oil painting, 14th century English village, weathered peasants at dawn walking with scythes and staves, warm brown palette, ominous gray sky, museum quality, illuminated manuscript aesthetic
02. medieval engraving, a tax collector harassing a woman in front of her home, Kent England 1381, onlookers gathering, detail of angry faces, black and white crosshatch woodcut style
...
```

### 3. Image generation (remote, no creds — B-013)
`python tools/generate_images.py <video-slug>` — reads the Pollinations prompts from the script file, calls `https://image.pollinations.ai/prompt/{url-encoded-prompt}` for each, downloads to `assets/<slug>/img_NN.jpg`, writes `images.md` manifest.

**Rate-limit courtesy:** 2-second delay between requests. Pollinations is a community resource — don't hammer it.

**Quality gate:** after generation, an automated pass (if agent has vision) or human review flags bad images. Bad generations get revised prompts and regeneration. Target: all 20 images are "good enough to ship."

### 4. Narration (remote for Edge TTS, local for StyleTTS2 — B-014)
Default: `python tools/narrate.py <video-slug>` runs Edge TTS via the `edge-tts` Python package.

Voice rotation per episode to A/B test:
- Odd episodes: `en-US-GuyNeural`
- Even episodes: `en-US-AriaNeural`

Long scripts are split into paragraphs, each narrated, then concatenated with ffmpeg's concat demuxer to reduce API stutter.

**Upgrade path — StyleTTS2:** if Robert's local machine has a capable GPU (≥8GB VRAM), switch `narrate.py` to use StyleTTS2 via the `sidharthrajaram/StyleTTS2` Python package. Noticeably higher quality, especially for emotional prosody. Requires local execution (not remote-doable).

**Output:** `assets/<slug>/narration.mp3`

### 5. Storyboard (remote)
Write `assets/<slug>/storyboard.json` mapping each image to narration timestamps. This drives the ffmpeg render. The storyboard should time image transitions to narration beats (image 01 is on screen while the hook is spoken, etc.).

```json
{
  "video_slug": "peasants-revolt-1381",
  "title": "The Peasants Who Nearly Toppled an English King (1381)",
  "target_length_seconds": 600,
  "images": [
    {"file": "img_01.jpg", "start": 0.0, "end": 8.5, "motion": "slow-zoom-in"},
    {"file": "img_02.jpg", "start": 8.5, "end": 17.0, "motion": "pan-right"}
  ],
  "narration": "narration.mp3",
  "music": "background.mp3",
  "output_resolution": "1920x1080"
}
```

### 6. Video render (local — B-015)
`python tools/render_video.py <video-slug>` — reads the storyboard, runs ffmpeg with Ken Burns pan/zoom on each image, mixes narration (0 dB) + background music (-20 dB), exports 1080p H.264 MP4, CRF 18. Depends on ffmpeg being installed locally.

Output: `assets/<slug>/final.mp4`

### 7. Thumbnail (remote or local)
Pick the most striking image from the 20 generated (usually image 01, the hook). Overlay the episode's 3–5 word title in high-contrast white text with a dark outline. Use ffmpeg's `drawtext` filter.

Output: `assets/<slug>/thumbnail.jpg`

### 8. Description + tags (remote)
Use `video-description-template.md` and fill in: video-specific hook line, timestamps, sources list, donate links (all 4 rails), music credit, tags. First 150 characters show in search preview — make them count.

### 9. Upload (local — B-016 if OAuth token exists, else manual)
- **Automated:** `python tools/youtube_upload.py <video-slug>` uploads MP4 + sets title/description/tags/thumbnail + schedules publish. Needs `YOUTUBE_OAUTH_REFRESH_TOKEN` in `.env`.
- **Manual:** Robert opens YouTube Studio, drags the MP4 in, pastes the description, uploads the thumbnail, publishes. ~2 minutes.

### 10. Update themes.md (remote)
After upload, the next run copies the episode's theme intensities into `themes.md` (append-only) and updates the "Observations" section if this is the 3rd+ episode. This is the step that makes the channel's analytical thesis real over time.

### 11. Track metrics (remote, next run)
Next run pulls view/watch-time/CTR/sub-gain stats via YouTube Data API (read-only — same token). Updates the metrics table in the episode script file.

## Tools to build
- `tools/generate_images.py` (B-013) — Pollinations.ai wrapper
- `tools/review_images.py` (B-013b) — quality gate, regenerate bad images
- `tools/narrate.py` (B-014) — Edge TTS + StyleTTS2 wrapper
- `tools/render_video.py` (B-015) — ffmpeg storyboard-to-MP4
- `tools/youtube_upload.py` (B-016) — YouTube Data API upload
- `tools/youtube_stats.py` (future) — fetch metrics for published episodes

All helpers follow the `tools/deploy_pages.sh` pattern: read `.env` safely, never echo credentials, append to `state/publish-log.md` on success.

## Honesty checkpoint
If at any step something doesn't work (Pollinations down, Edge TTS broken, ffmpeg missing), the agent writes an honest runlog entry and stops on that task. No fake completion.
