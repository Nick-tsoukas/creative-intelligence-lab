# Task-to-Source Router — Elite UX Director — optional research router (v0.6 integration; v0.4 source map preserved)

**Purpose:** select a *small, directly relevant* evidence packet for an actual user task. This is an index, not a bibliography to paste into Claude's working context. Linked scholarly notes are stored separately in the Lab's `reading-dossiers/`; each local entry below is self-contained if only the installed skill is available.

For routine implementation start with the compact SKILL.md, not this research map. If sibling creative/frontend skills are absent, use the core visual pass plus VISUAL_CRAFT_AND_MEMORY.md and DESIGN_TO_CODE.md; no model handoff is required.

## Selection policy
1. Read the active app's actual code and product contract first where possible. This reference library cannot tell you what is currently deployed.
2. Classify primary uncertainty: **user job**, **information architecture**, **state/permissions**, **discoverability**, **visual meaning**, **technical implementation**, or **quality evidence**.
3. Load **at most two decision cards** from `DECISION_CARDS.md` and **one task pattern** from `INTERACTION_PATTERNS.md`; pull another original source only when it changes an actual decision.
4. Cite primary chapter/page/article when a claim depends on a source; label the application as interpretation. Do not re-label an article as a full book.
5. If it is routine code/CSS implementation, defer to engineering or frontend-design; do not invent a UX mission.

| Reported user problem | Diagnose first | Card(s) | Pattern / specialized reference | Source anchor |
|---|---|---|---|---|
| “I don't know where to do this” | Entry point, expected label, user vocabulary, navigation | C01 + C02 | P1 Task-oriented journey | HCI (2025) Ch 3, Lynch/Horton Ch 4 |
| “These two screens are completely different” | Actual semantics, state ownership, competing implementations | C03 + C04 | P2 Multi-entry canonical flow | Frost Ch 2, Keith Ch 6 |
| “It says sent, but nothing arrives” | Actual job queue / delivery state / API responses | C05 + C06 | P3 Consequential submission | Keith Ch 5; status-message W3C reference |
| “The gallery became public” | Published vs shared vs permission, actor authority | C04 + C07 | P4 Media/visibility lifecycle | Costanza-Chock participatory chapter; HCI safety topic *queued* |
| “The QR won't download / scan / edit” | Asset generation, scannability, target integrity and scan route | C02 + C06 | P5 QR lifecycle | HCI Ch3; QR domain adapter; technical standard **must be verified separately** |
| “Users leave the form” | Comprehension, errors, state persistence, focus | C01 + C06 | P6 Forms, failures and recovery | Boulton Ch 7–8; WCAG 2.2 (current primary standard) |
| “Fans can't follow during a show” | Physical environment, attention, permission, connectivity | C08 + C07 | P7 Situated mobile task | Design Justice chapter; HCI Ch3; field evidence needed |
| “Visitors don't understand our homepage” | First-view product purpose, priority audience, real proof, primary action and destination | H01 + H05 (selective) | [Homepage Intelligence](HOMEPAGE_INTELLIGENCE.md), [UX packet](../templates/HOMEPAGE_UX_PACKET.md); Creative Design Director for art thesis | NN/g Wang 2024; real route/content check |
| “Our cinematic homepage is gorgeous but confusing” | Narrative legibility, real evidence, skip/reduced-motion and mobile speed | H03 + H04 or H06 | Homepage Intelligence; creative-design-director and frontend-design only for their roles | NN/g Wang; W3C motion; Google Web Vitals |
| “This dashboard looks generic” | Is the actual problem UX or creative direction? | C02 + C09 | Route to creative-design-director if visual thesis | Vignelli Semantics/Syntactics; Boulton Hierarchy |
| “A screen reader can't use the dialog/tabs” | Keyboard interaction, focus, role/behavior mismatch | C06 + C08 | P8 Accessible interaction | W3C APG dialog/tabs and WCAG 2.2 |
| “What would an agency manager do?” | Decision authority, multiple teams, competing actor jobs | C07 + C08 | P9 Multi-actor permissions | Participatory design (read); project adapter if relevant |

**Homepage source boundary:** `HOMEPAGE_INTELLIGENCE.md` includes practitioner articles and standards reviewed 2026-11-15; these are **not books** or validated effects on a specific page. Baymard ecommerce research is a retail category-navigation comparator, not evidence about startup acquisition or Faneqo visitors.

**Source-evidence boundary:** `sources/UX_DESIGN_BOOK_CATALOG_2026-11-15.md` has 130 candidates but 103 are **unverified** leads; it is an acquisition queue, NOT 130 learned books. `reading-dossiers/008–012` are **section-scoped**. `skills/elite-ux-director/references/SOURCE_LEDGER.md` records earlier reading of Keith, Lynch/Horton, Boulton, Pickering article examples and Nielsen articles. Do not cite unread candidate books as studied evidence.

## External authoritative standards (not books)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): inspect relevant success criteria; actual conformance requires real evidence, not prompts.
- [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/understanding/): explanatory non-normative guidance.
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/): patterns including dialog, tabs, menu; implement only pattern that matches the real interaction; check support.
- [GOV.UK Design System](https://design-system.service.gov.uk/): authoritative field-tested component guidance in government context, not universally appropriate.
- [NN/g Homepage Design 5 Principles](https://www.nngroup.com/articles/homepage-design-principles/): 2024 original article covering comprehension, content/examples, navigation, prioritized action and simplicity; distinguish practitioner guidance from product-tested success.
- [Google Core Web Vitals](https://web.dev/articles/vitals): performance standards, not measurements of a particular homepage.
- [Nielsen's 10 Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/): heuristic lens, not participant evidence.

## Source provenance
- HCI: Hornbæk, Kristensson and Oulasvirta, *Introduction to Human-Computer Interaction* (OUP, 2025), selected Chapter 3 passages, PDF on coauthor site https://pokristensson.com/pubs/IntroductionToHumanComputerInteraction.pdf . `reading-dossiers/008-HCI-2025-PERCEPTION.md`.
- Lynch/Horton: *Web Style Guide*, 4th ed., online Chapters 4 and selected 7, https://www.webstyleguide.com/ ; `reading-dossiers/007-UX-TASKS-ARCHITECTURE-RESILIENCE.md`.
- Keith: *Resilient Web Design*, author-hosted full text; Chapters 5–6 examined, https://resilientwebdesign.com/ .
- Frost: *Atomic Design* (2016), Chapter 2 examined, https://atomicdesign.bradfrost.com/chapter-2/ ; `reading-dossiers/010-FROST-ATOMIC-DESIGN-METHODOLOGY.md`.
- Costanza-Chock: *Design Justice* (MIT Press, 2020), selected chapter sections, https://designjustice.mitpress.mit.edu/pub/cfohnud7/release/4 ; `reading-dossiers/011-COSTANZA-CHOCK-PARTICIPATORY-DESIGN.md`.
- Vignelli: *The Vignelli Canon* (2009), selected PDF spreads at RIT Vignelli Center; `reading-dossiers/009-VIGNELLI-CANON-SEMANTICS-AND-GRID.md`.
- Boulton: *Designing for the Web*, author-hosted chapters 7, 8, 13, https://designingfortheweb.co.uk/ .
- Pickering: free [Notifications](https://inclusive-components.design/notifications/) and [Tabbed Interfaces](https://inclusive-components.design/tabbed-interfaces/) articles, **not** the separately sold book.
