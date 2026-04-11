# YouTube History Channel — Strategy (REVISED 2026-04-11)

**Existing channel:** https://studio.youtube.com/channel/UCv8vMc6ZN9Tkc0K5gx53iAA (Robert's, pre-existing, will be rebranded)
**Backlog items:** B-012 through B-017
**Status:** revised — first video queued

## The pivot (2026-04-11)
An earlier version of this file proposed a generic "obscure history" niche using public domain imagery + flat Edge TTS narration. That plan matched 2 of 4 risk signals for YouTube's January 2026 mass-termination wave against templated faceless AI content (see `research/markets/06-faceless-youtube.md`). Per Robert's direction: **pivot to quality over cadence**, with a sharper editorial thesis, better voice work, and original generated imagery tailored to each episode.

## Channel concept: the history of rebellions, with consistent thematic through-lines

Every episode tells the story of a specific rebellion — pre-Roman to modern — and analyzes it across **six recurring dimensions** (the "themes tracker"). Over many episodes these accumulate into a cross-historical database of *why people revolt*. That analytical through-line is the differentiation: most history channels tell one story at a time; this one is incrementally building a theory.

**The six themes** (analytical spine of every episode, and of `themes.md`):
1. **Economy** — inflation, price shocks, food scarcity, taxation, wealth concentration
2. **Royalty / leadership** — legitimacy crisis, succession disputes, weak or absent ruler, visible excess
3. **Government** — corruption, failed justice, representation denied, bureaucratic overreach
4. **Wars** — military overreach, veteran grievances, conscription, border losses
5. **Environment** — famine, plague, weather shocks, resource depletion
6. **Debt** — sovereign, personal, religious (indulgences, tithes)

**Why this works:**
- Strong editorial thesis viewers can follow across episodes
- Repeat-viewer mechanic: "if you liked the Peasants' Revolt one, you'll like the Bread March one"
- SEO-friendly: each episode targets a specific event + a universal theme
- Non-templated: the thematic analysis prevents the "recycled script" trap that gets faceless channels flagged
- Genuinely educational: real historians teach rebellion history this way

## Channel name — three candidates, pick one

- **Breaking Points** — the inflection moments when tolerable grievance becomes revolt
- **Powder Keg** — the accumulation of tension that eventually explodes
- **Rising** — short, direct, evocative of popular movements

**Default: Breaking Points** unless Robert picks a different one. Rationale: names the analytical framework ("what was breaking?") and is already associated with serious editorial content.

## Video format
- **Length:** 8–12 minutes. Rationale: enough room for the story + the thematic analysis + the cross-episode "previously on Breaking Points" callbacks; also clears the ≥10 min mid-roll-ad threshold once the channel hits YPP. The 2026 research sweet spot is 7–15 min; 8–12 is the educational-content peak.
- **Structure:**
  - **0:00–0:30 Hook** — a vivid 2-sentence opening scene from the climax of the rebellion
  - **0:30–1:30 Context** — when, where, who, what the world looked like
  - **1:30–6:00 The story** — three narrative beats, each ending on a beat of tension
  - **6:00–8:30 Thematic analysis** — walk through the six themes, calling out which ones were present with what intensity. Cite earlier episodes where the same pattern appeared ("we saw this same fiscal overreach in the Boxer Rebellion two episodes ago")
  - **8:30–9:30 Why it matters now** — the through-line to 2026, never preachy, never political-tribe-coded
  - **9:30–10:30 Outro + CTA** — rotate one tip rail per video in the spoken copy
