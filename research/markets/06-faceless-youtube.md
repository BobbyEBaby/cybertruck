# 06 — Faceless YouTube / Shorts

## What it is
A YouTube channel where the agent generates scripts, the human (or a free TTS) does voice-over, stock footage / generative imagery is the visual, and the channel uploads on a schedule. Niches: explainer, top-10, AI news, creepypasta, history shorts.

## Monetization paths
- YouTube Partner Program (requires 1k subs + 4k watch hours, or 1k subs + 10M shorts views)
- Affiliate links in description
- Sponsorships once channel hits scale

## Why this is interesting at $0
- YouTube hosting is free
- Free TTS exists; free stock footage exists (Pexels, Pixabay)
- Compounds over time (old videos earn for years)

## Risks / honest downsides
- YouTube is hostile to obviously-AI content with no value-add
- Monetization eligibility is high: minimum 1k subs is a serious bar
- Time-to-first-dollar is **months** even when it works
- Quality bar for TTS + video editing is rising fast; the floor is now near-human
- This category requires sustained creative judgment — "what do people actually want to watch" is the entire game

## Scoring
- Time-to-first-dollar: **1**
- $0 viability: **5**
- Automation-friendliness: **2** (script yes; deciding what's good and what's not is hard for an agent)
- Ceiling: **5** (top faceless channels clear five figures/mo)
- **Total: 13 / 20**

## First concrete experiment idea
Defer. High ceiling but slow and creatively bottlenecked — bad first bet.

## Refreshed 2026-04-11

Remote run #6 (see runlog). This refresh fires specifically to sanity-check the experiments/youtube-history-channel/ build (B-012..B-017) **before** more effort sinks in, because that whole experiment assumes the "faceless + TTS + slideshow" path is still viable. Turns out the answer is "yes, but not in the shape we planned."

