# Decision log — Trading

> Keep only durable decisions. A functional PR records its decision and
> Gotchas; a pure deploy/status change is exempt unless it changes a durable
> operating fact.

## 2026-09-28 — Evaluate by pipeline stage, criteria before scores

- **Context:** The first-round evaluations (PR #21, #22) gave hand-assigned 0–100 scores before any criteria existed, used one five-dimension rubric for every category, and laid out each category page differently. Park rejected the scores as not counting.
- **Decision:** Place every product on a ten-stage trading pipeline (fetch, clean, store, indicator, strategy, backtest, lifecycle, risk, execute, monitor). Each catalog category gets its own objective and five weighted criteria in `evaluations/criteria.json`. Ratings are one of done, partial, failed, unverified, not-applicable, each citing an existing screenshot or record. The score is derived mechanically. All pages are generated from `evaluations/assessments/*.json` by `scripts/render-hub.py`.
- **Why:** Different stages have different jobs, so one rubric misjudges them. Deriving the score from cited ratings makes every number traceable and lets Park change a weight without re-judging products.
- **Alternatives rejected:** Keeping the first-round scores with a new page layout, because the numbers still had no agreed basis. Re-running all trials, because the existing evidence was sufficient for most ratings.
- **Evidence:** [PR #23](https://github.com/zinan92/trading/pull/23); `python3 scripts/check-hub.py` passes.
- **Gotchas:**
  - A Park OS README export wipes the `HUB` block and the per-row `[评测]` links. Run `python3 scripts/render-hub.py` last, after the two old archive renderers.
  - Not-applicable criteria leave the denominator; unverified criteria stay in it and score zero. A narrow product can therefore outrank a broad one. Each category page carries a reading note where this inverts a ranking (Data, Trading Infra).
  - Products with less than 40% verified weight, or less than 60% applicable weight, are listed but not ranked.
  - A product has one full card, filed under the category it is evaluated as. A placeholder in its catalog-category file carries `stub: true`.
  - Category suggestions are evaluation opinions. The canonical category and lock stay in Park OS.
  - Never hand-edit generated pages: `evaluations/README.md` and `evaluations/<category>/README.md`.

## 2026-10-04 — Catalog entries without a card are pending, not errors

- **Context:** The October 2 Park OS export (PR #25) rewrote the README, which removed the `HUB` block and every `[评测]` link, and added two repos with no evaluation evidence. `check-hub.py` then failed on the missing cards.
- **Decision:** Restore the hub by re-running `render-hub.py`. Repos in the catalog without a card are listed as 新加入、尚未评测 on their category page and in the overview, with a 待评测 count on the README; the checker reports them as a note instead of failing.
- **Why:** New stars arrive faster than trial rounds. A failing checker would block every catalog refresh, and an empty card would imply evidence that does not exist.
- **Alternatives rejected:** Writing placeholder cards with every criterion unverified, because it pads the catalog with fake rows.
- **Evidence:** this PR; `python3 scripts/check-hub.py` passes with 2 pending.
- **Gotchas:** The README wipe will recur on every export until the Park OS exporter preserves the `HUB` block; that fix lives in zinan92/park-operating-system.

## 2026-10-04 — Scores round half up; equal scores share a rank

- **Context:** FRAMEWORK.md promised 四舍五入, but `render-hub.py` used Python `round()`, which rounds halves to even. Vibe AStock's ratings sum to exactly 72.5 and showed as 72; twelve existing cards ending in .5 were also off by one in either direction.
- **Decision:** Compute percentages with Decimal `ROUND_HALF_UP`. Equal scores share a rank (1, 2, 2, 2, 5); within a tie, order by verified ratio, then name.
- **Why:** The framework text is the contract, and a tie broken by alphabet should not read as a lower rank.
- **Evidence:** PR #27; scores that moved by one point: A Share Heatmap 83, Maverick MCP 83, Gloomberb 73, standard-kline 73, datafeed 73, NautilusTrader 53, KHunter 63, Qlib 58, a-stock-data 58, Chancode 43, Meme Radar 23, finhack 23.
- **Gotchas:** Never use Python `round()` for displayed scores; use the `pct` helper.
