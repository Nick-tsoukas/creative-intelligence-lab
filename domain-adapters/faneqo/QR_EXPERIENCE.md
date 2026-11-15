# Faneqo QR Experience — Domain Adapter (Research/UX Only)

**Scope:** use only for Faneqo QR tasks. This card does NOT attest to today's frontend/backend implementation. The founder has previously reported problems with dashboard QR download and unknown QR codes resolving to the wrong artist, and later reported those fixes working. Treat those statements as **REPORTED**, not independently rechecked here. Prior fixes are regression targets, not proof every QR surface works. Confirm implementation and production status from current Faneqo repositories before asserting specifics.

## User-facing jobs (independent of implementation)
- **Artist owner:** create a valid artist QR, know where it goes, download/share/print it, and use the same QR over time as promised.
- **Artist/manager:** manage an event/show QR in the correct artist context and understand safe edit/replacement effects.
- **Fan:** scan a clear physical/digital code in a distracting environment, know the destination is the intended artist/show, make an informed choice to follow/check in, and recover when offline or denied camera permission.
- **Team or agency operator:** select the correct band/show before exporting/editing; avoid exposing another artist's code or changing a code already printed.
- **Support/analytics:** distinguish scanned requests, successfully resolved destinations, verified check-ins and fan follow conversion; avoid duplicate/false statistics.

These are **provisional job statements**, not verified persona research; see `PERSONA_AND_CONTEXT_METHOD.md`.

## QR UX and integrity matrix
| Journey | Primary contract | Common failure / user risk | What to verify |
|---|---|---|---|
| Create | Server-authoritative owner + entity, correct slug/target, unique intended code, saved success | Wrong band/show, empty target, duplicate code or stale file | Creation route/API, stored destination/owner, logged-in role |
| Preview | Clearly show intended target, label/code context and basic scan-readiness | Pretty QR that cannot be scanned, wrong logo/contrast/quiet zone | Actual generated payload and multi-device camera reading, not screenshot alone |
| Download | Action returns valid image/file with correct name/format and clear feedback | Click does nothing, expired blob, bad encoding/size, mobile cannot save | Authenticated actual download + file decode + printer-ready physical scan |
| Edit | Explicit whether physical code stays stable, target redirects, or code must be replaced | Printed code silently re-routes; wrong artist targeted | Change history, immutable vs mutable code rules, confirmation and rollback |
| Scan | Unknown code is handled safely; valid resolves only to intended owned entity | Unknown code redirects to unrelated artist (P0); ambiguous expired/unpublished state | Public route and backend resolver, invalid/corrupt codes, permissions, event lifecycle |
| At venue | Fast, readable landing/action; permission request has fallback | Dim lighting, weak network, phone interaction during performance | Real device/venue constraints, camera denied/offline, later reconnection |
| Follow/check-in | Distinct fan consent and attendance status; no invisible enrollment | Scan incorrectly treated as follow or check-in | Product policy, explicit user flow, server logs and consent model |
| Analytics | Metrics labeled honestly (scans vs unique visitors vs checked-in fans) | Inflated “fans acquired” from repeated scans | Definitions, de-duplication, privacy retention and event/band isolation |

## Hard invariants
1. Unknown, malformed, expired or disabled QR identifiers must not silently resolve to an unrelated artist or show.
2. UI authorization and backend validation must agree; no “owner-only” QR edit enforced only by disabled frontend controls.
3. Scanning a code does not imply consent to be enrolled or messaged. Any opt-in is separately designed and verified.
4. Export/re-issue must explain impact on already distributed/printed codes.
5. Generated QR imagery and underlying URL/identifier must match. Visual customizations must not break real device decoding.
6. When network, permission or destination fails, give a safe explanation/retry/manual fallback; do not invent valid targets.
7. Never expose secret tokens or personal fan data in a public QR payload or a debug URL.
8. Keep scan telemetry separate from check-in, follow and message eligibility; meanings are defined by current product policy.

## Suggested audit order (no production changes implied)
1. Inventory all QR surfaces and purposes: artist Headquarters, dashboard download/share, events, Show Mode and any Creative Studio/print outputs. Confirm actual routes before adding to the list.
2. Trace one known-good artist QR and one known-good event/show QR from creation through decoded URL, storage, download, external phone scan and intended destination.
3. Inspect mutation semantics: edit vs regenerate vs deactivate, ownership checks, printing consequences, unknown/expired/disabled handling and public fallback.
4. Enumerate negative cases: malformed identifier, dead artist, unauthenticated scan, wrong owner edit, stale cached export, duplicate save, offline, phone denied camera.
5. Map trust boundaries; rank P0 wrong-target/privacy defects over visual decoration; propose minimal repair before “elite look” improvements.
6. Verify the prior **reported-fixed** dashboard download and unknown-target regression with authorized accounts/synthetic codes when product work is authorized.
7. Only then refine QR design/printing guidance, scan landing hierarchy and venue interactions.

## Faneqo cross-feature caution
A fan scanning a Show Mode QR, visiting artist Headquarters, following an artist, attending a Night and becoming eligible for messages are **not automatically equivalent** states. Map actual transitions; preserve consent, ownership and anti-abuse protections. Do not create a new QR/check-in backend model merely for better UX.

## Sources and evidence
This adapter is a task-specific application of `INTERACTION_PATTERNS.md` P5 and `DECISION_CARDS.md` C02/C05/C06/C07/C08. HCI 2025 selected Chapter 3 informs human perception and visual search but does **not** certify QR scanning technical conformance. Verify QR encoding/scanning against actual generator and relevant standard/vendor documentation before technical claims. Current Faneqo architecture and regression status remain to be inspected when a QR task is authorized.
