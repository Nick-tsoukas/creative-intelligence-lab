# UX Reading Dossier 001 — Tasks, Information Architecture, and Resilient Interaction

**Date:** 2026-11-14. **Status:** ORIGINAL BOOK CHAPTERS DIRECTLY READ, NOT COMPLETE BOOKS. Sources: three author/publisher-hosted books and an author-hosted interface pattern series, plus NN/g's usability heuristics. This dossier preserves distinctions between author claims, interpretive transfer and evidence from Faneqo.

## Book A — Jeremy Keith, *Resilient Web Design*

**Author's complete book:** https://resilientwebdesign.com/  
**Scope studied:** [Chapter 5, Layers](https://resilientwebdesign.com/chapter5/), and [Chapter 6, Steps](https://resilientwebdesign.com/chapter6/). Author site's license: CC BY-SA 4.0. **Other chapters not studied in this pass.**

### Chapter 5: layering enables *different* capable experiences
The crucial layer is meaningful HTML: the web's structure/content should make sense before enhancement. CSS and JS can add expression and accelerated interaction, but should not turn the experience into an inaccessible all-or-nothing widget. Keith rejects the expectation that identical pixel layouts are universal. Enhancement depends on real capabilities rather than fragile browser assumptions.

**Transfer, not original claim about Faneqo:** first define a truthful accessible message and recipient review; only afterward enhance with inline gallery creation, toast notices and sophisticated mobile transitions. Don't assert a Nuxt/Strapi flow works with all JS disabled without engineering evidence.

**Counterexample:** live chat, image upload and fan messaging legitimately require dynamic behavior; “progressive enhancement” is not an excuse for 1990s interactions.

### Chapter 6: meaningful verbs underneath interaction mechanics
Keith explicitly studies social communication: the user's goal is communicating with others, not using Ajax or tapping forms. Start with the core action and add technological enhancements that do not break it.

**Faneqo UX design hypothesis:** Artist's natural-language goal: “Send last night's photos to people who came.” This should structure UI labels and context inheritance rather than “create campaign + attach gallery entity + select segment.”

**Falsifiable task:** Present an ended Night with CTA “Message attendees.” Ask first-time artist to message only eligible attendees, attach a gallery and explain who sees the photos. Observe backtracking, mistakes and privacy comprehension.

## Book B — Patrick J. Lynch / Sarah Horton, *Web Style Guide* (4th ed.)

**Author/publisher full online TOC:** https://www.webstyleguide.com/  
**Scope studied:** [Chapter 4, Information Architecture](https://www.webstyleguide.com/4-information-architecture.html) and selected [Chapter 7, Interface Design](https://www.webstyleguide.com/7-interface-design.html). Complete book NOT read.

### Chapter 4: taxonomy and controlled vocabulary *are* the experience
The chapter calls for content inventory, consistent vocabularies, hierarchy, navigation conventions and qualitative testing with representative people. It warns that visual polish alone cannot fix broken underlying conceptual organization.

**Our application:** public Night, gallery visibility, campaign audience, private conversation, fan request, Sent history and raw attendance are different domain concepts. A coherent workspace can connect them, but labels and visual presentation must remain honest.

**Counterexample:** unifying surfaces is not always good: combining a campaign's delivery status into a private conversation may create harmful ambiguity. Preserve semantic distinctions while reducing navigational friction.

### Chapter 7: consistency, orientation, feedback
Interface cohesion gives a user confidence about location and options. Reliability matters as much as visual identity. Beware of older numerical performance and mobile adoption statistics present in the text; they are historical examples, not current performance thresholds.

**Transfer:** the sidebar should express selected thread and unread status, the panel should show context, and the composer should confirm the current audience. Avoid silent failure and hidden drafts.

## Book C — Mark Boulton, *Designing for the Web*

**Author's free book and formats:** https://designingfortheweb.co.uk/  
**Scope studied:** [Chapter 7 The Brief](https://designingfortheweb.co.uk/part2/chapter7/), [Chapter 8 Research](https://designingfortheweb.co.uk/part2/chapter8/), [Chapter 13 Hierarchy](https://designingfortheweb.co.uk/part3/chapter13/). Whole book not read; CC BY-NC-ND 4.0 (do not repost adapted book content).

### Chapter 7: a brief must not smuggle the answer
Boulton distinguishes client, technical, creative and idea briefs, and criticizes briefs too vague or too prescriptive. A usable problem statement creates room for appropriate solutions.

**Faneqo transfer:** “artist loses draft when adding show gallery” is a problem; “use a 500px drawer with three tabs” is an implementation assumption to validate.

### Chapter 8: research must result in decisions
Boulton differentiates stakeholder/product research, primary vs secondary inputs, qualitative vs quantitative user evidence, and visual research. The goal is useful insight and ideation, not an unexamined collection of references.

**Faneqo transfer:** screenshot-derived critique can establish that a screen has large empty space; it cannot establish that every musician wants more action cards. Test desired action and discoverability.

### Chapter 13: hierarchy via visual weight and type
The original chapter emphasizes typographic scale, weight and contrast. Use relationships to distinguish what should be read first, but do NOT transplant a historical 11px body font example into current mobile UX. Small text can be aesthetically neat and still unusable.

**Experiment:** compare screenshot and first-click comprehension of 'Message attendees', 'Message all fans' and 'New private conversation'; prioritize distinction of intent over visual brightness.

## Accessibility companion — Heydon Pickering, *Inclusive Components* author articles

**Not the separately sold book:** https://inclusive-components.design/ ; full updated book NOT read.
**Articles studied:** [Notifications](https://inclusive-components.design/notifications/) and [Tabbed Interfaces](https://inclusive-components.design/tabbed-interfaces/).

- A notification with no action should not steal focus.
- Real-time chats require selective announcements, not an exhausting stream of live updates.
- Color alone cannot be the only differentiator for statuses.
- Tabs are a keyboard and screen-reader interaction model, not just an underline on unrelated routes.

**Faneqo application:** distinguish whether Inbox/Sent are router destinations or in-place tab panels; implement appropriate semantics instead of adding roles blindly. Do not force the keyboard focus to a “message sent” toast. Test incoming message update behavior with actual AT, if available.

## Nielsen Norman Group — heuristic context, not a read book
Read 10 usability heuristics and heuristic evaluation guidance: https://www.nngroup.com/articles/ten-usability-heuristics/ ; https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/ . Heuristics are diagnosis aids. A heuristic violation is **not automatically measured evidence** that a real user fails.

## Cross-source synthesis — seven operational rules

1. **Name the human outcome before designing steps.** Keith Ch. 6, Boulton Ch. 7.
2. **Make the taxonomy honest and familiar.** Lynch/Horton Ch. 4.
3. **Preserve core outcomes through enhancement and failures.** Keith Ch. 5.
4. **Don't let a beautiful surface disguise a broken model.** Lynch/Horton Ch. 4; Boulton Ch. 13.
5. **Communicate states without disruptive focus or announcement noise.** Pickering Notifications.
6. **Tabs are semantics and keyboard behavior, not merely styling.** Pickering Tabbed Interfaces.
7. **Distinguish observed friction from expert predictions.** Boulton Ch. 8; NN/g heuristics.

## Design experiment to run

**User:** working musician, limited time after a show.  
**Task:** share a Night gallery to verified eligible attendees, check send state and respond privately to one fan.  
**Setup:** correct test permissions, synthetic attendees and galleries, one cancelled upload and one failed send; no production delivery.  
**Compare:** Current layout vs proposed unified Messages.  
**Capture:** initial comprehension, wrong-recipient concern, required steps, backtracking, lost-state incidents, misunderstood visibility and retry behavior.  
**Do not preclaim:** “50% faster” or “elite UX” before data exists.

## Honest limitations
- Actual Faneqo production code and real users not inspected during this reading increment.
- Three author-hosted books **partially** read in identified chapters; no book claimed fully read.
- Accessible component blog articles are **not** its separately sold book.
- No controlled UX study or screenreader evaluation performed.
- Some published examples and screenshots reflect historical technologies; current standards must govern implementation.
