# UX + Design Intelligence — Master Development Plan (Research-first, Wild-use Validation)

**Date:** 2026-11-15
**Owner directive:** Dramatically improve UX and visual design guidance for Claude. Do not run formal skill benchmarks or interrupt active Faneqo work. Put improvements into practical use as appropriate and refine from actual project feedback. No production code changes authorized by this plan.
**Relationship:** Companion implementation plan under `docs/MASTER_PRODUCT_PLAN.md`; do not supersede its approved scope, design philosophy, or safety gates.

## Purpose

Build a compact, deeply informed **UX + Art Direction + Frontend implementation** system. It should help Claude produce *understandable, safe, emotionally compelling, accessible and implementable* experiences. Faneqo is the first use case; the core skill system stays generalizable.

**Outcome:** Claude understands the human job and domain, designs the complete journey (not just a screen), composes visually distinctive design direction, uses grounded sources and correct implementation contracts, and takes responsibility for actual states, failures and recovery.

**Anti-goal:** Huge unverified book dump, faux scientific design commandments, untested superiority claims, multiple competing mega-prompts, or a second Faneqo messaging application.

## Roles and skill boundaries

1. `elite-ux-director`: tasks, mental models, information architecture, interaction journeys, affordances, error prevention and recovery, real behavior, accessibility and evaluation hypotheses.
2. `creative-design-director`: visual communication, artistic concept, editorial hierarchy, cultural authenticity, photography/typography/composition, art-direction alternatives and critique.
3. `frontend-design` and engineering: real project implementation using established patterns, component architecture, responsive behavior, accessible semantics, performance and automated feedback.
4. Context/source libraries: external referenced books, author notes, case studies, decision cards, design standards, Faneqo domain adapter and current product truth. Keep source library independent of skills.

**Rule:** One skill should orchestrate an artifact only inside its distinct role. Don't make all skills mandatory for every routine task. Prefer brief activation with selective links into deeper reference notes.

## Research tracks and study curriculum

The separate acquisition/research chat must build a verified, deduplicated book catalog (not merely a popular list) with legitimate free access prioritized. We need broad depth across:

A. Human factors and cognitive psychology — attention, perception, memory, mental models, decision-making, error, cognitive load, affordances, perceptual organization. Distinguish robust research from overgeneralized lab findings.

B. Interaction design and HCI — task modeling, feedback, signifiers, constraints, progress, transitions, error handling, expert/novice differences, mobile/touch/keyboard, information scent.

C. Information architecture/content design — navigation, classification, naming, findability, taxonomies, search and filtering, microcopy, plain language and service design.

D. Usability research — observation, interviews, usability tests, task analysis, field work, inclusive qualitative research, uncertainty, prioritization. Don't fabricate study metrics.

E. Accessibility and inclusive interaction — WCAG 2.2, WAI-ARIA APG, screen readers, cognitive accessibility, color/zoom/reflow, reduced motion, inclusive copy and error feedback. Standards are supplemental primary references, not mislabeled books.

F. Visual communication — typography, graphic design, hierarchy, editorial grids, Gestalt, layout, color, iconography and image art direction. Study authors in context; aesthetic history is not UX empirical validation.

G. Mobile/messaging and social/product systems — conversation UX, inbox and notification models, broadcast vs chat, privacy and permissions, galleries/media, upload/publishing, audience selection, retention vs dark patterns.

H. Product strategy and systems — jobs to be done, service blueprints, design systems, tradeoffs, feature discoverability, implementation reality, ethics.

I. Contemporary digital products — real interface breakdowns across strong design systems (GOV.UK, Material, Apple HIG, Adobe Spectrum, inclusive-components) using direct authoritative sources, supplemented by actual screenshots/browser review when later permitted.

## Honest source acquisition / reading policy

- Seek actual full accessible primary books in public domain, author-authorized full text, open access, libraries, and loan access. Private study does not automatically make unauthorized copies lawful. Do not ask Claude to access paywalls without permission or source pirated material.
- A bibliographic listing is **not** a book read. Use statuses: DISCOVERED, FULL TEXT VERIFIED, ACQUIRED, PARTIALLY READ [exact chapters], FULLY READ [complete text verified], NOTES VERIFIED, APPLIED and REVISITED.
- Keep author, exact edition/year, source URL, page/chapter locator, language, media format, accessibility, reading confidence, availability, and limitations. Don't conflate translation, edition, blog excerpt and whole text.
- No need to copy entire books into GitHub. Store short original synthesis, short lawful quotations, citations and external URLs; authorized source material can stay private and offline.
- Use a prioritized bibliography, not '100 books equals 100 learned'. Prefer concentrated close reading of highest-yield works and source-grounded comparison.

