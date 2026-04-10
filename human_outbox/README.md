# human_outbox/

This is where **you** (Robert) write updates for the agent. Drop any file here. The next scheduled run will read it, update state, and move it to `human_outbox/processed/`.

## What to put here
- "I created an itch.io account, my username is X, profile URL is Y."
- "I uploaded the prompt-cleaner tool, here's the link: ..."
- "Made $3 from a Gumroad sale today."
- "Tried the steps in inbox 0003 but step 2 didn't work because ..."
- "Pause everything for a week, I'm on vacation."

## Format
Anything readable. Plain text, markdown, screenshots — whatever. Be brief but specific. The agent will parse it.

## Hard rule
**Do not paste passwords, API keys, or tokens here.** This folder lives on disk in plain text. If you accidentally paste a secret, the agent will redact it and warn you in the inbox.
