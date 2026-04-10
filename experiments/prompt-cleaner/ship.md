# prompt-cleaner — ship checklist

This file is a fallback for when the automated `tools/deploy_pages.sh` path is broken or unavailable. The default path is the automated one — see `tools/deploy_pages.sh`.

## Automated path (default)
```
bash tools/deploy_pages.sh prompt-cleaner experiments/prompt-cleaner
```
This script:
1. Reads `GITHUB_TOKEN` from `.env`
2. Creates a new public repo `BobbyEBaby/prompt-cleaner` if it doesn't exist
3. Copies `experiments/prompt-cleaner/index.html` to the repo's root
4. Pushes
5. Enables GitHub Pages on the `main` branch
6. Returns the live URL
7. Appends an entry to `state/publish-log.md`

## Manual path (only if automated path fails)
1. Create a new public repo on GitHub: **prompt-cleaner**
2. From `experiments/prompt-cleaner/`, run:
   ```
   git init -b main
   git add index.html
   git commit -m "initial: AI Prompt Cleaner"
   git remote add origin https://github.com/BobbyEBaby/prompt-cleaner.git
   git push -u origin main
   ```
3. Repo Settings → Pages → Source: Deploy from branch → main → / (root) → Save
4. Wait ~30s. Live URL will be `https://bobbyebaby.github.io/prompt-cleaner/`
5. Open it. Confirm it loads, paste sample text, hit Clean, verify it works.

## Distribution (one-time, organic, rate-limited)
After the URL is live:
1. **One** Reddit post in `r/PromptEngineering` (largest fit). Title:
   *"I made a free in-browser AI prompt cleaner — strips filler and markdown, no signup, no upload"*
   Body: 2–3 sentences, link to the tool, mention it's open source. **Do not reply to comments.** Log the post URL in `README.md` metrics table.
2. **No** cross-posting to multiple subreddits in the same day (anti-spam rule).
3. The next day's run *may* post to one *different* subreddit (`r/ClaudeAI` or `r/LocalLLaMA`) — but only one per 24h.

## Hard rules (from CLAUDE.md, restated here for reference)
- Max 1 publication per platform per 24 hours
- Never reply to comments or DMs
- Never post in more than one subreddit in the same day
- If a moderator removes the post, **do not repost**, do not appeal — record it in the runlog and move on
