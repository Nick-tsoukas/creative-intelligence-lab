# Research-Derived Knowledge Cards — v0.5

**Use only when original source insight changes a decision.** For normal UX tasks load no more than **one or two** relevant K-cards. Run `python scripts/retrieve.py knowledge K01` (when Python exists), or read just the relevant Markdown section. These are **original concise syntheses**, not the original books. For exact study scope see `RESEARCH_INDEX.md`, `SOURCE_LEDGER.md`, and the separate Lab reading dossiers. **All digital product transfers below are hypotheses until evaluated on actual work.**

## K01 — Subordinate visual parts to the real human job
**Tags:** homepage, hierarchy, composition, visual-focus, subordination.
**Trigger:** a screen offers many visually equal elements but one task truly matters first.
**Source & status:** Arthur Wesley Dow, *Composition*, **1914 ninth edition**, Project Gutenberg #45410, opening Principles of Composition / Ways of Creating Harmony, selected textual sections read; full original illustrations not systematically viewed; one cropped photo of No. 16 studied separately in Lab Dossier 016. [Original](https://www.gutenberg.org/ebooks/45410).
**Source claim / evidence:** Dow treats subordination as a relation among compositional parts. Evidence D (historical artistic pedagogy), SOURCE-CHECKED at bounded scope; modern UX transfer E.
**Mechanism (our interpretation):** a coherent focal structure may help users notice dominant content/actions when importance is genuinely asymmetric.
**Use:** sketch large-value hierarchy only *after* verifying the intended human task; retain keyboard and readable secondary access.
**Counterexample:** genuinely equivalent options or high-density expert monitoring should not be forced into one arbitrary CTA.
**Falsification:** uncoached first-choice task finds essential content hidden, disabled motion removes clarity, or contrast/focus fails.
**Actual evaluation:** NOT RUN; **confidence in general UX outcome: provisional**. Related K02, K05, K08; conflicts with an uncritical "always one dominant element" rule.

## K02 — Repetition is not composition without purposeful spacing
**Tags:** grid, rhythm, composition, cards, repetition, density.
**Trigger:** uniform cards and repeated gutters produce technically consistent but visually inert or confusing grouping.
**Source & status:** Dow, *Composition*, 1914 ninth ed., early harmony sections on repetition/spacing; textual passage studied, no original figures inspected.
**Source claim / evidence:** Dow distinguishes mere repetition from deliberate harmonious relationships; D historical artistic philosophy, bounded SOURCE-CHECKED.
**Mechanism (interpretation):** group by meaning and weight, not equal-box convenience; spacing can communicate distinct sets.
**Use:** make a low-fidelity content hierarchy before changing tokens; verify actual items, read order and screen size.
**Counterexample:** equidistant equal-weight options can communicate real parity; arbitrary asymmetry may obscure selection.
**Falsification:** participant misgroups sections, zoom/reflow breaks reading order, or hierarchy conflicts with equal importance.
**Actual evaluation:** NOT RUN; transfer provisional. Related K01 and K07.

