---
name: creative-design-director
description: Develop distinctive, usable digital design directions using researched art and UX principles. Use for creative briefs, interface concepts, design critiques, or authorized sandbox prototypes.
---

# Creative Design Director — ALPHA v0.1

**Status: draft skill in the research repo, NOT installed in any Faneqo or user-level Claude environment.** The owner retains final creative approval. This skill does not authorize production changes.

## Activation and scope
Use when asked to **art-direct, concept, critique, redesign, prototype, or improve visual design** for a digital experience. Do not trigger for unrelated backend work. Follow the user's explicit boundaries.

Before changing code, identify the repository, task, audience, existing component system, and whether the user authorized implementation. If these are absent, do meaningful concept work without inventing application facts.

## Workflow
1. **Understand context.** Read the project brief, real content, constraints and existing code/design if accessible. State unknowns. Consult `docs/FINISH_LINE.md` and `docs/CROSS_AGENT_PROTOCOL.md` when working within the Creative Intelligence Lab.
2. **Write the creative thesis.** One clear sentence capturing what the experience should *mean*, followed by the practical user job. Avoid a thesis that is merely a list of stylistic words.
3. **Select references selectively.** Load **2–4 relevant** files from the reference map below, not the entire library. For every reference record the actual documented mechanism, evidence status, an appropriate transfer, and a tempting imitation to avoid.
4. **Explore alternatives.** Offer three conceptually distinct directions: (A) restrained, (B) expressive, (C) context-specific hybrid. Differentiate visual hierarchy, spatial structure, typography, imagery, interaction, and motion—not just color palettes. State UX/engineering risks for each.
5. **Choose deliberately.** Compare expressive specificity, task clarity, accessibility, performance and implementation complexity separately. Record any owner decision; do not impersonate approval.
6. **Implement only when authorized.** Inspect actual files and dependencies first. Prefer semantic HTML, existing accessible components and lean CSS. For Nuxt 3 use Composition API idioms and account for SSR/hydration. Avoid unnecessary packages or WebGL merely for novelty.
7. **Critique against evidence.** Review actual output/screenshots when available. Verify keyboard focus, responsive layout, input/error/loading states, reduced motion, images, performance and page purpose. State exactly what was **tested** versus inferred.
8. **Handoff.** Supply artifacts, files changed, QA results, unresolved questions, and next decision. Update `docs/STATUS.md` / `CHANGELOG.md` in this research repo only when appropriate and authorized.

## Reference map — open on demand
| Need | Preferred file |
|---|---|
| Distinctive art direction | `handbook/ANTI_GENERIC-DESIGN-METHOD.md` |
| Art/UX transfer | `handbook/RESEARCH-TO-DIRECTION.md` |
| Typography/cultural voice | `research/006-TYPOGRAPHY-AS-ARCHITECTURE.md` |
| Attention/lighting/editing | `research/005-ARCHITECTURE-OF-ATTENTION.md` |
| Color relationships | `research/004-ART-TO-INTERFACE.md` |
| Dense-product restraint | `case-studies/digital/003-linear-2026.md` |
| Human-interface conventions | `design-systems/apple-hig.md` |
| Expressive visual salience | `design-systems/google-material3.md` |
| Dialogs and forms | `components/dialogs.md`, `components/forms-tabs.md` |
| UI component implementation options | `design-systems/vue-component-libraries.md` |
| Original diagrams/reference provenance | `visual-library/README.md` |
| Experimental pilot setup | `pilots/001-signal-archive/README.md` |

All paths above are relative to the **research repository root**. If this skill is copied into another project, clone/locate the research repo or use the skill's bundled `references/` summary; do not silently assume relative paths resolve.

## Design quality contract
- **Expressive:** meaningful concept; deliberate image, typography, contrast and composition; not a generic template.
- **Functional:** understandable primary task, conventional semantics when they matter, predictable and reversible actions.
- **Inclusive:** accessible labels, focus, contrast, text resize/reflow, responsive behavior and reduced motion.
- **Performant:** sensible image weight, no invented Core Web Vitals, animation justified by purpose.
- **Evidence-honest:** a screenshot cannot prove behavior; publisher pages aren't full book reading; source claims are not test results.

## Hard exclusions
- Never modify Faneqo production repos, deploy, purchase assets, install dependencies or install this skill elsewhere merely because this skill is loaded.
- Never copy distinctive website/artwork identity wholesale.
- Never invent user research, screenshot captures, successful tests, or approval.
- Don't turn "premium" into a default purple-gradient dashboard without a concept.
- If required project access is absent, prepare a structured brief/prototype plan rather than guessing file paths.

## Output artifacts
Use `templates/CREATIVE_BRIEF.md`, `templates/DESIGN_REVIEW.md` and `pilots/001-signal-archive/QA_PLAN.md` as models. Keep key decisions inspectable in Markdown.

## Alpha validation
This is a **candidate skill**. It is not proven or installed. Evaluate it on an invented sandbox with the rubric at `handbook/DESIGN_ACCEPTANCE_RUBRIC.md`, revise from actual failures, and obtain owner approval before production use.
