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
