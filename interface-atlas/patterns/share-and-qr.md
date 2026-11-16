# Pattern 04 — Share a Real Destination (URL + QR)

**Use when:** content has a stable public/shareable route that can be distributed by link, device share sheet or printed QR. **Status:** original contract, not a confirmed product flow.

**Research:** official browser Web Share API https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share ; W3C APG (dialog/focus semantics), real mobile share flows to inspect from Mobbin/Refero. The sources are research candidates; no particular application's UI was visually audited here.

## Essential trust rule
**The QR and copied link must resolve to exactly the same verified intended resource** with correct access, role and expiration behavior. A decorative QR in an event poster is NOT a checked-in or Night-specific code by default. Never make a second QR/resolver without product authorization.

## Design
One clear “Share” action opens a concise sheet with URL/copy, native share when supported, QR preview/download where supported, and accurate scope disclosure (public, link-only, attendee-restricted, unpublished).

## Behavior
- Copy gives actual copy result; error handling if clipboard permission denied.
- Native share has fallback; doesn't falsely report “sent” on dismiss.
- QR rendered from canonical URL; verify mobile scan to exact destination in real testing.
- If content is draft/private, don't expose its URL or assets accidentally.
- Screenshot/PDF/printed QR is not the same as a dynamically permissioned deep link.
- Mobile/share sheet: large touch targets, readable destination and clear dismiss/keyboard focus.

**Reject if:** QR sends visitors to generic homepage when Night link was requested, copy returns outdated URL, link bypasses access, or sharing button promises send completion when only share sheet opened.

**Next evidence:** exact current target route and actual device/browser share behavior; rights/security checks.
