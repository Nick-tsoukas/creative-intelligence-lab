# Book Canon Intake and Edition-Aware Reconciliation — 2026-11-15

**Purpose:** expand our UX, visual communication and interdisciplinary book knowledge **without duplicate-count inflation, piracy or fake reading claims**. Input files preserved verbatim in `sources/intake/2026-11-15/`. This is a repository research record, NOT a statement that books were downloaded/AI-studied.

## Incoming inventory vs existing Lab
- Historical Mission 001 library: **130 candidate book rows** (27 verified direct full-text links, 103 bibliographic leads, with some read sections and many not read). That was an independent earlier research snapshot.
- Submitted *Elite UX Design Source Manifest* contains **122 rows: 82 books + 40 articles/standards/archives**; its `study_status` fields are all **not-ingested**. A URL in that CSV is often a publisher's sales page, **not** a full readable source.
- A first-pass title normalization identified **40** matching titles between the incoming 82 and the historical 130; **42** required edition/alternate-title review. This is **not** a claim of 42 distinct new books. Some alternate subtitles, source references and different editions overlap. The deterministic, read-only `scripts/reconcile_ux_book_canon.py` now reports exact/possible/manual-review title candidates without merging editions or declaring books ingested.
- Three works newly verified here as complete *authorized online originals* receive separate access status below. Their inclusion in a canon may already be reflected as a non-verified mention in an earlier index; do not inflate unique-book totals.

## New verified full-readable works — access ≠ full study

