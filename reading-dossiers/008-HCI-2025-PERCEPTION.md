# UX Reading Dossier 008 — Hornbæk, Kristensson & Oulasvirta: Perception and Interface Tasks

**Research date:** 2026-11-15. **Work:** Kasper Hornbæk, Per Ola Kristensson, Antti Oulasvirta, *Introduction to Human-Computer Interaction* (Oxford University Press, 2025), DOI 10.1093/oso/9780192864543.001.0001. **Original full text:** https://pokristensson.com/pubs/IntroductionToHumanComputerInteraction.pdf (PDF on a co-author's site); publisher contents https://academic.oup.com/book/60808 . **Access:** verified complete OA PDF, CC BY-NC-ND 4.0. **Reading:** introduction, selected passages of Chapter 1 pp. 3–6, Chapter 3 pp. 37–40, 49–57, and the book's contents; NOT full textbook and NOT full Chapter 3. Figures were identifiable in extracted text; PDF screenshot retrieval failed because file exceeded visual tool limits, so figures are **not visually verified** here.

## Original question
How does a UI present a changing system to a human perceptual system that is selectively attending, interpreting, and acting toward a goal, rather than passively absorbing everything drawn?

## Source-supported mechanisms
1. **HCI is not UI ornamentation (Chapter 1, pp. 3–6).** The authors describe computing as a useful tool only insofar as people can control it and receive feedback. Their motivating question considers differences of goals and capabilities, enjoyment and safety. This rejects a feature checklist as a substitute for task success.
2. **Perception is organized and expectation-driven (Chapter 3, pp. 37–40).** Example of finding a button on a phone: the user brings learned strategies and expectations; the designer cannot force attention by visual layout alone. The book distinguishes bottom-up sensory evidence and top-down prior experience. Practical deduction: conventional position, clear label, familiar category and content grouping matter alongside emphasis.
3. **Operationalize a perceptual task (Chapter 3, pp. 49–51, and summary).** Rather than generic “make more visible,” ask whether the user needs to **detect** a state change, **discriminate** two controls, **recognize** an icon/label, **estimate** a property, or **search** for a target. These are different demands with different design remedies.
4. **Visual grouping and attention (Chapter 3, approx. pp. 55–57).** The book illustrates layout grouping as a way to indicate related menu items and discusses selective/divided attention and feature versus conjunction search. Translation: grouping should reflect actual task/permission boundaries, not only visual symmetry. High contrast alone cannot make an unfamiliar icon semantically recognizable.

## Reasoning and limits
This work bridges scientific mechanisms and design decisions, but does not establish that any particular Faneqo redesign will improve real outcomes. It warns indirectly against claiming saliency is a magic power: learned expectations and task strategies modulate perception. The chapter's theory should lead to testable interface predictions rather than universal “F-pattern” or “one color always wins” commandments. This text is contemporary but application remains an interpretation. Complex studies and equations in the chapter have **not** been independently replicated.

## Counterexamples
- A brightly colored gallery icon may be detected but still not recognized as “send photos from this Night.”
- A perfectly uniform header may be cohesive but hide that broadcast and private chat have different recipients and consequences.
- Increasing one target's size may not help if the expected task is in an unexpected workspace.
- Low-vision or screen-reader experiences cannot be established solely from a visual grouping diagram.

## Faneqo decision case
**Reported symptom:** Artists face two visually different message composition screens; attaching a Night gallery is hard to discover; audience and privacy semantics are confusing. **Hypothesis only, not tested:** A task-first entry labeled “Share photos with attendees” in the ended Night, inheriting the known Night context, could reduce a user's need to search across Galleries, Messages, and Night. A visible recipient summary + preview differentiates **recipient recognition** from **recipient selection**. “Broadcast to eligible attendees” must not look like a one-to-one conversation. Track actual permission and delivery state separately.

**Proposed contract:** Enter Night → choose task → verify eligible audience → choose existing/create gallery → review visibility and recipients → send or save draft → truthful delivery result. For each transition define detection/recognition/search demands, inaccessible/empty/error states and recovery. This is a research recommendation, NOT a code specification or permission decision.

## Skill transfer
- **Elite UX Director:** require a task table with columns “human verb / perceptual subtask / expected location / discriminability / state feedback / recovery / evidence status.” Ask whether an error is in navigation, label recognition, state detection, or conceptual architecture before proposing styling.
- **Creative Design Director:** use the intended attentional path and authenticated task hierarchy to select image/text/whitespace composition. Emphasize the action without erasing artist authenticity or rival tasks. Artistic weight is conditional on comprehension, not a guarantee.
- **Frontend implementer:** after authorized handoff, preserve meaningful semantics, text labels, proper keyboard target/focus and screen-reader status. Avoid treating interface screenshots as usability proof.

## Cross-source connections
- James, *Principles of Psychology*, Ch XI: historically emphasizes selective attention; HCI 2025 provides current operational tasks rather than relying on James's nineteenth-century neuroscience.
- Lynch/Horton, *Web Style Guide*, Ch IV: content taxonomy sets what can be found; HCI perception concerns how finding unfolds.
- Frost, *Atomic Design*, Ch II: component reuse provides consistent presentation, but does not determine meaningful domain concepts.

## Outstanding questions
What are Faneqo's exact attendee eligibility rules? Which user entry path is most frequent? Which controls are misunderstood rather than unseen? Which error and failure states exist? How do touch/keyboard/screen readers differ? Requires actual product/people research when authorized.

**Evidence status:** SOURCE TEXT EXCERPTS READ; FIGURES NOT FULLY INSPECTED; FANEQO TRANSFER HYPOTHESIS; NO PRODUCT TESTING. No full PDF bytes committed.