## Research outputs per deeply studied source

1. **Original question**: What UX/visual problem is the author addressing?
2. **Exact scope**: Chapters/pages/figures actually examined; edition/translation.
3. **Key mechanisms**: Distinguish original claims from our interpretation; cite precise locations.
4. **Counterexamples and limitations**: Context, historical assumptions, normative vs empirical claims, likely misapplication.
5. **Faneqo scenario**: One concrete application to Messages, Night, gallery privacy, audience clarity, Show Mode, onboarding or artist Headquarters.
6. **Design translation**: A concise actionable conditional guideline; avoid “always”.
7. **Failure/edge cases**: Permission boundary, interrupted workflow, cognitive/accessibility issues.
8. **Artifact**: Interaction contract, annotated diagram, decision card or visual direction (not mandatory for every source).
9. **Evidence**: Distinguish tested, observed, inferred, reported and proposed outcomes.

## Skill evolution plan (no formal tests for now)

### Phase 1 — Structural refactor
- Review current `elite-ux-director`, `creative-design-director`, project North Star, selected Matt Pocock skills and the Lab's master plan.
- Adopt composable scope and a domain glossary; keep skill entrypoint brief and references scoped to the task.
- Avoid overwriting installed Claude copies while separate agents are working. Write improved skills into Lab repo and provide explicit install/update instructions for authorized integration.

### Phase 2 — Prioritized book research
- Have dedicated research chat produce 50–100 **verified candidates** and a **top 20 reading order** weighted by full-text accessibility, primary-source quality, usability relevance, contemporary applicability and Faneqo transfer.
- Assign source reading batches by topic; maintain citations and status.
- Every batch should result in reusable insight cards, not a generic summary dump.

### Phase 3 — Deep source synthesis
- Curate ~20–30 source-backed conditional UX principles, ~10–15 visual principles and a compact set of tested-where-available interaction patterns.
- Connect principles to users, jobs, failure states and design alternatives.
- Build useful matrices: task → domain → source → behavior → visual emphasis → verification observation.
- Identify conflicts across books rather than hiding them.

### Phase 4 — Strengthen the two skills
- Improve UX skill with: task-first journey, domain vocabulary, screen/state inventory, privacy/recipient semantics, recoverability, accessibility, minimal repair vs ambitious option, evidence labels.
- Improve Creative Design skill with: narrative/artistic thesis, original references, three distinct viable concepts, hierarchy and typography guidance, authentic media treatment, responsive critiques, technical feasibility.
- Align both with project engineering skill; each has defined handoff and receives only relevant book knowledge.
- Create a small host routing guide: when to invoke which skill and how not to overwhelm Claude.

### Phase 5 — Start using in real authorized work
- Deliver versioned, source-linked skills. Install only when authorized and without disrupting active worktrees/tasks.
- Use them on real Faneqo assignments within existing scope; do not create separate fake pilots just to check a box.
- Record friction or corrections that arise naturally: what Claude misunderstood, what fixed it, what was a false promise, where visual taste conflicted with task clarity.
- **No formal benchmarking, blind comparisons, standalone testing project or founder testing demand right now.** Normal project QA remains required when actual product features are changed.

### Phase 6 — Iterate from the wild
- Every real encounter produces a small entry: symptom → likely cause → evidence → skill/reference improvement → result if known.
- Update skills based on recurring issues and source evidence; remove ineffective or redundant instructions.
- Claim 'better' only where actual project results support it; don't call the skills empirically proven 'elite' without evidence.

## Example core experience contract — Faneqo Night → Messages

User job: “Send the people from last night's show photos and a thank-you without exposing private content.”

