# Pilot 002 — Faneqo Night Recap: Real Visual Reference → Original Design Premises

**2026-11-16.** **Status:** evidence-based *design briefing* only; NOT a new Faneqo frontend, not a user-approved replacement, not tested with artists/fans, not the current verified deployment. No screenshots or production user data copied into the public Lab repository. This pilot is original analysis of the owner-supplied Night screenshots (in prior ChatGPT conversation) and ten external screenshot previews, not an implementation.

## Primary problem / actual owner intent
Owner wants the show recap to feel like **entering a band's world**: cinematic, polished, spacious, emotionally significant, richly photographic, easy to navigate. The owner also explicitly liked a **simple Add Audio surface**, strong QR/link sharing, artist-selected video including a studio music video/song used at the show (not exclusively recorded that Night), and a beautiful editing experience.

### Observed in owner's screenshots (not current route re-verified)
- Current long dark Night view carries an oversized heading, compact date/venue, share/preview/edit, 6/3/0 counters, Story/Recordings and repeated two-column guitar-photo tiles and placeholder blocks. Equal-sized media items lose hierarchy; repeated captions and small actions make the page feel database-like.
- Editor screenshot shows a tall right overlay/drawer covering part of the page with hero image, QR/night photo, story, lineup and private notes stacked in plain input fields. The composer is distant from the narrative preview; utility controls are visually small.
- Existing QR artwork is present near the Night header, but screenshots alone do NOT verify what destination it resolves to. Do not claim the live QR route works.
- The beloved concept image is a separate **illustrative design**, not current verified app features; extra photo/video/audio counts in that concept are made-up demo values until independently confirmed.

## High-value reference synthesis from inspected specific images

| Evidence | Observed mechanism | Faneqo candidate move | Necessary contradiction |
|---|---|---|---|
| EI-002 Wax Poetics | Bold editorial rhythm, one strong story, deliberate asymmetry | Hero → one featured memory → meaningful chapters, not dozens of identical cards | Tight magazine copy can't become tiny mobile controls |
| EI-004 HEM Records | A visually expressive record field beside a compact, clearly separated playing UI | Music/video embeds in a Night, with legitimate media credit and unmistakable play/stop | Historical studio composite ≠ verified player implementation |
| EI-005 Lady Gaga site | Artist portrait is the environment; explicit event/promo actions remain overlaid | Credible human performance hero with clear *single* fan action and understated share | Too many floating offers hide visual meaning and CTA |
| EI-007 Tiptap editor | Calm document field and contextual toolbar | Inline Story editing; contextual formatting/keyboard, real save states | Plain-text backend ≠ free rich-text persistence |
| EI-008 Apple Photos Memory | One featured photographic memory with a visible See All destination | Curate dominant gallery image and meaningful groups; separate fan-facing collection entry | Older personal photos app ≠ fan consent or public gallery rights |
| EI-009 Uppy uploader | File source choices → previews → metadata/edit actions | Simple Photos / Video / Audio picker; clear file title/visibility/progress | Old Uppy screenshot ≠ current support/permissions or resumable uploads |
| EI-010 mobile audio player | Big obvious play control, timeline, reduced secondary controls | Beautiful first-class recording/music-video module | Spotify visual trade dress, artwork and song rights cannot be borrowed |
| EI-001 RCA Records | Curated artist/article sections, recognizable content grouping | Group media by Night role/artist curation rather than repeated gallery cards | Carousels can hide items and become inaccessible on mobile |

These are **PREVIEW_OBSERVED** art/interaction hypotheses. The Lab has not tested the original sites in a browser, inspected mobile reflow for each, or established user success.

## Three *different*, not cosmetic, original artistic theses

### A — Afterglow Journal (editorial-first)
**Premise:** the performance becomes a beautifully authored permanent record. Artist photography opens the page; a restrained event/date lockup sits in ample negative space. The narrative unfolds in highly legible chapters: The Night, featured moment (photo/video/song), fan memories, setlist, contact/message.

