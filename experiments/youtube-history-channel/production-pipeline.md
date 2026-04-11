# Production Pipeline — YouTube History Channel

End-to-end flow for turning a topic into a published video. Designed for **remote-doable build** + **local-only upload**.

## Overview
```
Topic  →  Script  →  Source list  →  Image download  →  Narration (Edge TTS)
  →  Storyboard  →  Video render (ffmpeg)  →  Thumbnail  →  Description + tags
  →  [human handoff: upload to YouTube Studio]  →  Metrics tracking
```

## Step-by-step

### 1. Topic selection (remote, no creds)
Open `experiments/youtube-history-channel/scripts/` and pick the next script file that's marked `status: queued`. If none, WebSearch for "strange/forgotten/surprisingly consequential historical events" and add 3 candidates to a `topic-queue.md` file, then pick one.

**Topic criteria:**
- Happened before 1960 (so public domain imagery exists)
- Has a clean narrative arc (beginning, conflict, resolution, lesson)
- Some existing search demand (check Google Trends / YouTube search bar autocomplete)
- Not already dominated by a massive channel (search YouTube, skip if top result has >1M views)
- Ethically unambiguous (don't do Holocaust-adjacent or recent trauma content without serious care — this is a faceless channel, not the venue for that weight)

### 2. Research + script (remote, WebSearch)
Before writing a single line, collect:
- 3+ reputable sources (academic, Wikipedia, primary-source archive, museum site)
- A list of provable facts with sources
- A list of common misconceptions to correct

Then write the script. Structure:

```
## Hook (0:00–0:20, ~50 words)
A surprising claim or question. No throat-clearing.

## Context (0:20–1:30, ~180 words)
Set the scene. Where, when, who, why the world was the way it was.

## The story (1:30–5:30, ~720 words)
Three beats. Each beat ~240 words / ~90 seconds. Clear transitions.

## Why it matters (5:30–6:30, ~180 words)
The through-line to now. Why a viewer should care in 2026.

## Outro + CTA (6:30–7:30, ~180 words)
Thank the viewer, mention 1 donate link naturally (rotate which one per video to measure), soft sub ask, tease next video.
```

**Word count target: 1,300–1,500 words** (at a 165 wpm narration pace = 7.9–9.1 minutes). Every claim must have an inline source citation (not in the spoken narration, but in the script file as a comment for verification).

Save as `experiments/youtube-history-channel/scripts/<NN>-<slug>.md` with frontmatter:
```
---
status: scripted  # queued, scripted, sourced, narrated, rendered, uploaded, live
title: <exact YouTube title, ≤60 chars, SEO-friendly>
slug: <kebab-case-for-filenames>
target_length_seconds: 480
sources:
  - <url 1>
  - <url 2>
  - <url 3>
topic_queue_position: <N>
---
```

### 3. Image sourcing (remote, no creds)
For each ~30 seconds of narration, source 1–2 images. Target: 15–25 images per 8-minute video.

**Sources (in order of preference):**
1. **Library of Congress Free to Use & Reuse** — https://www.loc.gov/free-to-use/ — 40,000+ genuinely public domain images, U.S. government origin, zero copyright risk.
2. **Wikimedia Commons** — https://commons.wikimedia.org — public domain + CC-licensed. Check the license on each image. Avoid "Fair use" flagged.
3. **Internet Archive** — https://archive.org — old books, maps, photographs.
4. **Flickr Commons** — https://www.flickr.com/commons — institutional uploads, all public domain.
5. **New York Public Library Digital Collections** — https://digitalcollections.nypl.org — ~900,000 public domain items.

**Forbidden:**
- Getty Images (paid, aggressive DMCA)
- Shutterstock / Alamy / Adobe Stock (paid)
- Google Image Search "as-is" (random licensing)
- AI-generated images (undermines credibility + YouTube "inauthentic content" policy)

For each sourced image, download to `experiments/youtube-history-channel/assets/<video-slug>/` and record in a `sources.md` file:
```
- img01.jpg — https://www.loc.gov/item/... — public domain (LoC)
- img02.jpg — https://commons.wikimedia.org/wiki/File:... — CC-BY-SA 4.0 (credit: Foo Bar)
```

### 4. Narration (remote or local, depends on tooling)
Use **Microsoft Edge TTS** — free, no signup, compatible with OpenAI API shape via the `edge-tts` Python package. Install once: `pip install edge-tts`. Usage:
```
edge-tts --voice en-US-GuyNeural --text "script text here" --write-media narration.mp3
```
For long scripts, split by paragraph and concatenate — reduces API stutter.

**Voice selection:** en-US-GuyNeural (warm male baritone) or en-US-AriaNeural (clear female) — rotate per video to A/B test which performs better over the first ~10 videos.

Save as `assets/<video-slug>/narration.mp3`.

### 5. Storyboard (remote)
Write a `storyboard.json` mapping each image to narration timestamps. This drives the ffmpeg render.

```json
{
  "video_slug": "dancing-plague-1518",
  "images": [
    {"file": "img01.jpg", "start": 0.0, "end": 8.5, "motion": "zoom-in"},
    {"file": "img02.jpg", "start": 8.5, "end": 17.0, "motion": "pan-right"},
    ...
  ],
  "narration": "narration.mp3",
  "music": "background.mp3",
  "output_resolution": "1920x1080"
}
```

### 6. Video render (local — needs ffmpeg)
Render with ffmpeg. A helper script `tools/render_video.py` (to be built when B-013 picks up this task) will:
- Read the storyboard
- For each image: apply Ken Burns zoom/pan using ffmpeg's `zoompan` filter
- Concatenate image clips
- Mix narration + background music (narration at 0 dB, music at -20 dB)
- Export as 1080p H.264 MP4, ~60fps, CRF 18

Save as `assets/<video-slug>/final.mp4`.

### 7. Thumbnail (remote or local)
One image from the sources, high-contrast, with 3–5 words of title text overlaid. Use ffmpeg's `drawtext` filter or PIL. No AI-generated thumbnails — use a real image from the video.

Save as `assets/<video-slug>/thumbnail.jpg`.

### 8. Description + tags (remote)
Use `experiments/youtube-history-channel/video-description-template.md` and fill in:
- Video-specific intro line
- Timestamps (generated from the script's structure)
- Sources (cited)
- Donate links (all 4 streams)
- Subscribe CTA

### 9. Upload (local or manual)
Two options:
- **Automated** (requires YouTube Data API OAuth refresh token in `.env`): `tools/youtube_upload.py <video-slug>` — uploads the MP4, sets the title/description/tags/thumbnail, schedules publish. Helper script to be written in B-016.
- **Manual**: Robert opens YouTube Studio, clicks "Upload video", drags `final.mp4`, pastes the description, uploads `thumbnail.jpg`, publishes. ~2 minutes per video until the API token is wired.

### 10. Track (remote, next run)
After upload, the next remote run pulls the video stats via YouTube Data API (read-only — uses the same token) and updates `experiments/youtube-history-channel/scripts/<NN>-<slug>.md` with views, watch time, CTR, subs gained.

## Tools to build (each as a future backlog item)
- `tools/source_images.py` — given a list of search terms, queries LoC + Wikimedia + Archive.org APIs and downloads results
- `tools/narrate.sh` — wraps `edge-tts` with our voice preferences and file conventions
- `tools/render_video.py` — storyboard → final.mp4 via ffmpeg
- `tools/youtube_upload.py` — OAuth + upload + metadata (future, after Robert provides the API token)

**Constraint:** each of these tools, when built, follows the same rules as `tools/deploy_pages.sh` — read `.env` safely, never echo credentials, append to `state/publish-log.md` on success.