1. Artist arrives from ended Night via explicit **Message attendees**.
2. Canonical Messages workspace preserves context; verified eligible audience and show are visible.
3. One canonical composer supports writing, authorized Night link, compatible gallery attach/create, secure visibility choices.
4. Draft survives gallery creation and recoverable failures; gallery publishing remains separate from notification.
5. Review shows accurate audience, eligibility, privacy and channel.
6. Send preserves protections, duplicate safeguards and honest queued/sent/delivered terminology.
7. Replies return to private individual threads; return-to-Night and mobile navigation coherent.

**Do not alter production Show Mode, QR behavior, fan data, recipient eligibility, billing or S3 permissions from this plan.**

## Research governance / deliverables
- Single canonical bibliography with verified links and access statuses, prioritized by next actual reading.
- Source dossiers keyed to editions/chapters and annotated citations.
- Source-to-principle ledger and decision cards.
- Versioned `elite-ux-director` and `creative-design-director` skills with slim entrypoints and modular references.
- One handoff/routing document for Claude Code; minimal Faneqo adapter.
- Incremental STATUS, ROADMAP and CHANGELOG entries. Keep research in Lab repo; no unrequested Faneqo repo mutations.

## Near-term instructions for a separate book-acquisition chat

1. Start from canonical plan and catalog above, but independently research and verify direct full-text URLs.
2. Show what is free in full and legally accessible versus excerpts/catalogs/loans, without moralizing.
3. Find 50–100 distinct candidates by categories, then prioritize top 20 with direct access links and edition details.
4. Do not claim all sources were read. First deeply study 3–5 verified accessible high-yield books/chapters and write concrete UX principles and Faneqo application examples.
5. Return results in an actionable Markdown/CSV bibliography and reading queue with provenance, accessibility and status.

## Definition of progress

Progress = genuinely studied source material + a more discriminating decision/handoff method + fewer confusing/unsafe UX proposals in real work. A large bibliography or green static checks alone is not progress.

## Field Program 001 — Live music context, personas, and situational UX (added 2026-11-15)

**Priority: essential UX research input.** Artists, bands, managers, agencies, venue collaborators and fans do not operate in a quiet, idealized office environment. Product behavior must be examined in actual music-industry contexts **before** treating a screen as intuitive. This section extends—not supersedes—the research curriculum and skill responsibilities above.

### Parallel-research coordination (important)

**Another ChatGPT chat has already been assigned and is working on the UX/design book discovery and original-text reading program.** Treat its output as an **independent workstream in progress**. Do **not** restart its assignment, create a competing catalog, overwrite its files, or infer that it has finished. The canonical books catalog belongs to that research chat until its results are handed off or reconciled.

**This workstream owns only:** music-industry domain understanding, personas, live-event ethnographic/contextual research, actor journeys, environmental constraints, situational use cases, and their traceable implications for UX. It may cite relevant books and articles, but must send proposed additions to the canonical book catalog as a **handoff list**, not mutate the book program's files in parallel. Before editing any shared file, inspect the latest version and conflicting changes; prefer append-only scoped research with named ownership.

### Research objectives

1. Understand the daily work, constraints, incentives and vocabulary of different artist types and career stages: aspiring solo artists, working local bands, touring artists, digital-first producers, artist managers, agencies, labels, content partners and fans.
2. Understand concerts from **both artist/staff and fan perspectives**, before, during and after the show; include fans who prefer not to use a phone during the performance.
3. Study contextual variables: venue size/genre, lighting and glare, noise, crowd density/mobility, connectivity and battery, one-hand use, interrupted attention, accessibility, social/privacy norms, travel, load-in, soundcheck, merch, load-out, exhaustion and follow-up time.
4. Map differences by responsibility and authority: who owns the band account, who can run Show Mode, publish a Night/gallery, authorize audience messaging, approve campaigns or see fan information.
5. Connect field insights to scenario-specific design hypotheses, **not** instant requirements or invented personas.

### Source and evidence hierarchy

- **Primary:** actual, consent-based artist/fan/crew interviews, field observations, diary reports and usability sessions when feasible.
- **Published research:** scholarly concert-experience and audience-participation studies, occupational ethnographies and artist/manager interviews with methods and source links.
- **Industry materials:** musicians' unions, touring and venue-operational guides, professional journalism and artists' first-person essays. Label promotional surveys and unrepresentative samples.
- **Inferred scenarios:** clearly marked research hypotheses until observed or verified.

