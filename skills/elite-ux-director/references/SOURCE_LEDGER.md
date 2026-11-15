# UX Research Source Ledger — 2026-11-14

**Scope:** texts actually inspected on official free author/publisher pages, not claims of entire books read. Use narrow references per problem. Never reprint copyrighted books or unlicensed PDFs.

## Book A — Jeremy Keith, *Resilient Web Design*
- Original freely readable web book, author-licensed CC BY-SA 4.0: https://resilientwebdesign.com/
- **Directly read in this increment:** Chapter 5 *Layers* https://resilientwebdesign.com/chapter5/ and Chapter 6 *Steps* https://resilientwebdesign.com/chapter6/
- **Did not read:** other full chapters as part of this increment; do not label whole book FULLY READ.
- **Key source mechanisms:** baseline semantic content remains usable underneath enhancements; progressive enhancement adapts to capabilities without prescribing one identical visual result; define meaningful user verbs before building interface actions; Keith explicitly uses messaging as an example in Chapter 6.
- **Faneqo translation (interpretive):** the essential flow is compose → review audience → submit → truthful status → continue conversation; gallery attach, enhanced draft recovery, animation are additions without destabilizing that core. **Do not promise a JS-free Faneqo app** without engineering validation.
- **Counterexample:** “simplest possible technology” does not imply refusing rich media or realtime feedback when the task genuinely benefits.

## Book B — Patrick J. Lynch & Sarah Horton, *Web Style Guide* (4th ed.)
- Complete online chapter index https://www.webstyleguide.com/ ; print/publisher edition https://yalebooks.yale.edu/book/9780300225259/web-style-guide-4th-edition/
- **Directly read:** Chapter 4 *Information Architecture* https://www.webstyleguide.com/4-information-architecture.html and selected sections Chapter 7 *Interface Design* https://www.webstyleguide.com/7-interface-design.html
- **Not read:** the complete fourth-edition book or all site chapters. The third edition is a separate archived edition and must not be passed off as 4th.
- **Key source mechanisms:** controlled vocabulary for navigation/content; taxonomy and hierarchy; content inventory; test organization and wayfinding; consistent identity/orientation and functional feedback. Ch. 4 emphasizes that visual styling cannot repair bad underlying content architecture.
- **Faneqo translation (interpretive):** keep Inbox, Sent campaigns, Requests, private conversation, gallery, Night and eligible audience conceptually distinct, but let task-based entry points unify the experience.

## Book C — Mark Boulton, *Designing for the Web*
- Author-hosted complete book and optional downloadable editions; **CC BY-NC-ND 4.0**: https://designingfortheweb.co.uk/
- **Directly read:** Ch. 7 *The Brief* https://designingfortheweb.co.uk/part2/chapter7/ ; Ch. 8 *Research* https://designingfortheweb.co.uk/part2/chapter8/ ; Ch. 13 *Hierarchy* https://designingfortheweb.co.uk/part3/chapter13/
- **Not read:** entire book. PDF/EPUB offered, but not downloaded or redistributed in this increment.
- **Key source mechanisms:** separate client, technical, creative and idea briefs; the useful brief is specific without prescribing the solution; research should yield insights; distinguish qualitative from quantitative evidence; hierarchy is conveyed through weight and scale.
- **Caution:** Boulton's example containing 11px body text is a historical illustration, **not a modern mobile accessibility recommendation**. Do not copy prescriptive old pixel sizes. Likewise aesthetic claims about traditional type scales are art judgment, not universal science.
- **Faneqo translation (interpretive):** founder's task problem + product restrictions + audience clarity + screen-context brief before redesigning UI. Report user feedback separately from designer hypotheses.

