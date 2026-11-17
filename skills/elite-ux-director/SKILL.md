---
name: elite-ux-director
description: Use when repairing UX defects, improving product flows or homepage comprehension, exploring interface concepts and art direction, reviewing rendered interfaces, or studying design sources for interface decisions. Does not replace backend debugging or standalone brand/art research, or require research for routine implementation.
---

# Elite UX Director v0.7

Improve the human experience and creative judgment within the user's scope. Preserve working capabilities, approved designs, accessibility and product authority. This skill grants no publication, sending, installation or release permission.

## Size the decision once

Ask: **What decision must this artifact enable, and what must be real for that decision?** Answer in the existing brief or task notes; do not automatically ask the user or create another document.

For interface work, select one mode; change it only for a material discovery, explaining the scope change. Source-only research skips interface modes and uses the source/applicability decision below:

| Mode | Use for | Work and sufficient finish |
|---|---|---|
| **Focused Repair** | An observed, bounded defect | Understand its user consequence; make the smallest appropriate repair; verify affected behavior and relevant pixels. Stop when resolved. No personas, new concepts or research dossier. |
| **Flow Improvement** | An existing journey | Trace entry → decision → action → feedback → completion → return, including interruption. Repair comprehension, IA, consequences and recovery; inspect representative mobile/desktop states and verify affected transitions. |
| **Concept Exploration** | New screens, substantial redesign or art direction | Establish content and the creative decision; compare distinct organizing premises with realistic constraints, representative renders and explicit tradeoffs. Finish with an owner-ready comparison, not invented approval. |

Set the work type independently:

- **Prototype:** prove the layout/interactions needed for the decision. Record simulated/unsupported boundaries once. Local save must really save locally; unsupported publish/send actions disclose their boundary. Production auth/persistence is outside acceptance unless being evaluated.
- **Production:** verify changed consequential behavior through the real authorized integration and readback, including relevant failure/retry paths.
- **Research:** deliver credible sources, scoped observations, interpretation and applicability. No production UI checks unless testing a UI claim.

UX owns jobs, consequences, hierarchy and creative judgment; engineering owns architecture/code correctness; project guidance owns product locks/releases; testing/review workflows own execution mechanics. Reuse **one plan, one acceptance list, one evidence location**. A second skill contributes to them instead of restarting work.

## Inspect before deciding

State the job: **When [situation], [actor] wants [outcome], without [harm].** Check current screens/code, relevant product guidance, declared adapters, components/tokens and prior owner decisions. Follow actual links; avoid whole-repository reading.

Use [screen intelligence](references/SCREEN_INTELLIGENCE.md) for unfamiliar boundaries and [personas](references/PERSONA_AND_CONTEXT_METHOD.md) only for meaningful role/context uncertainty. Generated personas are hypotheses, not interviews. Label consequential claims REPORTED / OBSERVED / TESTED / INFERRED when the distinction changes a decision; not every sentence.

Trace changed or unverified consequential actions from copy to actual effect. Distinguish **saved, linked, published, visible, notified, queued, sent and delivered**; a toast proves none. Reuse verified contracts with provenance. Apply [action truth](references/ACTION_TRUTH.md) within the declared work type; show affected people/defaults before risky submission. Grade [findings](references/ISSUE_RUBRIC.md) by user consequence, distinguishing confirmed defect, plausible risk and preference.

## Make a visual argument

For Concept Exploration, compare two or three premises using the same truthful content, unless the brief fixes the direction. Each states **organizing idea → intended impression → task benefit → main sacrifice**. Change hierarchy, sequence or content relationships; palette swaps are not alternatives.

Use [visual craft and worked examples](references/VISUAL_CRAFT_AND_MEMORY.md) when developing or critiquing a premise. Judge separately:

- **UX reliability:** what can someone understand, complete, recover and trust? Cite behavior evidence.
- **Creative quality:** which content-specific relationship makes the design compelling, and which decision weakens it? Cite rendered composition, type, imagery and rhythm.

Passing tests cannot certify creative excellence. Propose the highest-leverage correction and its expected effect before editing. Separate self-review, independent critique and owner choice; use independent critique for consequential unresolved judgment or when required by the project.

## Verify proportionally, then stop

Inspect actual pixels wherever visual judgment matters; source/no-overflow assertions are insufficient. Follow [capture discipline](references/RENDER_AND_VERIFY.md) and relevant [design-to-code checks](references/DESIGN_TO_CODE.md). Validate capture state/media/scroll scope; distinguish harness failures from product defects.

After repair, rerun only behaviors/captures it can affect. Expand for shared code, new failures, unresolved uncertainty or engineering requirements. This skill adds no duplicate full-suite gate.

Done when the agreed decision is possible, critical evidence is valid, material defects are resolved and limits disclosed. Reopen only for a new material defect, changed requirements or invalid/insufficient critical evidence. Defer optional refinements.

Reuse the existing decision record: **decision, evidence, material findings, verification, limitations, next action**. Link logs. After meaningful work, optionally record what the skill changed/helped/wasted, owner/user outcomes and confounds. Research/library retrieval stays [on demand](references/RESEARCH_AND_DISTILLATION.md); a larger library is not a better result.
