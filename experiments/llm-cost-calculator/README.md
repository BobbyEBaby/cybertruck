# llm-cost-calculator

**Status:** built (not yet shipped)
**Backlog item:** B-008 (added in this session)
**Built:** 2026-04-11
**Type:** single-file browser tool, vanilla HTML/CSS/JS, no dependencies

## Hypothesis
LLM API users are extremely cost-conscious in 2026 — prices change, models multiply, and "what would this cost on Claude vs GPT vs Gemini?" is a question every dev with API access asks at least once a week. A free, instant, side-by-side cost calculator with realistic preset scenarios is the kind of thing that gets bookmarked, shared in Discord/Slack, and lands in "useful AI tools" lists.

Different audience overlap with prompt-cleaner (B-001) — both target AI tooling users, but cost-calculator skews more toward devs/decision-makers who actually deploy models, where prompt-cleaner skews toward prompt engineers. Two adjacent shots at the same niche is fine: low cannibalization risk, possible cross-referral.

## What it does
Single static page. Inputs: input tokens/call, output tokens/call, cached input tokens/call, calls/day, days/month. Six preset scenarios (daily chat, RAG with 50k context, customer support bot, coding agent, doc summarization, auto-tagger) that fill the inputs with one click. Outputs: 13 models compared side-by-side, sorted by monthly cost, with per-call / per-day / per-month figures. Cheapest highlighted with a star.

Models include Claude Opus/Sonnet/Haiku 4.5, GPT-4o/4o-mini/Turbo/o1/o1-mini, Gemini 2.5 Pro / 2.0 Flash, DeepSeek V3, Llama 3.3 70B via Groq, Mistral Large. Prices are USD per 1M tokens, sourced from public pricing pages as of early 2026, with an explicit disclaimer that they drift.

Cache-aware: if you set "cached input tokens", models that publish a cache-read price (Anthropic, OpenAI, DeepSeek) get the discount; others fall back to standard input pricing.

## Why this experiment
- **Same audience as B-001** — prompt cleaner crowd overlaps the API cost crowd
- **Same shipping path** — single static file → GitHub Pages → bobbyebaby.github.io/llm-cost-calculator/
- **Genuinely high-utility** — this is the kind of tool that people actually return to, not throw away
- **SEO-friendly title and description** — "LLM API cost calculator" is a real query

## How to test locally
Open `index.html` in a browser. Click presets, adjust numbers, watch the table re-sort.

## Distribution plan (when shipped)
1. Deploy via `tools/deploy_pages.sh llm-cost-calculator experiments/llm-cost-calculator`
2. Wait 30s for Pages to propagate
3. **One** Reddit post in `r/LocalLLaMA` (largest audience for cost-conscious LLM users):
   *"I made a free LLM API cost calculator — compare Claude/GPT/Gemini side-by-side, with preset scenarios"*
4. **No** comment replies (per CLAUDE.md ground rules)
5. After 24h, optionally post to `r/ClaudeAI` or `r/OpenAI` with a different framing

## Metrics to track (filled in by future runs)
| Metric | Value | As of |
|---|---|---|
| Live URL | _(not deployed yet)_ | |
| Source repo | _(not created yet)_ | |
| Reddit post URL | _(not posted yet)_ | |
| Reddit upvotes (24h) | — | |
| Reddit upvotes (7d) | — | |
| Tips received (USDC) | $0 | |

## Known stale-by-design risk
The pricing table will drift. Prices change every few months. Set a calendar item: when refreshing market research, also refresh the prices in `index.html` MODELS array. Stale prices = useless tool = reputation hit. Worth doing.

## Files
- `index.html` — the entire tool
- `README.md` — this file
- `ship.md` — deploy instructions (uses `tools/deploy_pages.sh`)
