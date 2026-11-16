# Pattern 02 — Media Source Selection & Resilient Upload

**Use when:** creators add photos, audio, video or linked media within a larger narrative. **Status:** original UX/design research brief, not a shipped component.

**Discovery:** Mobbin/Refero, Nuxt UI https://ui.nuxt.com/, Uppy https://uppy.io/, W3C APG https://www.w3.org/WAI/ARIA/apg/. Specific reference-screen behavior **not visually or functionally verified**.

## Visual composition
A visually calm one-job-at-a-time picker: clear recognizable source icon, meaningful label and short hint, grouped by **local upload vs external link**. Show the selected media, title, caption, target audience, upload state and primary action in a sequential surface without burying error messages.

## State matrix
`EMPTY → CHOSEN_SOURCE → VALIDATING → UPLOADING → PROCESSING → READY → SAVED_DRAFT / PUBLISHED`, plus `VALIDATION_ERROR`, `NETWORK_ERROR`, `CANCELLED` and `RESUMABLE` where backend supports it. Never label "uploaded" as "published". Don't advertise resumable behavior unless supported.

## Key decisions
- Scope: file upload ≠ YouTube/Spotify embed; test URL validation and embedding policies.
- Security: enforce permissions, consent, public/private distinction and storage authorization at backend.
- Reliability: real bytes and file-size constraints; idempotency and progress/retry states; server truth.
- Copy: distinguish publish for everyone vs save draft / limited audience. Don't hide consequence behind an icon.
- Mobile: choose file/record, handle keyboard, close/reopen, lost connection and large videos.
- Art: media preview can evoke cultural context, but utility controls must remain legible and fast.

**Reject if:** upload successes are optimistic fiction, file selection is hidden, cancel is destructive, private media becomes public, an external link is treated as uploaded bytes, or art direction blocks the main action.

**Study next:** one real audio upload flow and one video upload flow, each observed at mobile and desktop with error/failure states and rights-aware screenshots.
