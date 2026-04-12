# 0008 — Rate-limit rule clarification: do unlisted uploads count?

**Priority: low, but decide before the next YouTube upload.** This is a governance / rule-interpretation question, not a ship task. Two minutes of your time. No code changes required from you — if you agree with the recommendation below, the next remote run will patch `CLAUDE.md` itself.

## The ambiguity

`CLAUDE.md` "Max-autonomy rules" section says:

> **Max 1 publication per platform per 24 hours.** Track in `state/publish-log.md`.

The rule is clean for **public** publications. It is ambiguous for **unlisted** uploads — which is the privacy mode we have been using on YouTube for every episode so far.

Two rows in `state/publish-log.md` trigger the ambiguity:

| UTC time | platform | privacy | note |
|---|---|---|---|
| 2026-04-11 ~15:39 | youtube | unlisted | Ep1 v2 ("Popular Uprisings Ep 1 v2", id `sBUTZhrbMPU`) |
| 2026-04-12 00:11 | youtube | unlisted | Ep3 Harpers Ferry 1859 (id `tI2OfCTkWp4`) |

The gap is ~8½ hours, well under 24. **If the rule counts unlisted uploads, ep3 was a minor violation. If it does not, nothing was violated.** This was flagged in the 00:11 runlog entry by the local run that did the ep3 ship; nobody has ruled on it yet.

Note that earlier in 2026-04-11 there were also ep1 v1 / v2 / v4 uploads clustered together, all unlisted. None of those were flagged at the time — de facto precedent suggests unlisted ≠ publication, but precedent isn't a rule.

## Why the rule exists (re-reading the intent)

The header of the section is **"Hard rate and behavior limits (so we don't get banned or embarrass anyone)"**. The stated purpose is twofold:

1. **Not getting banned.** Platforms flag accounts that upload/post too frequently as potential spam. The thing platforms actually *measure* is upload velocity (or post velocity for Reddit/HN) — they don't distinguish public from unlisted when computing that velocity. YouTube's "upload rate limit" and trust-signal logic treats unlisted and public the same way inside its spam/abuse systems. The anti-ban purpose therefore **applies to unlisted uploads** too.
2. **Not embarrassing anyone.** This is about public-facing cadence — a reader seeing three videos from the same channel in one day thinks "this channel is LLM-farmed." That reasoning **does not apply to unlisted uploads**, which have no public cadence.

The two purposes pull in opposite directions when the upload is unlisted. The existing rule text doesn't resolve the tension.

## The recommendation

**Adopt this clarification as an amendment to `CLAUDE.md` "Max-autonomy rules" > "Hard rate and behavior limits":**

> - **Max 1 publication per platform per 24 hours.** Track in `state/publish-log.md`.
>   - "Publication" here means **any upload to a third-party platform**, regardless of privacy setting. Unlisted YouTube uploads and private/draft Gumroad products **count** — because the anti-ban purpose of this rule is about upload velocity, which platforms measure regardless of privacy. An unlisted→public transition **does not** count as a new publication (no new upload occurred).
>   - If the agent needs to re-upload the same episode (e.g. a v2 render replacing a v1), wait 24 hours from the prior upload OR take down the prior version first via `youtube_upload.py --delete <id>`. Never leave multiple versions of the same content on a platform at once.

**Why this specific wording:**
- It takes the **conservative** interpretation (unlisted counts), which keeps us safely inside platform spam thresholds. The downside is slower iteration on YouTube re-renders; the upside is we don't burn the channel before it earns its first view.
- It **explicitly exempts** the unlisted→public flip, which is the ep3 path Robert is about to make a decision on — no upload happens on that flip, just a visibility change, so no rate-limit budget is consumed.
- It **adds a re-upload rule** that prevents the ep1 v1/v2/v4 mess from recurring. Keeping multiple versions of the same content live is the most embarrassing failure mode of the "shipping fast" instinct.
- It **does not** try to carve out separate budgets for public vs unlisted (e.g. "1 public + 1 unlisted per day"). That complexity has no upside — we are trying to stay under a velocity threshold we cannot even see, and carving out buckets increases the total velocity for no benefit.

## What you need to do

Drop a file at `human_outbox/0008-reply.md` with one of:

```
ruling: accept
notes: <anything>
```

```
ruling: modify
replacement: <your preferred wording, I'll use it verbatim>
notes: <anything>
```

```
ruling: reject
rationale: <why, so I understand the constraint you're protecting>
```

The next remote run will:
1. Read your ruling from `human_outbox/`
2. If `accept` → patch `CLAUDE.md` with the exact wording above
3. If `modify` → patch `CLAUDE.md` with your replacement
4. If `reject` → leave `CLAUDE.md` alone and record your rationale in `state/runlog.md` so future runs stop revisiting this question
5. Archive the outbox file to `human_outbox/processed/YYYY-MM-DD-0008-reply.md`

## One more thing (retroactive ep3 adjudication)

Whatever you decide, please also answer retroactively:

- **Does ep3's 00:11 upload need to come down** (because it was <24 hours after ep1 v2) or **stay as-is**? My honest recommendation is **stay** — taking it down would destroy a successful pipeline-shipping signal for no platform-safety gain (YouTube didn't flag it, nobody has seen it because it's unlisted), and the ambiguity that allowed it was a rule-writing failure of ours, not a ship-discipline failure. But this is your call. Add `ep3_ruling: stay | takedown` to your `0008-reply.md` if you want to be explicit; otherwise I'll default to `stay`.

## Why this is on your desk at all

Because `CLAUDE.md` is the contract between you and the loop. The loop should not silently redefine its own hard rules — especially rules in the "Max-autonomy" section, which exist precisely to constrain the loop's autonomy. So even a clarification that looks obvious to the agent needs a human ruling. That's the whole point of this file.

---

**Written by:** remote run #19, 2026-04-12, per `scripts/daily-remote.md` Step 8 (new human ask) and adjudicating open item (b) from the 00:11 local-run runlog entry.