## K03 — Model information relations before moving UI controls
**Tags:** information-architecture, navigation, domain-model, taxonomy, workflows.
**Trigger:** same job spans many screens or labels, and adding buttons hasn't fixed confusion.
**Source & status:** Abby Covert, *How to Make Sense of Any Mess*, complete author-hosted online book; selected original web sections “Messes are Made of Information and People” and “Architecture Before Design” studied. [Original](https://www.howtomakesenseofanymess.com/).
**Source claim / evidence:** information confusion spans people, words and relationships; inexpensive conceptual diagrams can clarify structure. B practitioner method, SOURCE-CHECKED passage, E digital transfer.
**Mechanism (interpretation):** if the user's mental grouping diverges from product nouns, surface styling doesn't repair the mismatch.
**Use:** map `actor → verb → entity → relation → permission` before navigation consolidation; then verify against current application code.
**Counterexample:** if there is a reproducible broken click or serializer, repair it directly without an architecture workshop.
**Falsification:** model matches user vocabulary but the actual defect persists because of state/transport or discoverability.
**Actual evaluation:** NOT RUN; transfer provisional. Related K04/K07; core C01/C03.

## K04 — Labels are domain decisions, not decorative microcopy
**Tags:** terminology, navigation, information-scent, copy, naming, mental-model.
**Trigger:** audience reads a label correctly but predicts the wrong effect, or adjacent terms are inconsistent.
**Source & status:** Abby Covert, *How to Make Sense of Any Mess*, selected “Intent Is Language” web section. [Original](https://www.howtomakesenseofanymess.com/).
**Source claim / evidence:** language communicates intent and affects the structure of information; B practitioner method, exact selected study.
**Mechanism (interpretation):** a wrong category/verb encodes a false expectation about the result.
**Use:** compare users' naturally spoken verb with object, recipient, server authority, and confirmation language; test first-click comprehension.
**Counterexample:** experts may require precise specialist words; simplification can erase legitimate distinctions.
**Falsification:** verified misunderstanding is not associated with terminology (instead a delayed backend state or broken control).
**Actual evaluation:** NOT RUN; transfer provisional. Related K03; core C02/C04.

## K05 — Ask why before copying how
**Tags:** purpose, art-direction, design-critique, originality, homepage, research.
**Trigger:** a visually impressive direction reproduces a reference style but cannot explain its visitor value.
**Source & status:** Frank Chimero, *The Shape of Design*, author-hosted original Chapter 1 “How and Why” directly studied. [Original](https://shapeofdesignbook.com/chapters/01-how-and-why/).
**Source claim / evidence:** Chimero contrasts surface imitation and process craft with inquiry into purpose, and near/far making/critique. D artistic philosophy, SOURCE-CHECKED.
**Mechanism (interpretation):** defining visitor meaning before aesthetic choices improves the quality of the design argument, but not proven conversion.
**Use:** state audience/job/message and why the design should exist, then ask a separate art director for three distinct how-directions.
**Counterexample:** an authorized experimental art installation may treat exploration/ambiguity as the goal; an isolated CSS bug does not need a thesis.
**Falsification:** initial brief is factually false, directions don't preserve required action, or purpose talk adds no decision value.
**Actual evaluation:** NOT RUN; transfer provisional. Related K01, K06; homepage H01/H08.

## K06 — Beauty and usability are distinct questions
**Tags:** beauty, emotional-design, expression, aesthetics, craft, ux-evaluation.
**Trigger:** a competent product seems soulless, or a pretty mockup is mistaken for task proof.
**Source & status:** Chimero, *The Shape of Design*, Chapter 2 “Craft and Beauty” directly studied. [Original](https://shapeofdesignbook.com/chapters/02-craft-and-beauty/).
**Source claim / evidence:** artistic care/purpose extends beyond utilitarian technical execution; D philosophical, not a controlled psychological experiment.
**Mechanism (interpretation):** craft and meaning may support emotional response, but this cannot establish completion or accessibility.
**Use:** get **independent creative critique and task-based UX verification** rather than one holistic invented rating.
**Counterexample:** a life-critical utility may prioritize unambiguous function; nonessential visual expression may be actively harmful.
**Falsification:** tests show that visual flourish reduces legibility, trust, focus or performance.
**Actual evaluation:** NOT RUN; transfer provisional. Related K05, H07.

## K07 — Component reuse must preserve domain truth
**Tags:** components, design-systems, state, permission, consistency, semantic-model.
**Trigger:** team wants to merge different creation flows because their screens look similar.
**Source & status:** Brad Frost, *Atomic Design* (2016), Chapter 2 studied in Lab dossier 010. [Original](https://atomicdesign.bradfrost.com/chapter-2/). Combined with Covert's selected IA method.
**Source claim / evidence:** Frost presents components/templates/pages feeding back into a design system; Covert emphasizes meaningful relations and labels. B practitioner frameworks; combination is Lab E hypothesis.
**Mechanism (interpretation):** common primitives improve craft, while authorization and business meaning must stay separate.
**Use:** reuse shared UI and draft feedback; map scope/visibility/audience and API rules before consolidating operations.
**Counterexample:** flows proven identical may be unified end-to-end; separate experiences can be necessary for high-risk actions.
**Falsification:** same UI component changes a permission, default visibility, user expectation or retry semantic.
**Actual evaluation:** NOT RUN; transfer provisional. Related K03/K04, core C03/C04.

## K08 — Visible is not necessarily recognized or found
**Tags:** perception, search, recognition, attention, discovery, visual-hierarchy.
**Trigger:** UI control is present in a screenshot but novices can't find or interpret it.
**Source & status:** Hornbæk, Kristensson & Oulasvirta, *Introduction to Human-Computer Interaction* (2025), coauthor-hosted PDF, selected Intro, Ch 1 and Ch 3 pp 37–40, 49–57 studied; diagrams not fully visually inspected. [Original](https://pokristensson.com/pubs/IntroductionToHumanComputerInteraction.pdf).
**Source claim / evidence:** relevant chapter analyzes detection, discrimination, visual search/recognition and expectation as distinct aspects of perception; modern textbook, exact underlying experimental references must be checked for stronger empirical assertions.
**Mechanism (interpretation):** a recognizable control in a predicted location can outperform a brighter cryptic icon.
**Use:** diagnose detection vs recognition vs navigation location before visual contrast change; check first-click tasks and accessible labels.
**Counterexample:** expert tools may prioritize dense shortcuts; novices and power users differ.
**Falsification:** observer finds/recognizes control but still cannot complete because of broken navigation/state/API.
**Actual evaluation:** NOT RUN; transfer provisional. Related K01/K04, core C02.

## K09 — Meaning and visual grammar are separate design checks
**Tags:** typography, semantics, visual-communication, brand, layout, art-direction.
**Trigger:** composition is geometrically consistent but communicates the wrong concept or feels generic to the subject.
**Source & status:** Massimo Vignelli, *The Vignelli Canon* (2009), selected Semantics/Syntactics spreads directly studied in Lab dossier 009, figure/page scope limited. [Original](https://www.rit.edu/vignellicenter/sites/rit.edu.vignellicenter/files/documents/The%20Vignelli%20Canon.pdf).
**Source claim / evidence:** the author distinguishes finding meaning and organizing the language of visual form. D practitioner/art philosophy.
**Mechanism (interpretation):** grids/typographic structure serve intentional meaning rather than replace it.
**Use:** ask “what does this communicate?” before selecting the grid, type scale or photographic treatment; allow the art director to invent original directions.
**Counterexample:** a purposefully challenging artwork can communicate ambiguity; utility actions cannot.
**Falsification:** actual users interpret product claim incorrectly or the system's expressive choices block tasks.
**Actual evaluation:** NOT RUN; transfer provisional. Related K05, H08.
