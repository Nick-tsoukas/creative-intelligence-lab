# Conditional UX Decision Cards — v0.3

Compact expert reasoning, not universal rules. Choose at most **two** cards relevant to the job. **Source** says what was actually studied; **hypothesis** is our transfer to a specific product. Additional citations: `TASK_SOURCE_ROUTER.md` and original `SOURCE_LEDGER.md`.

## C01 — Begin with the human verb
**Trigger:** steps are named after backend objects or features. **Ask:** what is the person attempting, from where, and what counts as success? **Do:** map natural-language job → entry → necessary decisions → result; preserve prior context. **Avoid:** building a new workflow to satisfy taxonomy labels. **Counterexample:** expert operators may need direct access to advanced objects; do not remove it.
**Source:** Keith, *Resilient Web Design*, Ch 6 (read); Boulton, *Designing for the Web*, Ch 7 (read). **Transfer:** design hypothesis until actual task flow observed.

## C02 — Visible does not mean findable or understandable
**Trigger:** icon or action exists yet users miss/misinterpret it. **Distinguish:** detection, discrimination, recognition, location/search, meaning, action consequence. **Do:** match likely vocabulary and entry point; add explicit label and visual grouping if necessary; check the first click. **Avoid:** recommending bigger/brighter icons without checking semantics. **Counterexample:** established expert workflows may rely on compact iconography or keyboard shortcuts.
**Source:** Hornbæk et al., *Introduction to HCI* (2025), Ch 3 selected passages read (see Dossier 008). **Transfer:** inference, not product-tested fact.

## C03 — Shared UI ≠ identical domain operation
**Trigger:** two composers/cards/dialogs inconsistent, or consolidation proposed. **Do:** inventory which behavior may be shared (draft, attachments, input, feedback) and what must remain distinct (recipient type, ownership, privacy, moderation, idempotency). Route multiple entry points to a canonical *contract*, not necessarily the same screen every time. **Avoid:** a fake universal composer sending broadcast as private chat. **Counterexample:** genuine workflows with different risk/complexity can require different review steps even with shared primitives.
**Source:** Frost, *Atomic Design*, Ch 2 directly read; Lynch/Horton, *Web Style Guide*, Ch 4 read. **Transfer:** original synthesis.

## C04 — Separate visibility, audience and transmission
**Trigger:** sharing media, messaging fans, publishing events, or permission changes. **Do:** define separately who can see stored media, who may be notified, who is eligible to receive, who owns it, what “public” means, and how authorization is checked. Preview consequences before irreversible changes. **Avoid:** toggling media to public as a hidden side effect of attaching/sending. **Counterexample:** explicitly public content may be intended; permit it only by an authorized, understandable path.
**Source:** Lynch/Horton Ch 4; Costanza-Chock selected *Design Practices* chapter sections (read). Actual security/policy rules must come from **current app code/spec**, not books.

## C05 — Tell the truth about system progress
**Trigger:** status mismatch or async operations. **Do:** model draft → validated → submitting → accepted/queued → processing → sent to provider → delivered or bounced, using only distinctions backed by backend evidence; add failed/retry/unknown states and timestamp as appropriate. **Avoid:** “sent” as a synonym for “queued”, fake success toasts, or duplicating requests on retry. **Counterexample:** product may lack delivery telemetry; show “queued” or “status unknown,” not an invented delivered state.
**Source:** Keith Ch 5; WCAG 2.2 status message guidance (standard, not book); domain-specific state contract requires inspection.

## C06 — Recover before you celebrate
**Trigger:** drafts, forms, uploads, QR edit, or intermittent venue connectivity. **Do:** define progress persistence, back/refresh, safe cancel, pending state, retry, duplicate prevention and conflict recovery; test with interruptions. **Avoid:** animations or snackbars that imply persistence without a server or local save contract. **Counterexample:** highly sensitive data may deliberately not persist; state this clearly.
**Source:** Keith Ch 5 (read); Boulton Ch 8 (read); relevant W3C WCAG success criteria are external standards. **Transfer:** task-specific contract.

## C07 — User authority is not permission authority
**Trigger:** content, fan identity, collaborative roles, real recipients, unsafe default. **Do:** separate creator/editor/manager/operator/recipient and actual backend rights; model who can view, publish, retract, resend, revoke, delegate. Gather affected-user evidence; don't equate fictional personas to real consent. **Avoid:** new permissions, loopholes or silent policy changes to simplify the UI. **Counterexample:** anonymous/public viewing has different rules; enforce actual product policy.
**Source:** Costanza-Chock, *Design Justice*, selected chapter sections; actual app authorization inspected separately.

## C08 — The environment changes the task
**Trigger:** show, backstage, merch booth, phone, dim light, one hand, interruptions, accessibility. **Do:** specify device, lighting, noise, movement, connectivity, attention, user agency and alternative path; design for resume/skip/later. **Avoid:** assuming that fans want to use phones during performances or that staged demographic personas are evidence. **Counterexample:** advanced desktop workflows may intentionally trade simplicity for density.
**Source:** HCI 2025 selected Ch 3 and Design Justice selected sections; music-industry context must come from published/field evidence when available. **Most situations are hypotheses until observed.**

## C09 — Meaning before aesthetic geometry
**Trigger:** design looks polished but action hierarchy is wrong. **Do:** state intended meaning, primary/secondary actions and audience; then hand to creative-design-director for image/typography/rhythm options, with UX constraints intact. **Avoid:** prescribing pixels/animation when problem is conceptual. **Counterexample:** a pure art-direction study may be intentionally open-ended; differentiate it from an operational workflow.
**Source:** Vignelli, *The Vignelli Canon*, selected Semantics/Syntactics spreads directly studied; Boulton Ch 13. **Status:** design philosophy / interpretation, not scientific proof.

## Escalation rule
If a problem threatens wrongful exposure, unauthorized access, irreversible sending or real-world safety, triage it first with `ISSUE_RUBRIC.md`, then hand technical enforcement and release decisions to the actual product engineering/security owner. Do not substitute elegant UX for real checks.
