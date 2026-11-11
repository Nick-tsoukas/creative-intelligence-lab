# Research 011 — Perceptual Organization: Arnheim, Gestalt, Kandinsky, Albers, Kelly

**Creative Intelligence Lab | research increment 014 | 2026-11-11**

**Scope and access:** Publisher records, museum catalog essays, official institutional articles and practitioner UX research reviewed online. Arnheim's books were NOT read in full; no claim of primary passage-by-passage reading. The Guggenheim/Kelly works were examined via museum descriptions and web reproductions, not in-person or with calibrated color. No user research, accessibility testing, or website implementation. This is interpretive research with testable design hypotheses.

## Research question
How do position, scale, contrast, similarity, empty space and context lead people to perceive a composition as coherent, tense, lucid or confusing — and how can art directors exploit those mechanisms without turning perception into a rigid formula?

## 1. Arnheim: perception as organization, not passive recording

**Primary work / edition verification:** Rudolf Arnheim, *Art and Visual Perception: A Psychology of the Creative Eye* (original 1954; revised 1974; UC Press 2004 printing, 528 pages). Publisher describes a psychological account of how the eye organizes visual material. Publisher also lists *Visual Thinking* (1969), which argues against a strict split between perception and thought.

Sources:
- https://www.ucpress.edu/book/9780520243835/art-and-visual-perception-second-edition
- https://www.ucpress.edu/books/visual-thinking/paper

**Interpretive synthesis, not verbatim Arnheim:** (a) A composition is experienced as relationships among elements, not a ledger of isolated features. (b) “Balance” can involve asymmetrical distributions of mass and attention. (c) Organizing a picture makes certain structures perceptually available before the viewer consciously inspects detail.

**What must not be claimed:** That a single perfect proportion, rule of thirds, symmetry ratio or eye-tracking path guarantees beauty. Psychological descriptions require observation and controlled tests to predict individual outcomes. Arnheim's theoretical system should not be represented as universally confirmed contemporary cognitive neuroscience.

**Open close-reading task:** Acquire a legitimate edition or authorized preview; analyze actual passages with page numbers from I. Balance and II. Shape, distinguish the author's original demonstrations from our applications.

## 2. Gestalt: grouping as communication

**Published UX source:** Nielsen Norman Group, Aurora Harley, “Proximity Principle in Visual Design,” 2020-08-02, https://www.nngroup.com/articles/gestalt-proximity/ ; “Similarity Principle in Visual Design,” https://www.nngroup.com/articles/gestalt-similarity/ ; broader https://www.nngroup.com/articles/principles-visual-design/

**Documented guidance:** proximity groups elements; distance separates; similarity in color/shape/size can communicate common function; responsive changes can destroy proximity groupings.

**Art-direction translation (interpretation):**
- Proximity: position the evidence next to the claim it supports.
- Similarity: visual sameness should express genuine common purpose, not merely convenience.
- Figure/ground: one dominant event gains power from a controlled supporting field.
- Common region: use containers only when enclosure clarifies relationships; arbitrary cards flatten narrative.
- Continuity: align visual paths with conceptual dependencies, but preserve navigational choice.

**Counterexample:** A dramatic hero and purchase action separated by multiple scroll lengths may be aesthetically impressive yet fail an information-retrieval task. A heavily grouped dashboard may feel tidy while disguising the primary next action among secondary controls.

## 3. Institutional case A — Kandinsky, *Several Circles* (1926)

**Verified object:** Vasily Kandinsky, *Several Circles (Einige Kreise)*, January–February 1926; oil on canvas, approx. 140.7 × 140.3 cm; Solomon R. Guggenheim Museum, accession 41.283.
Source: https://www.guggenheim.org/artwork/1992

**Museum account:** Kandinsky pursued psychological and spiritual expressive effects of color/form at Bauhaus; geometric overlap and circles culminate in *Several Circles*. The Guggenheim institutional discussion contextualizes its geometric vocabulary.

**Our observation from published reproduction, interpretive:** One large dark disc and its bright halo establish a dominant weight; many smaller chromatic discs and overlaps make a field of distributed secondary events; the dark ground makes the boundaries legible. This is asymmetrical equilibrium, not a proof of ideal balance.

**Transferable mechanism:** establish a focal hierarchy using scale *and* contextual contrast; distribute smaller accents as counterweights rather than adding seven competing heroes.

**Tempting imitation to reject:** cosmic glowing circles, black backgrounds, and faux-Bauhaus motifs without relevant content.

**Falsifiable design test:** Show equal-content mockups with one focal group versus three rival focal groups; measure 5-second recall of purpose, primary action identification, and confidence. Do not predict a winner before testing.

## 4. Institutional case B — Josef Albers, *Interaction of Color* (1963)

**Publisher/context:** Yale University Press 1963 original limited edition, 2013 anniversary edition with expanded studies. Publication and instructional purpose documented:
https://yalebooks.yale.edu/book/9780300179354/interaction-of-color/
https://news.yale.edu/2023/02/17/book-color-never-fades

**Documented mechanism:** an identical color can appear different in different contexts; Albers used hands-on colored-paper demonstrations of color relativity, vibrating/vanishing boundaries, and apparent transparency.

**Transferable mechanism:** test a brand accent **in situ**, next to photo, type, and surrounding colors; standalone swatches are insufficient.

