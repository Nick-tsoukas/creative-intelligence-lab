# Worked UX Decisions — Examples for Claude v0.3

**Use only as reasoning demonstrations.** These are not executed Faneqo audits, confirmed backend facts or approved specifications. They model concise, evidence-honest UX outputs.

## Example A — “I can compose two different ways and neither makes sense”

**Reported:** founder describes two distinct message composition screens; one makes media/galleries less discoverable. **Not observed in this skill package:** current routes, screenshots, permission implementation, audience eligibility, delivery logs.

**Human job:** when an artist has just finished a show, send a gallery to eligible show attendees without exposing private photos or losing a draft.

**Primary diagnosis:** likely *architecture/continuity + comprehension*; the differences may be legitimate if one composer is private chat and another is broadcast, so first map semantics rather than forcing identical UI.

| Transition | Proposed expectation | Required product truth |
|---|---|---|
| Night → Messages | Preserve current artist/show; show action “Message attendees” | Server ownership/eligibility; valid Night |
| Compose → Gallery | Draft text persists; gallery visibility explicit | Draft persistence and permitted attachment API |
| Back from Gallery | Restore draft and eligible-audience context | Stable draft ID and route state, if supported |
| Review → Send | Explicit scope, target count, privacy and channel | Server-authoritative recipient eligibility and policy |
| Accepted → Sent | Honest queued/sent/delivered states | Backend job/provider status and idempotency |

**Smallest repair:** adjust entry label/route and draft context; show recipient summary. **Larger option:** consolidate compatible composer flows around shared components, preserving different recipient contracts. **Never:** publish gallery implicitly or relax send limits because UX is confusing.

**Verification after authorization:** one working artist role; invalid Night role; draft survives navigation/refresh; private gallery remains private where policy says so; duplicate-click and failed-send behavior; keyboard and mobile flow; explicit fan identity protection. **Evidence label:** recommendation/hypothesis; not tested.

**Sources:** Keith Ch6; Frost Ch2; Lynch/Horton Ch4; Costanza-Chock selected chapter sections.

## Example B — “Download QR does nothing; unknown codes land on another band”

**Reported:** founder previously observed these defects and later reported corrections working. **Not verified by this document:** which deployment is live or which routes implement fixes.

**Human job:** create an artist QR, download it, print/use it, let a fan scan and reach the correct artist; handle unknown/expired codes safely.

**Diagnosis:** separate *file-export feedback*, *identifier resolution correctness*, *physical scan usability*. Different defects require different evidence.

| Symptom | UX impact | Safe response | Verification |
|---|---|---|---|
| Click Download does nothing | Primary task blocked (P1) | Visible progress/success/failure; validated file download | Authenticated manual download + file inspection |
| Unknown QR redirects to an unrelated artist | Wrong target / trust harm (P0 if reproduced) | Explicit invalid/unrecognized state, safe path to artist search/home; no guessed fallback | Server resolver negative cases and scan |
| Code scans but landing is confusing | Comprehension/discoverability (P2 subject to impact) | Clear artist/show identity + next safe action | Real device first-use observation |
| Edited code breaks printed posters | Destructive continuity risk (potential P0/P1) | Clearly define stable-target vs reissue semantics, review/confirmation | Existing printed code on representative devices |
| Scan analytics count = “fans” | False data interpretation | Label scan, follow, attendance distinctly | Definitions/analytics contract |

**Smallest repair:** correct export action and wrong-target resolver; don't replace QR model wholesale. **Larger option:** one lifecycle management experience with preview/print/scanning guidance and scoped permissions. **Never:** weaken backend ownership checks or quietly re-route unknown codes.

**Evidence:** reports only; risk classification conditional on reproduction. **Sources:** HCI Ch3 for finding/recognition, Keith Ch5 for resilience, actual QR technical standards for scan conformance when inspected.

## Example C — “A site looks stunning but nobody sees the actual action”

**Reported only:** vague aesthetic praise/complaint. **Method:** classify whether UX task is findability or artistic identity. Identify the intended first action and likely entry before modifying page design. Ask creative-design-director for a thesis and 3 distinct visual directions only if the problem is meaning/art direction; frontend-design handles implementation. Keep labeled controls and task semantics stable.

**Counterexample:** an editorial/artist storytelling page may intentionally prioritize mood over immediate conversion; do not impose a giant CTA without understanding audience intent. **Sources:** Vignelli Semantics/Syntactics; Boulton Hierarchy; HCI Ch3 (section-scoped).
