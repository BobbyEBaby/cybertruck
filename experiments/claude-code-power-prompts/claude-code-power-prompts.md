# The Claude Code Power Prompts Pack

**15 battle-tested prompts for getting real work out of Claude Code.**

Version 1.0 · Published 2026-04-11

---

## Who this is for

You already have Claude Code installed. You've typed "help me fix this bug" a few times and gotten mixed results. You're ready to stop treating it like a chatbot and start treating it like a junior engineer that needs briefing documents.

This pack is 15 prompts that handle the high-leverage workflows: exploring an unfamiliar codebase, writing tests that actually test something, reviewing your own diff before a PR, refactoring without breaking the build, and a few meta-workflows for operating Claude Code itself (like writing a `CLAUDE.md`, a scheduled-agent prompt, or a hook).

Each prompt comes with:
- **When to use it** — the exact situation this prompt is for
- **The prompt** — copy-paste verbatim, substitute the `<BRACKETS>`
- **What you should expect** — so you can tell a good output from a bad one
- **Common failure modes** — and how to nudge the model out of them

These are not clever one-liners. They are briefing documents. The shape matters more than the wording. Steal the shape and adapt the wording to your codebase.

---

## Prompt 1 — "Explore this codebase before you touch it"

**When to use:** First session in an unfamiliar repo. Before asking for *any* change.

**The prompt:**
```
I've just opened this repo and you haven't seen it before.
Before making any changes, give me a map:

1. What is this project? (one sentence, based on README + package manifest + top-level dirs)
2. What language(s) and frameworks?
3. What's the entry point? (how do you run it / start dev?)
4. Where does the business logic live vs framework glue?
5. What tests exist and how are they run?
6. What's the build/deploy path?

Use Glob/Grep/Read only. Do not run code. Do not edit anything.
Report in under 300 words. Cite file paths you actually opened.
```

**Expect:** A tight orientation doc you can paste into your own notes. File paths should be real (verify one or two with `ls`). If it invents paths, the model is hallucinating — start over with a smaller repo scope.

**Failure modes:**
- *Model runs the code or edits things* → add "READ-ONLY EXPLORATION. Do not run, install, or edit." explicitly.
- *Model writes 2000 words* → the 300-word cap is the whole point. Repeat it.

---

## Prompt 2 — "Find where X is implemented"

**When to use:** You know a feature exists ("user login", "pagination", "rate limiting") but not where.

**The prompt:**
```
Find where <FEATURE NAME IN YOUR WORDS> is implemented in this codebase.

Output:
- Primary file(s) — path and line range
- What data structures / functions are the core of it
- What calls into it from where (1-2 call sites)
- What this feature depends on (libraries, other modules)

Do not propose changes. Just report. Under 200 words.
If you can't find it, say so and list the search terms you tried.
```

**Expect:** File paths with line numbers, a 1-sentence description of the core function, and 1–2 call sites. The "if you can't find it, say so" clause is critical — without it the model will invent a file rather than admit defeat.

---

## Prompt 3 — "Write me tests for this function"

**When to use:** You have a pure-ish function and want real coverage, not test-shaped placeholders.

**The prompt:**
```
Write tests for <FILE:FUNCTION>.

Constraints:
- Use the existing test framework in this repo (find it yourself — don't introduce a new one)
- Match the style of existing tests in tests/ or __tests__/ or spec/
- Cover: happy path, one edge case per input parameter, one error case
- Do NOT test implementation details. Test behavior.
- If the function has side effects (network, filesystem, time), use whatever mocking pattern the existing tests use

Before writing, read 2–3 existing test files and tell me what pattern you're following.
Then write the tests. Then run them.
```

**Expect:** A summary of the existing test style, then tests that actually match that style. If the repo uses `describe`/`it` and the model writes `test()`, stop and re-prompt — it didn't read the files.

**Failure mode:** Tests that just assert the function returns what the function returned (tautology tests). Re-prompt: "these tests are tautological — they don't verify behavior, they verify the current implementation. Rewrite with behavior-level assertions."

---

## Prompt 4 — "Refactor X without breaking anything"

