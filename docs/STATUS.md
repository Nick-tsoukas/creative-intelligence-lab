# Project Status

Last revised: 2026-11-11.

## Confirmed mission
An independent, versioned research library to teach exceptional visual communication, UX, components, digital design and implementation. Future Claude Code skill planned, not yet installed.

## Existing research, preliminary
- Research chapters 001 and 002 were developed in chat, not entire books read cover-to-cover.
- An earlier v0.2 portable archive was prepared containing 17 Markdown research files, including a source catalog, web design notes, experience and component atlases.
- The new GitHub repository was created by the user. Initial files in this repository may be a **curated foundational subset** of previous notes; check contents before claiming full migration.

## Evidence standards
A source on a list is not the same as a source thoroughly examined. Labels: QUEUED, LINK-VERIFIED, EXCERPT-REVIEWED, PARTIALLY-READ, FULLY-READ, DIRECTLY-OBSERVED, and NEEDS-RECHECK. Do not infer FULLY-READ from memory.

## In progress
- GitHub onboarding docs and research scaffolding.
- Detailed inspection of actual digital experiences, components and UX patterns.
- Annotated source verification.

## Not done
- Exhaustive reading of bibliography.
- 30–50 deep digital case studies.
- Comprehensive visual asset archive (third-party rights must be handled).
- Claude Code skill creation / deployment.
- Any Faneqo homepage implementation or production modifications.

## Next action
Select and fully analyze an initial set of outstanding digital experiences with primary project links and clear limitations, then compare against exemplary usability systems. Update bibliography and changelog with each reviewed increment.
## 2026-11-11 research increment — verified GitHub commit
- Five published-source dossiers now in `case-studies/digital/`: FinalFinal, David Whyte, Linear's 2026 interface refresh, GOV.UK Design System and Adobe Spectrum.
- Comparative analysis in `research/003-DIGITAL-EXCELLENCE.md`.
- **Evidence limits:** official creator/design-system documents inspected; no live mobile, keyboard, screen reader, user testing or measured performance. These are source-grounded first-pass studies, not five completed independent usability audits.
- Next: direct observed study of exact projects and a dialog/form component pattern comparison; preserve unverified status until actually tested.

## 2026-11-11 — Design systems and visual evidence expansion
- Added `design-systems/` with official-source readings of Apple HIG, Google Material 3 Expressive, a cross-system matrix (Fluent 2, Carbon, Polaris, Spectrum, GOV.UK, Atlassian, Primer and more), and Vue/Nuxt component library research.
- Added `visual-library/` with 10 source-hosted illustrated example links, screenshot capture/provenance protocol, and an original SVG concept illustration (not a screenshot).
- Original visuals currently committed: **one**. Direct captured screenshots of Apple/Google and component examples: **zero**. See visual-library README for legal and access constraints; do not claim screenshots were captured.
- Apple/Google official guidance was read online. Google-reported experimental outcomes remain **creator-reported**, not independently validated.
- No libraries installed; no application code changed.
- Next: direct screenshot capture using a browser with access, rights checks before public publication, and a component-by-component comparison.

## 2026-11-11 — Component Anatomy research cycle 005
- Added `components/` research index and official-source analysis of buttons, dialogs and interruptions, and forms/errors/tabs. Sources include Apple HIG, Fluent 2, GOV.UK and W3C APG.
- Created original `visual-library/original-studies/component-anatomy.svg` illustrating generic action hierarchy and form recovery; **this is not a real UI screenshot**.
- Evidence scope: official documentation reviewed; no interactive browser, keyboard or screen reader audits of shipped products. Research hypotheses remain explicitly labeled.
- Next: compare Material 3, Fluent, Apple, GOV.UK and Vue implementations of the same components with hands-on captured screenshots; verify behavior in a controlled test environment.

## 2026-11-11 — Art × Interface research release 006
- Committed `research/004-ART-TO-INTERFACE.md` with first-pass source-grounded analysis of Albers, Block, Lupton, and Google Material expressive research.
- Committed `handbook/ANTI_GENERIC-DESIGN-METHOD.md`, a **working hypothesis** for producing distinctive, task-effective interfaces; it is not a validated method or an automatic skill.
- Committed `sources/ART-READING-TRACKER.md` with access-status honesty: official pages and foundation articles were reviewed, **not full books**.
- Added an original SVG experiment at `visual-library/original-studies/albers-color-context.svg`; it is **not** an artwork copy or a real website screenshot.
- No Faneqo frontend/backend or production implementation changed. Next: expand primary source access, case studies, and actual visual/browser experiments.

