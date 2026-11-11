# Research 008 — Art Direction Field Manual

**November 11, 2026 · Draft v0.1**
This is an editorial guide to *decisions*, not an aesthetic template and not a substitute for actual user research.

## The core proposition
An extraordinary digital product unifies **subject, meaning, composition, interaction, and technical medium**. When those aspects are pursued independently, the result can be decorative, generic or unusable.

## 1 — Build with a tension, not a trend
Identify a genuine tension: private/public; stage/backstage; spontaneous/structured; human/mechanical; memory/instant; silence/noise. Let it govern hierarchy, photography, motion and language.

**Grounding:** FinalFinal's studio-articulated control/chaos tension; Pentagram's long-running Public Theater identity balances stable brand grammar with campaign reinvention.

**Bad transfer:** Recreating another studio's typography and branding.
**Good transfer:** Choosing an ownable tension from the content and designing multiple interpretations of it.

## 2 — Teach the eye with a single variable
**Grounding:** Albers's original educational texts argue for observation and controlled material/color experimentation.

Take the same headline; vary scale only. Same image; vary crop only. Same accent; vary adjacent surfaces. Test perceived hierarchy before committing to a direction.

**Limitation:** Real pages have interacting variables. Isolated experiments reveal mechanisms but cannot by themselves predict overall product effectiveness.

## 3 — Let content dictate photography
The image is not a generic decoration. Specify subject, lens/vantage, light source, photographic moment, subject position, negative space for text and crop behavior. Prefer rights-cleared authentic photography.

**Reference:** Sugimoto's repeated horizon and Crewdson's constructed visual worlds are distinct lessons—restraint versus narrative staging.

**Wrong:** fake users pointing at screens or photos chosen only for brand color.
**Right:** photographs selected because they communicate something true about the subject.

## 4 — Design with an architectural section
Think of a page as a sequence of spaces: arrival, orientation, proof, exploration, decision, and resolution. Different spaces warrant different density and visual emphasis.

**Art source:** Architectural light-and-space research, to deepen through primary architecture records.
**UX source:** clear information scent and explicit calls to action.
**Check:** Can a visitor bypass the entire narrative and still act?

## 5 — Give typography two coordinated jobs
**Identity typography:** expressive, memorable, culturally located.
**Utility typography:** readable, robust, accessible, consistent in control labels and longer copy.

**Case:** Pentagram's Public Theater campaigns demonstrate a stable grammar allowing seasonal invention; current 2026 work uses hand-drawn lettering. This is not a reason to draw every button label in display lettering.

## 6 — Treat motion as editorial punctuation
Specify *why* motion exists: spatial continuity, reveal, attention, or system feedback. Animate a single meaningful transition instead of everything. Respect reduced motion. Ordinary operational UI should be immediate.

**Documented standards:** MDN prefers-reduced-motion; WCAG motion and interaction guidance.
**Risk:** large scroll-locked animations delay content and create discomfort.

## 7 — Keep a stable interaction grammar
Radical art does not require eccentric keyboard conventions. Links navigate; buttons act; dialogs manage focus; form errors aid recovery.

**Sources:** W3C APG, GOV.UK patterns and Material/Fluent/Apple system documentation.

## 8 — Separate identity from decoration
Ask, "Would this element still be here if it had no impressive animation?" If yes, it may support meaning, hierarchy or usability. If not, require an explicit narrative/expressive justification and a cost budget.

## 9 — Direct through constraints
A page's concept can be anchored by:
- One strong typographic relationship.
- One dominant image or image-treatment rule.
- A small, meaningful color system.
- A recurring spatial rhythm.
- One purposeful motion grammar.
This is an experiment framework, not a mandatory "one of everything" checklist.

## 10 — Produce alternatives before polish
Develop **three different theses**, not three colorways:
- A: editorial restraint and readable density.
- B: cinematic imagery and narrative movement.
- C: a subject-specific hybrid that challenges both.
Describe the content and UX consequences before production.

## 11 — Record failure conditions up front
Every technique has costs:
- Expressive type → narrow-screen overflow.
- Full-bleed images → crop loss, insufficient contrast.
- Glass/blur surfaces → poor text clarity, GPU cost.
- Motion → latency, discomfort, scroll interruption.
- Minimalism → missing affordances.
- Creative layouts → inaccessible reading order.

## 12 — Evaluate on independent axes
Concept specificity, visual craft, comprehension, accessibility, performance, evidence. Use the rubric in `handbook/DESIGN_ACCEPTANCE_RUBRIC.md`. Do not average them into a single false 'beauty score'.

## 13 — Respect the physical device
Mobile isn't a compressed desktop poster. Check actual reflow, thumb targets, text zoom, virtual keyboard, focus, image positions, and reduced motion. Browser support for newer scroll animation techniques must be checked.

## 14 — Design visual proof into the story
A claim without evidence is weak. Prefer screenshots of real product behavior, grounded outcomes, honest customer quotes with permission, or informative demos to vague benefit text. No fabricated UI screenshots or usage metrics.

## 15 — End with a decision, not an inspiration board
Each research session should yield:
- One or more sources examined with access status.
- A precise mechanism.
- Its applicability and counterexample.
- A proposed test or useful design choice.
- An updated repo entry and changelog.

## The practical creative director packet
For Claude (when available) provide:
1. Current product/feature reality and user goal.
2. One-sentence thesis.
3. Three competing direction outlines.
4. Source-specific art mechanisms, no style cloning.
5. Content hierarchy with real copy/imagery rights.
6. UX invariants and accessibility checks.
7. Motion and image performance budget.
8. Definition of finished and evidence to submit.
9. Areas where Claude may disagree and offer alternatives.

## Not yet proven
This manual is a **hypothesis-driven synthesis**, not a proven methodology. It will earn its authority by producing better mockups and surviving independent critique and functional tests.

## Research anchors
- [Albers original educational writing](../reading-dossiers/001-ALBERS-ART-INSTRUCTION.md)
- [Typography architecture](006-TYPOGRAPHY-AS-ARCHITECTURE.md)
- [Attention and dramatic composition](005-ARCHITECTURE-OF-ATTENTION.md)
- [Cinema and photographic language](007-CINEMATIC-IMAGE-LANGUAGE.md)
- [Apple / Material / Fluent and other systems](../design-systems/README.md)
- [Anti-generic method](../handbook/ANTI_GENERIC-DESIGN-METHOD.md)
