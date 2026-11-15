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
