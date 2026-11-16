# Pattern 01 — Inline Editorial Writing (Research Brief)

**Use when:** content must be authored in the visual context where it will later be read. **Status:** original proposed pattern, NOT an audited case study, a proven design or implemented rich-text editor.

**Research references:** Tiptap (https://tiptap.dev/), WAI-ARIA APG (https://www.w3.org/WAI/ARIA/apg/), Mobbin and Refero as *discovery libraries* (no individual product flows viewed). Do not cite uninspected screenshots as verified.

## Visual decision
Frame the writing region as an editorial page, with one readable measure, meaningful headings, beautiful paragraph rhythm and breathing room. Contextual tools should appear only when helpful, while a **persistent trustworthy save state** remains perceivable.

## Interaction contract
- Empty state: give a clear writing invitation and visible target.
- Enter edit: focus intended insertion point; preserve surrounding readable page context.
- Toolbar: formatting roles, selection retention, keyboard accessibility, touch adaptation.
- Draft/save: distinguish local edits, saving, saved, unsaved error, retry and publish.
- Undo/redo: preserve document state and focus; safe links and pasted content.
- Exit: don't silently lose unsaved edits or auto-publish to a broader audience.
- Mobile: keyboard occlusion, selection handles, constrained toolbar, touch hit targets, sticky save state.
- Data: actual backend may store plain text; rich text requires explicit format/migration decisions.

## Artistic tension
Chimero-like purpose/craft suggests writing should *feel* meaningful, but full-bleed photography behind body text can destroy readability. Use expression in context and durable utility for editing.

**Reject if:** autosave is fictional, edit feels like a different screen, formatting disappears on mobile, publish semantics change without explicit approval, output is unreadable.

**To study for real:** acquire authorized product screen/flow references with exact product/viewport/source/date; inspect selection, error, navigation and focus in a functioning editor.
