# Faneqo Public Homepage — UX Domain Adapter (2026-11-15)

**Purpose:** Faneqo-specific product facts and candidate homepage review tasks for `elite-ux-director` v0.4. This document is **outside the universal skill**: `domain-adapters/faneqo/HOMEPAGE_EXPERIENCE.md`. No Faneqo code was modified or live page browser-tested to produce this adapter.

## What is verified from GitHub main (code/doc inspection, 2026-11-15)
- Frontend repo: `Nick-tsoukas/musicbizqr`. Route `pages/index.vue` renders `components/home-v2/HomeV2Page.vue` with SEO via `utils/home/homepageContent.js`.
- The component's opening contains `HomeHeroSection` and `HomeHeadquartersSection`; code calls this an approved opening and describes the later sequence as a concert night told in order. Actual mobile/desktop rendering and activation of these sections **not inspected** in this research increment; code shows some elements may be hidden by CSS at given breakpoints.
- Main component imports `HomeV2LiveMoment`, `HomeV2AfterTheShow`, a lazy Messaging showcase, `HomeV3NightLives`, `HomeV3FanIntelligence`, `HomeV3AudienceInsight`, a real-artist showcase, closing and FAQ. These are component names, **not a claim all visuals or claims are accurate in production**.
- FAQ/content file includes user-facing statements around artist Headquarters, links, QR, fans, messaging, price and trial terms, plus JSON-LD and SEO metadata. Any display copy, pricing, eligibility, free-trial duration and messaging limits must be **reconciled with current real signup/product/back-end**, not copied as gospel from marketing file.
- Document `docs/FANEQO_DESIGN_NORTH_STAR.md` calls the app a real artist → Night → fan → memory → messages → relationship system and says `390px` is its canonical mobile canvas; locked compositions should change only for demonstrable defects or approved redesign.
- `docs/design/FANEQO_VISUAL_LANGUAGE.md` defines existing Poppins typography, established dark artist/marketing identity, editorial photography, meaning-before-decoration and preference against generic SaaS/neon/card soup. It explicitly says it **does not override** the North Star.
- `docs/FANEQO_CURRENT_PHASE.md` on GitHub main was last updated 2026-09-09; **its status is stale** relative to later Show Mode/Night/Messaging work. Do not treat its old locks or queue as current without consulting the active branch/handoff and owner-approved scope.

## Priority UX research questions — not assumed defects
1. **New visitor**: in five seconds and without knowing “Faneqo”, can an artist distinguish it from Linktree, a generic QR maker or marketing CRM? What actual user job and benefit is communicated?
2. **Proof of differentiated value**: can visitors see the real product loop (artist Headquarters → show QR → fan check-in/follow → Night/photos → messaging/relationship) rather than an abstract animation? Distinguish demonstration from current live capability.
3. **Single coherent narrative**: do the show, after-show, galleries/messaging, Passport and analytics chapters reveal why the relationship matters, or become too long or repetitive?
4. **Actions**: on every viewport is “Start free” or equivalent obvious, accurately described and truly routed to a coherent signup/trial state? Can current customers log in without scrolling? Is `/presentation` a meaningful optional detour rather than a trap?
5. **Audience fork**: primarily market to active independent artist/band users; make manager/agency and interested fan paths intelligible without multiplying hero CTAs. **Target segmentation requires owner-approved product strategy and real source evidence**, not inferred user percentages.
6. **Trust and pricing**: copy/FAQ/SEO/pricing consistency, no made-up growth outcomes, no false fan counts or endorsements; clearly labeled demo artist and accurate privacy language.
7. **Real device**: at 320/390/430/768/1440, does the header, first screen, CTA, product mockup, long scroll, FAQ and footer remain legible and operable? Test with JS disabled/failed video where meaningful; keyboard, focus, zoom and reduced motion.
8. **Speed and SSR**: inspect hero LCP image and hydration, eager/lazy section loading, click readiness and layout stability on real low-end mobile; report LCP/INP/CLS only when actually measured. An 8 GB dev machine needs one browser harness and owned-server cleanup.
9. **Narrative vs task**: can someone get to signup and pricing without being forced through cinema? Can someone deliberately explore deeper detail without losing the page's identity?
10. **Independent visual direction**: preserve the approved opening unless a concrete issue warrants change. Ask Creative Design Director for three distinct *new choices in unlocked areas*; don't secretly reset typography/tokens/photo identity.

## Core operating handoff
- **Reusable UX skill:** `elite-ux-director` v0.4 uses `references/HOMEPAGE_INTELLIGENCE.md`, max two H-cards and optional `templates/HOMEPAGE_UX_PACKET.md` to define first-view comprehension, actual CTA journeys, proof and accessibility/performance acceptance.
- **Faneqo facts:** load THIS adapter and verify current product code/docs/routes before acting; avoid importing it into personal universal skill.
- **Creative intelligence:** `skills/creative-design-director/SKILL.md` + research field manual, art/typography/cinematic references, existing branded Faneqo doctrine; output meaningfully distinct theses, not variants of the same hero.
- **Implementation:** authorized frontend-design + Nuxt 3 Composition API, current packages/brand tokens; ensure real screenshot/evidence loop. **No modifications or deployments authorized by this document.**

## Suggested zero-coaching task narratives (hypotheses to validate)
- **Independent artist on mobile**: “What is this, and can I get a music page that lets me reach people from my shows?” From unfamiliar homepage → understand → inspect real example → start honest signup.
- **Working touring band**: “What happens with fans after the night?” From homepage → discover show/relationship loop → understand Night/Gallery/Messages without a CRM vocabulary lesson.
- **Manager with multiple artists**: “Is this useful for my roster, and can I investigate the terms?” From homepage → see professional workflow proof → reach pricing/FAQ/contact; no invented bulk-management ability.
- **Returning artist**: “I just want my dashboard.” From familiar homepage → log in without promotional obstruction.
- **Fan who arrived on home by accident**: “Where's the artist I was looking for?” From home → understand this is the product's marketing site → find a safe route to artist discovery where the app actually supports it; do not invent a search or fan signup path.

## Evidence to collect during future authorized homepage work
- Current local branch/commit, route tree, active components and owner-approved locked areas.
- Browser screenshots of real first fold, section order and CTA at mobile/desktop; screenshots are **observations**, not user comprehension evidence.
- Manual or actual participant first-exposure comprehension/first-click data when feasible; if unavailable label proposed comprehension results **hypotheses**.
- Route/CTA target inspections, auth/trial/price consistency, and FAQ/SEO/structured-data claim audit.
- Performance/accessibility checks and actual failures under reduced motion/media error/low-end constraints.
- Independent UX critic vs creative director critique, with disagreements and verified fixes.

## Maintainers and source anchors
- Verified paths: `musicbizqr/pages/index.vue`, `components/home-v2/HomeV2Page.vue`, `utils/home/homepageContent.js`, `docs/FANEQO_DESIGN_NORTH_STAR.md`, `docs/design/FANEQO_VISUAL_LANGUAGE.md` (GitHub `main`, inspected 2026-11-15; may have advanced in active branches).
- General research: [NN/g 2024 homepage principles](https://www.nngroup.com/articles/homepage-design-principles/), [web.dev vitals](https://web.dev/articles/vitals), [W3C carousels](https://www.w3.org/WAI/tutorials/carousels/). Claims about Faneqo visitor comprehension are **not** contained in these articles.
- **Status:** research adapter ready; no live homepage testing, no actual audience interviews, no production code changes, no trial/price claims certified.
