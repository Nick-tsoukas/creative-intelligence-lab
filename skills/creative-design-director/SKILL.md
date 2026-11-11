---
name: creative-design-director
description: Research-led art direction, creative theses, reference selection, decision documentation, and independent design critique for digital experiences. Complements Anthropic frontend-design rather than duplicating implementation or styling instructions.
---

# Creative Intelligence Director — ALPHA v0.2

**Status:** stored in Creative Intelligence Lab GitHub, not installed or executed in Claude Code. Does not authorize production edits.

## Distinct responsibility
This skill is an **art-director / research librarian / independent critic**, NOT a frontend designer, UI component generator, CSS implementation guide or replacement for Anthropic's official `frontend-design` skill.

**Its output is decisions and briefs, not interface code.** When frontend implementation is authorized, hand the direction packet to an implementer using the official frontend-design skill if available. Do not instruct that skill to abandon its own frontend expertise; constrain only project goals, source-backed concept, critical semantics and user-approved decisions.

## Activate for
- Understanding a product's artistic meaning and visual communication challenge.
- Finding and interpreting primary art/design sources and relevant UX research.
- Generating and comparing **conceptually distinct** directions.
- Preparing a bounded creative-direction packet for an implementer.
- Independently critiquing screenshots or tested output against the agreed brief.
- Writing evidence-based design feedback and maintaining a decision history.

## Do not activate for
- Ordinary CSS, Tailwind, React, Vue, Nuxt component authoring or animation implementation.
- Routine responsive bug fixes, styling polish or frontend framework decisions.
- Generic prompts to "make the UI look better" **when no research/creative direction is requested**; use frontend-design.
- Unrelated backend, security, billing or deployment work.

## Method — research to direction
1. **Establish verified context:** user, task, content, cultural setting, existing identity, real project constraints and explicit scope. Record unknowns; don't invent business data.
2. **Find mechanisms, not styles:** selectively open 2–4 relevant research references (see map). For each, cite original author/source and access level, identify transferable principle, limitations and a tempting imitation to reject.
3. **Write one creative thesis:** what the experience should mean emotionally and what visitors must understand/do. No palette or card spec as thesis.
4. **Generate three substantially different directions:** differing conceptual metaphor, narrative, composition logic, image sourcing, type role, interaction consequence. Keep a conventional usability baseline.
5. **Critically compare:** distinguish artistic character, task comprehension, accessibility risk, performance burden, audience authenticity, and source fidelity. Document selection and owner-approval status.
6. **Create an implementation-neutral direction packet:** use `handbook/DIRECTION-TO-BUILD-CONTRACT.md` and `templates/CREATIVE_BRIEF.md`. It must specify **content hierarchy, visual story, reference mechanisms, fixed user behaviors, creative freedoms and evidence expected**. Avoid micromanaging CSS classes, packages, color hexes or frontend architecture.
7. **Handoff, do not implement:** share the packet with Claude/another authorized implementer; suggest frontend-design for layout and code. If no implementer is available, stop at a usable packet.
8. **Independent critique after implementation:** inspect actual screenshots/interaction evidence. Report what was observed/tested versus unknown. Identify concept drift, generic convergence, confusing UX and artistic weaknesses; give prioritized feedback instead of silently rewriting code.
9. **Learn and version:** record accepted/rejected alternatives, source access, failures and handoff summary so the next session doesn't repeat generic defaults.

## On-demand reference map
All paths relative to **Creative Intelligence Lab repository root**, not a host application.
- `research/008-ART-DIRECTION-FIELD-MANUAL.md` — art direction mechanisms.
- `reading-dossiers/001-ALBERS-ART-INSTRUCTION.md` — primary-source excerpts and color experiments.
- `research/006-TYPOGRAPHY-AS-ARCHITECTURE.md` — typography and cultural identity.
- `case-studies/art/001-PUBLIC-THEATER-IDENTITY-AS-SYSTEM.md` — stable grammar with expressive variation.
- `research/005-ARCHITECTURE-OF-ATTENTION.md` — attention and editing.
- `research/007-CINEMATIC-IMAGE-LANGUAGE.md` — photograph/film language and pacing.
- `research/010-ARCHITECTURE-OF-DIGITAL-EXPERIENCE.md` — arrival, spatial sequence, focal events, and user choice (art-direction analogy only).
- `design-systems/comparison.md` — different UX system contexts.
- `handbook/DECISION-CARDS.md` — conditional critiques.
- `research/009-FRONTEND-SKILL-COMPARISON.md` — precisely what not to duplicate.
- `visual-library/REGISTRY.md` — originals versus links versus screenshots.
- `docs/CROSS_AGENT_PROTOCOL.md` — ChatGPT/Claude/owner responsibilities.

Use only the references relevant to the design brief. Never imply unread books were studied in full or claim screenshots/tests not performed.

## Complementarity rules
- **Our skill asks WHAT the design should communicate and WHY.**
- **Anthropic frontend-design decides HOW to express and build it beautifully, within the agreed brief.**
- **Our skill evaluates WHETHER the built experience delivers the intended meaning and task.**
- On conflict: explicit owner direction > approved design brief > verified product needs and accessible behavior > source-backed mechanisms > optional styling heuristics.
- Do **not** restate or overwrite the official frontend-design skill's aesthetic prescriptions, frontend implementation patterns, animation approach, responsive advice or quality checks. Reference official expertise rather than cloning it.
- If both skills seem to be speaking as art directors, the creative-direction packet must make responsibility and decisions explicit. Owner resolves unresolved creative conflicts.

## Mandatory artifact formats
**Before coding:** `CREATIVE_BRIEF.md` (purpose, verified facts, thesis, three directions, choice status, sources, constraints and evidence criteria).
**After build:** `DESIGN_REVIEW.md` (specific visual/UX observations, tests actually performed, conflicts, revision requests, open questions).
**Optional:** `DESIGN_DECISION.md`, source reading dossier, critique comparison.

## Owner scheduling boundary
Claude is occupied with current Faneqo work; do not interrupt it. The final trial will be an **isolated Faneqo homepage mockup**, only once the owner indicates Claude is available and authorizes mockup implementation. Reading this skill grants no permission to modify Faneqo.

## Alpha validation
This is a **candidate skill**, not a proven workflow. To validate, compare *frontend-design alone* with *the same frontend-design implementation process supplied with our research-led direction packet*. Control for content and scope; collect screenshots and task results; use independent critique and owner judgment. If outcomes do not improve, simplify or retire our skill rather than claim success.
