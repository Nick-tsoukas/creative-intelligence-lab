# Visual Evidence Library — Screenshots, Examples & Original Experiments

**Policy established:** 2026-11-11

We want a **visually rich, annotated research atlas**, not a folder of random uncredited screenshots.

## Two different visual objects
1. **Captured screenshots of external works:** must identify the exact source URL, capture date, viewport, browser, visual state and creator; do not alter a screenshot and pass it off as original. Investigate copyright/terms and publication rights **before committing actual images to a public repo**.
2. **Original visual teaching studies:** our own SVGs/diagrams exploring concepts (e.g., hierarchy, density, rhythm); label clearly as original, not an Apple/Google screenshot or recreation of a proprietary app.

## Current status
- **Original demonstrations created:** [Attention vs restraint](original-studies/attention-vs-restraint.svg) and [Component anatomy](original-studies/component-anatomy.svg), intentionally generic comparative interface illustrations.
- **Actual site screenshots:** **not captured or uploaded yet.** Current tool environment could retrieve page text and image search references but could not reliably load public sites for screenshot capture. Therefore this repository uses **links to source-hosted screenshot examples** and a capture queue. Never fabricate screenshots, device tests, or visual annotations.
- The public repository should not host copied full-resolution copyrighted screenshots without checking applicable rights. Linking to official examples for study and later making small necessary documented analytical captures can be assessed individually.

## Official illustrated examples to inspect
| Ref | Owner / source | Link | What the illustration teaches | Evidence |
|---|---|---|---|---|
| APPLE-01 | Apple 2026 HIG Layout | https://developer.apple.com/design/human-interface-guidelines/layout | Content vs controls, grouping, progressive disclosure, platform adaptation | Apple official docs describe illustrated iPad and layout examples; screenshot not independently captured |
| APPLE-02 | Apple WWDC25 design-system session | https://developer.apple.com/videos/play/wwdc2025/356/ | Component anatomy, navigation continuity, materials | Official presentation contains demonstrations |
| APPLE-03 | Apple 2026 design guide | https://developer.apple.com/wwdc26/guides/design/ | Updated principles and modern system design | Official video/documentation |
| GOOGLE-01 | Google M3 Expressive research article | https://design.google/library/expressive-material-design-google-research | Illustrated email Send button before/after, sizes and placement | Official research article describes images and comparison |
| GOOGLE-02 | Material 3 typography | https://m3.material.io/styles/typography/applying-type | Type-role ladder, display vs body readability | Official component guidance |
| GOOGLE-03 | Material 3 canonical layouts | https://m3.material.io/foundations/layout/canonical-examples/overview | Feed/list-detail/supporting-pane across breakpoints | Official documentation with layout example images |
| FLUENT-01 | Microsoft Fluent 2 Figma kit | https://fluent2.microsoft.design/get-started/design | Design tokens/variants and code-aligned components | Official docs with Figma component imagery |
| CARBON-01 | IBM Carbon | https://www.carbondesignsystem.com/ | Enterprise components, data visualization, AI components | Official documentation |
| POLARIS-01 | Shopify Polaris | https://shopify.dev/docs/api/app-home/latest | Merchant admin app components, navigation and forms | Official docs with example UI |
| NUXT-01 | Nuxt UI docs | https://ui.nuxt.com/ | Vue component examples, dashboards, combobox and overlays | Official component documentation |

## Screenshot capture backlog (not completed)
Capture 1440 × 900 desktop and 390 × 844 mobile where meaningful. Capture normal, focus, error and reduced-motion states when applicable. Standard filename:
`YYYY-MM-DD__source-id__viewport__state.png`.

Record for each image:
`source_id, creator, canonical_url, captured_at_utc, viewport, browser, page_state, rights_status, screenshot_path, analysis_doc, annotations, caveats`.

## Recommended workflow
- Use a browser you can actually interact with (e.g. Claude Code with Playwright or a user-controlled browser).
- Obtain source page and preserve provenance. Hide personal data, cookies, login credentials, tokens, accounts.
- Capture **only** what is reasonably needed for criticism and comparison; verify site terms and image redistribution rights before public GitHub publication.
- Record context before drawing conclusions. A screenshot cannot reveal animation timing, keyboard handling or conversion metrics.
- Prefer links and original diagrams where image rights are uncertain.
- Later, build a small gallery of thumbnails linking to detailed case studies, clearly captioned and versioned.

## Why this matters
Visual education needs artifacts. Text-only research cannot train recognition of typographic hierarchy, cropping, spatial rhythm or component polish. However visual evidence must be honest about its provenance and limitations.