**Counterexample:** a color may feel visually vivid yet render small interface text unreadable; aesthetic color relationships must not override contrast or usability requirements.

**Hypothesis/test:** build two compositions containing identical target accent samples within different surrounds; ask viewers whether the accent appears lighter, more saturated, or more urgent. Confirm physical pixel identity; avoid claiming color-vision uniformity.

**Reading status:** verified publisher/institutional descriptive sources, NOT entire primary book or full plates.

## 5. Institutional case C — Ellsworth Kelly, *Spectrum Colors Arranged by Chance IX* (1953)

**Source:** National Gallery of Art, “Who Is Ellsworth Kelly? 10 Things to Know,” https://www.nga.gov/stories/articles/who-ellsworth-kelly-10-things-know

**Documented:** Kelly numbered colors and used chance to choose sequences in this body of work. NGA interprets this as an effort to minimize the artist's hand and direct attention to spatial/formal experience.

**Our interpretation:** structured repetition, systematic alternatives and nonhierarchical variation can be artistically compelling; controlled systems do not always require one iconically dominant gesture.

**Transferable mechanism:** for a gallery or editorial index, establish a strong invariant grammar (size, baseline, type role) while permitting meaningful variation in image/form.

**Tempting imitation to reject:** random decorative color tiles implying creative sophistication while hiding content taxonomy.

**Test:** compare an editorial index using arbitrary accent variance with one whose accent distinctions encode categories. Measure grouping comprehension and mistaken categorization, not “beautiful” alone.

## 6. Four tensions worth studying next
1. **Tension vs comprehension:** a mild imbalance may create attention; too much may obscure action. Find the useful range for a specific task.
2. **Novelty vs fluency:** unusual compositions attract attention but may impose interpretation cost.
3. **Hierarchy vs polyphony:** some cultural narratives need one lead image; others need a network of equal voices.
4. **Expressive abstraction vs authenticity:** color/shape metaphors cannot replace actual people, work or audience evidence.

## 7. The Perceptual Composition Review (v0.1, unvalidated)
For each proposed direction, record:
- **Primary proposition:** what must the viewer understand within seconds?
- **Dominant visual force:** what attracts attention first and why (scale, location, contrast, motion)?
- **Counterweight:** what prevents the composition becoming visually one-sided?
- **Group meaning:** which objects seem related, and is that relationship accurate?
- **Figure/ground:** what is deliberately subordinate, and what remains legible?
- **Responsive conservation:** which relationships survive a 390px viewport?
- **Emotional register:** does the experience express a project-specific meaning rather than fashionable styling?
- **Failure condition:** what user task could the artistic choice damage?
- **Evidence:** screenshot/observation/user result needed before asserting success.

Each answer must be a concrete sentence; “strong hierarchy” with no specified focal event is invalid.

## 8. Original experiment specification: three perceptual studies
Not yet built or tested.
A. **Visual weight:** same seven shapes, compare balanced central, strongly asymmetrical, competing highlights. Outcome: viewer-described focal point and dominant message recall.
B. **Semantic grouping:** same labels/links, vary proximity and shared enclosure. Outcome: grouping accuracy, scan time.
C. **Contextual color:** same foreground patch on two grounds. Outcome: relative brightness/saturation judgments; include a neutral control.

No artwork reproduction should be committed without explicit rights. Diagrams must be newly drawn, clearly labeled experiments, not museum images.

## 9. Decision implications for future Faneqo art direction (NOT A DESIGN)
- An artist/fan platform should organize actual artists, imagery and evidence into meaningful hierarchies; visual effects are subordinate to that.
- The typography, imagery and whitespace should support a central cultural idea, rather than copying abstract-painting motifs.
- “Cinematic” should mean intentional sequencing of attention, not compulsory animation.
- Review a proposed hero at mobile width before treating desktop grandeur as proof.
- Any later isolated homepage test requires explicit owner authorization; no production app modifications.

## 10. Sources and verification status
| Source | Verification | Limitation |
|---|---|---|
| UC Press — Arnheim *Art and Visual Perception* | publisher description and bibliographic facts reviewed | full book unread |
| UC Press — Arnheim *Visual Thinking* | publisher description reviewed | full book unread |
| Guggenheim — Kandinsky *Several Circles* | museum record/context reviewed; published reproduction observed | no original viewing, museum rights apply |
| Yale University Press/News — Albers *Interaction of Color* | publisher/institutional descriptions reviewed | full plates/text unread |
| National Gallery of Art — Ellsworth Kelly | institutional overview reviewed | not a full catalog or original |
| Nielsen Norman Group — proximity/similarity/visual principles | practitioner articles reviewed | not independent experimental replication |

## Next research increment
1. Legally obtain and analyze a **specific** Arnheim chapter (I. Balance, II. Shape) with precise page evidence.
2. Develop an original composition experiment and test it in a browser, with controlled viewport, contrast and actual participant observations.
3. Study M. C. Escher figure/ground vs contemporary visual ambiguity critically, or compare Paul Klee's teaching notebooks with Arnheim.
4. Deepen digital examples: two authentic visually expressive projects **and** one high-comprehension public service interface, not style galleries.

**Status:** source-backed research complete for this increment; new hypotheses are unvalidated; Faneqo frontend/backend untouched.
