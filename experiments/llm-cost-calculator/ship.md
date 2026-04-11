# llm-cost-calculator — ship checklist

## Default path (automated)
```
bash tools/deploy_pages.sh llm-cost-calculator experiments/llm-cost-calculator
```
This creates the public repo `BobbyEBaby/llm-cost-calculator` if it doesn't exist, copies `index.html`, pushes, enables GitHub Pages, and appends to `state/publish-log.md`. Idempotent — re-running just updates content.

Live URL after success: `https://bobbyebaby.github.io/llm-cost-calculator/`

## Optional follow-up: Reddit post
After Pages propagates (~60s) and you've manually verified the live URL works:

```bash
python tools/post_reddit.py LocalLLaMA "I made a free LLM API cost calculator — compare Claude, GPT, Gemini side-by-side with preset scenarios" "https://bobbyebaby.github.io/llm-cost-calculator/"
```

(`tools/post_reddit.py` exists, requires `REDDIT_*` env vars in `.env`, hard 24h rate-limit enforced against `state/publish-log.md`.)

If `r/LocalLLaMA` has community rules against link posts or self-promo, switch to `r/ClaudeAI` or `r/OpenAI` instead. Pick exactly one — no cross-posting same day per CLAUDE.md.

## After distribution
- Check the live URL one more time
- Update `experiments/llm-cost-calculator/README.md` metrics table with the live URL, repo URL, and Reddit post URL
- Add a runlog entry recording the ship
- Move B-008 to "Done" in `state/backlog.md`

## Hard rules (from CLAUDE.md, restated)
- **Never reply to Reddit comments**
- **Never DM anyone**
- **Never post to more than one subreddit in 24h**
- **Never engage with critical comments — record them in README, do not respond**
- **If a moderator removes the post, do not appeal, do not repost — log and move on**