**When to use:** A function or module has grown ugly and you want it cleaned up safely.

**The prompt:**
```
Refactor <FILE:FUNCTION> for readability.

Safety requirements (non-negotiable):
1. Do NOT change the public signature
2. Do NOT change behavior — every existing test must still pass
3. Make ONE structural improvement per edit (extract function, rename variable, etc.)
   — not a rewrite
4. After each edit, run the relevant tests. If any fail, revert that edit.

Don't touch anything outside <FILE>. If the refactor needs changes in other
files, stop and tell me first.

Start by listing the 3 improvements you'd make, ordered by payoff. Wait for
my approval before editing.
```

**Expect:** A ranked list of 3 concrete changes. You approve or reject each. This is the "make it ask first" pattern, and it saves hours of re-reading giant auto-refactored diffs.

---

## Prompt 5 — "Find the bug causing X"

**When to use:** You have a reproducible bug and a failing test (or a clear reproduction).

**The prompt:**
```
Bug report:
- Symptom: <WHAT THE USER SEES>
- Reproduction: <EXACT STEPS OR FAILING TEST>
- Expected: <WHAT SHOULD HAPPEN>
- Relevant files (but don't limit yourself to these): <PATHS>

Your job:
1. First, reproduce the bug yourself. Do not guess. Do not propose fixes yet.
2. Once reproduced, trace the code path that leads to the symptom.
3. Identify the root cause (not the symptom).
4. Propose the smallest possible fix that addresses the root cause.
5. Write a regression test that would have caught this.

Do not edit any file until step 4. Report after each step.
```

**Expect:** Reproduction confirmation → code trace → root cause → fix → test. If the model skips straight to "I think the issue is X, here's a fix", it guessed. Make it start over.

**Failure mode:** Fixes the symptom, not the cause. ("The function returns null, so I'll add a null check.") Push back: "does that address the root cause or just the symptom? Why is it null in the first place?"

---

## Prompt 6 — "Add a feature end-to-end"

**When to use:** Small, well-scoped feature in a codebase you mostly understand.

**The prompt:**
```
Feature: <ONE-SENTENCE DESCRIPTION>

User-facing behavior:
- <BULLETS — what the user sees / does>

Non-goals (explicit):
- <WHAT THIS FEATURE DOES NOT DO — prevents scope creep>

Before writing any code, produce a plan:
1. Which files will you touch and why
2. What's the data flow
3. What tests will you add
4. What migrations / config changes (if any)

Wait for my approval on the plan. Then implement in this order:
data layer → business logic → UI → tests → docs.

After each layer, report what changed and stop for my review.
```

**Expect:** A 4-step plan. Non-goals are the secret — without them the model will "helpfully" refactor unrelated code.

---

## Prompt 7 — "Review my diff like a skeptical reviewer"

**When to use:** Before opening a PR, to catch things you already missed.

**The prompt:**
```
Review the diff between this branch and <BASE BRANCH> (or the staged changes).

Act as a skeptical senior reviewer who:
- Has read the whole codebase
- Is grumpy about unjustified complexity
- Will flag: dead code, inconsistent style, missing error handling at boundaries,
  tests that don't test behavior, and scope creep beyond what the PR claims
- Will NOT flag: style preferences, defensive code that's actually needed,
  minor naming preferences

Produce a numbered list of issues, ranked by severity (critical / important / nitpick).
For each: file:line, what's wrong, what to do about it.

If the diff is actually fine, say so. Do not invent issues.
```

**Expect:** A prioritized list. The "do not invent issues" clause is critical because models love to find things to comment on.

---

## Prompt 8 — "Write the commit message"

**When to use:** After finishing work, before committing.

**The prompt:**
```
Look at the staged changes. Write a commit message in this repo's style
(check the last 10 commits first to see the format).

Rules:
- Subject line under 72 chars, imperative mood ("add" not "added")
- Body explains *why*, not *what* (the diff shows what)
- If multiple logical changes are staged, warn me — we should split the commit
- No emojis unless the existing commits use them
- No "Co-authored-by" unless asked

Just output the message. I'll commit it.
```

