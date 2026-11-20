# Faneqo Creative Engine — on-demand direction adapter (candidate)

Use only for a founder-authorized Faneqo Creative Studio campaign. This is an *art-direction layer* over the existing engine, not a new generator or an installed integration. Source of truth: `musicbizqr/scripts/creative-engine.mjs`, `scripts/creative-engine-brief.mjs`, the live Studio templates, and `docs/FANEQO_NEXT_AGENT_HANDOFF.md`. Re-read those files in the target revision before execution.

## Creative contract

1. Start from a real audience, objective, single message, required action, available licensed media, and intended formats. Mark unknown features, artist claims, endorsements and rights; never invent them.
2. Identify one organizing idea. Develop **three conceptually distinct** approaches, not three colorways: change the image's job, composition logic, typographic voice, and argument. Each must use an actual supported Studio template and editable fields; do not invent template IDs or config keys.
3. Describe each approach in the existing Markdown grammar: one campaign heading, audience/objective/message/direction/supporting copy/asset notes, then exactly three concept headings containing `Name`, `Template`, `Strategy`, `Headline`, `Copy`, `CTA`, and only supported optional fields. Use `|` for intentional headline breaks. Read the target parser before adding fields.
4. Do a preflight for distinctness, product truth, rights, copy length, likely portrait legibility, and template capability. Fix concept flaws before rendering. Do not claim an unrendered composition is strong.
5. Let the **existing** `node scripts/creative-engine.mjs compose <brief.md> <fresh-output-dir>` validate and render the concepts. Never overwrite an earlier proof directory. Inspect `comparison.png` **and** individual full-size PNGs. The command runs against a local Nuxt preview; the script does not itself call Codex, Claude or ChatGPT.
6. Critique actual output against the campaign goal: focal hierarchy, originality, music authenticity, accurate product depiction, CTA, photo crop, mobile legibility, and export fidelity. Separate visible observations from hypotheses. Recommend at most three precise fixes per concept; revise the Markdown and recompose into a new directory when justified.
7. Founder approval is a hard gate: no `select`, `produce`, distribution, commit, merge, or deployment merely because a concept scores well. Record which concept and exact proof was approved. Respect existing asset-rights and production gates.

## Efficient execution

- Default to one planning pass, one render-and-critique pass, and one targeted revision. A third render needs a named remaining defect or founder request.
- Reuse the current assets, supported templates, generator, validation, and export pipeline. Avoid new dependencies, separate design applications, image generation, or asset downloads unless the chosen direction specifically needs them and authorization is clear.
- Protect the founder's low-memory machine: one Nuxt preview and one browser instance, no parallel browser suites, proofs in ignored local directories.
- Compare directions at an identical format and content budget. Quality wins over minimal tokens; report extra model calls and run time when actually measured, never estimated as telemetry.

## Review handoff (maximum seven lines)

Report: campaign / source revision; three direction theses and template IDs; rendered evidence paths; strongest and weakest observable qualities; exact recommended revision; rights/technical unknowns; founder decision pending or recorded. This handoff does not replace the validated campaign package.

## Quality experiment

Use `pilots/003-faneqo-creative-engine/PROTOCOL.md` before claiming the adapter improves results. A successful parse, render, or scorecard is not evidence of superior art direction. Keep baseline and candidate prompts, outputs and human judgment separate.
