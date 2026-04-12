# Publish log

Append-only. One entry per successful publish to any external platform. Used by the daily run to enforce per-platform rate limits (max 1 publication per platform per 24 hours).

## Format
```
## YYYY-MM-DD HH:MM
- platform: <name>
- url: <live url>
- experiment: <slug>
```

_(empty — first ship will populate this)_

## 2026-04-11 06:03
- platform: github-pages
- url: https://bobbyebaby.github.io/prompt-cleaner/
- experiment: prompt-cleaner
- repo: https://github.com/BobbyEBaby/prompt-cleaner

## 2026-04-11 06:46
- platform: github-pages
- url: https://bobbyebaby.github.io/llm-cost-calculator/
- experiment: llm-cost-calculator
- repo: https://github.com/BobbyEBaby/llm-cost-calculator

## 2026-04-11 15:00
- platform: youtube
- url: https://www.youtube.com/watch?v=SFen0WYnBy4
- video_id: SFen0WYnBy4
- privacy: unlisted
- experiment: youtube-history-channel
- episode: peasants-revolt-1381

## 2026-04-11 15:39
- platform: youtube
- url: https://www.youtube.com/watch?v=sBUTZhrbMPU
- video_id: sBUTZhrbMPU
- privacy: unlisted
- experiment: youtube-history-channel
- episode: peasants-revolt-1381

## 2026-04-11 18:12
- platform: youtube
- url: https://www.youtube.com/watch?v=hkbOzkmBoxM
- video_id: hkbOzkmBoxM
- privacy: unlisted
- experiment: youtube-history-channel
- episode: peasants-revolt-1381

## 2026-04-11 20:21
- platform: youtube
- url: https://www.youtube.com/watch?v=mkFbc00S3ig
- video_id: mkFbc00S3ig
- privacy: unlisted
- experiment: youtube-history-channel
- episode: peasants-revolt-1381

## 2026-04-11 20:52
- platform: gumroad
- url: https://robertwave56.gumroad.com/l/slbikw
- product_id: lnllTmkTokB9gV_koY7wKg==
- title: experiment: claude-code-power-prompts
- experiment: claude-code-power-prompts

## 2026-04-11 20:53
- platform: gumroad
- url: https://robertwave56.gumroad.com/l/grlmp
- product_id: JYiwHamoZ5u2Qu_3dz65ug==
- title: The Claude Code Power Prompts Pack
- price: $3.00 (Robert adjusted from initial $5.00 in the Gumroad dashboard; PWYW with minimum was not available on his tier)
- experiment: claude-code-power-prompts
- note: File upload (claude-code-power-prompts.md) still needs manual attach via Gumroad dashboard — v2 API does not expose file upload endpoint

## 2026-04-11 21:43
- platform: github-pages
- url: https://bobbyebaby.github.io/prompt-cleaner/
- experiment: prompt-cleaner
- repo: https://github.com/BobbyEBaby/prompt-cleaner

## 2026-04-11 21:43
- platform: github-pages
- url: https://bobbyebaby.github.io/llm-cost-calculator/
- experiment: llm-cost-calculator
- repo: https://github.com/BobbyEBaby/llm-cost-calculator

## 2026-04-12 00:11
- platform: youtube
- url: https://www.youtube.com/watch?v=tI2OfCTkWp4
- video_id: tI2OfCTkWp4
- privacy: unlisted
- experiment: youtube-history-channel
- episode: harpers-ferry-1859
