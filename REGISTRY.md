# Registry — Trading

> Current snapshot only. Put why a durable decision was made in
> `decision-log.md`.

**Last verified:** 2026-09-28 10:40 CST

**State authority:** this file for this project's current state
**North Star:** none yet; the line's purpose is stated in the Park OS manual (Trading 线：交易与投研)

## What we are building

A scoped Trading catalog that works as a hub: every library is placed on the trading pipeline, judged against criteria fixed in advance for its stage, and backed by first-round screenshots and records.

## Where we are now

66 catalog repos, synced from Park OS. 59 of them (all except Knowledge & Collections) have a pipeline evaluation card in `evaluations/assessments/`, rendered into `evaluations/README.md` and six category pages by `scripts/render-hub.py`. Criteria and weights live in `evaluations/criteria.json`. Raw first-round evidence stays in the dated round directories.

Gaps: no product completed a paper order→fill→position closed loop in the first round; six products were tested at a revision different from their catalog lock.

## Milestone position

**2/3 complete** — the evaluation framework is live; the next milestone is a second round that closes the gaps the cards list under 未验证.

| Milestone | Status | Evidence |
| --- | --- | --- |
| First-round trials and screenshots | complete | [PR #21](https://github.com/zinan92/trading/pull/21), [PR #22](https://github.com/zinan92/trading/pull/22) |
| Pipeline framework with criteria-first scoring | complete | [PR #23](https://github.com/zinan92/trading/pull/23) |
| Second round: paper closed loop, lock alignment, unverified criteria | not started | [issue #24](https://github.com/zinan92/trading/issues/24) |

## Next move

1. Re-test the six lock-mismatched products at their catalog lock ([issue #24](https://github.com/zinan92/trading/issues/24)).
2. Run one paper closed loop (data → signal → risk → simulated fill → position readback) on the top Full Trading System candidates.

## ETA

unknown — no reliable basis

## Project pulse

| Field | Value | Source / as-of |
| --- | --- | --- |
| Latest merged PR | #23 pipeline evaluation hub | 2026-09-28 |
| Merged PRs, last 30 days | 7 before #23 | GitHub query 2026-09-28 |
| Project age / activity | created 2026-08-26; three evaluation PRs in three days | GitHub API 2026-09-28 |

## Evidence and history

- Decision rationale: [decision-log.md](decision-log.md)
- Evaluation framework: [evaluations/FRAMEWORK.md](evaluations/FRAMEWORK.md)
