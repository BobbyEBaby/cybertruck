# Themes Tracker — cross-episode analysis database

Every episode of Popular Uprisings is analyzed across **six recurring themes** that research suggests are the most predictive conditions for rebellion. This file is the accumulated database. **Every episode must update this file** — it's what makes the channel's analytical thesis real instead of just talked-about.

## The six themes

Each theme has a dedicated wiki page that accumulates observations across every rebellion added to the database:

1. **[[../../wiki/themes/economy|Economy]]** — inflation, price shocks, food scarcity, taxation, wealth concentration
2. **[[../../wiki/themes/royalty|Royalty / leadership]]** — legitimacy crisis, succession disputes, absent or weak ruler, visible excess
3. **[[../../wiki/themes/government|Government]]** — corruption, failed justice, representation denied, bureaucratic overreach
4. **[[../../wiki/themes/wars|Wars]]** — military overreach, veteran grievances, conscription, border losses
5. **[[../../wiki/themes/environment|Environment]]** — famine, plague, weather shocks, resource depletion
6. **[[../../wiki/themes/debt|Debt]]** — sovereign, personal, religious (indulgences, tithes)

## Intensity scale
For each theme, rate **0–3**:
- **0** — theme was absent or irrelevant to this rebellion
- **1** — present as background condition, not a proximate cause
- **2** — a significant contributing cause, visible in the revolt's stated grievances
- **3** — the dominant cause, the thing participants and historians name first

## Database

| # | Episode | Year | Place | Econ | Royal | Govt | War | Env | Debt | Total | Outcome |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [[../../wiki/rebellions/peasants-revolt-1381\|Peasants' Revolt (Wat Tyler)]] | 1381 | England | 3 | 1 | 3 | 2 | 3 | 2 | **14** | `partial_win` |
| 2 | [[../../wiki/rebellions/german-peasants-war-1524\|German Peasants' War]] | 1524–25 | Holy Roman Empire | 3 | 1 | 3 | 1 | 1 | 3 | **12** | `crushed` |
| 3 | [[../../wiki/rebellions/harpers-ferry-raid-1859\|Harpers Ferry raid (John Brown)]] | 1859 | United States | 2 | 1 | 3 | 2 | 0 | 0 | **8** | `triggered_reform` |

_(more episodes will fill this table as they ship)_

## Observations (accumulate as data grows)

_(empty until ≥3 episodes are in the database. Then write 1–3 paragraphs here about the patterns emerging. Examples of the kind of observation to look for: "every rebellion so far had at least 2 themes rated ≥2", "environmental shocks preceded every successful rebellion but not every failed one", "pure debt rebellions are rarer than expected", etc. This is the through-line content that makes viewers want to watch the next episode.)_

## Rules for filling in this table (for future runs writing episodes)

1. **Intensity ratings are a judgment call, but document the call in the episode script.** Each episode script file should have a section near the end called `## Theme intensities (for themes.md)` that lists the 6 numbers with a one-sentence justification per rating. When the episode publishes, those numbers get copied here.
2. **Never retroactively rewrite a rating.** If a later episode's research makes you reconsider an older rating, leave the old one and add a footnote. The database must be append-only for credibility.
3. **"Outcome"** is: `crushed`, `partial_win`, `full_win`, `triggered_reform`, or `unclear`. Keep the vocabulary consistent so aggregations are possible.
4. **Total column** is the sum of all six theme ratings (0–18). Not a fancy aggregate — just a quick "how intense were the conditions overall" signal for hover-viewing.
