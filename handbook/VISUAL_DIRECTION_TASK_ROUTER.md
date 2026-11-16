# Art Direction Task Router — On-Demand Research, Not a Mega-Prompt

**2026-11-15.** Optional read-only decision map for the existing v5.0 system *once its actual source/installation is verified*. Do not replace a newer skill with the Lab's legacy `creative-design-director` alpha. Use it when art direction/visual communication is materially in scope, not for standard CSS/backend work.

## Minimal operating sequence
1. **Establish truth:** user, media, task, actual information and approved brand/locks. For Faneqo consult latest code and `domain-adapters/faneqo/` separately.
2. **Choose the problem category** below and retrieve **one source mechanism**, optionally one contradictory one, rather than the entire atlas.
3. **Make original variations** using unchanged real content; `experiments/004-visual-grammar-studio/` demonstrates three materially different premises in one controlled fictional example.
4. **Critique actual output** at mobile/desktop and in failure states. Record specific defects and revised decisions, not a self-awarded “masterpiece” score.

| Task signal | Source/retrieval | Proposed art-direction judgment | Reject if |
|---|---|---|---|
| Homepage feels generic despite polish | AD01, AD07; `research/015` or MA-001/MA-002 | Product truth → specific artistic thesis → three different hierarchy mechanisms | New concept hides value/CTA, copies famous image/style |
| Hero image powerful but content lost | MA-001, `research/015` | Clear a **local detail region** and use image/negative-space relations | Text fails real contrast, crops hide meaning at 320px |
| Big poster type competes with UI | MA-004, MA-008; `research/016` | Separate expressive display from precise utility type | Form labels/terms overflow, 200% text or text spacing loses content |
| Colors strong but visual hierarchy unstable | MA-005; `research/016` | Test same token/color in different surrounding areas; check real photo overlays | Semantic warning/focus/CTA not distinguishable or contrast unmeasured |
| Creative page needs a compelling sequence | MA-003 and MA-006; AD05 | Sequence meaningful content with visible bypass and quiet interludes | Scrolljacking, delayed action, motion discomfort or performance regressions |
| Photography feels generic or inauthentic | MA-007, MA-008; AD03 | Brief real subject/activity/light/vantage/consent before choosing images | Fake documentary photo, unlicensed artist assets, celebrity/name appropriations |
| Music artist identity lacks culture | MA-004, MA-008; `domain-adapters/faneqo/MASTERPIECE_ART_DIRECTION.md` | Artist/source-specific graphic grammar, not universal “music = neon” | Uses jazz sleeve design wholesale, fabricates performers or genre stereotypes |
| Existing art concept impresses creator but not users | AD08, `templates/MASTERPIECE_DIRECTION_PACKET.md` | Independent semantic/creative/UX/technical critique on actual render | No screenshots, real actions, accessible checks or honest test status |
| A specific artwork needs deep study | `visual-library/masterpiece-atlas/README.md` and exact MA card | Source description vs observed pixels vs interpretation vs transfer | Only a cropped preview exists but detail is invented |
| Pure utility/permissions/error handling | `elite-ux-director` task/status cards | Accurate recipient/state/recovery; subtle brand identity only | Art direction delays a real safety fix |

**Bounded retrieval:** `python3 scripts/query_masterpiece_atlas.py search "type"` → ID list; `... show MA-004` → one study. If Python is missing, manually read selected file from `visual-library/masterpiece-atlas/studies/`. Don't require Python for a normal UX task.

## Source-depth caution
Source-rich is not automatically skillful. The Atlas currently has eight **preview-observed first-pass works**, not eight full deep photographic/paintings studies. `research/015` contains original museum curatorial reading and clearly qualified preview observation; `research/016` contains official publisher content and W3C specifications, NOT the complete licensed Albers book.

## Learning loop
`problem → actual rendered/user evidence → mechanism selected → original variant → observed failure/success → card retained/revised/retired`. Log unexpected failures and where a reference misled the designer. Formal skill benchmarks are deferred; real interface regression and independent visual critique are not.

**Boundary:** no installed v5.0 changes from adding this document, no Faneqo application changes or production releases, no unlicensed external images; owner-approved direction/brand/product truth outrank optional art-theory inference.
