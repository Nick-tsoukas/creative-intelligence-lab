# Vue 3 / Nuxt 3 Component Library Observatory

**Date checked:** 2026-11-11. **Status:** DOCUMENTATION-REVIEWED / CATALOG (not benchmarked or installed).

A library provides implementation code; a design system provides both code and a decision language. A visually pleasing component gallery does not prove accessibility.

| Library | Source | What to study | Caveats |
|---|---|---|---|
| Nuxt UI | https://ui.nuxt.com/ | Nuxt integration, typed components, Tailwind theming, dashboard patterns, Reka primitives | Verify version and peer dependencies before use; current Nuxt modules page identifies v4. |
| Reka UI | https://reka-ui.com/ | Headless accessible Vue primitives and controlled state/focus management | Accessible primitive is foundation, not guarantee of accessible composition. |
| PrimeVue | https://primevue.org/ | Data-rich controls, DataTable, selection, forms, styled vs unstyled | Large component breadth; consider styling/complexity/accessibility behavior for exact need. |
| shadcn-vue | https://www.shadcn-vue.com/ | Copy-in/source-owned components built around Reka UI | Ownership means maintenance burden; verify generated source and updates. |
| Headless UI Vue | https://headlessui.com/v1/vue | Unstyled accessible disclosure/menu/dialog/listbox patterns | Confirm current Vue-specific API and supported release. |
| Vuetify | https://vuetifyjs.com/ | Material-style comprehensive Vue component toolkit | Opinionated aesthetics and CSS; verify current compatibility. |
| Quasar | https://quasar.dev/ | Framework/CLI and broad Vue components across platforms | Framework-level commitment rather than drop-in component choice. |
| Naive UI | https://www.naiveui.com/ | Themeable Vue 3 component variety | Verify maintenance and test desired behaviors. |
| Element Plus | https://element-plus.org/ | Enterprise data/form components | Component styles and accessibility need task-specific evaluation. |
| Ark UI Vue | https://ark-ui.com/ | Headless state-machine-driven component model | Verify Vue package/version and implementation complexity. |

## Observations grounded in official sources
- Nuxt UI's official Nuxt module page describes typed accessible Vue components based on Reka UI, Tailwind CSS and Tailwind Variants. Its docs list a recent v4 series.
- Reka UI is described by its Nuxt module page as a Vue port of Radix-style primitives.
- PrimeVue explicitly documents an *unstyled mode*: core behavior/accessibility remains available while application authors supply CSS.
- Shopify Polaris web components are framework-neutral but tied to the Shopify-admin look and environment; they are research material, not a natural drop-in for unrelated branding.

## Component decision matrix for later engineering
For any task, evaluate:
1. SSR/hydration compatibility (Nuxt 3); test actual client-only patterns.
2. Keyboard, focus, ARIA semantics and screen-reader behavior; test rather than trusting marketing.
3. Controlled and uncontrolled state models, `v-model`, events, composition API ergonomics.
4. Token/theming control, CSS layering, design-system fit.
5. Overlay/portal behavior, mobile touch, scroll lock, motion preferences.
6. Bundle cost, tree-shaking, update frequency, dependency security and license.
7. Data-heavy features and accessibility under large/virtualized lists.

**No instruction to install any library.** The purpose of this document is to teach future creative engineers how to choose intentionally.