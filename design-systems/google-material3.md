# Google Material 3 / M3 Expressive — Attention, Emotion and Behavior

**Date reviewed:** 2026-11-11  
**Evidence:** OFFICIAL-GUIDANCE-REVIEWED + GOOGLE-REPORTED-RESEARCH. No independent replication of claims or device study.

## Primary references
- Material Design 3 — https://m3.material.io/
- Get started — https://m3.material.io/get-started
- Google's research account — https://design.google/library/expressive-material-design-google-research
- Typography roles — https://m3.material.io/styles/typography/applying-type
- Canonical responsive layouts — https://m3.material.io/foundations/layout/canonical-examples/overview

## Documented direction
Material 3 includes foundations, styles and components. M3 Expressive expands color, shape, typography, motion and adaptive components. Google's official documentation describes a typography role system (display, headline, title, body, label; three sizes each) and canonical layout patterns (feed, list-detail, supporting pane) with compact/medium/expanded configurations.

Google's own research article reports **46 studies** covering more than **18,000 participants**, using techniques including eye tracking, surveys, preference experiments and usability exercises. In tested examples, certain important elements were noticed **up to four times faster** in expressive versions; Google's report does **not** make that a universal guarantee for all apps or tasks.

## A close reading of Google's disclosed Send-button example
**FACT (Google-authored research description):** The expressive email example enlarges the Send action, moves it near the keyboard, and uses contrasting color. Google's team reports participants spotting it substantially faster than a small top-toolbar Send button in its comparison.

**INTERPRETATION:** Placement and contrast are interacting with task context. The strongest explanation is not "bright buttons are better," but *position and emphasis should reflect the user's current task*. The nearby keyboard makes the action geographically relevant.

**COUNTEREXAMPLE:** In an editing app with several equally dangerous commands, exaggerated color and size can misdirect attention and make other actions hard to find. Salience is a limited resource.

## Expressive typography
Material separates display/headline styling from readable body text. Decorative or expressive faces are discouraged for small body text. The lesson is to budget expressive novelty according to legibility demands.

## Motion
Google highlights motion physics/spring-based transitions and expressive shapes. We should study timing as feedback and continuity, but animation can reduce control or cause discomfort if unrestrained. Test reduced motion and interruption/reversibility.

## Discussion and uncertainty
- Research claims are **published by the system creator**, not independently replicated here.
- The cited effect concerns a specific comparison, not evidence that the entire system universally outperforms alternatives.
- We did not inspect source data, study protocols or the exact participant breakdown in this pass.
- Design components and recommendations may evolve; dated source check required for future use.

## Visual study targets
1. Large vs small primary buttons, placement relative to task.
2. Expressive shape/contrast vs neutral controls.
3. Adaptive list-detail across 3 width classes.
4. Type role distinctions in editorial and dense workflows.
5. Motion with and without preference for reduced movement.

**Screenshots:** linked from original source pages in [visual library](../visual-library/README.md). No actual Google UI screenshot has yet been independently captured into this repository.

## Transferable synthesis
Use color, size, containment, motion and placement as instruments for **task-relevant attention**, not blanket expressiveness. Prefer experimentable hypotheses and measured outcomes over aesthetic fashion.