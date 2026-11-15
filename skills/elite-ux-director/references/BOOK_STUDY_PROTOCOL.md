# Book-to-Design Intelligence — Study Protocol v0.5

**Load only for a research/reading assignment, book-derived claim verification or knowledge-card contribution; NOT an ordinary UI bug.** The canonical raw user-authored source is `sources/intake/2026-11-15/BOOK_TO_DESIGN_INTELLIGENCE_PROTOCOL.md` in the Lab. These instructions operationalize it without expanding the always-on skill.

## Source identity — immutable before interpretation
Record stable `source_id`; original title; author; specific **edition and year** (separate original vs translation vs reprint); publisher/host; stable URL/owner file pointer; format; language; rights/access constraints; section/page/figure locator; complete-vs-excerpt; presence/legibility of illustrations; source method (empirical / interpretive / historical / normative). Bibliographic leads and online previews are NOT full text. Keep copyright material in authorized locations; publicly version original paraphrase/metadata rather than book reproductions.

## Reading states (independent dimensions, never a single inflated stage)
`CATALOGED` → `IDENTITY_VERIFIED` → `FULL_TEXT_ACCESS_VERIFIED` → `STRUCTURE_INSPECTED` → `SECTIONS_STUDIED` → `WHOLE_TEXT_STUDIED`. A partial/preview-only work can be `STRUCTURE_INSPECTED` without ever reaching `FULL_TEXT_ACCESS_VERIFIED`. Track **visual coverage separately**: `NO_IMAGES`, `IMAGES_PRESENT_NOT_INSPECTED`, `SELECTED_FIGURES_VISUALLY_STUDIED`, `MAJOR_FIGURES_REVIEWED`. Track synthesis and application **separately**: `CARD_PROPOSED`, `CARD_SOURCE_CHECKED`, `APPLIED`, `OUTCOME_EVALUATED`. These labels do not imply model weight changes or permanent memory.

**Critical example:** Dow's Project Gutenberg illustrated *Composition* is the 1914 **ninth edition**; do not confuse it with a 1913 seventh edition, even when titles match.

## Stage A — Map the book, do not pretend to read it
Inspect table of contents, title pages, introductions, chapter sequence and stated scope. Write a **Book Intelligence Profile**: author goal; intended reader/time/medium; core thesis and principal methods; assumptions; argument type; high-value chapters for the current task; relevance and counter-relevance; major visuals; known access gaps; source status. A profile is a routing artifact, NOT a substitute for deep study.

## Stage B — Read bounded real sections thoroughly
Select only sections capable of changing an actual design judgment, not 20 books at once. Record:
1. **Author's actual thesis** and supporting chain, not only a title/marketing blurb.
2. **Exact source anchor** (chapter, page/figure, stable URL, edition); never invent a quote/number.
3. **Method / mechanism** as described by author, distinguished from a later psychological explanation.
4. **Examples or data** and whether observed visually, quoted by author, or inferred by agent.
5. **Opposing claim or limit**: scope, audience, historical assumptions, alternate environment, unsupported leap.
6. **Digital transfer hypothesis** in our words, clearly separated from what the author wrote.
7. **Rejection criteria**: when using this advice would damage comprehension, agency, trust, accessibility or performance.
8. **Actual application status**: none / brief only / prototype / observed user behavior / measured outcomes.

Persist a small dossier with **what was actually read**. A short, accurate chapter record is better than an ornate fictitious complete-book report.

## Stage C — Visual study is separate
If a chapter uses images, load [Visual Analysis Protocol](VISUAL_ANALYSIS_PROTOCOL.md); view the actual figure/photo/spread, not its caption or OCR. If the image isn't accessible, say **NOT VISUALLY STUDIED** and stop making specific spatial claims. Page-image rights and reproduction constraints still apply.

## Stage D — Convert evidence into conditional cards
Use [Knowledge Card Schema](DESIGN_KNOWLEDGE_SCHEMA.md). One **atomic design claim per card** with source locator, evidence class, target problem, proposed mechanism, counterexample, risk, falsification and maturity. Use **no more than one or two cards** for a normal UX task. A chapter synopsis is background, not automatically a card.

When two texts seem to agree, read [Cross-Book Synthesis](CROSS_BOOK_SYNTHESIS.md): explicitly keep conflict and uncertainty, and do not force agreement.

## Stage E — Verify before release
- Source can be opened; date/edition/locator are correct and status is exact.
- An agent could retrace each claim to a real passage; quotations remain appropriately brief.
- Distinguish primary research from professional heuristic/art philosophy, normative standards and our inference.
- Cards answer a practical *when?* question; counterexample and failure mode are present.
- No universal beauty ratio, assumed mental-model law, manufactured participant data, or promised conversion improvement.
- Where feasible, inspect current implementation and independently check output with real tasks/screenshot/user evidence.
- If a new card merely repeats an existing one, **link/update it rather than adding a duplicate**.

## Release boundary
Installing a SKILL folder does not “teach” the underlying model new weights. It makes **retrievable, selectively loaded, revision-controlled knowledge** available. The Library is the external source of truth; the installed skill is a tiny decision engine + selected evidence. Never bundle entire copyright books or private Faneqo actor/user data inside the universal skill.