**Hero:** one truly excellent authorized photograph, artist and venue in an intentional hierarchy; real Share, Fan Preview, and Edit always available. No glowing dashboard islands everywhere.
**Gallery:** one larger curated memory at a time; remaining photos presented as supportive groups with honest captions and a clear View Gallery action.
**Editing:** click text itself to begin inline editing; editing actions look like quiet editorial tools, saving status is always visible, publishing/visibility explicit.
**Mobile:** single column, hero crop selected deliberately, compact actions grouped, media-first hero and text without truncation.

### B — The Encore Room (sound/video-first)
**Premise:** the artist welcomes fans back into the sound and energy of the show. After a concise hero, the featured verified media artifact (studio video, live recording or licensed track) acts as the visual and emotional center, not a wall of photos.

**Hero:** simple contextual photograph, small venue/time and one dominant CTA to play/watch the featured moment; share/link/QR unobtrusive but accessible.
**Media:** meaningful artwork, track/video title, artist credit, real player controls, captions/transcripts as supported, view recording/source rights, audio file/upload state.
**Gallery:** visually varied concert-film contact sheets as a second act. Privacy and credits honest.
**Mobile:** player and action controls maintain correct hit areas; no autoplay/audio and reduced-motion/low-end support. Artist can replace the featured media from a one-step source picker.
**Risk:** embedding an unlicensed music video or autoplaying audio is not acceptable; provider policy and permission must be validated.

### C — The Night Edition (typography/collection-first)
**Premise:** one concert becomes a collectible artist publication rather than a social-feed or ordinary event record. A dramatic editorial title and deliberate whitespace establish an identity. An issue-like sequence juxtaposes event archival facts, one powerful image, a private author reflection, a setlist, and fan recollections.

**Hero:** type takes the primary role; imagery establishes context but does not take every available pixel. The band controls the visual identity using approved media and simple templates.
**Components:** short expressive labels, precise operational controls, low-card density, action zones consistently aligned.
**Mobile:** responsive typography with semantic reflow and smaller text roles, no poster-like tiny rotated controls.
**Risk:** could become too literary or slow for busy touring bands uploading post-show media in poor network conditions.

## One common utility contract for all directions
- Header action hierarchy: **Share Night**, **Preview Fan View**, Edit; actual routes/actions must be checked. QR and copied link go to the same **canonical Night destination**, respecting public/private boundaries.
- **Story:** inline authoring should not overwrite an existing draft, lose private notes, or silently publish. Save, saving, saved, error, retry and cancel behavior explicitly designed; capabilities verified against current Strapi and FE first.
- **Media picker:** Photos, Video, Audio, external YouTube/Spotify, Gallery *only where truly supported*. Recognizable icons + text labels. File upload ≠ URL embed. Simple initial choices, details after choosing, progress/status, per-item visibility and appropriate draft behavior.
- **Video can be any artist-approved contextual media** (hit song's music video, song performed, artist recap, crowd clip). Do not falsely label a music video as shot at this concert; distinguish "Featured song" from "Recorded that Night".
- **Galleries:** curated first, bulk grid second, clear caption/privacy/manage, sensible empty and many-photo cases; don't copy a famous site or misrepresent real band photos.
- **Fan relations:** attendee count is not a claim of verified fan identity unless actual data semantics established. Messaging recipients/consent must be checked.
- **Operations:** high-speed, stable 320/390/768/1440, keyboard/focus, 200% zoom, low-end GPU, slow/offline upload recovery. Protect existing Faneqo backend permission and payments boundaries.

## Prototype brief (not yet created in Faneqo)
Use existing North Star, latest real app files, and founder-approved locks. Build **three genuinely different isolated concepts**, with the *same real content, CTA and media rights*, then obtain owner preference. Critique first-glance clarity, emotional imagery, reading hierarchy, editing speed, audio selection and recoverability, mobile/low-end behavior. Source IDs above are research **mechanisms**, not code/assets to copy.

## Evidence and approval
- Owner provided actual screenshots and preference in chat; original pixels are **not stored by this repo**.
- Source-linked visual studies are preview-only; no tested external flows.
- **No owner selection yet** among A/B/C. A/B/C are candidate creative strategies, not deployed solutions.
- No actual Faneqo route, pricing, media permission, QR resolver or rich text store was verified in this release.
- Comparison against plain AI with equal brief remains **NOT RUN**; exceptional quality is a target to earn through critique.
