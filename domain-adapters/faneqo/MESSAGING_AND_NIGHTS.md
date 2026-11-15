# Domain Adapter — Faneqo Messaging, Show Mode, Nights and Galleries

**Scope:** interpret only for authorized Faneqo UX tasks; do not automatically change production. Derived from founder-supplied Unified Messaging & Night Experience mission, not an independently verified current repo audit.

## Canonical distinctions
- **Show Mode:** existing show attendance/check-in; don't introduce another QR or check-in model.
- **Night:** recap/memory of a specific show.
- **Messages:** shared canonical artist-to-fan workspace for broadcasts, private conversations, history.
- **Message attendees:** explicit scoped audience inherited from specific Night; verify band/show ownership server-side.
- **Message all fans:** different audience; don't silently change recipients.
- **Private fan chat:** one-to-one thread, not large broadcast group chat.
- **Campaign:** can be queued/sent/fail; do not imply delivery solely from queue status.
- **Gallery:** separate visibility/publishing lifecycle from messaging/notification audience. Do not enable uncertified protected-gallery delivery.

## First journey to audit
1. Artist opens an ended Night, presses **Message attendees**.
2. Canonical Messages workspace opens; show identity and eligible audience are apparent and accurately scoped.
3. Artist writes; attaches authorized Night link and selects or creates compatible gallery.
4. Gallery create returns to unfinished draft with context retained. Visibility stated explicitly.
5. Artist previews, reviews audience and channel, and sends through existing guarded system.
6. Artist observes truthful campaign state; can inspect Sent and continue private responses.
7. Return to Night is straightforward, including on mobile/back/refresh.
8. Generic all-fans broadcast and private fan chat remain intact.

## Crucial edge cases
- Night inaccessible/not owned by band; stale/deleted event; invalid return URL.
- Zero eligible recipients vs raw attendance count.
- Send limits, channel eligibility, email cooldown, idempotency/duplicate click and delivery failures.
- Gallery created but upload partial; gallery saved but not published; public/private exposure; show link permission.
- Draft recovery when dialog closes, route changes, browser refreshes, mobile keyboard appears, device loses connectivity.
- Repeated anonymous fan labels, message requests, unread state, conversation search.
- Empty conversation space must be useful without fictitious counts/content.
- Screenreader chat announcement flood; receiving replies should not steal focus.

## Scope rules
Do not modify artist payment, Stripe, production Strapi, S3 permissions, live fans, show check-in, or auto-deploy. Work in real local Nuxt 3 application only when owner has separately authorized that implementation. Existing mission says local-only and owner acceptance required.

## Candidate UX test tasks (not executed)
A. Starting from an ended Night, message only eligible show attendees and know who will receive it.
B. Create and attach Night gallery without losing draft; identify who can see photos.
C. Deliberately fail upload and return safely to message.
D. Verify a broadcast is queued vs actually delivered.
E. Reply privately to one fan without confusing it with a campaign.
F. Find one of two identically labeled anonymous fan conversations using available safe context.