### Sources
1. YouTube Help — Changes to YouTube Partner Program terms (https://support.google.com/youtube/answer/12843009)
2. YouTube Help — channel monetization policies / inauthentic content (https://support.google.com/youtube/answer/1311392)
3. Fundmates — "YouTube Monetization Rules 2025: Activity Requirements" (https://www.fundmates.com/blog/youtube-monetization-rules-2025-activity-requirements)
4. Onewrk — "YouTube's AI Disclosure Requirements: The Complete 2025 Guide" (https://onewrk.com/youtubes-ai-disclosure-requirements-the-complete-2025-guide/)
5. Subscribr — "YouTube AI Policy 2025: Will Your Faceless Channel Get Banned?" (https://subscribr.ai/p/youtube-ai-policy-faceless-channel-future)
6. Flocker — "YouTube Inauthentic Content Policy: AI Enforcement Wave 2026" (https://flocker.tv/posts/youtube-inauthentic-content-ai-enforcement/)
7. MilX — "AI slop on YouTube and how to protect your channel in 2026" (https://milx.app/en/news/why-youtube-just-suspended-thousands-of-ai-channels-and-how-to-protect-yours)
8. invideo.io — "YouTube's New Policy Just Killed Faceless AI Channels" (https://invideo.io/blog/youtube-kills-ai-faceless-channels/)
9. Piunikaweb — "Reports surge on YouTube's 'Inauthentic content' crackdown" (Jan 12 2026) (https://piunikaweb.com/2026/01/12/youtube-inauthentic-content-policy-enforcement-reports/)
10. Influencer Marketing Hub — YouTube Shorts RPM Benchmarks (https://influencermarketinghub.com/youtube-shorts-rpm/)
11. Digiday — "How YouTube Shorts revenue compares to long-form video revenue for creators" (https://digiday.com/media/how-youtube-shorts-revenue-compares-to-long-form-video-revenue-for-creators/)
12. youtubers.me — Simple History estimated earnings (https://us.youtubers.me/simple-history/youtube-estimated-earnings)
13. youtubers.me — Our History estimated earnings (https://us.youtubers.me/our-history/youtube-estimated-earnings)
14. youtubers.me — History Bypass estimated earnings (https://us.youtubers.me/history-bypass/youtube-estimated-earnings)
15. Outlierkit — "23 Profitable, Low Competition YouTube Channel Ideas and Niches in 2026" (https://outlierkit.com/blog/low-competition-youtube-channel-ideas)

### Headline change: faceless AI is no longer a safe automation target
YouTube executed the largest mass-termination wave in its history in **January 2026** against "faceless AI" channels. The pattern it enforced against was recognizable and is directly relevant to our build plan:
- **Synthetic voiceover with no tonal variation** (canned TTS read of a script)
- **Stock / reused footage with no original editing** (slideshow + Ken Burns + music)
- **Templated scripts recycled across uploads** (same intro/outro/structure every video)
- **High publication cadence** (multiple videos per day, "volume over substance")

The policy hook is the July 15, 2025 rename of "repetitious content" → **"inauthentic content,"** which broadened the definition from "copy-paste uploads" to "content lacking genuine human creativity." Enforcement at scale started six months later. Channels built purely on AI scripts + synthetic voice + templated slideshows are the first to fall and they are falling in the thousands.

The experiments/youtube-history-channel/ plan as currently designed matches **two of the four risk signals** (Edge TTS `en-US-GuyNeural` narration, Ken Burns on public-domain images with minimal editing) and is mitigated on the other two (obscure-history angle is researched per episode, cadence is 1–2/week not N/day). That is not a passing grade — it is a "might survive, probably gets flagged eventually" grade. The build needs an injection of human creative contribution before shipping episode 1 to avoid becoming a statistic.

### YPP threshold — slightly improved for the first dollar
YouTube lowered the early-monetization bar:
- **Early tier (fan-funding tools — Super Chat, Super Thanks, channel memberships, Shopping):** 500 subs + (3,000 public watch-hours in 12 mo **OR** 3M Shorts views in 90 days).
- **Full tier (ad revenue share):** 1,000 subs + (4,000 watch-hours in 12 mo **OR** 10M Shorts views in 90 days). Unchanged from the prior threshold.

This marginally helps TTF$ — the early tier could cross at a realistic 500 subs and 3k watch-hours, which for a niche history channel posting weekly 7–9 minute videos is **maybe 6–9 months** if the channel has any traction at all. For the monetization gate we care about (ad revenue share), the threshold is unchanged and still expensive in time.

### Shorts vs long-form — long-form decision validated, hard
- **YouTube Shorts average RPM:** ~$0.05 (3–7¢ range). Pooled revenue model — Shorts don't run individual ads; a shared pool is divided by view share.
- **YouTube long-form average RPM:** $3–$6 (range $1–$30 depending on niche). History/education sits around the $3–5 band.
- **Ratio:** long-form earns roughly **60–100× more per view than Shorts**.
- **Correct use of Shorts:** discovery funnel to drive subs to the long-form channel, not a revenue stream. A Short that gets 500k views might earn $25; a long-form history video that gets 50k views with a 5% mid-roll CTR might earn $150+.

Our strategy's decision to prioritize 7–9 minute long-form survives this refresh intact. If we ever add Shorts, they are strictly a top-of-funnel instrument.

### AI disclosure — does it apply to our plan?
YouTube's AI disclosure toggle (introduced 2024, enforced 2025) is required when realistic synthetic content depicts a real person saying/doing something they didn't, alters real footage, or depicts a realistic-looking scene that didn't occur. It is **NOT** required for:
- Animations, special effects, and clearly non-realistic visuals
- AI assistance with scripts, outlines, or thumbnails
- TTS narration (this is production assistance, not a "realistic synthetic person")
- Use of public-domain historical images

**Bottom line:** our plan (public-domain images + TTS narration + written script) does not trigger the AI disclosure requirement. We are in the "allowed AI use" lane, not the "must disclose" lane. However — and this is the catch — the *inauthentic content* policy is a **separate and stricter** gate than the disclosure requirement. A channel can be policy-compliant on AI disclosure and still get demonetized under the inauthentic content policy. The two policies enforce different things: disclosure is about honesty with viewers; inauthentic is about whether the channel is genuinely creator-driven.

### Activity requirements — must stay above the floor
New in 2025: after 30 days of inactivity a warning fires, after 60 days features like Super Chat and memberships are disabled, after 90 days monetization may be suspended and the channel requires reapplication to YPP. Our planned 1-per-week cadence sits well above the floor — but if the experiment stalls for a month, we risk kicking ourselves out of the program. Flag for the weekly review: if the channel goes silent, note it explicitly rather than "just let it sit."

### Niche-specific: history
From the earnings data we could actually verify on youtubers.me (take with a grain of salt — these are third-party estimates, not YouTube Studio truth):
- **Simple History:** ~$60,000/yr (well-established, produced animations, not a direct comp)
- **Our History:** ~$2,310/30 days (~$27k/yr; closer to the "obscure/storytelling" profile)
- **History Bypass:** ~$133k recent months on 819M total views, 796k subs (far-right-tail)

These confirm the **5/5 ceiling** rating. The median faceless history channel earns $0. The top end, when you're in the right niche with quality storytelling, is real money. Research-driven "obscure history" is still flagged by industry write-ups as one of the sub-niches facing *little* saturation — unlike "Top 10 WWII facts" which is a red ocean. Our "Margins of History" positioning is defensible.

### Rescoring
| Dimension | Old | New | Reason |
|---|---|---|---|
| Time-to-first-dollar | 1 | 1 | YPP early tier lowered to 500 subs is marginally better, but for a brand-new channel the months-long floor is unchanged. No category upgrade. |
| $0 viability | 5 | 5 | YouTube hosting, Edge TTS, public-domain images, CC music all still free. Unchanged. |
| Automation-friendliness | 2 | **1** | **This is the downgrade.** The Jan 2026 enforcement wave directly targets "TTS + slideshow + templated + automated" — the exact profile our build assumed was safe. To survive the inauthenticity filter, a human must be materially involved (real narration, creative editing commentary, or per-episode unique treatment). Automation can still help (script, source, render) but "post-and-forget" is dead. |
| Ceiling | 5 | 5 | Simple History ($60k/yr), Our History (~$27k/yr), History Bypass (huge) confirm the top-end is real. Unchanged. |
| **Total** | **13 / 20** | **12 / 20** | |

Small drop, but the important thing is the *reason* for the drop, not the number. The automation story has changed. Any future agent reading this file must NOT plan a YouTube experiment as if "TTS-narrated slideshow with public-domain images" is a safe automated ship path. It's not anymore.

### Recommendation for the loop (binding for B-012..B-017)
The current experiments/youtube-history-channel/ strategy needs these **non-optional** adjustments before episode 1 ships:

1. **Narration must not be pure Edge TTS alone.** Options in priority order:
   - **(A — best)** Robert records the narration himself from the agent-written script. This is the single largest mitigator against inauthentic-content flagging and is a one-time ~15 minute cost per episode for Robert. Write the inbox note accordingly when episode 1 is ready.
   - **(B — fallback)** Use Edge TTS but add explicit **per-episode creative differentiators**: a short human-recorded intro/outro by Robert (even 15 seconds), inline editor's-note commentary cut into the narration, and visible variation in the visual treatment from episode to episode. Ken Burns on 20 images with no commentary = maximum risk.
   - **(C — worst, do not do)** Ship Edge TTS narration + Ken Burns + no human voice at all. This is the January-2026-enforcement-wave profile. Do not do this.
2. **Visuals beyond Ken Burns.** Mix pan/zoom with at least two of: inline text overlays quoting primary sources, map animations, timeline graphics, or side-by-side comparisons. The goal is to look unlike a slideshow at a glance.
3. **Hard cap on cadence:** 1 episode/week maximum for the first 12 weeks, regardless of how fast the agent can produce. The enforcement wave specifically flagged volume as a risk signal. Quality + slow > volume, always.
4. **No AI-generated visuals of historical scenes.** Public domain only. Already in strategy.md but worth restating — AI-generated "medieval woodcut" images are both inauthenticity risk AND disclosure risk AND credibility risk for a research-driven channel.
5. **Do not auto-upload multiple episodes back-to-back.** Space publications at least 3 days apart minimum. Burst publishing is one of the profile signals the crawler uses.
6. **Weekly channel-health check:** the weekly review must read channel analytics and flag any inactivity warning or policy notice immediately.

These constraints partially invalidate the "hands-free automated shipping" assumption but preserve the channel as a real long-term bet. Robert's occasional 15-minute involvement is the honest price of staying on the right side of the inauthenticity filter.

### What this refresh did NOT change
- The niche (obscure/forgotten history) is still defensible — industry write-ups explicitly flag "historical explainer videos" as facing little saturation and research-heavy storytelling as the differentiator that still works in 2026.
- The revenue plan (crypto tips + Ko-fi + BMaC + Gumroad cross-sell on day 1, YPP aspirational) is unchanged — good, because it didn't depend on monetization thresholds being forgiving.
- The long-form 7–9 minute format is unchanged — the Shorts RPM data validates the decision to prioritize long-form for revenue.
- The public-domain sourcing plan is unchanged.
