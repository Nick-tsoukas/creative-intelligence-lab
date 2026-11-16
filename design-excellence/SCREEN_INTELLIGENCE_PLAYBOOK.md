# Screen Intelligence — Read-Only Implementation Context

**Mission:** Before a design agent changes any Nuxt 3/Vue screen, it needs to know which information and behaviors genuinely exist. Visual inspiration must not turn into fake controls, invented API fields, disappearing permissions or broken editing states.

This complements the other chat's **Project Design Packet Router**: that router selects project screenshots and research examples, whereas this tool records the *technical and data implementation reality* of an authorized application.

## Implemented today

`screen_intelligence.py` can inspect a specifically selected `.vue`, `.ts`, `.js` or `.mjs` file **without executing it**. It extracts limited indications of:
- Nuxt/Vue composables (such as `useFetch`, `useAsyncData`, `useState`, `useRoute`, `computed`).
- Fetch callsites and straightforward static URL literals.
- Relative imports and UI event/binding evidence.
- Optional explicitly sourced contract facts: data names/shapes, code/API origins, what is editable, authority/permissions and state handling.
- Mandatory unknowns and implementation constraints.

It deliberately does **NOT** infer exact response shapes, backend authorization, connected data, runtime behavior or actual artist/visitor entitlements from a frontend call.

## Working sequence

**First:** find and select the actual route and a few related components/composables in an *authorized local checkout*, not production. The tool does not crawl the repo on its own, run app code, read .env files or access network services.

```bash
python design-excellence/screen_intelligence.py \
  --repo-root /path/to/musicbizqr \
  --screen pages/[bandSlug]/event/[eventSlug].vue \
  --include composables/useShowRecap.ts \
  --format markdown
```

That example path and composable are **illustrative, not verified file locations**. Select real existing paths first. There is a cap of 12 explicitly selected source files, 256KB per file. All findings from regex-based inspection are `STATIC_HINT_NOT_VERIFIED`.

**Next:** inspect the actual backend route/controller/schema and a sanitized authorized dev response or tests. Confirm which fields, operations, permission checks and states truly exist. Never display live tokens or personal records. Write a compact local JSON contract using [the example](examples/screen-contract.example.json).

```bash
python design-excellence/screen_intelligence.py \
  --repo-root /path/to/musicbizqr \
  --screen pages/example.vue \
  --include composables/useExample.ts \
  --manifest /path/to/private-reviewed-contract.json
```

Manifest `route` must exactly match `--screen`. A `CODE_OBSERVED` fact must identify a real code location; a `RUNTIME_TESTED` claim requires actual executed evidence; `OWNER_CONFIRMED` is an explicitly supplied owner requirement, not proof of implementation. Tool validation cannot authenticate a claim; the reviewer is accountable.

## What the design agent must know

| Dimension | Grounding source | Design relevance |
|---|---|---|
| Route and entry state | Actual page and navigation routes | What the user first sees |
| Actor and job | Product requirements or real task research | Why this screen exists |
| Frontend components | Vue source/composables | Existing control architecture |
| Data fields / relationships | Strapi content types and verified dev payload | Which information can be designed around |
| Read API | Client and backend routes | Real data availability, loading states |
| Write operations | Mutations/controller logic | Save, publish, upload, send, delete actions |
| Permissions | **Server-side** policy, not just hidden buttons | Who can view/edit/publish/send |
| Media | Image/video/audio schemas, storage and rights | Genuine player/gallery/upload capabilities |
| Errors/recovery | Real network and form states | Reliability, feedback, interruption |
| Routing/share | Live destination semantics | Links and QR must lead to the right resource |
| Performance | Device/browser facts | Asset sizes, lazy loading, SSR, low-end GPU |
| Unknowns | Named explicit gaps | Features design must NOT invent |

### Faneqo-specific truth constraints (do not assume implementation)

- A photo uploaded is not necessarily public, attached to a Night, published, or shown to fans.
- A message composed is not necessarily delivered; fan targeting and limits require verified policy.
- A QR image existing in a UI does not prove its destination or download is functional.
- A music embed is not necessarily licensed, playable or allowed for a particular account.
- An artist's editing controls are separate from a fan's public view.
- A dashboard number must be connected to a real, authorized metric, not a visual placeholder.

## Review and handoff gate

Before implementation, provide a compact **Screen Implementation Contract**:

1. Screen/route and relevant source files with explicit evidence references.
2. Actual displayable data fields and source (mark `UNKNOWN` where uncertain).
3. Actual available actions and server-owned permissions.
4. Data lifecycle: loading, empty, editing, saving, saved, failed, retry, published/private, where truly supported.
5. Content/asset provenance, data privacy and consent.
6. Functional invariants that redesign cannot remove.
7. Any genuinely missing API/schema support as **proposed backend work**, not an implicit frontend feature.
8. Optional visual audit and Atlas research, provided separately; art direction should not claim to validate backend reality.

Don't let a large source dump replace the interface brief. A small number of verified code references and a field/action/state matrix are usually more useful than dozens of files.

## Security and data privacy

- Tool scans only explicit relative code paths, refuses symlinked source files and potential secret-like filenames, and never sends code to external services.
- It emits only references to static calls/imports, not entire file contents. Dynamic endpoint paths are `UNKNOWN` rather than guessed.
- Keep sanitized backend responses **outside Git** and avoid copying secrets, customer emails, private fan media, or authentication tokens into manifest evidence.
- Regex extraction is lossy: multiline templates, aliases, runtime wrappers and server-side permissions require a developer's manual code and runtime inspection.
- No feature implementation or Faneqo deployment is authorized by running this tool.

## Future integration after concurrent work

The Atlas research packet and a Screen Intelligence packet can be used together: one explains **how the new design might become extraordinary**; the other defines **what it must actually display and do**. Both should remain optional and independently inspectable. Add at most one on-demand integration pointer to the verified active v5.0 skill, only after other work completes.
