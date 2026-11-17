# Render and verify: states, captures and outcomes

## Derive the state matrix

Select applicable rows from the current flow; combine equivalent cases rather than multiplying every state by every width.

| State family | Questions |
|---|---|
| Entry/data | First use, empty, populated, loading, stale, unavailable backend? |
| Editing | Long title/caption, missing required data, last-second edit, reorder/selection? |
| Work in progress | Uploading/processing, partial success, failure, interrupted/resumed, cancel/retry? |
| Authority | Own/team/other scope, eligibility, blocked action with truthful reason, public/third-party effects? |
| Completion | Saved/published/queued exactly as supported, readback, back/reload and duplicate prevention? |
| Presentation | Mobile/desktop, narrow/short, keyboard/focus, zoom, overlay/fixed navigation, reduced motion? |

Record `state | setup/role | width/height | task | expected truth | capture | result`. Screen labels are not evidence that a state was reached.

## Capture without fooling yourself

Use the browser already available and existing servers. No mandatory Playwright/MCP install or persistent capture service. On a 16 GB machine, start with sequential captures and a single browser context; increase only for a measured need.

1. Confirm route, role and target state. Wait for actual fonts, relevant image decoding and stable layout, with a bounded timeout; disclose pending media. Do not wait for network-idle on continuously updating apps.
2. Identify the actual scrolling element. Full-page screenshot covers the document, not necessarily an internally scrolling pane. Record CSS viewport, device scale, document and relevant scroller dimensions, capture mode, state and date.
3. Capture viewport and full intended content where useful. Inspect top, middle and bottom. If an internal scroller cannot be captured faithfully, take overlapping viewport segments, recording scroll offsets. Preserve real sticky/overlay occlusion as a finding.
4. Run optional `python scripts/check_capture.py shot.png --expected-width 390 --expected-height 2400` from this skill root. Expected dimensions are physical screenshot pixels, calculated from capture scope and device scale, not copied blindly from viewport size. Exit 1 means invalid/mismatched; exit 2 means suspicious and requires recapture or documented visual review; exit 0 only means no automated concern detected.
5. Open the image pixels before critique, even on exit 0. Flat-tail detection is a heuristic; dark/minimal art can legitimately trigger it, and incomplete captures can evade it. Unsupported PNG encodings should be re-exported by the existing capture tool; no new decoder dependency is required.

## Two review passes

First catch concrete defects: clipping, semantic/visual order, unreadable field boundaries, hidden actions, sticky height, missing media, false state/copy and bad captures. Then assess creative quality using VISUAL_CRAFT_AND_MEMORY.md. A checklist does not select the artistic winner.

Verify important transitions against backend/read-model truth when authorized; no toast-only success. Re-render affected states after repairs. Mark TESTED / NOT TESTED / BLOCKED with evidence and retain the baseline. Report assistive-technology and user-task testing separately from screenshot review. Research-only work supplies this verification plan rather than pretending to execute it.
