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
