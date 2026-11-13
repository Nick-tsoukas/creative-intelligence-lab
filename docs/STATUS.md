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

## 2026-11-11 — Release 011: major cross-disciplinary consolidation
- Added first original-text reading dossier: `reading-dossiers/001-ALBERS-ART-INSTRUCTION.md`, based on passages from Albers Foundation transcriptions (1934, 1939 and 1954 excerpts reviewed; complete texts not verified line by line). **Not a full reading of Interaction of Color.**
- Added `research/008-ART-DIRECTION-FIELD-MANUAL.md` (15 conditional design moves), `handbook/DECISION-CARDS.md` (12 cards), `engineering/CREATIVE-FRONTEND-QUALITY.md` (implementation quality and motion), and `case-studies/art/001-PUBLIC-THEATER-IDENTITY-AS-SYSTEM.md` (Pentagram 2014/2016/2026).
- Added two **original** visual teaching SVGs: identity invariants and competing vs focused event hierarchy; `visual-library/REGISTRY.md` records eight original SVG files and **zero real site screenshots captured**.
- Updated skill alpha's reference map; **Claude skill is still not installed or executed**. Do not interrupt Claude's existing Faneqo work. Final pilot remains isolated Faneqo homepage mockup, not production.
- Quality limits: studio-authored case evidence isn't an independent visual/UX test; original SVGs were committed as markup, not inspected in every browser; handbook needs validation.
- See `docs/RELEASE_011_PLAN_AND_SCORECARD.md` for gaps. Next highest-value work: two further original-source reading dossiers, specific artifact audits, and a measured mockup evaluation after Claude is available.

## 2026-11-11 — Release 012: explicit complement to Anthropic frontend-design
- Reviewed Anthropic's official `frontend-design` skill. It already handles distinct visual styling, typography, responsive frontend implementation, animations and self-critique; the Creative Intelligence skill must not repackage those capabilities as unique.
- Added `research/009-FRONTEND-SKILL-COMPARISON.md`, `handbook/DIRECTION-TO-BUILD-CONTRACT.md`, and `experiments/001-ANTI-GENERIC-SELF-AUDIT.md`.
- Revised `skills/creative-design-director/SKILL.md` to **alpha v0.2**: research, primary-source selection, original creative theses, implementation-neutral brief, independent critique and a documented feedback loop. **No CSS/UI generation or styling duplication.**
- Alpha remains stored in the repository only: not installed, executed, compared or shown to outperform the official skill.
- Claude continues separate Faneqo work; final validation remains an isolated Faneqo homepage mockup when owner indicates availability.

## 2026-11-11 — Release 013: architecture and experience
- Source-grounded first-pass architecture chapter in `research/010-ARCHITECTURE-OF-DIGITAL-EXPERIENCE.md`, covering Foundation Le Corbusier's Villa Savoye, Ando's Church of the Light (secondary architectural account), and Peter Zumthor's 2011 Serpentine Pavilion (commissioning institution and architect statement).
- New substantial primary-statement excerpt dossier `reading-dossiers/002-ZUMTHOR-SERPENTINE-STATEMENT.md`; three architecture art case studies, one creative-direction card, a links-only visual atlas and an original sequencing SVG.
- Primary-source reading dossiers now **2**, with access scope different for each (Albers excerpts; Zumthor short statement). Do not confuse with full books.
- The visual teaching diagram count is now **9 originals**, based on the prior eight-file registry plus this new SVG; browser rendering and UX tests are unverified. No actual source screenshots captured or copyrighted photographs redistributed.
- Critical design distinction: architecture's composed path should not be copied as mandatory web scroll path; preserve direct navigation and accessible task completion.
- Claude skill remains research/direction/critique-only and uninstalled. Owner's final test is an isolated Faneqo homepage mockup once Claude is free. No production changes.

## 2026-11-13 — Research engineering release 015: Perception Workbench
- Added [standalone HTML experiment](../experiments/002-perception-workbench/index.html) and [study protocol](../experiments/002-perception-workbench/PROTOCOL.md).
- Three working-source UI studies: visual weight (3 conditions), semantic grouping (3 conditions), contextual color (3 conditions). Controls, keyboard tab navigation, in-memory answer recording and JSON copy are coded.
- **Only source-level checks were performed:** 12 static structural checks passed on committed GitHub source. No browser screenshots, interactive runtime execution, screen-reader QA, user participants, empirical findings, or formal accessibility conformance claims. See protocol for exact untested checks and experimental confounds.
- No external art copied, no Faneqo app code modified, no Claude skill installed.
- Next acceptance gate: execute browser QA with exact viewport/keyboard records before claiming the prototype tested; refine confounded stimuli before controlled user study.

- Release 015 follow-up: committed a Playwright Test source suite `experiments/002-perception-workbench/workbench.spec.mjs` (nine cases including 1280px, 390px, 320px). **Not executed**, no passing-test claim.