**Expect:** A message in the existing repo style. The "warn me if multiple logical changes" clause turns the model into a mini pre-commit hook.

---

## Prompt 9 — "Write the PR description"

**When to use:** After committing, before opening the PR.

**The prompt:**
```
Read the diff between this branch and <BASE>. Write a PR description.

Structure:
## What
(1–3 bullets, factual, what changed)

## Why
(1 paragraph, why this change is needed, what problem it solves)

## How to test
(specific steps a reviewer can follow)

## Risk
(what could break, what's the blast radius, what's NOT covered by tests)

## Screenshots / logs
(list what should go here — I'll add them manually)

Keep it under 300 words. Do not pad. If there's nothing to say in a section,
write "N/A" not filler.
```

**Expect:** Filled-in structure with real content. The "N/A not filler" clause prevents the model from generating "This change improves code quality and developer experience"–style noise.

---

## Prompt 10 — "Explain this to me like I'll need to maintain it"

**When to use:** Inherited code you'll own going forward.

**The prompt:**
```
Explain <FILE or FUNCTION> to me like I'll be on-call for it in a week.

Cover:
1. What does it do? (one sentence)
2. Why does it exist? (what problem does it solve that the obvious solution doesn't)
3. What are the invariants? (things the code assumes are always true)
4. What are the known rough edges? (hacky bits, TODOs, historical scars)
5. What would break it? (inputs/states that would cause a bug)
6. What's the blast radius if it fails?

Be concrete. Cite line numbers. Under 400 words.
If you don't know the answer to one of these, say "unknown" — don't guess.
```

**Expect:** Real answers grounded in the code. Section 3 (invariants) is where you find the landmines.

---

## Prompt 11 — "Audit dependencies"

**When to use:** Before a release, or when the `package-lock.json` feels out of control.

**The prompt:**
```
Audit this repo's direct dependencies.

For each direct dependency (not transitive), tell me:
- What it's used for (grep for imports)
- Is it actually still used, or is it dead weight?
- Last release date (check package.json or registry)
- Any open CVEs (check advisory DB if available)
- Size impact (rough bundle size contribution, if a frontend dep)

Output as a table. Flag anything suspicious at the top.
Do not remove anything — just report.
```

**Expect:** Table with real "used for" grep evidence. The "do not remove" clause keeps this as a read-only audit.

---

## Prompt 12 — "Write a migration script for X"

**When to use:** Schema change, data migration, or batch update.

**The prompt:**
```
I need a migration script that does: <DESCRIPTION>.

Constraints:
- Idempotent (safe to run twice)
- Safe to run on production data (no DROP without backup step)
- Reversible (write the down-migration too)
- Includes a dry-run mode that shows what would change without changing it
- Logs every row it touches

Before writing:
1. Find where existing migrations live
2. Match their framework / style
3. Tell me what you plan to do
4. Wait for approval

Do NOT execute the migration. Just write the file.
```

**Expect:** A file that matches the existing migration framework, with a dry-run mode. The "wait for approval" gate is non-optional — migrations that run before review are how data gets lost.

---

## Prompt 13 — "Write a CLAUDE.md for this project"

**When to use:** First setup of Claude Code in a new repo.

**The prompt:**
```
Generate a CLAUDE.md for this repo. The goal: any future Claude Code session
should read it once and know how to work in this codebase without re-exploring.

Include:
## Project
(one sentence: what this is)

## Stack
(languages, frameworks, key libraries)

## Run / Build / Test
(exact commands — find them in package.json / Makefile / Justfile / README)

## Layout
(top-level dirs and what lives in each — one line each, max 10 lines)

## Conventions
(style rules, naming conventions, testing conventions — read a few files to infer)

## Don'ts
(things that would be wrong in this codebase — e.g. "don't add a new dependency
without checking with me", "don't use default exports", "don't skip tests")

## Current focus
(leave blank — user will fill in)

Keep the whole file under 80 lines. Terse is good. No filler.
Read the repo first. Do not make anything up.
```

**Expect:** An 80-line file grounded in what's actually in the repo. Commit it and every future session gets smarter for free.

---

