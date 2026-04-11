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
