# UX Reading Dossier 010 — Brad Frost, *Atomic Design*, Chapter 2

**Research date:** 2026-11-15. **Source:** Brad Frost, *Atomic Design* (2016), author full web edition https://atomicdesign.bradfrost.com/ . **Original chapter directly examined:** [Chapter 2, Atomic Design Methodology](https://atomicdesign.bradfrost.com/chapter-2/) from opening through template and page-level applications, including the later feedback and iterations. **Complete Chapter 2 read**, NOT complete book. Author's illustrations were listed/identified in accessible HTML; this research reviewed their descriptions and accompanying examples, not every original high-resolution figure.

## What problem is the author solving?
Design teams maintain interface pieces, page templates and actual products in separate silos. Frost proposes a way to reason from reusable controls to complex screens **without losing the page context that gives components their job**.

## Five stages, with underlying reasoning
1. **Atoms:** lowest useful UI elements, including button, input and label. The point is not chemistry literalism; it is naming primitive presentational/semantic building blocks.
2. **Molecules:** purposeful connected group of atoms; Frost illustrates a **search form** containing a label, input and action button. A label alone has a different functional role from the complete interaction.
3. **Organisms:** larger sections such as a site header combining logo, primary navigation and search. These convey context, not merely visual grouping.
4. **Templates:** page-level content structures with meaningful placeholders. Frost explicitly emphasizes characteristic image sizes and copy lengths. This sets constraints for real content, not just a beautiful empty mockup.
5. **Pages:** representative real content in the template; here the pattern system may fail under content variance, so designers revise upstream components/templates.

Crucially Frost states the stages **are not linear**. A design team can reason from the whole page back to atomic elements. This prevents a mechanical “start by drawing a button, then discover the user's actual problem” workflow.

## Source examples
- Search form's label/input/button combination is more usable as a unit than loose individually styled atoms.
- Header organism includes navigation, brand and search.
- A page with real representative media and text exposes template failures invisible when using lorem ipsum and ideal character lengths.

## What the author does NOT prove
Component taxonomy does not establish whether a user finds the right task, understands consent, or trusts the system. A brand-consistent composer can still send messages to the wrong people. The chapter is design methodology, **not comparative empirical proof** that atomic systems outperform alternatives on usability, accessibility or artistic quality. Some apps benefit from more domain-specific names than molecules/organisms.

## Specific Faneqo transfer
The current reported issue is **multiple message composition experiences** and uncertain gallery/attendee context. Shared components can eliminate mismatched styling and inconsistent behavior, but a shared *domain interaction contract* must come first:

- One **recipient-review molecule**, clearly showing recipient kind, eligible count, exclusions and privacy.
- One **attachment molecule**, exposing source gallery visibility, upload/saving state and recoverability.
- One **composer organism**, assembling draft, recipients, media, validation, submit, feedback.
- Distinct **templates** for private conversation, all-fans broadcast and Night attendee message; shared building blocks must not imply identical permissions.
- Real-content **pages** include zero eligible recipients, long artist names, 20-photo gallery, slow upload, interrupted drafts, failed send and long mobile translations.

Each layer has an independent responsibility; the app's task/permission model controls semantics.

## Cross-author tension and synthesis
Frost helps consistency through reusable parts; Keith focuses on enduring user verbs and resilient outcomes. Lynch/Horton warn that taxonomy/navigation may remain wrong despite stylistic consistency. Vignelli adds relational visual grammar, but not an argument to merge semantically different functions. Our synthesis: **task model → domain contract → shared components → real-content page checks**, with feedback loops in both directions.

## Skill transfer
- **Elite UX Director:** first produce task/state/permission map; then identify which interaction contract is reusable and which differs legitimately. Reject “consolidate screens” that sacrifices recipient clarity.
- **Creative Design Director:** use a family of coherent visual patterns, preserving distinctive content and art direction; specify visual hierarchy at page context, not only token/atom level.
- **Engineering:** after authorization, map contracts to Nuxt 3 reusable components, prove local state and API errors, avoid code duplication without false domain equivalence. This is not authorization to modify Faneqo.

## Testable questions for eventual wild use
Can an artist tell who will receive a Night message? Can a failed gallery attachment recover without losing text? Does the same “Send” pattern predict the same kind of outcome across contexts? Does long copy break template hierarchy at 320px?

**Evidence status:** ONE CHAPTER READ from original full web book; source claims and extrapolation separated; NO benchmark and NO code/test change.