| Study ID | Work, exact source | Full readable original | What was actually studied here | Visual caveat | Action |
|---|---|---|---|---|---|
| N-V01 | Arthur Wesley Dow, *Composition*, **9th ed. revised**, Doubleday Page, **1914** | [Project Gutenberg #45410](https://www.gutenberg.org/ebooks/45410), US public-domain illustrated HTML/EPUB | Opening, Three Elements and initial harmony/spacing passages; `reading-dossiers/013-DOW-COMPOSITION-HARMONY-AND-HIERARCHY.md` | Figure files exist, but images not systematically visually analyzed | Study selected notan/line figures separately with exact image provenance |
| N-V02 | Abby Covert, *How to Make Sense of Any Mess*, author's living complete online edition (site ©2022) | [Author's complete text](https://www.howtomakesenseofanymess.com/) | Selected sections “Messes...”, “Intent Is Language”, “Architecture Before Design”; Dossier 014 | Web layout rather than illustrated print edition used | More taxonomy/category and navigation chapters when needed |
| N-V03 | Frank Chimero, *The Shape of Design*, author's CC BY-NC-SA online edition | [Author full text/download](https://shapeofdesignbook.com/download/) | Chapters 1 *How and Why*, 2 *Craft and Beauty*, and 3 *Improvisation and Limitations* (latest chapter addition, see note below); Dossier 015 for first two; scope of Ch3 noted in supplement | Paintings/illustrations not independently analyzed at full pixel fidelity | Deepen selected context/narrative chapters later |

**Edition discrepancy fixed:** earlier user manifest proposed Dow 1913; the Gutenberg text's original title page unambiguously says 1914 ninth edition. The study cites what it actually examined. **Legal caveat:** free author web reading does not authorize arbitrary republication of artwork/book text, and Gutenberg US public-domain status doesn't establish global status.

### Additional reading note — Chimero Chapter 3 (2026-11-15)
Directly reviewed [Chapter 3: Improvisation and Limitations](https://shapeofdesignbook.com/chapters/03-improvisation-and-limitations/) in original author text. Chimero argues that explicit objectives guide useful work but may stifle early idea generation when clutched too tightly; structured constraints and improvisation can allow exploratory alternatives, **then objectives are reintroduced to judge them**. This supplements Chapter 1's purpose-before-imitation: research should specify the *why*, creative direction should explore surprising *hows*, and independent UX checks should reapply the actual product/task constraints. Aesthetic process philosophy, not measured usability or a license to disregard accessibility. No artwork from the chapter was visually verified.

## Ten verified bibliographic additions — **licensed/borrowed, NOT read or freely downloaded**

These titles are *additional acquisition candidates* not found as book-title entries in our two pre-existing title inventories. Each has an original publisher, institutional or author bibliographic page inspected in 2026-11-15 research. **Publisher listing != complete book access.** Prioritize small legitimate excerpts, libraries/authorized subscriptions, and source-based notes.

| ID | Work / edition source (link) | Status | Why it belongs in our Leonardo-like research system | Stage / priority |
|---|---|---|---|---|
| ADD-01 | Donella Meadows, *Thinking in Systems* (2008), [Chelsea Green](https://www.chelseagreen.com/product/thinking-in-systems/) | Verified publisher metadata, full text **not** inspected | System feedback, unintended consequences, longer-term outcome loops | High, T1 |
| ADD-02 | Christopher Alexander et al., *A Pattern Language* (1977), [author estate archive](https://christopher-alexander-ces-archive.org/book/a-pattern-language/) | Verified author archive, full text **not** inspected | Recurring human-environment problems, pattern languages and careful physical→digital analogy | High, T2 |
| ADD-03 | Caroline Jarrett & Gerry Gaffney, *Forms That Work* (Morgan Kaufmann; March 2009 listing), [O'Reilly bibliographic/preview](https://www.oreilly.com/library/view/forms-that-work/9780080948485/) | Publisher preview only; full text **not** read | Relationship, conversation, appearance and testing of forms | High, T1 |
| ADD-04 | Kim Goodwin, *Designing for the Digital Age* (Wiley 2009 first edition), [Smithsonian catalog](https://www.si.edu/object/designing-digital-age-how-create-human-centered-products-and-services-kim-goodwin%3Asiris_sil_1091677) | Catalog verified; do not copy unlicensed PDFs | Long-form goal-directed design, research→personas→requirements→prototype | High, T1 |
| ADD-05 | Karen McGrane, *Content Strategy for Mobile* (2012), [A Book Apart official listing](https://abookapart.com/products/content-strategy-for-mobile.html) | Publisher metadata; publisher no longer distributes it; full text not accessed | Reusable content models across devices and channels | High, T2 |
| ADD-06 | Stewart Brand, *How Buildings Learn* (Penguin 1995 edition), [Penguin Random House](https://www.penguinrandomhouse.com/books/320919/how-buildings-learn-by-stewart-brand/) | Publisher metadata; not read | Architecture over time, adaptation by actual occupants; analogy for maintainable product systems | High, T2 |
| ADD-07 | Scott McCloud, *Understanding Comics* (HarperCollins 1994 paperback edition), [publisher metadata mirrored by retailer](https://www.thebookco.com/understanding-comics/) | Bibliographic edition verified; pages/figures not inspected | Sequencing, image-text systems and interpretation of visual narrative | High, T2; must inspect actual illustrations |
| ADD-08 | Henry Dreyfuss, *Designing for People* (Allworth 2003 reissue), [Allworth publisher](https://www.skyhorsepublishing.com/allworth-press/9781581153125/designing-for-people/) | Publisher metadata; not read | Industrial ergonomics and design responsibility, real human fit | Medium, T2 |
| ADD-09 | Steven Pinker, *The Sense of Style* (Penguin 2014 ebook), [Penguin Random House](https://www.penguinrandomhouse.com/books/310859/the-sense-of-style-by-steven-pinker/9780698170308/) | Publisher metadata/sample, not full text; not read | Clear technical explanation, microcopy/copy rhetoric; test transfer instead of assuming English prescriptions universal | Medium, T3 |
| ADD-10 | *Strategic Content Design* (Erica Jorgensen, 2026), [O'Reilly bibliographic preview](https://www.oreilly.com/library/view/strategic-content-design/9781808812170/) | Contemporary publisher preview only, authorship/edition metadata should be double-checked | Evidence-based content research, plain language and named screen actions | High, T2 |

**Avoid claim inflation:** books inside the user's CSV are **already** in the incoming 82; ADD-01–10 are additional *bibliographic leads*, not a verified net-unique master inventory. The 2026 O'Reilly metadata for `ADD-10` includes publisher/author formatting that warrants a human bibliographic audit before acquisition.

## Study priorities for an actual product task
1. **Before Faneqo homepage:** Chimero Ch1–3 (purpose / craft / exploratory constraints), Covert selected language and architecture, Dow 1914 value hierarchy and **actual** notan figures later. Add no forced citations to a simple bug.
2. **Before role/IA redesign:** direct sections of Covert + authorized Goodwin passages (once obtained), and actual current app code/user evidence.
3. **Before signup-form overhaul:** legit access to Jarrett/Gaffney, actual W3C and current form component patterns, then real task testing.
4. **Before complex brand/story work:** verified McCloud visual panels and historical Dow figure study; not descriptions of artwork we have not inspected.
5. **Before broad systems change:** Meadows/Brand/Alexander cautiously as analogies, never authority to rewrite real permissions or make business claims.

## License/ingestion and count rules
- `CATALOGED` ≠ `IDENTITY_VERIFIED` ≠ `FULL_TEXT_ACCESS_VERIFIED` ≠ `SECTIONS_STUDIED` ≠ `VISUAL_EXAMPLE_STUDIED` ≠ `APPLIED` ≠ `OUTCOME_EVALUATED`.
- Keep whole copyrighted books outside public skill outputs/repo unless authorized; use original source-linked analysis and exact inspected excerpts in suitable limited form.
- Counts refer to rows in specific inventories with separate ID namespaces. Never silently assume name-variant rows represent distinct books or that a sales page is an accessible PDF.
- A source that becomes irrelevant should be deprioritized; measured skill gains and user benefit matter more than sheer book volume.

## Next catalog maintenance
Reconcile via `python scripts/reconcile_ux_book_canon.py` in the Lab repo; manually review uncertain matches and editions before promoting counts. Prioritize actually reading and inspecting the best sources, not downloading 100 items at once. This process uses stdlib and modest RAM (suitable for a constrained 8GB machine).
