# Research 015 — Two Opposing Ways to Build Attention: Vermeer and Hokusai

**2026-11-15 original-source critical study.** Exact works:
1. Johannes Vermeer, *Woman Holding a Balance*, c.1664, oil on canvas, National Gallery of Art accession **1942.9.97**. [Museum object and visual description](https://www.nga.gov/artworks/1236-woman-holding-balance). [National Gallery Open Access policy](https://www.nga.gov/artworks/free-images-and-open-access).
2. Katsushika Hokusai, *Under the Wave off Kanagawa (Kanagawa oki nami ura)*, ca.1830–32, woodblock, Metropolitan Museum of Art **JP10 / object 36491**, 24.4×35.7 cm. [Object](https://www.metmuseum.org/art/collection/search/36491), [official object metadata and original image URI](https://collectionapi.metmuseum.org/public/collection/v1/objects/36491), [Open Access policy](https://www.metmuseum.org/hubs/open-access).

**Actual inspection:** Vermeer: NGA original object descriptive text and visual analysis read; a widely circulated digital image viewed at preview resolution (not paint texture, full-resolution canvas). Hokusai: Met official object/API record and publication image previews viewed, some constrained/cropped relative to full sheet; official full original-resolution Met JPEG URL **identified but not downloaded/inspected at original resolution**. Neither work has been viewed in person or analyzed with instrumentation. The existing MA-001/MA-002 source-study level remains **PREVIEW_OBSERVED**. No uninspected micro-geometries or verified gaze heatmaps are claimed.

## Vermeer: legibility without maximal contrast
- **Source-observed / curator-described:** a figure at a table holds a small balance in a dim chamber; light from a left window illuminates face and hands, white trims and dark/blue drapery; a Last Judgment picture occupies the backdrop.
- **NGA specific curatorial point:** the hand and balance are positioned against a relatively spare wall region, with the frame of the painting subtly adjusted to make physical room for the delicate balance. This is a highly useful **object-space relation**: preserving a small but meaningful object by avoiding local clutter and by adjusting its neighbor's edge.
- **What cannot be concluded:** no universal eye-stop time, no knowledge of the exact painterly brush work from a preview, no proven “balance scales convert visitors” rule. Religious/iconographic meaning matters; don't turn the woman or Last Judgment into generic marketing decoration.
- **Digital composition hypothesis:** if a small, important action/detail is being lost, first **clear its immediate neighboring region**, improve separation and cluster it with intelligible contextual text. Do not automatically increase every font size or saturate every CTA. A sparse local field may carry nuance while preserving the whole page.

## Hokusai: counterweight across multiple scales
- **Source data:** Edo-period multicolor woodblock print, from a named series of Mount Fuji views, not one-off painting. Met JP10 is one impression; its physical medium, print variations, Japanese context and reproduction format matter.
- **Preview-observed:** giant curling navy wave shape with white foam dominates near field; narrow long craft with tiny human figures are held in turbulent water; distant Fuji is remarkably small and visually stable. Repeating prongs/foam rhythms vary scale and direction. This is an observation of displayed previews, not Met high-resolution plate edge inspection.
- **Interpretive tension:** the apparent huge/small opposition is not evidence that primary CTAs ought to be tiny. Fuji is central to the series' subject and meaning, not simply a convenient logo anchor.
- **Digital composition hypothesis:** dramatic hero imagery can coexist with a small, *legible* stable navigation/proof context **only when that context stays independently discoverable**. Use scale contrast as a design question, not a visual formula.

## Cross-study decision matrix
| UX communication problem | Source mechanism | Hypothesis to prototype | Risk / falsification |
|---|---|---|---|
| Small meaningful object or action lost behind rich content | Vermeer: isolate precise hand/scales against relatively quiet plane | Clear a localized information field; preserve visual warmth elsewhere | If task isn't found or hover/focus fails, quiet hierarchy is insufficient |
| Everything tries to be the loudest element | Vermeer: controlled local focal contrast | Reduce unrelated salience rather than increase CTA screaming | High-stakes warnings may require stronger salience and visible text |
| Hero feels inert and characterless | Hokusai: changing scales, rhythm and an orienting reference | Give primary content a strong near/middle/distant relation with stable navigation | Mobile crop destroys story or pushes real action below an optional scroll gate |
| Small “anchor” hides required next step | Misapplied Hokusai | Keep an explicit primary link visible despite expressive size difference | Reject if first-click fails or focus/contrast disappear |
| Designer imitates cultural image | Both works have specific sacred/historical or Japanese artistic context | Extract *relationship*, not identifiable iconography | Reject if composition reproduces an existing recognized work |

## Controlled creative exercise — portable across projects
Create three original layouts with the **same user-facing facts, action and navigation**:
1. **Localized quiet focus:** keep surrounding artwork expressive; protect 1 human detail/action with clean adjacent space.
2. **Scale-driven spectacle:** one large content mass against small but clear orientation/proof and a functioning CTA.
3. **Human-task baseline:** prioritize comprehension, legible headline/proof/action without any artistic citation.

Observe actual render at 320/390/768/1440, keyboard, text zoom, contrast, failed image, reduced motion; separately inspect whether an unfamiliar person understands product proposition. Distinguish art direction preference, readability, task results and cultural authenticity. No template may be declared superior from this source study alone.

## Source/rights
The NGA explicitly says this image is Open Access/public domain; the Met API marks JP10 `isPublicDomain=true` and supplies original-resolution image URI. This does not establish that *other* museum works, museum logos, third-party site screen captures or modern commercial derivative assets may be reused. **No artwork pixels are embedded in the Lab repo or the Visual Grammar Studio.**

**Transfer status:** historical interpretation + modern UX HYPOTHESIS; no real Faneqo screenshot/visitor test. **See:** Masterpiece Atlas MA-001/MA-002 and `experiments/004-visual-grammar-studio/`.