- **Visuals:** **AI-generated imagery via Pollinations.ai**, prompted per narration beat with period-appropriate style (e.g., "oil painting, 14th century English countryside, serfs with scythes, warm brown tones, museum quality"). 15–25 unique generated images per video. Ken Burns pan/zoom via ffmpeg. For specific famous paintings that audiences recognize (the Vermeer of the Dutch Golden Age, etc.), use the public-domain original instead of a generation. The mix is: ~80% generated, ~20% real historical art when the real art is iconic.
- **Narration:** **Microsoft Edge TTS** as the default (free, decent intonation, zero setup). **StyleTTS2** as the quality-upgrade path for any episode we want to push harder on — it produces genuinely studio-grade narration that rivals ElevenLabs for long-form content. StyleTTS2 requires a local GPU (tested working on RTX 3060 12GB via one-click Microsoft Store installer). If Robert's machine has a capable GPU, we default to StyleTTS2; if not, Edge TTS for the first batch of episodes and we re-evaluate.
- **Music:** Public domain classical (IMSLP) or CC-BY from incompetech.com / YouTube Audio Library. Score the video to the narrative beats — ominous during the context setup, driving during the rebellion itself, contemplative during the analysis.
- **Human creative layer (strongly recommended, final call is Robert's):** A short (10–20 second) hand-recorded intro per video from Robert: *"I'm [voice], this is Breaking Points. Today: the peasants who nearly toppled an English king."* That small human element is the single biggest cheap hedge against the inauthentic-content policy. Without it we rely entirely on content quality to pass.

## Publishing cadence
- **When it's ready, ship it.** No weekly deadline pressure. A channel of 6 excellent videos in 6 months beats a channel of 24 mediocre ones.
- **Minimum activity floor:** must publish at least 1 video per month to stay above YouTube's 30/60/90-day activity thresholds and avoid inactivity-triggered demonetization warnings.
- **Target rhythm:** 1–2 videos per week once the pipeline is smooth, but not before the first 3 videos have proven the process.

## Revenue streams (unchanged from the original plan — all still apply)
Day-1: crypto tips (Kraken USDC-SOL + backup rails), Ko-fi (0% fee), Buy Me a Coffee (5% fee), Gumroad "deep dive PDF" per video ($3+).
Gated (later): YouTube Partner Program (ad share) at 1,000 subs + 4,000 watch hours. Early tier (Super Chat, memberships) at 500 subs + 3,000 watch hours.
Affiliate: Amazon Associates for history books (requires application + first sale within 180 days).
Sponsorships: year 1+, only when audience is real.

## Guardrails (inherited + tightened)
- **No AI-generated imagery of real modern people.** Historical figures only. No deepfakes of living people.
- **Every factual claim cited in-script.** Historical accuracy is the whole credibility anchor. One bad fact undermines the thesis.
- **Balanced analysis, never tribal.** The themes framework is designed to be politically neutral — we describe the structural conditions, not pick a side from the present.
- **Never use manipulative hooks** (*"You won't believe..."*, *"THIS CHANGED EVERYTHING"*). The audience we want responds to substance.
- **1 upload per 24h max** (rate limit).
- **Never reply to comments from the agent.** Log them, don't engage.
- **Circuit breaker:** if 4 consecutive videos get <50 views each in their first 14 days, pause the channel for a strategic review.

## Tech stack
| Component | Default | Upgrade path |
|---|---|---|
| Voice | Microsoft Edge TTS (free, `en-US-GuyNeural` or `en-US-AriaNeural`, remote-runnable via `edge-tts` Python package) | StyleTTS2 locally (free, studio quality, requires GPU) |
| Images | Pollinations.ai (free, no key, URL-based API, SDXL/Flux) | Local Stable Diffusion if Pollinations gets rate-limited or shuts down |
| Music | Incompetech / YouTube Audio Library (free, CC-BY) | IMSLP public domain classical for period fit |
| Video render | ffmpeg (free, standard) | same |
| Upload | YouTube Data API v3 (requires OAuth refresh token in `.env`) | Manual drag-drop into YouTube Studio as fallback |
| Analytics | YouTube Data API v3 read-only (same token) | same |

## Measurement
| Metric | Target by month 1 | Target by month 3 |
|---|---|---|
| Videos published | 2 | 6 |
| Average views per video (7d) | 50 | 300 |
| Average retention (AVD) | 55% | 60% |
| Subscribers | 20 | 150 |
| Crypto tips | $0 (normal) | $5–20 |
| Ko-fi / BMC tips | $0 (normal) | $5–20 |

## Honesty anchor
From `state/honest-expectations.md`: most creators never break 1,000 subs. The "rebellions with thematic analysis" concept is strong but unproven. The loop's job is to make the *highest-quality attempt possible at $0*, measure honestly, and kill the experiment if it doesn't work by month 3.
