# YouTube History Channel — Strategy

**Existing channel:** https://studio.youtube.com/channel/UCv8vMc6ZN9Tkc0K5gx53iAA (Robert's, pre-existing, will be rebranded)
**Backlog items:** B-012 through B-017
**Status:** planning → first video in production

## Decision log (made without user input per "minimal interaction" directive)

### Niche: Obscure / Forgotten History
**Why:** Current 2026 research explicitly identifies "unusual historical events, obscure facts, or short storytelling" as still-working niches that aren't saturated, while broad history (WWII, Rome, etc.) is a battlefield. Obscure history rewards curiosity-driven CTR and is easy to differentiate with depth of research.

**Sub-niche focus:** Strange, forgotten, or surprisingly consequential events that most people have *heard of vaguely* but don't actually know. The hook is "you've heard of this — here's what actually happened, and why it matters." That beats "here's something you've never heard of" because pure novelty has no search demand.

**What we are not:** Not "Top 10" listicle content. Not "In 60 seconds." Not rage-bait. Not conspiracy-adjacent.

### Channel name proposal: "Margins of History"
Evocative, literate, describes the niche (the stuff in the margins of the main textbook), easy to say, available as a handle likely. Robert can rebrand the existing channel (`UCv8vMc6ZN9Tkc0K5gx53iAA`) to this — edit in YouTube Studio → Customization → Basic info.

### Video format
- **Length:** 7–9 minutes. Rationale: the 2026 data puts the sweet spot at 7–15 min; educational content peaks at 8–12; retention beats length; we pick 7–9 as the lower-risk sweet spot for an unproven channel because shorter videos need less sustained quality to keep retention at 60%+. Bump to 10–12 min once monetization is on (mid-roll ads need ≥8 min, ideally ≥10).
- **Structure:** Hook (0:00–0:20) → context (0:20–1:30) → the actual story (1:30–5:30) → why it matters now (5:30–6:30) → light CTA + donate mention (6:30–7:30).
- **Images:** Public domain only — Library of Congress Free to Use collection (40,000+ images), Wikimedia Commons, Archive.org, Internet Archive, Flickr Commons. Ken Burns pan-and-zoom effect via ffmpeg. NO AI-generated images — they undermine credibility on a history channel and YouTube is cracking down on "inauthentic content."
- **Narration:** Microsoft Edge TTS (free, high-quality, OpenAI-API-compatible). Use the "en-US-GuyNeural" or "en-US-AriaNeural" voices — both clear and natural. Coqui is dead as of Dec 2025.
- **Music:** Free background music from Kevin MacLeod / incompetech.com (CC-BY) or YouTube Audio Library. Always credit in description.
- **Subtitles:** Auto-generated via whisper.cpp, hand-correctable. Accessibility + watch-time boost.

### Publishing cadence
- **Week 1–4:** 1 video per week. Sustainable, lets us measure each one's performance without muddying the signal.
- **Week 5+:** If retention and CTR are good (CTR >4%, AVD >60%), bump to 2/week.
- **Never more than 3/week.** Quality collapses first, reputation follows.

## Revenue streams (multiple, day-1 unless noted)

| # | Stream | Status | Mechanism | Cost | Notes |
|---|---|---|---|---|---|
| 1 | **Crypto tips to Kraken** | Day 1 | 5 deposit addresses in video description (USDC-Sol, XRP, DOGE, BTC, ZEC) | $0 | Primary. Works from the first view. Highest-leverage per tipper. |
| 2 | **Ko-fi** | Day 1 | ko-fi.com/bobbyebaby link in description | $0 (0% fee) | Creator-friendly tip rail. |
| 3 | **Buy Me a Coffee** | Day 1 | buymeacoffee.com/bobbyebaby link | $0 (5% fee) | Wider audience than Ko-fi. |
| 4 | **Gumroad bonus PDFs** | Day 1 after B-002 ships | "Deep dive PDF for $3" linked from each video's description | $0 (free Gumroad tier) | Most viewers won't pay but a fraction will. Cross-promotes B-002 and any future Gumroad assets. |
| 5 | **YouTube Partner Program (ads)** | Month 6+ (gated) | Standard YouTube ads | $0 | Requires 1,000 subs + 4,000 watch-hours. Not depended-on in the plan. |
| 6 | **Amazon Associates affiliate** | Month 2+ (needs application) | "If you want to read more, this is the book I used" link at end | $0 | Requires AA approval + first sale within 180 days. Book recommendations are natural for history. |
| 7 | **Channel memberships** | Month 6+ (gated, needs 1k subs) | YouTube-native membership | $0 | Long-term only. |
| 8 | **Sponsorships** | Year 1+ (unlikely before) | Brand deals | $0 | Need real audience first. Do not chase. |

**Revenue priority (first 90 days):** Streams 1–4 only. Don't even mention YPP in descriptions — it's aspirational noise until hit.

## Production pipeline (see `production-pipeline.md` for details)
Remote agent writes the script + sources the public-domain images + renders the video locally via ffmpeg. Local agent uploads to YouTube (or Robert drags-and-drops into Studio). Description, tags, thumbnail all pre-generated. The manual step is exactly 1 click (publish).

## Guardrails (inherited from CLAUDE.md)
- No AI-generated images (quality + credibility + TOS)
- No fake engagement, no comment astroturf, no view-bot anything
- Never reply to comments from the agent — log them for the next run to read, do not respond
- 1 upload per 24h max (hard rate limit)
- Factual accuracy is non-negotiable. History content lives and dies on credibility. Every claim must cite a source. If the agent can't source a claim in ≤5 min of WebSearch, the claim gets cut.
- Public domain imagery only. No "fair use" wiggle-room. No stock footage with unclear licenses.

## Measurement
| Metric | Target by week 4 | Target by month 3 |
|---|---|---|
| Subscribers | 20 | 200 |
| Video views (per video, 7d) | 100 | 500 |
| Watch time per video | >50% AVD | >55% AVD |
| Crypto tips received | $0 (normal) | $5–$20 |
| Ko-fi / BMC tips | $0 (normal) | $5–$20 |

**If by week 4 we're at 0 subs and <20 views per video, circuit-break the category** — same rule as other experiments. Stop shipping new videos, do research and a strategic review.

## Honesty anchor
From `state/honest-expectations.md`: most creators in this space never break 1,000 subs. We're designing the system for honest shots-on-goal and compounding quality, not for guaranteed outcomes. The Partner Program threshold may never be crossed. Crypto tips + direct tip rails are the real near-term path; we design around them.
