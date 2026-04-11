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

- **Popular Uprisings** — the inflection moments when tolerable grievance becomes revolt
- **Powder Keg** — the accumulation of tension that eventually explodes
- **Rising** — short, direct, evocative of popular movements

**Default: Popular Uprisings** unless Robert picks a different one. Rationale: names the analytical framework ("what was breaking?") and is already associated with serious editorial content.

## Video format
- **Length:** 3–5 minutes (~500–700 words at ~130 wpm effective rate, given the -15% narration rate). Changed 2026-04-11 from the original 8–12 min long-form format. Rationale: ep1 and ep2 were written at 11 min / ~1,650 words and the production cost per episode was too high relative to the unknown-channel discovery ceiling; short-form is cheaper to iterate and matches the 2026 YouTube-Shorts-adjacent attention pattern. Ep1 and ep2 remain as long-form archive — the new format starts at ep3.
- **Short-form structure (ep3 onward, ~3–5 min):**
  - **0:00–0:20 Hook** — the climax-first opening, one vivid sentence
  - **0:20–1:00 Context** — when, where, who, stripped to essentials
  - **1:00–3:00 The story** — two narrative beats, not three; each ends on tension
  - **3:00–4:00 Thematic analysis** — hit 2–3 themes max at high intensity, don't force all six
  - **4:00–4:30 Why it matters now + outro + CTA** — one tip rail rotation per video
- **Deprecated long-form structure (ep1/ep2 only, archived):**
  - 0:00–0:30 Hook / 0:30–1:30 Context / 1:30–6:00 Story (3 beats) / 6:00–8:30 Thematic analysis (all 6 themes) / 8:30–9:30 Why it matters / 9:30–10:30 Outro. Listed here so the ep1/ep2 scripts still match a documented format — do not use for new episodes.
- **Visuals:** **AI-generated imagery via Pollinations.ai**, prompted per narration beat with period-appropriate style (e.g., "oil painting, 14th century English countryside, serfs with scythes, warm brown tones, museum quality"). 15–25 unique generated images per video. Ken Burns pan/zoom via ffmpeg. For specific famous paintings that audiences recognize (the Vermeer of the Dutch Golden Age, etc.), use the public-domain original instead of a generation. The mix is: ~80% generated, ~20% real historical art when the real art is iconic.
- **Narration:** **Microsoft Edge TTS** as the default (free, decent intonation, zero setup). **StyleTTS2** as the quality-upgrade path for any episode we want to push harder on — it produces genuinely studio-grade narration that rivals ElevenLabs for long-form content. StyleTTS2 requires a local GPU (tested working on RTX 3060 12GB via one-click Microsoft Store installer). If Robert's machine has a capable GPU, we default to StyleTTS2; if not, Edge TTS for the first batch of episodes and we re-evaluate.
- **Music:** Public domain classical (IMSLP) or CC-BY from incompetech.com / YouTube Audio Library. Score the video to the narrative beats — ominous during the context setup, driving during the rebellion itself, contemplative during the analysis.
- **Human creative layer (strongly recommended, final call is Robert's):** A short (10–20 second) hand-recorded intro per video from Robert: *"I'm [voice], this is Popular Uprisings. Today: the peasants who nearly toppled an English king."* That small human element is the single biggest cheap hedge against the inauthentic-content policy. Without it we rely entirely on content quality to pass.

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

### Narrator voice (locked 2026-04-11)
The canonical narrator is **`en-GB-RyanNeural`** (Edge TTS, UK male, older tone). Rate `-15%`, pitch `-2Hz`. Hardcoded in `tools/narrate.py` (lines 56–64). This is the voice ep1 v2 shipped with. **Do not change it silently.** If a future run wants to swap to StyleTTS2 or a different Edge voice, it must open a decision note in `human_inbox/` first and get Robert's sign-off.

Reason for the lock: an earlier commit message ("clean XTTS") suggested an engine/voice swap that did not actually correspond to a code change — the tool was still Edge TTS UK throughout — which made the v4 voice state ambiguous for later runs. The lock eliminates that ambiguity. The voice decision is part of the brand, not an implementation detail.
