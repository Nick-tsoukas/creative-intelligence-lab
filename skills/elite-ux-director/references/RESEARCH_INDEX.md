# Research Router — Problem → Source-Checked Mechanism (v0.5)

**Purpose:** answer “which specific study changes this decision?” without reading a huge catalog or forcing an art-direction process on every task. Read this on a **research-rich task** or when the current cards don't resolve a real conflict; otherwise the existing `TASK_SOURCE_ROUTER.md` and core C/H cards suffice.

| Problem type | First card(s) | Exact studied source and status | When NOT to use |
|---|---|---|---|
| A homepage visually overwhelms its message | K05 then K01 or K09 | Chimero Ch1; Dow 1914 text; Vignelli selected spreads | Pure art-direction exercise where ambiguous mood is intentional |
| Every screen is equal-weight card soup | K01 + K02 | Dow early composition text, figures not studied | Equal-choice lists or expert dashboards |
| Naming/IA fails across screens | K03 then K04 | Abby Covert selected author-hosted pages | Confirmed code-only bug |
| Two composer flows look similar | K07 | Frost Ch2 + Covert selected IA pages | Backend contract identical and clearly proven |
| A control is visible but users cannot find it | K08 + K04 | 2025 HCI Ch3 selected passages + Covert | Already confirmed API outage |
| Visually dull yet usable experience | K06 then K05 | Chimero Ch2 + Ch1 | Unapproved product redesign; high-stakes clarity risk |
| Visual system polished but semantically wrong | K09 then K05 | Vignelli selected spreads + Chimero | Aesthetic-only change with no content/meaning uncertainty |
| Learning from artwork/figure | Load `VISUAL_ANALYSIS_PROTOCOL.md` | Author original page/figure must actually be seen | Only caption/OCR available |
| Reading a book, not auditing UI | Load `BOOK_STUDY_PROTOCOL.md` | Original text + precise edition/section | Ordinary short UX task |
| Two authorities disagree | Load `CROSS_BOOK_SYNTHESIS.md` | Exact studied sections of both; retain disagreement | Single clear backend/permission fact |

## Retrieval behavior
1. Inspect task and **current product** first. If ordinary UX, use C/H/P cards only.
2. For a genuinely knowledge-dependent problem, `python scripts/retrieve.py list knowledge` prints compact headings or `python scripts/retrieve.py knowledge K03` returns exactly one K-card. No Python? Open this Markdown and manually select only the matching section in `KNOWLEDGE_CARDS.md`.
3. Normally load **one or two K-cards total**, not two K plus two C plus two H. Prefer the narrowest relevant set; stop retrieving when enough decision value exists.
4. Check original reading claims through `SOURCE_LEDGER.md` and, if accessible, the Lab dossier; **do not invent quotes or studied artwork**. New candidate source titles from the uploaded manifest are not read evidence.
5. Create a decision with conditions, counterexample and falsification; preserve user research/real product facts over abstract book tradition.
6. If no relevant source exists, solve the user's task with ordinary engineering/product evidence and log a *new reading question*. Don't hallucinate an expert answer.

## Study index / provenance
- `K01–K02` → Lab `reading-dossiers/013-DOW-COMPOSITION-HARMONY-AND-HIERARCHY.md` (selected text, 1914 9th ed; separate limited No.16 visual study in Dossier 016).
- `K03–K04` → `reading-dossiers/014-COVERT-INFORMATION-ARCHITECTURE-MICROSTUDY.md` (selected original pages only).
- `K05–K06` → `reading-dossiers/015-CHIMERO-WHY-CRAFT-AND-FEEDBACK.md` (two chapters only).
- `K07` → `reading-dossiers/010-FROST-ATOMIC-DESIGN-METHODOLOGY.md` and Covert selected.
- `K08` → `reading-dossiers/008-HCI-2025-PERCEPTION.md` (selected Ch3).
- `K09` → `reading-dossiers/009-VIGNELLI-CANON-SEMANTICS-AND-GRID.md` (selected spreads).

## Library source catalogs vs actual learning
- Legacy Lab `sources/UX_DESIGN_BOOK_CATALOG_2026-11-15.md`: 130 candidates, 27 direct full-access works and 103 bibliographic leads, not 130 completed readings.
- New user intake `sources/intake/2026-11-15/ELITE_UX_DESIGN_SOURCE_MANIFEST.csv`: **82 books + 40 other references** marked **not-ingested**. Do not add 82 to 130 and claim independent new titles; multiple duplicates/edition variants exist.
- Reconciliation and high-priority source intake `sources/BOOK_CANON_RECONCILIATION_2026-11-15.md`. Source-book acquisition research and reading are separate stages.
- No new real participant test, conversion metric or formal Claude skill benchmark was performed in v0.5.

**Knowledge is valuable only if it improves a real decision.** Delete/revise an unhelpful card rather than generating a new one for every book section.
