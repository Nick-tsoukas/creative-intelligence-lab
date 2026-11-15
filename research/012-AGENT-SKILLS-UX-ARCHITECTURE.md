# Agent Skills Architecture Review — Applying Matt Pocock's Engineering Patterns to Creative Intelligence

**Date:** 2026-11-15. **Scope:** design of a usable Claude UX/creative skills system, not implementation in the Faneqo repo.

## Verified primary source
- Matt Pocock's [Skills for Real Engineers](https://github.com/mattpocock/skills) README and actual skill entrypoints studied on this date:
  - [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)
  - [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)
  - [prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)
  - [research](https://github.com/mattpocock/skills/blob/main/skills/engineering/research/SKILL.md)
  - [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)
  - [code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md)
- These were inspected for workflow patterns, not downloaded/installed/copied. This note is an original adaptation plan.

## Major architectural findings

1. **Small and composable.** Matt's README rejects heavyweight orchestration, favors small skill boundaries and project control. Our UX skill should remain independently usable and selectively load detailed references.
2. **Product glossary matters.** His domain-modeling workflow explicitly maintains concise shared vocabulary and ADRs for important trade-offs. For Faneqo distinguish attendee, eligible recipient, Night, gallery visibility, publication, campaign and one-to-one chat. A model that silently equates these causes dangerous UX.
3. **Prototype answers one named question.** His prototype entrypoint splits LOGIC (test state model) from UI (multiple dramatically different presentations). Our UX skill should route to a state-machine experiment when uncertainty is domain state, or visual experiment when uncertainty is layout; no second production composer built as a 'prototype'.
4. **Test at public seams.** His TDD skill prioritizes user-visible outcomes, tests of public behavior, one red/green slice at a time, and rejects tautological or overly internal assertions. For the Lab choose user journeys (entry → compose → attach → review → send → feedback) rather than assertions against Vue component internal variables.
5. **Two-axis review.** His code-review entrypoint reviews conformance with project standards and original task separately. Our design review should similarly separate **workflow/task correctness** from **design/art-direction quality**, while preserving independent accessibility/safety checks.
6. **Primary-source research to saved note.** His research skill prefers primary documentation and a compact cited Markdown artifact. Our UX book system already uses chapter-scoped reading dossiers and can link exact claims to design decisions. His background subagent invocation is an option within supported Claude environments, not evidence that research happened or must run asynchronously in this chat.

## Proposed core skill routing

- `elite-ux-director`: **user intent, information architecture, tasks, mental models, state/permission mapping, failure recovery, usability test plan**; core remains generic.
- `creative-design-director`: **artistic thesis, culturally authentic visual expression, three coherent directions, critique**.
- Existing `frontend-design`: **code implementation and responsive visual craft**.
- Existing engineering/testing skills: **debugging, implementation, browser/keyboard/accessibility checks**, with actual pass/fail evidence.
- Optional one-line host instruction: invoke UX first when flow is confusing, creative direction when visual expression is in question, frontend-design to build an authorized solution. Do not load every skill by default.

**No fourth monolithic 'UX + Art + Code' mega skill.** Interoperability through small contracts is more valuable than duplicated instructions.

## Specific practical upgrades to elite-ux-director v0.2

### A. Introduce a Domain Vocabulary Gate
Before designing a complex cross-feature interaction: use the approved project glossary if present and clarify conflicts. Write a concise terminology decision only when necessary. Do not introduce Faneqo terms into unrelated projects.

### B. Route by uncertainty
- **UNKNOWN USER JOB** → observe/research; write job statement before proposing UI.
- **UNKNOWN DOMAIN STATE/PERMISSIONS** → state transition/logic prototype; do not create a second functional app.
- **UNKNOWN COMPOSITION/STYLE** → 2–3 concept variants; keep all functional facts stable.
- **UNKNOWN IMPLEMENTATION** → inspect source and design minimal behavior contract.
- **UNKNOWN QUALITY** → execute relevant browser/user checks.

A prototype is not the deliverable by default. When current user asks to improve an actual app, use a prototype only for a bounded unresolved question, then return to real app work.

### C. Establish two-axis acceptance
1. **Behavioral correctness:** real task finishes, permissions valid, truthful states, recovery, keyboard/accessibility.
2. **Experience/art direction:** comprehensibility, hierarchy, coherence, authenticity, visual refinement and emotional appropriateness.
Do not call design 'elite' because one axis passes. Do not declare UX successful without actual evidence.

### D. Benchmark a true failure
Use existing 8 Faneqo synthetic scenarios in EVALUATION.md; compare with a strong baseline at equal effort, separately count high-severity caught issues and false/unsafe suggestions. Test procedures do not replace representative artist observation.

## Deployment/ownership
- No skill installed in Claude, no user project changed and no evaluation run as part of this research.
- Skill improvements can be made in the standalone Creative Intelligence Lab repo without invoking or interrupting current Faneqo Claude tasks.
- When user wants activation, install only curated skills and their source references; verify actual discovery and continue original development task.
- Don't adopt auto-update blindly where skill changes could affect stable development runs.
- Prefer retaining Faneqo-specific product facts in project repository glossary/adapter, not in reusable core skills.

## Sources to revisit
See original Matt Pocock repository skill files linked above, our source-ledger UX books, and the Lab [Elite UX Director](../../skills/elite-ux-director/SKILL.md) / [Creative Director](../../skills/creative-design-director/SKILL.md) entrypoints.