## Component engineering monograph companion — Heydon Pickering, *Inclusive Components*
- Free author-authored public blog articles https://inclusive-components.design/ ; a separately sold edited book https://book.inclusive-components.design/ is **not read**.
- **Directly read public articles:** *Notifications* https://inclusive-components.design/notifications/ ; *Tabbed Interfaces* https://inclusive-components.design/tabbed-interfaces/
- **Key mechanisms:** non-actionable state updates shouldn't steal keyboard focus; use judicious live regions; consider chat update verbosity; do not distinguish status using color alone; tabs should have the expected keyboard/ARIA pattern; don't turn route navigation into faux tabs.
- **Faneqo translation:** avoid noisy aural alerts for every incoming fan event; announce relevant arrival in active thread without forcibly moving focus; distinguish campaigns vs inbox tabs only if interaction and keyboard model truly match.
- **Caution:** example code is historical educational material. Verify current WCAG, WAI-ARIA APG and browser/screen-reader support before copying it.

## Heuristic reference — Jakob Nielsen, NN/g
- **Actual source reviewed:** *10 Usability Heuristics*, original 1994; updated online explanatory article reviewed 2024: https://www.nngroup.com/articles/ten-usability-heuristics/
- **Actual source reviewed:** *How to Conduct a Heuristic Evaluation* https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/
- **Not read:** Nielsen's copyrighted *Usability Engineering* or *Designing Web Usability* books.
- **Mechanisms:** show status; match mental models; control/undo; consistency; prevent errors; recognition; flexibility; minimalist content; recovery; contextual help. Use as heuristic hypotheses, not observed user data.

## Future reading queue (not read yet)
1. Don Norman, *The Design of Everyday Things* — copyright-protected. Obtain licensed edition/library access; study feedback, mapping, signifiers, constraints and conceptual models with exact pages. **Do not claim read.**
2. Steve Krug, *Don't Make Me Think, Revisited* — copyright-protected; actual chapters not read. Prioritize navigation/scanning and usability sessions through a legal edition.
3. Alan Cooper et al., *About Face* — copyright-protected; inspect goal-directed design/personas after authorized acquisition.
4. Indi Young, *Mental Models* — copyright-protected; valuable for artist/attendee mental models.
5. Luke Wroblewski, *Web Form Design* — copyright-protected; relevant for recipient review and form errors.
6. Sarah Horton & Whitney Quesenbery, *A Web for Everyone* — copyright-protected; valuable for disability-inclusive user research.
7. Heydon Pickering, *Inclusive Components* printed edition — copyright-protected; freely hosted preceding articles are not the entire book.
8. *Encyclopedia of Human-Computer Interaction*, 2nd Ed., free contributed chapters https://ixdf.org/literature ; inspect exact chapters selectively before claiming read.
9. W3C WCAG 2.2 / WAI-ARIA Authoring Practices and GOV.UK Design System — living standards/pattern libraries, not books; review for implementation currency.

## Citation/evidence statuses

- **DIRECTLY READ CHAPTER:** source page inspected for chapter scope, not independently checked against physical print or facsimile.
- **PARTIALLY READ BOOK:** subset of chapters examined; no FULLY READ label.
- **ARTICLE READ:** author text, not book.
- **LINK VERIFIED ONLY:** no claim of understanding the work.
- **NOT READ:** planning reference only.
- **TESTED:** actual product behavior observed using identified environment.
- **HYPOTHESIS:** an intended transfer to Faneqo, not tested user behavior.

## Learning-to-behavior links
- Architecture labels/grouping → Web Style Guide Ch. 4 → information architecture map + task/user labeling test.
- Task-first messaging, resilient fallback → Keith Ch. 6 + Ch. 5 → core flow and interrupted-task scenario.
- Clear brief/evidence limits → Boulton Ch. 7–8 → no premature solution lock-in.
- UI hierarchy → Boulton Ch. 13 → recognizable primary actions and readable mobile screenshots.
- Realtime status/notification → Pickering Notifications → focus-safe, nonintrusive update test.
- Tab semantics → Pickering Tabbed Interfaces → keyboard test + consistent in-page versus routed semantics.
- General friction diagnosis → NN/g 10 heuristics → observe before rating.


---

