# Finish Line — Creative Intelligence Lab v1.0

**Established 2026-11-11.** The repository is a means to better design decisions, not an infinite bibliography.

## Definition of done
**Creative Intelligence Lab v1.0 is ready** when a new ChatGPT session and a fresh Claude Code session can each follow the same brief, produce a reviewable, distinctive design exploration, discuss tradeoffs using cited references, and deliver a working **sandbox** interface that passes agreed functional/accessibility checks. The owner then approves adoption. This is not a claim that our design taste becomes objectively perfect.

## Bounded initial scope (v1.0)
A compact, well-selected working corpus, not every book or example ever made:
- **12 deep case studies:** at least 4 artistic/graphic design, 4 real digital experiences, 4 functional UX/design-system cases. Cases must document specific artifacts, evidence, weaknesses and transfer conditions. First-pass directories or studio descriptions alone do not count as deep audits.
- **6 scholarly/primary-source reading dossiers:** full source or identified chapters/excerpts with exact scope, not book-cover summaries. Include typography, color, composition, visual storytelling, perceptual UX, and motion.
- **6 tested component patterns:** navigation, primary actions, modal/overlay, form validation, gallery/media, data/list. At least 3 systems compared per pattern; keyboard, focus, narrow-screen and loading/error states documented for sandbox implementations.
- **A visual atlas of 24 examples**, mixing rights-aware links to original works, 8 original teaching diagrams, and screenshots with provenance/permission where appropriate. Link-only entries are not presented as captured screenshots.
- **A concise handbook:** ~10–15 conditional principles, with evidence tags, counterexamples, decision questions and pointers to full studies.
- **A design brief + critique contract** that ChatGPT can use consistently, plus a documented collaboration format with Claude.
- **A scoped Claude Code design skill** with staged reference loading, critique checkpoints, accessibility and performance guardrails, and an explicit ban on changing production without approval.
- **A pilot:** three genuinely different concepts for one invented product, one implemented Vue/Nuxt sandbox, a reasoned comparative critique, documented responsive/keyboard/reduced-motion checks, owner review and recorded iteration.

These are planning thresholds and may be refined explicitly based on evidence. Quality gates matter more than raw counts.

## Stage gates — stop accumulating and start using
### Gate 1: Curated foundations
[ ] Above source dossiers and deep case studies satisfy evidence requirements.
[ ] Every source clearly labels access status, copyright/usage, author, URL and uncertainty.
[ ] Visual atlas references have provenance and original/captured distinction.

### Gate 2: Operational handbook
[ ] The handbook can answer: "What makes this visually meaningful for THIS audience?" with a citation and counterexample.
[ ] The design rubric separately covers artistic distinction, task effectiveness, accessibility, performance and engineering craft.
[ ] Prompt and brief schema can be used by a fresh session without undocumented context.

### Gate 3: Claude design skill — alpha
[ ] A packaged skill entry point exists in `skills/creative-design-director/SKILL.md`.
[ ] It names only stable curated references, not every raw article.
[ ] The skill produces alternatives before selecting a solution, distinguishes facts from aesthetic judgment, and reads actual project code before implementation.
[ ] Automated and manual sandbox QA checklist is specified.

### Gate 4: Cross-agent pilot
[ ] ChatGPT generates a context-specific brief and three nontrivially different concepts.
[ ] Claude reports the repo/code it inspected, builds only a sandbox prototype, captures artifacts where allowed and documents open questions.
[ ] ChatGPT independently critiques output against original concept and constraints; Claude revises.
[ ] Owner approves the chosen direction or rejects it, with reasons retained in a decision log.
[ ] Human keyboard/responsive inspection is actually performed or marked pending. No fictional test results.

### Gate 5: v1.0 release
[ ] Another new chat can resume solely from README/START_HERE, handbook, collaboration contract and skill package.
[ ] 1 reproducible sandbox pilot has passed the specified checks and decisions are documented.
[ ] Release tagged and changelog/status updated. Owner signs off on using the system on production projects.

## Ownership and safety
- **Owner:** vision, final taste, approval of major direction and any production deployment.
- **ChatGPT:** research lead, brief/art direction, independent critique and acceptance criteria.
- **Claude:** design engineering lead, implementation/prototype, instrumentation, screenshots, technical feedback and refinement.
- **Production:** code review, verified accessibility/performance, and explicit owner go-ahead.
- Do not claim monitoring or asynchronous background work; commits occur only when tools are invoked.

## First next slice (prioritized)
1. Typography chapter and case index.
2. v1.0 handbook skeleton + reference quality rubric.
3. Work an invented sandbox exercise to test the art-direction/engineering handoff.
4. Use pilot failures to sharpen the skill, rather than waiting for a perfectly exhaustive bibliography.
