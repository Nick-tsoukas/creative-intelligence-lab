# Creative Brief — Signal Archive

**Owner/approver:** user (pending)
**Project:** Invented sandbox for the Creative Intelligence Lab only
**Prepared:** 2026-11-11
**Status:** RESEARCH / CONCEPT EXERCISE — not approved implementation

## User and essential task
Audience: curious urban walkers, field-recording enthusiasts, and students of sound.
Job: discover an interesting recording by place, time or atmosphere, preview it, and save a **local mock favorite** (no account required).
Users should understand within five seconds that they are browsing and listening to an archive of field recordings.

## Content model
At least six fictional recordings:
- Night Rain / Chicago / Rain / 00:46
- Early Market / Lisbon / Human activity / 01:22
- Forest Before Sunrise / Kyoto / Nature / 00:58
- Ferry Terminal / Helsinki / Mechanical / 01:15
- Wind Through Grass / Plains / Nature / 00:39
- Summer Station / Berlin / Transit / 01:04
Place names are fictional descriptors for sample recordings; no real audio rights implied. Use generated **original** audio only if explicitly authorized, or a clearly labeled non-playing preview mock rather than fake playback.

## Functional contract
1. Search by title and place.
2. Filter by category: All / Nature / Human / Mechanical / Weather / Transit.
3. Show results count, an empty state and a clear reset.
4. Show recording title, location, duration, category and preview affordance.
5. Favorite toggle communicates state to all input modes; may be session-only.
6. Include a clear description of what the archive is, and an always-present path to browse.

## Constraints
- Mobile-first and usable at 320px CSS width and 200% text scaling in applicable contexts.
- Keyboard order and visible focus.
- Semantic controls and explicit states; no hover-only actions.
- Respect prefers-reduced-motion; no autoplay, no unwanted sound.
- Browser-native web technologies or Nuxt 3 sandbox if environment allows; no dependency bloat.
- Keep all data fictional and avoid copyrighted real recordings or imagery.
- Do not modify Faneqo repositories or deploy.

## Artistic objectives
Create the feeling of **listening as discovery**. The design should evoke atmosphere and memory, without sacrificing fast catalog search.

## Research anchors and things NOT to imitate
- [Vermeer / edited attention](../../research/005-ARCHITECTURE-OF-ATTENTION.md): concentrated focal attention. Don't mimic his paintings.
- [Scher / expressive institutional typography](../../research/006-TYPOGRAPHY-AS-ARCHITECTURE.md): identity can vary around consistent underlying utility. Don't copy Public Theater letterforms or composition.
- [Linear / restrained work interfaces](../../case-studies/digital/003-linear-2026.md): task hierarchy and quiet chrome. Don't copy proprietary UI.
- [GOV.UK forms](../../case-studies/digital/004-govuk-components.md): clear labels and error recovery.

## Success criteria and failure signals
Visual concept is clearly connected to field recordings; search/filter/favorites work; no misleading audio button; alternative directions look substantially different. A gorgeous hero with hidden browsing is failure. Any measured UX or performance claims require recorded tests.