## 2026-11-13 — Founder-aligned master product plan
- The Lab's primary business application is **Faneqo and music-industry web/mobile experiences**; its creative direction, UX, engineering-evidence and critique core must remain reusable across unrelated domains.
- Committed `docs/MASTER_PRODUCT_PLAN.md` as the canonical prioritized route to v1.0: research curation, compact art director handbook, skill/toolchain validation, owner-authorized isolated Faneqo flagship, portable release.
- **No new design tests run** by adding this plan; skill remains an unvalidated alpha, browser instrument not yet runtime tested, and no Faneqo application code was modified.


## 2026-11-13 — Independent research and test-readiness increment 016
- Added GitHub Actions Chromium workflow `.github/workflows/perception-workbench.yml`; actual CI result is **NOT VERIFIED** in this session. The Playwright source tests are still not counted as passed browser QA.
- New **primary original-text** reading dossiers: `reading-dossiers/003-WILLIAM-MORRIS-IDEAL-BOOK.md` (1893/1895 essays, carefully limited sections) and `reading-dossiers/004-EDWARD-JOHNSTON-LETTERING.md` (1906 preface and Ch. XIV qualities, exact pages). The scoped reading-dossier count is now **4 of target 6**, pending deeper audit of each; not four entire books.
- Added `sources/BOOK_ACQUISITION_AND_READING_QUEUE.md` with public-domain text access, rights distinctions and capped active reading queue. **No book files downloaded into the GitHub repository**.
- Added `pilots/002-creative-intelligence-comparison/PROTOCOL.md`, a fair baseline vs research-directed test plan; neither condition built or run and owner authorization for later Faneqo sandbox still needed.
- Creative Director skill remains uninstalled/unvalidated. No Faneqo production changes.

## 2026-11-13 — Release 017: Klee source close-reading increment
- Added `reading-dossiers/005-PAUL-KLEE-PEDAGOGICAL-SKETCHBOOK.md`: limited source-visible 1925 German/1953 English excerpts and translator commentary **clearly separated**; bibliography cross-checked with Met, SFMOMA and Bauhaus Kooperation.
- Original Centre Pompidou PDF link returned HTTP 404 in online retrieval; **no complete book downloaded**, no plates visually studied. Dossier count now provisionally **5/6 scoped**, zero additional fully-read books.
- Precise mechanisms: line as a moving point, active/passive/intermediate systems, non-symmetric balance, visual paths and arrow/spiral movement; includes proposed controlled comparative experiment, not actual test findings.
- Browser CI workflow source remains committed; no successful CI run verified in this session. Creative Director skill and Faneqo isolated homepage pilot remain unexecuted; Faneqo code untouched.


## 2026-11-13 — Release 018: first actually rendered art-direction comparison
- Built an isolated fictional music-platform two-variant design sandbox (neutral vs expressive). Used headless Chromium via Python Playwright to capture 6 real screenshots at 1280, 390 and 320px.
- **Actual checks passed** after revision: 6/6 viewport×variant no-horizontal-overflow, zero JS page errors; same principal heading/CTA; direction selector works; simple focus/nav hash checks. The source is provided as a user sandbox ZIP, **not committed to GitHub**.
- Eyes-on screenshot critique found mobile decorative-overlay text legibility problem despite passing code checks. Corrected caption contrast/stacking, corrected misleading 'Join' link, and reran.
- [Experiment 003 report](../experiments/003-music-art-direction-comparison/RESULTS.md) committed with precise scope; [Creative Director alpha](../skills/creative-design-director/SKILL.md) now demands actual viewport screenshot review before design-quality acceptance.
- This is not independent empirical proof of greater creative quality; no users, assistive-technology audit, actual Faneqo assets, or controlled A/B comparison. **Experiment 002 Playwright workflow run remains unverified**.
- Faneqo frontend/backend and production remain untouched.

## 2026-11-13 — Release 019: Walter Crane and reproducible engineering
- Added reading-dossiers/006-WALTER-CRANE-LINE-AND-FORM.md, grounded in selected original 1900 chapters on silhouette, movement, graphic and ornamental purposes, counterbalance, material constraints, and relational color.
- Six candidate **scoped** primary-text dossiers now exist (the numerical v1.0 target). This does not mean six full books read; quality review remains.
- Preserved Experiment 003's exact HTML in GitHub, plus advanced_qa.py and a dedicated GitHub Actions workflow. No longer dependent on the old chat ZIP for source.
- Executed local Chromium checks: **8/8 basic DOM/viewport cases passed** at 320, 390, 768, 1280px for neutral and expressive treatments: one heading, main landmark, labeled controls, valid hash targets, no horizontal overflow, no JS page errors, focusable selector, reduced-motion emulation.
- **Not tested:** screen readers, human participants, complete keyboard journey, WCAG conformance, independent artistic comparison. Workflow CI execution is NOT verified as passing.
- No Faneqo application code modified. Next: confirm hosted CI outcome, run exact Perception Workbench tests, and execute fair creative-quality test when authorized.