## 2026-11-15 research-integrated extension — section-scoped, no full books claimed

These source records reflect Mission 001's newly written original-text dossiers in `reading-dossiers/008–012`. Their interpretive UX cards are deliberately short in `DECISION_CARDS.md`, and `TASK_SOURCE_ROUTER.md` should be used for selection. **This skill was not performance-benchmarked, and this ledger is not a UX participant study.**

### Hornbæk, Kristensson and Oulasvirta — *Introduction to Human-Computer Interaction* (Oxford, 2025)
- Complete coauthor-hosted OA PDF: https://pokristensson.com/pubs/IntroductionToHumanComputerInteraction.pdf ; CC BY-NC-ND edition.
- **Studied:** selected Introduction/Chapter 1 and Chapter 3 pp. 37–40, 49–57 passages; **not whole chapters or whole book**. Figures not visually verified because screenshot retrieval of large PDF failed. See `reading-dossiers/008-HCI-2025-PERCEPTION.md`.
- **Useful mechanisms:** perceptual detection vs discrimination vs recognition vs search, prior expectations and attention, task before styling. **Interpretive transfer:** an action can be visible but not recognizable or in the expected location.
- **Caution:** this does not establish a specific visual ranking or actual Faneqo success rate.

### Brad Frost — *Atomic Design* (2016), author-hosted
- Full web book https://atomicdesign.bradfrost.com/ ; **Chapter 2 directly read**, not the complete book. Dossier 010.
- **Useful mechanism:** atoms/molecules/organisms/templates/pages with feedback between page-level real content and component patterns. **Interpretive transfer:** reuse composer controls while keeping broadcast, chat, and gallery sharing permission semantics distinct.
- **Caution:** the book is a design methodology, not empirical evidence that any specific component arrangement improves UX.

### Massimo Vignelli — *The Vignelli Canon* (2009)
- Institutional PDF https://www.rit.edu/vignellicenter/sites/rit.edu.vignellicenter/files/documents/The%20Vignelli%20Canon.pdf .
- **Studied:** selected original Semantics/Syntactics/Ambiguity and typographic/grid spreads; **not all pages**, see Dossier 009.
- **Useful mechanism:** understand subject meaning/context before organizing visual relationships.
- **Caution:** intentionally expressive ambiguity is not appropriate to wrong-recipient or permission-sensitive controls. No print-point-size prescription for web.

### Sasha Costanza-Chock — *Design Justice* (MIT Press, 2020)
- Open-authorized original HTML https://designjustice.mitpress.mit.edu/pub/cfohnud7/release/4 .
- **Studied:** selected sections of *Design Practices: “Nothing about Us without Us”*, not the whole book/chapter footnotes; Dossier 011.
- **Useful mechanism:** distinguish consultation, participatory authority, assumptions and real affected-user evidence. Do not treat synthetic artist/fan personas as field observations.
- **Caution:** normative framework, not quantified evidence that any specific Faneqo flow wins.

### William James — *The Principles of Psychology*, Vol I (1890 original; Gutenberg 1918 imprint)
- Public-domain edition https://www.gutenberg.org/ebooks/57628 .
- **Studied:** selected Ch IV *Habit* and Ch XI *Attention* passages only; Dossier 012.
- **Useful historical framing:** habit, selective interest and learned action; **modern technical claims require corroboration from contemporary research**.
- **Caution:** nineteenth-century physiology and cognitive claims are not modern proven UX laws.

### Standards that are not books
- W3C WCAG 2.2 https://www.w3.org/TR/WCAG22/ ; selected Understanding materials https://www.w3.org/WAI/WCAG22/understanding/ . Conformance cannot be claimed from source citation or code alone.
- WAI-ARIA Authoring Practices https://www.w3.org/WAI/ARIA/apg/ . Implement a real keyboard/focus pattern corresponding to actual interaction, rather than decorative ARIA roles.
- These current standards are used as normative implementation references; reading them does not constitute a completed accessibility audit.
