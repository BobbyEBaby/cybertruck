# prompt-cleaner

**Status:** built (not yet shipped — awaiting `GITHUB_TOKEN` in `.env`)
**Backlog item:** B-001
**Built:** 2026-04-10
**Type:** single-file browser tool, vanilla HTML/CSS/JS, no build step, no backend

## Hypothesis
There's a small but real audience of people writing AI prompts who would value a free, instant, no-signup tool to strip filler and markdown from prompts. The audience is the same crowd that follows AI tooling on Reddit (`r/PromptEngineering`, `r/LocalLLaMA`, `r/ChatGPT`, `r/ClaudeAI`) and Hacker News. Conversion to *paid* anything is unlikely; the goal is to:

1. Validate that the autonomous publish pipeline works (push to GitHub Pages, post on Reddit, measure traffic)
2. Get a "buy me a coffee" or USDC tip link in front of a niche audience
3. Learn what kinds of small AI tools get any traction at all

## What it does
A static page with two text areas (input + cleaned). Six toggleable cleaning operations:
- Strip markdown (headers, bold, italic, links, code fences, bullets)
- Normalize whitespace
- Collapse blank lines
- Remove filler phrases ("could you please", "I would like you to", "kindly", "just", etc.)
- Smart→straight quotes
- Trim line edges per line

Live char + rough token count for input and output, with a "% saved" stat. Copy-to-clipboard button. "Use cleaned as input" for chained passes. Works fully offline once loaded.

## How to test locally
Just open `index.html` in a browser. No build, no server, no dependencies.

## Why this experiment first
It scores 16/20 in `research/markets/01-browser-utilities.md`. It's the cheapest possible shot — no external account needed to even *exist* (it can be opened from the filesystem), and shipping it requires only `GITHUB_TOKEN` to deploy to Pages. Other experiments need exchange accounts, API tokens, or both, which are still pending in the setup.

## Metrics to track (filled in by future runs)
| Metric | Value | As of |
|---|---|---|
| Live URL | https://bobbyebaby.github.io/prompt-cleaner/ | 2026-04-11 |
| Source repo | https://github.com/BobbyEBaby/prompt-cleaner | 2026-04-11 |
| Reddit post URL | _(not posted yet)_ | |
| Reddit upvotes | — | |
| GitHub Pages visits (7d) | — | |
| Tips received (USDC) | $0 | |

## Decision points
- **7 days post-launch:** if zero engagement (no upvotes, no traffic), this counts as 1 of 3 toward the browser-tools circuit breaker.
- **30 days post-launch:** if zero tips, write a short post-mortem and decide whether to iterate (more cleaning options? niche-specific variant?) or pivot.

## Files
- `index.html` — the entire tool (one file, no dependencies)
- `README.md` — this file
- `ship.md` — manual-publish reference (the cron will use `tools/deploy_pages.sh` instead, but ship.md exists as a fallback if the automated path breaks)
