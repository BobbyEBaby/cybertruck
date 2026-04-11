# ship.md — claude-code-power-prompts → Gumroad

**Target:** Local-run Claude Code agent (has `.env` access). Remote agent built
the asset; this file is the handoff to ship it.

## Prerequisites (check before running)
- [ ] `GUMROAD_ACCESS_TOKEN` is set in `cybertruck/.env`
- [ ] Gumroad account exists and has a verified payout method
      (bank link OR PayPal OR Stripe — required for payouts, not for listing)
- [ ] `state/publish-log.md` shows no Gumroad publication in the last 24h
      (rate limit per CLAUDE.md)

If any prerequisite is missing, **stop** and write a `human_inbox/` note
asking Robert to finish the blocker. Do not invent a workaround.

## Step 1 — Convert the asset to PDF (optional but recommended)
Gumroad accepts `.md`, but buyers expect a PDF for a paid digital download.
If `pandoc` is installed locally, run:

```bash
cd experiments/claude-code-power-prompts
pandoc claude-code-power-prompts.md \
  -o claude-code-power-prompts.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V mainfont="DejaVu Serif" \
  -V monofont="DejaVu Sans Mono" \
  --toc \
  --metadata title="The Claude Code Power Prompts Pack" \
  --metadata author="Cybertruck Autopilot"
```

If `pandoc` or a LaTeX engine is not installed, fall back to uploading the
`.md` directly. **Do not install LaTeX just for this** — it's a multi-GB
dependency and not worth it for a first ship. Markdown upload is fine.

If `pandoc` succeeds but `xelatex` fails, retry without `--pdf-engine`
(lets pandoc pick whatever is available, e.g. `wkhtmltopdf`). If that also
fails, ship the `.md`.

## Step 2 — Zip the deliverable
Whether PDF or markdown, bundle it with the README snippet for buyers:

```bash
cd experiments/claude-code-power-prompts
mkdir -p dist
cp claude-code-power-prompts.md dist/
# If the PDF exists:
[ -f claude-code-power-prompts.pdf ] && cp claude-code-power-prompts.pdf dist/
cd dist
zip -r ../claude-code-power-prompts.zip .
cd ..
```

The zip is what Gumroad will serve to buyers.

## Step 3 — Create the Gumroad product via API
Gumroad's product-creation endpoint is `POST /v2/products`. The helper at
`tools/gumroad_publish.py` does not exist yet — the local-run agent should
create it on first use following this spec. Keep it tiny (under 100 lines).

**Endpoint reference (verify current at https://gumroad.com/api):**
- `POST https://api.gumroad.com/v2/products`
- Form fields: `access_token`, `name`, `price` (cents), `description`
- After creation: `POST /v2/products/:id/enable` or equivalent to publish
- File upload: `POST /v2/products/:id/variants` or the dashboard's file
  attachment endpoint (API docs for file upload are sparse — if the API
  path fails, fall back to uploading the file via the dashboard and
  setting everything else via API)

**Listing fields to set:**
- **Name:** `The Claude Code Power Prompts Pack`
- **Price:** `500` (cents = $5.00 USD)
- **Pay-what-you-want:** yes, minimum `300` (cents = $3.00)
- **Tags:** `claude`, `claude-code`, `ai`, `prompts`, `developer-tools`, `productivity`
- **Category:** `Software Development` (or closest)
- **Description:** use the listing copy in Step 4 below
- **URL slug:** `claude-code-power-prompts`

## Step 4 — Listing copy (paste into Gumroad description field)

```markdown
# The Claude Code Power Prompts Pack

**15 battle-tested prompts for getting real work out of Claude Code.**

Free prompt lists give you one-liners. This pack gives you briefing documents.
Each prompt is a standing order with constraints, non-goals, and failure-mode
guidance — the shape that actually produces good output, not just clever wording.

## What's inside
- Exploring an unfamiliar codebase before you touch it
- Finding where a feature is implemented (without hallucinations)
- Writing tests that test behavior, not implementation
- Refactoring safely with a plan-first gate
- Debugging with root-cause discipline, not symptom patches
- Adding a feature end-to-end without scope creep
- Reviewing your own diff like a skeptical senior reviewer
- Writing commit messages and PR descriptions that match the repo's style
- Explaining inherited code so you can actually maintain it
- Auditing dependencies
- Writing migration scripts (idempotent, reversible, dry-runnable)
- Writing a `CLAUDE.md` for a new project
- Designing a scheduled-agent prompt (for cron/hook workflows)
- Writing pre-commit hooks that don't get disabled
- Plus meta-rules that apply to every prompt above

## Format
Single markdown file (~3,500 words). PDF included if your purchase bundle
has one. Clean structure, no filler, no AI-generated fluff.

## Who this is for
Developers who already use Claude Code, already pay for the API, and are
tired of getting mediocre output from vague prompts.

## Not for
- People looking for one-liner clever prompts
- People who've never opened Claude Code
- Non-developers (these are developer workflows)

## License
You bought it, you use it. Adapt to your team, paste into your own
`CLAUDE.md`, share individual prompts with colleagues. Do not resell as-is.

---

Pay-what-you-want, $3 minimum, $5 suggested. If a single prompt saves you
an afternoon, we're even.

Built by the Cybertruck Autopilot project — an ongoing experiment in
autonomous Claude Code loops.
```

## Step 5 — Publish + record

Once the product is live:

1. **Record in publish-log:**
   ```
   echo "" >> state/publish-log.md
   echo "## $(date -u +%Y-%m-%dT%H:%MZ) — gumroad" >> state/publish-log.md
   echo "- product: claude-code-power-prompts" >> state/publish-log.md
   echo "- url: <PASTE GUMROAD URL>" >> state/publish-log.md
   echo "- price: \$5 PWYW (\$3 min)" >> state/publish-log.md
   ```

2. **Update `experiments/claude-code-power-prompts/README.md`**
   Metrics table — add row with the live URL and the ship date.

3. **Update `state/backlog.md`**
   Mark B-002 as `[done YYYY-MM-DD]` and move to the Done section.

4. **Append runlog entry** per CLAUDE.md format.

## Step 6 — Do NOT post promo yet

Promo posting (Reddit, X) is a **separate** decision and requires:
- `REDDIT_*` credentials (for Reddit via PRAW)
- An approved subreddit (default candidate: `r/ClaudeAI`, verify subreddit
  rules allow self-promotion or use the designated thread — **do not
  blind-post**; many AI subreddits ban self-promo on sight)
- Rate-limit check against `state/publish-log.md`
- A separate ship entry in a future daily run, not this one

If `REDDIT_*` credentials exist and a target subreddit is confirmed OK for
self-promo, the next daily run can handle that as a separate task.

## Safety
- **No fake reviews.** Do not create alt accounts to review your own product.
- **No astroturfing.** Do not post from multiple handles.
- **No DMs.** Do not message anyone about the product.
- **No spending.** This whole ship is $0 — if any step asks for money, stop.
- **One ship per platform per 24h.** Check `state/publish-log.md`.

These are restated from `CLAUDE.md` for emphasis because Gumroad is the
first paid product and the temptation to juice it will be highest here.
