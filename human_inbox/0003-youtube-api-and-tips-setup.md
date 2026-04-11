# 0003 — YouTube API token + tip rail accounts (no rush)

**Time estimate:** 25–35 minutes total. Break into parts, do when convenient. **Nothing is blocking any current work** — the agent can keep building infrastructure without any of this. This unblocks *automated* video uploads and the tip links in video descriptions.

## Why
The YouTube history channel (`experiments/youtube-history-channel/`) is being designed and scripted right now by the autopilot. The agent can write scripts, source images, generate narration, and render MP4s — all without touching your accounts. The two things it can't do:
1. **Upload the MP4 to YouTube** without a YouTube Data API OAuth refresh token
2. **Link to real Ko-fi / Buy Me a Coffee pages** in video descriptions if those accounts don't exist yet

All of this is optional: if you never do it, the workflow still works — you'd drag-drop MP4s into YouTube Studio manually (~2 min per video) and the descriptions would just skip the Ko-fi / BMC links.

## Parts

### Part A — Ko-fi account (5 min, do whenever)
1. Go to https://ko-fi.com/
2. Sign up as `bobbyebaby` (or whatever handle is available — tell me what you picked)
3. Complete basic profile: profile picture, one-line bio
4. Connect a payout method (Stripe or PayPal)
5. Drop a reply in `human_outbox/0003-reply.md` with: `kofi_url: https://ko-fi.com/<your-handle>`

Ko-fi takes **0% on direct tips** — strictly better than Buy Me a Coffee for tip revenue. Preferred rail.

### Part B — Buy Me a Coffee account (5 min, do whenever)
1. Go to https://buymeacoffee.com/
2. Sign up as `bobbyebaby` (or whatever is available)
3. Complete basic profile
4. Connect a payout method
5. Reply with: `bmc_url: https://buymeacoffee.com/<your-handle>`

BMC takes 5% but has a larger audience than Ko-fi. Worth having both.

### Part C — YouTube Data API v3 OAuth token (15–20 min, do whenever, can be last)
This is the trickier one. Skip it entirely if you'd rather do manual uploads forever.

1. Go to https://console.cloud.google.com/
2. Create a new project called `cybertruck-autopilot` (or pick any name)
3. Enable the **YouTube Data API v3**: APIs & Services → Library → search "YouTube Data API v3" → Enable
4. Create OAuth 2.0 credentials:
   - APIs & Services → Credentials → Create Credentials → OAuth Client ID
   - Application type: **Desktop app**
   - Name: `cybertruck-youtube-upload`
   - Click Create
5. Download the `client_secret.json` file
6. Save it to `cybertruck/secrets/youtube_client_secret.json` (the `secrets/` folder is `.gitignore`d)
7. Run the one-time OAuth consent flow to get a refresh token:
   ```bash
   # In a Claude Code session locally, ask me to write tools/youtube_oauth_bootstrap.py
   # and run it once. It opens a browser window, you click "Allow" on your channel,
   # it writes the refresh token to .env as YOUTUBE_OAUTH_REFRESH_TOKEN.
   ```
8. Reply with: `youtube_oauth: done` — the token never leaves your machine, never gets pasted anywhere, you don't need to send me its value.

### Part D — (Optional) rebrand the existing channel (5 min)
Your existing channel is at `UCv8vMc6ZN9Tkc0K5gx53iAA`. If you want it branded as "Margins of History" (my niche suggestion — see `experiments/youtube-history-channel/strategy.md`):
1. YouTube Studio → Customization → Basic Info
2. Change channel name to "Margins of History"
3. Grab a public-domain banner image from Library of Congress (e.g. an illuminated manuscript)
4. Write a one-paragraph About
5. Save

Or keep the existing branding — totally optional. The brand name is a suggestion, not a requirement.

## How to report back
Drop one file at `human_outbox/0003-reply.md` with whichever parts you've completed:
```
kofi_url: <url or "not yet">
bmc_url: <url or "not yet">
youtube_oauth: <done or "not yet" or "never doing">
channel_rebranded: <yes or "no, keeping existing name" or "not yet">
```

Partial replies are fine — I'll process whatever you send and keep waiting on the rest.

## Hard rules
- **Never paste your OAuth refresh token anywhere.** The bootstrap script writes it directly to `.env` — you don't need to see it or send it.
- **Never paste Ko-fi or BMC passwords.** Only the public URL.
- **Never spend money.** Ko-fi, BMC, Google Cloud Console for YouTube API are all free tiers. If anything asks for a credit card, stop and tell me.