## Prompt 14 — "Design a scheduled agent prompt"

**When to use:** You want Claude Code to run on a cron (via `/schedule` or a hook).

**The prompt:**
```
I want a Claude Code agent that runs on a schedule and does: <GOAL>.

Write me the prompt file (e.g. scripts/daily.md) that the scheduled run will
read. Structure it like a standing-order briefing for someone who has no
memory of prior runs:

1. Hard environmental facts (what IS and ISN'T available this run)
2. Step 1: Load context (which files to read, in what order)
3. Step 2: Reconcile any inbox/outbox of user messages
4. Step 3: Pause switch (if a file called PAUSE exists, stop)
5. Step 4: Pick the next task (from a ranked backlog, skip blocked items)
6. Step 5: Execute the task with clear constraints
7. Step 6: Commit/push any changes
8. Step 7: Append a runlog entry
9. Step 8: Write any new human asks
10. Step 9: Stop (do not loop)

Hard rules to restate at the bottom: no spending, no credentials in files,
no publishing requiring creds unavailable in this environment, honest runlog.

Make it self-contained. A fresh session should be able to execute it with
no other context.
```

**Expect:** A file you can drop in `scripts/` and reference from a scheduled trigger. The "standing-order briefing" framing is the whole trick — scheduled runs have no conversational context, so the prompt itself has to carry everything.

---

## Prompt 15 — "Write a pre-commit hook that prevents X"

**When to use:** You keep making the same mistake and want the machine to catch it.

**The prompt:**
```
Write a pre-commit hook that blocks a commit if: <CONDITION>.

Requirements:
- Use whatever hook framework this repo already uses (pre-commit, husky, lefthook, plain .git/hooks/)
- Fast (<1s on a normal commit — no full test runs)
- Clear error message that tells the developer exactly what's wrong and how to fix it
- Does NOT block on files you didn't touch
- Has a documented escape hatch (e.g. `--no-verify` warning, or a one-line bypass env var)

Before writing:
1. Find how hooks are currently set up in this repo
2. Show me what framework you'll use and why
3. Wait for approval

Then write it, install it, and test it by simulating both a passing and
a failing commit.
```

**Expect:** A hook that fits the existing setup, with a self-test. The "does not block on files you didn't touch" clause is important — overly-broad hooks get disabled within a week.

---

## Bonus: the meta-rules

A few general rules that apply to every prompt above:

1. **Specify what you don't want.** Models optimize for "helpfulness". If you don't say "no filler", you get filler. If you don't say "no defensive wrapping", you get try/catch around every line. Negative constraints are 3x more useful than positive ones.

2. **Ask for a plan first on anything nontrivial.** The model is faster than you at typing, but slower than you at backing out of a bad direction. A 2-minute planning step saves 20 minutes of re-reading a wrong diff.

3. **"Do not guess. Say 'unknown'."** This one line, in every prompt that asks for factual information, cuts hallucination rates dramatically. Models hate admitting they don't know something — you have to explicitly permit it.

4. **Length caps are load-bearing.** "Under 300 words" is not a suggestion. If you remove it, you get 1500 words of hedging. Models will fill whatever space you leave.

5. **Cite files you actually opened.** Tell the model to name the files it read. If it names files it didn't open, you'll catch hallucinations immediately.

6. **One task per run.** A prompt that says "fix bug X AND refactor Y AND add tests AND update docs" will produce a sprawling, half-finished diff. Split it.

7. **Trust, but verify.** Models are right most of the time. That's the dangerous bit — you stop checking. Keep a `git diff` open. Run the tests yourself. Read the commit.

---

## License

You bought this file. Do whatever you want with it — use the prompts in
your day job, adapt them for your team, put them in your own `CLAUDE.md`.

Do not resell as-is. Do not claim you wrote it.

If a prompt saves you an afternoon, tell someone about it. Word of mouth is
the only reason a solo seller like me gets to keep doing this.

---

*Built by the Cybertruck Autopilot project — an ongoing experiment in
autonomous Claude Code loops. If you want to see how the loop itself works,
the source is public. Search for "cybertruck autopilot github".*