## 2026-11-11 — Research release 007 (visual attention)
- Published `research/005-ARCHITECTURE-OF-ATTENTION.md` with source-grounded analyses of Caravaggio, Vermeer, Saul Bass, James Turrell, and NN/g's non-universal F-pattern.
- Published `handbook/ATTENTION-DIRECTION-CHECKLIST.md`, `visual-library/ATTENTION-ARTWORK-INDEX.md`, and an original SVG `visual-library/original-studies/attention-choreography.svg`.
- Access status: institutional source pages and published UX articles reviewed, **not** full books, museum visits, empirical user testing or live UI screenshots. No third-party images copied into repo.
- Next: legally accessible long-form reading and a repeatable visual experiment tested with real participants; develop deep typography/art direction chapter.

## 2026-11-11 — Release 008: bounded finish line and cross-agent system
- Added `docs/FINISH_LINE.md`: 5 stage gates for v1.0, including 12 deep case studies, 6 properly scoped reading dossiers, 6 tested component patterns, 24 visual examples, a curated handbook, a Claude skill, and a real sandbox pilot. These are targets, not completed counts.
- Added `docs/CROSS_AGENT_PROTOCOL.md`: ChatGPT as research/art director and independent critic; Claude as design engineering/prototyping partner; owner has final control and production authority.
- Added research `research/006-TYPOGRAPHY-AS-ARCHITECTURE.md`: officially sourced Scher, Tschichold, Müller-Brockmann, Lupton and WCAG/web typography references, with explicit access limits.
- Added `handbook/RESEARCH-TO-DIRECTION.md`, `templates/CREATIVE_BRIEF.md`, and `templates/DESIGN_REVIEW.md`.
- **Not yet built:** Claude Code design skill, installed skill, live pilot, independent user tests, complete v0.2 archive migration, and compliant screenshot collection. The existing case-study dossiers are mostly published-source reviews, not deep live audits. Do not count them toward completion without upgrading evidence.
- **Next focus:** curated case-study/reading quality and sandbox pilot. Avoid infinite collection.

## Release 008 visual supplement
- Added `visual-library/original-studies/typographic-voices.svg`: three original typographic directions using identical invented content, for future critique and sandbox experiments. Not an external screenshot. Agent onboarding files now reference the finish-line gates and cross-agent protocol.

## 2026-11-11 — Release 009: operational alpha skill and first pilot
- Created `skills/creative-design-director/SKILL.md` and a small on-demand reference file. **It is a candidate skill stored in GitHub, not installed in Claude Code or validated through a Claude run.** Structure is aligned with official Anthropic skill authoring guidance.
- Created pilot `pilots/001-signal-archive/`: fictional sound-archive brief, three distinct directions, explicit task/QA matrix, decision log, and a research-based independent rubric.
- Added a self-contained `pilots/001-signal-archive/prototype/index.html` representing the Field Notes concept, with mock search/filter/favorite interactions, a clear unavailable-audio label, original graphics and reduced-motion CSS. Corrected filter focus restoration in code. **No runtime/browser execution, keyboard testing, Nuxt port, Claude run, screenshots or human user test yet.**
- v1.0 gate progress: Gate 3 alpha artifact scaffold prepared; Gate 4 brief/concepts prepared; working pilot and QA still unproven. Human approval and actual implementation review pending.
- Next: execute prototype in a real browser, capture desktop/mobile/focus states, record defects, and have Claude independently inspect/rebuild in a real Nuxt sandbox only after user approval for that work.

## 2026-11-11 — Research 010 and owner pilot strategy
- Owner instructed that Claude Code remains focused on existing Faneqo development; **do not interrupt it or ask for skill testing now**. Continue independent research.
- Final applied validation changed to a **separate Faneqo homepage mockup**, only once Claude is available and the owner authorizes mockup implementation. Signal Archive remains an optional internal proof-of-concept; it is not compulsory near-term work. See `docs/PILOT-STRATEGY.md`.
- Added `research/007-CINEMATIC-IMAGE-LANGUAGE.md`: Sugimoto, Crewdson, Darius Khondji / Bong Joon-ho's cinematographic rhythm, concept-first motion titles, and W3C motion guidance. Evidence: museum, practitioner, and standards documents; not full cinema book reading or direct film analysis.
- Added `handbook/CINEMATIC-DIRECTION-CARD.md`, `visual-library/CINEMA-PHOTOGRAPHY-SOURCE-ATLAS.md`, and an original `three-rhythms.svg` teaching diagram. No third-party images uploaded.
- Claude skill draft remains committed, **not installed/tested**. The new docs are committed to the research repo only. No production files changed.
- Next: continue art/photography/architecture/typography research and make the art-direction handbook selective, then design the final mockup brief against current Faneqo reality when Claude is free.
