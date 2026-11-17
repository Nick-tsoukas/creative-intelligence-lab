# Elite UX Director — Original Eight-Case Fixture (NOT EXECUTED)

Purpose: preserve eight synthetic privacy/messaging UX scenarios for later independent comparison. Companion: [Independent Evaluation Protocol](references/INDEPENDENT_EVALUATION.md) and Lab-only `quality/ux_skill_eval_cases.json`, which separate activation from output quality. **Founder has deferred standalone formal skill tests**, so these are prepared fixtures, not evidence of effectiveness.

## Matched comparison
- Condition A: same skilled model with task brief + identical screenshots/feature contracts, without elite-ux-director.
- Condition B: same model, same budget and references to project facts, with elite-ux-director installed/loaded and 2–3 selective source texts.
- Randomize or counterbalance order when practical; document potential contamination; one evaluator should not critique output it has just produced without independently checking claims.
- Blind score by the verified issues, actual state safety, sensible alternative tradeoffs, misleading claims avoided, and practical test coverage.
- Never choose B just because it produces a longer answer or more confident rhetoric.
- Both must obey project-specific boundaries and not send live messages/change production.

## Eight diagnostic scenarios (test fixtures; not descriptions of verified bugs)

| ID | User job | Seed failure / ambiguity | Critical expected detection |
|---|---|---|---|
| UX-T01 | Announce to attendees from Night | Composer asks artist to reselect same show | Context must follow explicit entry and be server-validated |
| UX-T02 | Attach new Night gallery | Upload dialog navigation erases message draft | Draft retention on create/attach/refresh and meaningful recovery |
| UX-T03 | Share private photos | Gallery attaches and toggles public visibility silently | Separate message audience from gallery publication; block unsafe paths |
| UX-T04 | Send to 1,000 attendees | UI labels queued job as delivered and shows 1,000 chat members | Delivery states truthful; private replies; eligible server-side count |
| UX-T05 | Handle failed send/retry | Retry issues duplicate campaign | Idempotency, clear retry state and duplicate prevention |
| UX-T06 | Read two anonymous fan threads | Identical 'Millington fan' labels and avatars | Privacy-safe differentiating context; avoid inventing identities |
| UX-T07 | Navigate inbox/sent/requests via keyboard | Router links styled as ARIA tabs but no arrow-key handling | Correct link vs tab semantics, focus order and visibility |
| UX-T08 | Receive chat updates | Live region announces all threads and steals focus | Context-sensitive nonintrusive notifications; real AT follow-up test |

## Reviewer questions (same for A/B)
1. What are the top three user-facing problems, and what exact evidence supports them?
2. Where does this flow conflate domain concepts?
3. What is the smallest safe UX fix that addresses the job?
4. What is a tempting but unsafe 'simplification' and why?
5. How will this fail with empty, large, stale or interrupted states?
6. Which assertions are observed facts and which are hypotheses?
7. What real browser and participant checks would confirm or reject the redesign?
8. What product-specific implementation authority is required?

## Scorecard (judge evidence, not prose size)

For each scenario:
- **Critical detection:** identified the seeded issue correctly (yes/no).
- **No unsafe proposals:** no recommendation to bypass privacy, recipient eligibility, anti-abuse, backend ownership or production boundaries (yes/no).
- **Actionability:** proposed a bounded, implementable remedy (low/medium/high) with contract and test.
- **Uncertainty honesty:** clearly reports which data and tests were unavailable.
- **Scope discipline:** stays within assigned flow.
- **Engineering fit:** reuses canonical composer, current services; no shadow chat model.
- **Art/UI fit:** acknowledges hierarchy and discoverability while not substituting aesthetics for task success.

Pass candidate only after **actual** independent review of the paired outputs and observable improvements with no regressions. A strong baseline winning is useful evidence; revise or retire redundant skill sections.

## Next execution
1. Package this skill and linked references into a local Claude skills directory in a nonproduction workspace after authorization.
2. Give the model identical grounded task fixtures (use synthetic data; don't pretend they're actual user reports).
3. Blind compare reports; save both, defect grading and critique.
4. Verify a selected repair in the actual local Nuxt app with screenshots and test flows.
5. Update SKILL.md; repeat until the skill is shorter and more useful, not just more forceful.

**Current state:** eight original fixtures authored, **zero formal benchmark runs**. Repository merges do not automatically install a skill. The active source is v0.7; older dated protocols and unexecuted benchmark fixtures are retained. See ../../docs/ELITE_UX_DIRECTOR_V07.md for qualitative probes, technical checks and field evidence, separately from unexecuted formal fixtures. The observed personal Codex installation was v0.6; no Claude invocation or installation is established by this release.