Keep a source ledger with access type (**abstract-only**, article sections reviewed, full text read, interview heard, field observation completed), date, edition, limits and quotations within rights. Never claim an industry-wide prevalence from one venue or niche sample.

### Journey / contextual field map

| Moment | Artist/team provisional job | Fan provisional job | Core Faneqo UX question |
|---|---|---|---|
| Promotion / day before | Prepare show, QR and team roles | Find event, decide whether to attend | Can setup finish in advance, with clear readiness and authority? |
| Travel, load-in and soundcheck | Coordinate gear, merch, doors and set time | Travel, queue, locate accessibility info | Are essential flows reachable under fragmented attention? |
| Doors, pre-set and merch | Greet fans, confirm current show | Find friends, optionally scan/follow | Is check-in clear, fast, readable, privacy-respecting? |
| During set | Perform, limit device interaction | Listen, move, dance, photograph or avoid phone | Does software avoid demanding attention during music? |
| Immediately after | Merch, fan conversations, load-out, travel | Exit, meet friends, share memories | Can unfinished work safely resume later? |
| Next day | Review attendance, curate Night, gallery, thank-you | Revisit photos and opt into future contact | Does Night → Messages preserve context, audience and privacy? |
| Between shows | Maintain artist–fan relationship, coordinate teams | Manage communications and preferences | Are messages relevant, permission-based and manageable? |

### Persona architecture — behavior over stereotypes

Create **provisional archetypes**, with differences in goals, stage of career, touring frequency, audience scale, technology confidence, team size, permissions and device/work environment. Do not invent statistically representative names, ages, incomes or success rates. Include independent and managed artists, touring and local bands, solo/producer profiles, managers, agencies, label teams, limited-access collaborators, casual fans and highly engaged fans. One persona is not one UI theme.

For each persona capture: jobs-to-be-done; decisions and authority; task cadence; collaborators; pressures/interruptions; current tools; workarounds; privacy and consent expectations; accessibility/environment constraints; evidence; unknowns; example scenarios and what would falsify our assumptions.

### Scenario cards — initial *hypotheses*, not validated findings

- **SC-01 Solo artist, before doors:** Artist has competing soundcheck/merch/venue tasks. Can confirm existing QR/Show Mode is ready without entering a long setup?
- **SC-02 Local band at merch after the set:** A fan has seconds to engage. Can existing artist Headquarters/check-in convey clear value with minimal interaction?
- **SC-03 Fan in crowded, dim venue:** Can they follow/check in with accessible contrast, explicit consent and graceful interruption recovery?
- **SC-04 Attentive fan not using their phone during music:** Can they reconnect afterward without coercive in-show phone prompts?
- **SC-05 Touring manager with successive Nights:** Can they identify the active artist/show correctly and avoid messaging the wrong audience?
- **SC-06 Artist next morning:** Can they create a gallery and send to **eligible** Night attendees without losing draft, exposing private media or overstating delivery?
- **SC-07 Fan with accessibility barriers:** Are alternative discovery/participation paths available for visual, motor, hearing or cognitive needs?
- **SC-08 Multi-artist agency operator:** Are switching, authorization, approvals and account separation safe and understandable?

Every scenario should include: actor and purpose; precise venue/device/lighting/connectivity assumptions; entry point; action steps; interruption/failure; privacy/permission consequence; successful outcome; **what research would validate/reject it**. Avoid silently transforming hypotheses into Faneqo commitments.

### Skill interface and deliverables

Provide `music-industry-research/` as a clearly scoped optional evidence library, not a massive mandatory skill prompt. Create original source-grounded field dossiers, `PERSONA_INDEX.md`, `SHOW_JOURNEYS.md`, `SCENARIO_CARDS.md`, `CONTEXT_CONSTRAINTS.md` and `EVIDENCE_GAPS.md` if they do not already exist; prefer reuse of established repo conventions. Connect only relevant persona and scenario cards into `elite-ux-director` through its existing Faneqo adapter. The core UX skill must remain domain-neutral.

Claude UX deliverables must state: **persona + user job + venue/time context + likely interruptions + constraints + consent and permissions + resulting journey + observed vs assumed evidence**. A stylish desktop mockup is not proof an artist can complete the task backstage or a fan can scan at the venue.

