# Design Acceptance Rubric v0.1 — Separate Excellence Axes

**Status:** Rubric proposal for sandbox pilot; not a standardized scientific metric.

## Scoring
Score each axis **1–5**, but report the reasoning and exact evidence independently. Aesthetic judgments are subjective; passing accessibility cannot be inferred from scores. Note NOT TESTED wherever direct evidence is missing.

### 1. Concept specificity
1 = interchangeable page; 3 = some content-specific decisions; 5 = identifiable cultural/content thesis where imagery, typography and pacing reinforce meaning.

### 2. Visual craft
1 = unresolved hierarchy/spacing/crop/type; 3 = coherent composition with rough edges; 5 = refined, intentional rhythm, image art direction, color context and micro-detail.

### 3. Comprehension and task fluency
1 = essential task obscured; 3 = understandable with exploration; 5 = primary task clear and recoverable; verified with actual user/task observations before calling it proven.

### 4. Accessibility and resilience
1 = confirmed blockers; 3 = basic semantics/responsive states; 5 = appropriate keyboard/focus/zoom/contrast/reduced-motion states inspected and major barriers resolved. Full WCAG conformance cannot be concluded from this rubric.

### 5. Engineering quality
1 = fragile/sluggish; 3 = maintainable and functional; 5 = verified SSR/client behavior, motion/image strategy, tested core state transitions and sensible performance.

### 6. Evidence honesty
1 = invented tests/citations; 3 = accurate limitations; 5 = traceable source and runtime evidence, counterexamples and explicit unknowns.

## Hard stop conditions
- Broken primary task, missing labeling or keyboard barriers.
- Deceptive action affordance (e.g. fake playable audio).
- Unapproved production modifications.
- Unlicensed third-party content committed as one's own.
- Claims of tested compliance or real screenshots without evidence.

## Concept comparison
Do **not** average the six scores to choose a winner automatically. Explain non-negotiable UX/accessibility failures, artistic tradeoffs and context. An expressive concept can win only if operational risks are addressed.

## Acceptance sequence
Before implementation: three concepts, critique, decision ownership.
After implementation: inspected output, documented QA, screenshots (when accessible), revision log, owner review.
