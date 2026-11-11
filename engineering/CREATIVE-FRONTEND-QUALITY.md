# Creative Frontend Quality Contract — Nuxt/Vue and Modern Web

**Research date:** 2026-11-11. Official browser/standards docs reviewed. No actual Faneqo code inspected and no production changes made.

## Why this exists
A design skill must know when artistry becomes a technical defect. Craft is not limited to matching a Figma screenshot.

## 1. Content first
Semantic heading and reading order; actionable primary navigation; meaningful alternate text; media load failures handled; data from actual project sources rather than invented production numbers.

## 2. Responsive art direction
Use art-directed crops/source sets where appropriate, explicit image dimensions to avoid layout shifts, adaptable focal positioning, fluid type with appropriate bounds, no visually hidden essential actions.

## 3. Motion grammar
Reserve:
- Instant micro-feedback for buttons/controls.
- Short continuity motion for overlays and route transitions.
- Longer narrative sequences only in explicitly immersive sections, always skippable.
Use CSS transitions/animations or Web Animations API when sufficient; add GSAP only with a clearly justified timeline need and verified dependencies. Do not invent library support.

**Official references:** https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion and https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations .

## 4. Accessibility is behavior
Keyboard-visible focus, correct semantics, forms with recovery, accessible labels and names, headings, reading order and reduced motion. W3C's Non-text Contrast criterion (WCAG 2.2 SC 1.4.11) generally requires at least 3:1 contrast for essential graphical UI cues against adjacent colors. It is separate from text contrast and does not mean every decorative object needs 3:1 contrast.

Source: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast

## 5. Nuxt/Vue execution guardrails
- Preserve Composition API and existing component/contracts.
- Inspect `nuxt.config`, Tailwind setup and existing dependencies before writing.
- SSR/hydration: no random/time-dependent DOM divergence at render. Browser-only APIs in client lifecycle when appropriate.
- Controlled interactive states: use `ref`, `computed`, events and appropriate composables; don't use imperative DOM updates when declarative state is appropriate.
- Head metadata and route behavior; avoid accidental client-only SEO disappearance.
- If adding fonts, verify licensing, fallback and loading strategy; minimize layout shifts.
- Avoid pinning trendy CSS features without fallbacks and browser support checks.

## 6. Core Web Vitals measurement
When a sandbox or page is runnable, record real Lighthouse or browser measurements, including Largest Contentful Paint, Interaction to Next Paint and Cumulative Layout Shift; do not invent numbers. Test low-end mobile where possible. Qualitative motion-smoothness judgment is not a benchmark.

## 7. Separate design mode from product editing
- A research prototype is not production code.
- Build in an isolated branch or sandbox under explicit instructions.
- Never make payments, auth, analytics, billing or backend changes while implementing a visual-only brief without explicit authorization.
- Provide changed files, tests actually run, screenshots with metadata and rollback route.

## QA handoff checklist
Browser/device, viewport, logged-in/out context, image loading, keyboard, focus, 200% text zoom, mobile navigation, reduced motion, route transitions, no animation jank, visual and semantic regression. Each item: TESTED / NOT TESTED / BLOCKED with evidence.

## Sources
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion
- https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
- https://www.w3.org/TR/wcag/
