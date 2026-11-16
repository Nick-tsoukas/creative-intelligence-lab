# Visual Design Audit — Operating Method

**Goal:** Give a designer/AI critic an actionable, art-director-grade judgment of how a specific screen *actually looks*. Separate appearance from usability, data truth, brand constraints and owner taste. This is distinct from the existing Interface Atlas, which gathers external reference examples.

## What is implemented

- `visual_audit.py`: immutable audit record and image-specific observations associated with screenshot captures created by the existing private `visual_workspace.py`.
- `visual_audit.py prompt`: an exact local image path plus a bounded critique prompt for a vision-capable AI or human critic.
- `visual_audit.py report`: prioritized findings, evidence tags and explicitly **unreviewed** dimensions. It does NOT claim visually evaluated categories without an observation.
- `visual_audit.py audit`: validates report records and source image integrity. No image is copied or processed by this tool.

**Important:** The CLI does not see images, critique pixels, run a browser, or invoke a model. Actual visual inspection happens when a human or vision-capable agent OPENS the private image and evaluates its appearance. A test suite proving metadata integrity does not prove aesthetic judgment.

## Start from an existing private screenshot

Capture/import using the other chat's existing project workspace. This new script reads but never changes `.cil-private/projects/<project>/captures/<screen>.json` or its image.

```bash
python design-excellence/visual_audit.py start \
  --project faneqo-night --audit initial-mobile-01 --screen night-baseline-mobile

python design-excellence/visual_audit.py prompt \
  --project faneqo-night --audit initial-mobile-01
```

The prompt names the private image path. **Open the image with a visual tool, inspect it yourself, then record each real observation.** Do not invent a screen from source-code descriptions. Use screenshot provenance and user intent to establish context.

For a real visually verified issue:

```bash
python design-excellence/visual_audit.py observe \
  --project faneqo-night --audit initial-mobile-01 --id finding-01 \
  --category COMPOSITION --severity MAJOR \
  --observation "The feature photograph has no clear priority over the repeated tiles" \
  --because "Equal visual weight makes the night read as an inventory, not a memorable story" \
  --recommendation "Elevate one authorized photograph and reduce the scale of supporting thumbnails" \
  --evidence IMAGE_OBSERVED --pixels-inspected
```

This is a **command illustration**, not proof the current Faneqo screen has the issue. `--pixels-inspected` is a reviewer assertion, not computer vision validation.

Other evidence types: `OWNER_REPORTED` (faithful account of direct feedback, **not** image inspection), `DESIGN_HYPOTHESIS` (unverified proposal). Priority: `BLOCKER`, `MAJOR`, `REFINE`.

```bash
python design-excellence/visual_audit.py report --project faneqo-night --audit initial-mobile-01
python design-excellence/visual_audit.py audit --project faneqo-night --audit initial-mobile-01
```

All findings are append-only under `.cil-private/design-audits/<project>/<audit>/`, not committed. Repeated IDs cannot overwrite. The original screenshot hash must still match its capture record.

## Senior art director's inspection sequence

1. **Identity and intent:** What is the human and cultural subject? What should the viewer feel? Identify the actual content and avoid stock genre stereotypes.
2. **First visual impression:** At the specific viewport, where does the eye naturally land? What competes with it? Quote visible elements, not abstract judgments.
3. **COMPOSITION:** Scale relations, alignment, dominant mass, asymmetry, focal path, compositional tension, cropping, editorial sequence.
4. **SPACING:** Deliberate negative space versus accidental emptiness; section pauses; density; repeating card rhythms.
5. **TYPOGRAPHY:** Weight, voice, optical sizing, line length/breaks, kerning/leading, text hierarchy and small-screen reflow. Check legibility, not just novelty.
6. **PHOTOGRAPHY:** Image quality, subject authenticity, color/light, emotional effect, subject crop, attribution, mobile art-directed crops.
7. **COLOR:** Palette relationships, photo/background integration, tonal contrast, semantic colors and real contrast measurement if tools permit.
8. **HIERARCHY:** Main task versus supporting story; clear primary action, visible media controls, editor state and meaningful text.
9. **MOTION:** Does it communicate cause/continuity/story? Can it be disabled? Does it harm low-end devices? Screenshots alone **cannot** verify motion.
10. **MICRODETAIL:** Edge alignment, button geometry, icon consistency, fine type, separators, optical balance, visible affordances.
11. **RESPONSIVE/TASK_VISIBILITY:** Inspect separate mobile captures; do not infer them from desktop. Surface actual loading, editing, accessibility and empty states only when truly observed.

These are **prompts for judgment**, not numerical formulas. Avoid one 'masterpiece score.' An elegantly empty screen can be visually polished but unusable.

## Compare a revised screenshot against the original

Import the revised screenshot separately into the existing private Visual Memory workspace; do not overwrite the baseline. Start a distinct audit for the revised screen, then **visually inspect** both images.

```bash
python design-excellence/visual_audit.py start \
  --project faneqo-night --audit revised-mobile-01 --screen night-revised-mobile

# After an actual visually observed review of the candidate:
python design-excellence/visual_audit.py compare \
  --project faneqo-night --before initial-mobile-01 --after revised-mobile-01
```

The comparison identifies both source image locations, whether the viewport and state match, and the independently authored findings. It does **not** automatically choose a winner, make a stronger claim than the available evidence, or overwrite any historical audit. A changed viewport or app state is flagged as a comparability warning. The owner still decides whether the revision is better.

## Required report standard

- **At most five** high-impact recommended changes in a first iteration, prioritized by severity.
- Every recommendation cites a specific visual observation and explains how the correction would alter the composition or task clarity.
- Direct image observation, owner report and hypothesis stay separately labeled.
- The report explicitly names **categories not examined**. Unobserved does not mean passed.
- Keep the screenshot's viewport/state attached, so reviews of different states are not mixed.
- A full audit should compare before/after at matched viewport, and separately test real interaction, WCAG behavior, image rights and task success.
- Use `judgment_ledger.py` for actual **owner decision feedback**; do not auto-transfer an AI critic's assessment as the owner's taste.

## Next development gate

After the Atlas feature stabilizes and an authorized Faneqo screen is safely captured, have two independent critics inspect the same actual screenshot; consolidate precise findings into one owner-reviewed revision plan. Compare the revised render. Do **not** call a successful metadata test proof of world-class visual output.
