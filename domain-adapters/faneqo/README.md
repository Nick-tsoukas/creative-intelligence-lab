# Faneqo Domain Intelligence — Separate from Universal UX Skill

**Product:** Faneqo music artist/fan product. **Audience:** Claude when explicitly working in or analyzing Faneqo, **not** other projects. **Date:** 2026-11-15. This is a Lab evidence adapter, **not** a live production specification.

## Materials preserved
- [Messaging / Nights / Galleries](MESSAGING_AND_NIGHTS.md): actor and recipient semantics, Show Mode, campaign vs private conversation, gallery privacy and interrupted drafts.
- [QR Experience](QR_EXPERIENCE.md): artist/show QR create, download, print, edit, scan, resolver correctness and analytics. Reported prior fixes are regressions to verify, not proven current live behavior.
- [Worked UX cases](WORKED_UX_CASES.md): decision examples, intentionally marked hypotheses; not audit results.
- [Archived original source ledger](../../sources/UX_SKILL_PRE_V03_SOURCE_LEDGER_ARCHIVE.md): preserves older Faneqo transfers while the reusable package uses a smaller general source ledger.

## Ownership and retrieval boundary
This folder is NOT inside `skills/elite-ux-director/`. The universal skill is installed without these files and must remain useful for any app. In an **authorized Faneqo session**, supply this folder as a project reference when product/domain uncertainty requires it. Always verify current frontend/backend routes, actor/permission schema and product policy; these notes cannot supersede live code or founder decisions.

If Claude's working project is unable to read the Lab repository, copy/link this adapter **to a project-specific documentation location when permitted** and tell Claude where it is; do not inject this adapter into the universal personal skill folder. Updating Faneqo source files must follow current repo permissions, safe deployment and actual engineering acceptance.

## What is authoritative?
- **Current product code and backend authorization** for live implementation truth.
- **Owner-approved product decisions/spec** for desired behavior.
- **Direct actual user research** for people's jobs, vocabulary and context (when collected with provenance).
- **Published field studies** with method/source caveats.
- **These Lab examples** only as starting research hypotheses, never a silent product requirement.

## Separate workstream
The master plan's music-industry interviews/persona study belongs to its own scoped research track. Reconcile new verified field findings here after checking source ownership; do not overwrite ongoing researchers' files or fabricate participant results.