**No formal skill benchmarks or extra founder testing obligations now.** Record findings and let subsequent authorized real Faneqo work reveal flaws naturally. Normal feature QA remains mandatory. Do not interrupt the book-research chat or current development agents, and do not edit production.


---

## Architecture Increment 002 — Progressive Disclosure, Source Intelligence & Independent Quality (2026-11-15)

**Status:** implemented in isolated `feature/elite-ux-director-v0-3-research-driven` branch, subject to package CI and merge confirmation; not installed in active Claude/Faneqo environments. **This is an incremental upgrade of this plan, NOT a restart or competing skill.** Prior Field Program 001, separate music-industry research and separate book acquisition remain intact.

### External technical references audited
- Anthropic [Claude Code Skills](https://code.claude.com/docs/en/skills): activation metadata, on-demand references, context compaction, skill location/precedence and independent evaluation.
- [Agent Skills standard](https://agentskills.io/specification): name/description constraints, three-level disclosure and shallow bundled resources.
- Anthropic [Effective Context Engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents): minimum high-signal context, selective retrieval.
- Anthropic [Writing Effective Tools for Agents](https://www.anthropic.com/research/writing-tools-for-agents): small clear tool boundaries, useful concise outputs and evidence-driven optimization.
- Anthropic [Demystifying Evals](https://www.anthropic.com/research/demystifying-evals-for-ai-agents): task/trial/outcome separation and independent grading.
- Matt Pocock Skills for Real Engineers, reviewed in `research/012-AGENT-SKILLS-UX-ARCHITECTURE.md`: small composable tasks, domain modeling and public-seam verification.

See [technical architecture audit](UX_SKILL_ARCHITECTURE_AUDIT_2026-11-15.md) for original-scope review and detailed tradeoffs.

### Adopted decisions and high-impact modules
1. **General skill core:** `skills/elite-ux-director/SKILL.md` remains a short, reusable reasoning protocol; activates on real UX ambiguity, not style-only/backend-only/deployment.
2. **Progressive disclosure:** name/description always available; skill algorithm on activation; source router, cards, patterns and review templates only on need. One-card deterministic retrieval available without embedding full source documents.
3. **Knowledge organization:** nine conditional evidence-linked decision cards, nine interaction contracts (including QR and asynchronous state), source ledger with exact original reading limits, no fabricated book knowledge.
4. **Persona epistemology:** actor context/permissions over invented demographic stereotypes; separate reported testimony, verified field study, founder claims, product code and provisional scenarios.
5. **Independent quality strategy:** detection of skill activation and correctness of *output* are different; prepare positive/negative fixtures and reviewer rubric, but do **not** initiate formal benchmark now. Use normal product QA and natural issue outcomes. Actual benchmark effectiveness remains UNKNOWN.
6. **Strict domain boundary:** Faneqo-specific messaging/QR/real-case docs moved to `domain-adapters/faneqo/`, outside reusable skill install. Faneqo personas and environment research remain a separate scoped workstream; consume it later with provenance rather than overwrite.
7. **Long-term maintenance:** package checker, GitHub Actions gate, version/rollback instructions, source confidence and field feedback log; delete rules that do not improve real outcomes.

### What is preserved
Master Product Plan's Understand → Research → Thesis → Concepts → Handoff → Implementation → Evidence → Critique cycle; existing two-role architecture (UX and Creative Design); official frontend-design implementation responsibilities; original reading dossiers; issue rubric; Faneqo adapter; real-world field program; no formal benchmarks directive.

### Release and installation gate
A newer git commit is **not** the same as Claude having learned it. A safe install/reinstall notice must identify:
- exact commit/release on main;
- verified package integrity and correct frontmatter;
- path to all required reference files;
- discovery/precedence across Windows, WSL, project and personal installations;
- rollback backup;
- separate optional Faneqo domain adapter;
- explicit limitation: improvements to structure and source access may be substantial, **but effectiveness needs observations**.

### Next high-leverage work (without disrupting current Faneqo development)
- Use the upgrade in already-authorized Faneqo UX work after deliberate install; do not force a fake showcase.
- Record actual wrong/unsafe guidance, missing domain context and surprising user behavior; do not just aggregate positive testimonials.
- Incorporate field-persona research as project-specific evidence and keep generic UX core untouched.
- Enrich select HCI chapter reading on error and risk, dialogue, navigation and cognition; update only the cards that benefit.
- At a suitable later point, independently compare activation and output quality against baseline (owner defers controlled benchmarks now). No claim of proven UX excellence until supported.


## Architecture Increment 003 — Public Homepage Experience Intelligence (2026-11-15)

**Goal:** strengthen the existing universal UX skill for a coming Faneqo homepage project **without** converting it into an art-direction/visual implementation mega-skill or interrupting operational UX development. Earlier research, approved North Star, v0.3 cards, personas and field work remain intact.

### Added capability
- `elite-ux-director` v0.4 includes homepage/landing-page activation in frontmatter and a short conditional routing note in the core algorithm. It does **not** autoload all sources or redesign pages by default.
- `references/HOMEPAGE_INTELLIGENCE.md` has eight on-demand conditional H01–H08 decision cards: product comprehension, audience-job hierarchy, credible proof, skippable narrative, truthful CTA destinations, cinematic performance/accessibility, independent evaluation and approved visual identity.
- `scripts/retrieve.py homepage H01` retrieves exactly one H-card (or manually open that section when Python unavailable). Core C01–C09 and interaction P1–P9 are preserved.
- `templates/HOMEPAGE_UX_PACKET.md` records actual evidence, first-view value, real routes, narrative sequence, accessibility/performance risks, UX-versus-art-direction decision boundaries and independent critique. The Creative Design Director still owns the three visual theses; frontend-design and Nuxt engineering still own implementation.
- `domain-adapters/faneqo/HOMEPAGE_EXPERIENCE.md` stores **separately** verified current GitHub `musicbizqr` homepage architecture and design doctrine, plus clear unknowns and precise review tasks. It is not installed as a universal reference.
- The quality fixture set now includes homepage-specific positive/negative activation and synthetic performance/first-view/truth/CTA scenarios, marked **NOT RUN**. Static package CI checks retrieval IDs and paths, not actual UX effectiveness.

### Genuine research input and limits
- Original NN/g 2024 homepage principles, NN/g Nielsen 2002 historical homepage guidance, current Google Core Web Vitals/web.dev, W3C WCAG2.2 movement/carousels, and a 2026 Baymard *e-commerce-only* comparator. Links, exact scope and caution recorded inside `HOMEPAGE_INTELLIGENCE.md`.
- These sources guide **questions and conditional recommendations**, but cannot establish Faneqo's actual visitor comprehension, signup conversion or any before/after gain. No human or model tests were run.
- Existing Faneqo doctrine protects approved opening/brand and 390px priority. Current deployed app, business proposition, eligibility, billing and conversion paths require live review at execution time. The 2026-09-09 current-phase file is not necessarily current.

### Next real-product use
1. Complete the current Show Mode/Night/Messages assignment first; do not change an active worktree for a research update.
2. Reinstall the full v0.4 *personal* skill after a safe backup, and copy the separate updated Faneqo domain adapter to the known project-only folder, keeping universal and product intelligence separate.
3. For the homepage, inspect current routes, CTA destinations, copy/FAQ/legal claims, approved compositions and actual 390/320px screenshots. UX Director makes evidence-first UX contract; Creative Design Director develops three distinct concepts only for open decisions; frontend-design/engineer implements a permissioned sandbox; independent critic evaluates rendered output and task journeys.
4. Use natural Faneqo evidence to revise H-cards; do not claim a structural package check proves a UX win. Keep production/merge safeguards and human final approval.

### Source standards
Research references: `skills/elite-ux-director/references/HOMEPAGE_INTELLIGENCE.md`. Product adapter: `domain-adapters/faneqo/HOMEPAGE_EXPERIENCE.md`. Versioned installation details: `docs/ELITE_UX_DIRECTOR_V04_RELEASE.md`.


## Architecture Increment 004 — Book-to-Design Intelligence (2026-11-15)

**Direction:** preserve Elite UX Director v0.4 task-first discipline, Faneqo separation, public-homepage intelligence and prior research. Extend the skill's **ability to study, verify, selectively retrieve and apply original design literature**. This is not a restart, mass PDF ingestion, claim to retrain model weights, permission to modify Faneqo production, or a mandatory research detour for every UX bug.

### Source intake and measurable scope
- Founder supplied a 861-line Book-to-Design study protocol, an 82-book/40-reference research canon and its 122-row CSV manifest. Originals archived unchanged under `sources/intake/2026-11-15/`. **All 122 CSV rows are not-ingested**; do not claim they were read/acquired merely because indexed.
- Historical Mission 001 library remains 130 candidates: 27 full-text access entries, 103 bibliographic research leads. Candidate lists overlap. `scripts/reconcile_ux_book_canon.py` suggests matched and unresolved editions without auto-promoting them. First pass found 40 normalized matches and 42 remaining needing title/edition review; **NOT a claim of 42 unique books**.
- Three source-complete online works newly studied at **bounded** scope: Dow *Composition* 1914 ninth ed. (opening chapters), Covert *How to Make Sense of Any Mess* (selected pages), Chimero *The Shape of Design* (Chapters 1–3). Four dossiers 013–016 including an evidence-limited image fragment study. Ten additional publisher/authority-verified commercial bibliography leads, **not read or downloaded**; see `sources/BOOK_CANON_RECONCILIATION_2026-11-15.md`.

### Engine architecture / conditions
1. **Identity / rights:** exact book, author, edition, language/translation, figure, complete vs partial, source location, reuse rights, and status independent of content acquisition.
2. **Real reading:** whole-book structure first, relevant chapters in context, author argument vs evidence vs inference, counterexamples, real visual inspection and incomplete labels.
3. **Knowledge translation:** one conditional claim per K-card with trigger, source anchor, evidence class, application limits, counterexample, falsification, maturity.
4. **Interdisciplinary synthesis:** compare actual read sections, identify legitimate conflict and choose conditional resolution; never manufacture scientific agreement among design philosophers.
5. **Selective retrieval:** a small 88-line main `SKILL.md` delegates to optional `RESEARCH_INDEX`, **K01–K09**, study/visual/schema/synthesis protocols. CLI supports `knowledge K03` and short keyword ID suggestions, no embeddings/network/running models. Normally load no more than two cards total. Existing C/P/H retrieval preserved.
6. **Critical quality:** generated/synthetic persona != observed person; index != read; author philosophy != verified user success; cropped photograph != full illustration; structured lint != UX performance.
7. **Evidence/update loop:** actual UX task, real screenshots/user work, independent critique and documented failures may revise/retire cards. **Formal skill benchmarks remain deferred**; future fixtures now 26 activation and 16 quality, NOT RUN.
8. **Core/adapter boundary:** Faneqo-specific persons/culture/product truth remain `domain-adapters/faneqo/`, while book-study methods stay universal; Creative Design Director still owns art theses and frontend-design builds.

### Quality and release gates
- Python standard-library package checker verifies main YAML metadata and paths, all K01–K09, H01–H08, C01–C09, P1–P9, bounded selection, catalog rows/status, no Faneqo adapter in the personal skill. Lightweight read-only script suited to 8 GB laptop.
- GitHub CI must pass for exact release head. v0.5 is merged to `main` only after checker success. This structural check never certifies performance or user-facing superiority.
- Personal Windows installation is an explicit separate operation with backup, skill-source precedence, version check, and rollback, described in `docs/ELITE_UX_DIRECTOR_V05_RELEASE.md`. No surprise overwrite of an active Claude mission.

### Next evidence-driven work
- Deepen complete visuals/edition analysis for Dow and modern typography/graphic design works, study authorized sections of Goodwin, Jarrett/Gaffney and content design where relevant, and consult current W3C / HCI sources before implementation claims.
- Apply selectively during the next homepage assignment: resolve visitor purpose (Covert/Chimero), choose meaningful composition (Dow/Vignelli), test actual comprehension and accessible page navigation; never replace established Faneqo North Star with a generic marketing page.
- Track both successful and **failed** case decisions. The objective is reliably better experiences, not the number of K-cards.

## Art Direction Program 002 — Masterpiece-Level Visual Communication (added 2026-11-15)

**Creative ambition:** original, emotionally resonant, technically crafted interfaces informed by great painting, graphic design, photography, cinematography, architecture, music culture and contemporary digital art. “Mona Lisa interfaces” is the aspiration for craft, depth and coherence—not a claim that any UI can be objectively certified as a masterpiece.

**Canonical art program:** [research/013-MASTERPIECE-ART-DIRECTION-PROGRAM.md](../research/013-MASTERPIECE-ART-DIRECTION-PROGRAM.md). That file defines source portals, six art disciplines, visual dossier schema, source-to-concept exercises, art-direction grammar, and proposed enhancements for creative-design-director.

### Ownership and coordination
- The **other research chat** is already building the canonical UX/design bibliography and obtaining free full texts. **Do not interrupt, restart or duplicate its work.** Send art-book candidates as a handoff for deduplication.
- The **music-industry field research** stream owns persona and live-venue contexts.
- This **art-direction workstream** owns close inspection of actual artworks, digital artistic references, creative theses, composition experiments, visual grammar, and creative-design-director skill upgrades.
- The shared Lab master plan remains canonical; do not create a parallel master plan or a competing art-direction mega-skill.

### Near-term priorities
1. Build deeply inspected artwork dossiers with originals and object-level context (not keyword-based “style inspiration”).
2. Expand art-direction sources using the Getty Research Portal, MetPublications, museums, archives, authentic music photography and verified artist/designer statements.
3. Translate lessons into **conditional, original composition principles**; reject imitation and pseudoscientific proportion myths.
4. Refactor the existing Creative Design Director references into small, composable on-demand disciplines: composition, expressive typography, authentic music imagery, visual storytelling/sequence, art direction critique.
5. Make three conceptually different directions with responsive art-direction specs for authorized product projects.
6. Let real Faneqo work exercise the skill organically; no separate formal benchmark or interruptions of active Claude tasks.

### Two output modes
- **Expressive:** public Headquarters, marketing, artist imagery, Night memory experience, magazine advertising—high visual emotion within clear action hierarchy.
- **Utility:** Messages, campaign review, dashboards, permissions—restrained artistic identity, excellent readability, state clarity, and focused interactions.

**Both modes require original expression and verified project truth, appropriate accessibility and honest visual evidence.**


## Architecture Increment 005 — Masterpiece Atlas and Art Direction Bridge (2026-11-15)
An accompanying handoff requests a **v5.0-compatible** upgrade to artistic knowledge, not a restart or downgrade. The actual v5.0 skill source has not been located from the available GitHub branches; see `docs/V5_ART_DIRECTION_INTEGRATION_AUDIT.md`. Therefore this increment **adds** a reusable Masterpiece Atlas and art-direction decision engine while leaving existing older skill entrypoints untouched.

- Eight source-verified first-pass artwork/design/photography/architecture/music visual studies: `visual-library/masterpiece-atlas/studies/MA-001..MA-008`, status PREVIEW_OBSERVED + source/creator context read; **no complete original figure coverage or test outcome claims**. Rights/source links remain on museum/creator sites, no third-party pixels committed.
- Selective, low-cost retrieval via `python scripts/query_masterpiece_atlas.py search "typography"` and `show MA-004`; no embeddings, API fees, background jobs or heavy RAM usage. Optional knowledge only, not an always-on master prompt.
- `handbook/MASTERPIECE_ART_DIRECTION_DECISIONS.md`: AD01–AD08 conditional visual reasoning, counterexamples, 2 coherent expressive/utility modes, three genuinely distinct concept premises and independent critique. `templates/MASTERPIECE_DIRECTION_PACKET.md` gives an implementation-neutral artifact.
- `domain-adapters/faneqo/MASTERPIECE_ART_DIRECTION.md` contains only project-specific examples; current real app/approved areas must be inspected at use time. No artist assets, pricing claims or Faneqo app behavior invented as facts.
- Structural validation `scripts/check_masterpiece_atlas.py` with GitHub Actions; actual effect on Claude v5.0 or user outcomes **not tested**, owner continues to defer formal standalone benchmarks.
- `research/014-MASTERPIECE_VISUAL_INTELLIGENCE_IMPLEMENTATION.md` documents sources, book acquisition recommendations (not new parallel bibliography), remaining original-figure/film/digital browser gaps and next study order.

**Future v5 integration:** inspect the actual v5 checkout and feature set, then point to this **additive** Atlas rather than swapping in any older alpha skill. Do not clone artwork, generate synthetic testimonials, force scroll animations, or violate keyboard/motion/permission invariants to make a UI look painterly.
