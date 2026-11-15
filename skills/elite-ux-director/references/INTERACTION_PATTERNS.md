# Interaction Contracts — Task-Specific Patterns v0.3

This is a **design reasoning library**, not drop-in implementation code or permission policy. Choose only the pattern named by `TASK_SOURCE_ROUTER.md`. For any pattern, inspect real routes/backend and identify what is **observed**, **reported** or **hypothetical**. Keep a separate server-authoritative rights model.

## P1 — Human job to discoverable entry
**When:** user says a task is hidden behind confusing features. Model:
`situation/actor → goal verb → likely starting surface → entry label → inherited context → essential decision → outcome → next step`.
**Required questions:** where would a novice look? Is the action visible in their vocabulary? Can an expert still access it? Is the same intent discoverable from more than one legitimate context? **Example (hypothesis):** from a completed show, “Share photos with attendees” may be clearer than “Create campaign attachment.”
**Evidence check:** distinguish screenshot visibility, actual user first-click behavior, and backend state; never treat them as equivalent.

## P2 — Multi-entry canonical flow, semantically distinct variants
**When:** actions duplicated across screens. Map all entry points to the same underlying business intent, then list required invariant and variable fields.
- **Invariant:** named user job, draft identity, context, consistent component semantics, progress states, interruption handling, return path.
- **Variable:** recipient scope, channel, privacy, content type, review confirmation, permissions, throttling.
- **Potential architecture:** one underlying composer system and reusable subcomponents, with explicit variant contracts. Do **not** require identical rendered screens if risk differs.
**Decision:** choose minimal repair (labels/route/persistence) versus consolidation only after mapping state and API differences. Reject shadow service implementations.

## P3 — Consequential submission and truthful async outcomes
Use this state table; replace labels with actual backend truth:

| State | User-visible claim | Verification needed | Recovery |
|---|---|---|---|
| Editing draft | Unsaved / locally saved / server saved (exact truth) | Storage and expiration | Restore / discard |
| Validating | Checking audience / inputs | Current server-authoritative eligibility | Explain validation failure |
| Submitting | Request in progress | Endpoint response, lock / idempotency | Disable accidental duplicate, retry when safe |
| Accepted or queued | Queued, not delivered | Job/campaign identifier | View pending history |
| Processing | Processing / sending (only if known) | Provider status | Safe reload and status refresh |
| Delivered or partially delivered | Only if supported by telemetry | Recipient-by-recipient / provider semantics | Inspect failures / follow up |
| Failed/unknown | Failed or confirmation unavailable | Server idempotency and retry safety | Preserve draft, avoid second send if uncertain |

Never assume the backend supports delivery evidence. Differentiate fan reply notifications from new group-chat membership.

## P4 — Media / gallery publishing and sharing
Separate lifecycles:
- **Media object:** upload pending → uploaded → failed / removed.
- **Gallery collection:** draft → saved → publishable → published / hidden / deleted, according to actual app.
- **Audience access:** who can open/view right now, independent of a notification.
- **Message attachment:** reference/link/preview according to authorization, independent of publishing.
- **Fan consent:** participation in a show/following is not an automatic permission to expose all media publicly.

**Required user-visible review:** chosen gallery, current visibility, whether action changes visibility, eligible recipients, irreversible consequences, post-send ability to retract/hide. **Do not invent a security model or assume hiding revokes cached copies.**

## P5 — QR artifact lifecycle (create → present → scan → edit → recover)
A QR is **both** a visual artifact and a server-resolved destination. Distinguish:
1. **Create:** source entity/owner and canonical target; generated data/format; predictable saved state; accessible label/alt description; size/export.
2. **Download/print:** export action feedback, actual file validity, readable contrast/quiet zone/scale, test with representative real phone/camera and printed conditions. Exact encoding/conformance limits require appropriate QR standard/product generator validation.
3. **Distribute:** which active QR and version? artist/event/band context, expired/deleted handling, offline venue signage, non-digital fallback.
4. **Scan:** unknown/corrupt/not-owned/disabled/expired vs valid target; user-visible explanation with safe next action. An **unknown QR must never silently resolve to an unrelated artist.**
5. **Edit:** define whether same code routes to updated destination or a reissued code, and what happens to physical copies; confirm before mutating an old live target.
6. **Analytics and privacy:** raw scan ≠ unique fan ≠ follow/check-in; do not infer identity from camera scans without evidence. Ensure server ownership check and avoid leaking private tokens.
7. **Recovery:** non-downloadable code, rejected scan, network failure, camera blocked, low light, app/browser differences, back/refresh, retry without duplicate entity creation.

**Invariant:** public URLs and scanned identifiers resolve using current verified backend rules, never guessed artist fallbacks. Treat scans and edits as distinct jobs; don't conflate decorative QR customization with scanner reliability.

## P6 — Forms: errors, completion, resume
Map each field: label, input type, format/help, required/optional, validation boundary, error position, server error and recovery. Detect invalid state before consequential submission where possible; preserve entered values on failure. Move focus/announce errors appropriately with actual semantics; do not create duplicate live regions. Support zoom/reflow, autofill, small touch targets and keyboard. Verify recent W3C WCAG criteria in app context.

## P7 — Situated mobile task (venue/backstage/crowd)
Document **situation, actor, attention, lighting, noise, gloves/one-hand, connectivity, role/permission, device, stakes and interruption** as explicit observed facts or hypotheses. Split tasks into before/during/after, allow resume and later completion, minimize required taps at show, provide noncoercive alternatives. Avoid claiming one simulated “fan persona” represents all. Validate with real users when available; do not demand founder testing for routine research work.

## P8 — Accessible dialog / tab / live notification
- Router navigation between pages: use links/active-page semantics; do not misapply tab roles.
- In-place panels with a tablist: consider WAI-ARIA tabs pattern and real arrow-key behaviors/focus; inspect framework implementation rather than blindly adding roles.
- Modal dialog: consistent open/close focus and blocked outside interaction when modal; Escape and return focus as appropriate; verify APG.
- Status/live updates: announce important changes without forcibly moving focus; for fast chat updates prioritize relevance and noise management.
- Verify actual keyboard, screen reader, reduced motion, zoom/reflow and 2.4.11 focus not obscured. Not verified by code lint alone.

## P9 — Multi-actor team and agency permissions
Create actor × action × object × scope matrix. Examples of *roles to verify*, not guaranteed Faneqo roles: solo artist, manager, agency staff, venue assistant, label collaborator, fan. Explicitly ask:
- Can actor access multiple artists?
- Which artist and show currently selected?
- Who may send, approve, edit public media, export data, view fan contacts, reassign ownership?
- Is permission revoked immediately on server or only masked in UI?
- What happens to drafts and links if their role changes?
Always include switching confusion, stale permissions, audit history and delegated workflows; do not add new roles until approved.

## General contract format
For each proposed state/action record `actor | context/entry | UI state | intent | trigger | client validation | server-authoritative permission/state | visible outcome | focus/navigation | failure/interruption/recovery | evidence status`.

Use one compact matrix for the significant transitions rather than turning every small design fix into a lengthy formal report.
