# Design Excellence — Isolated Increment 001

This folder is an **additive, low-resource design research and creative-judgment tool**. It does not replace the current Visual Atlas, the private project screenshot workspace, the installed Claude skills, or Faneqo implementation. All changes currently live on a **dedicated unmerged branch**.

- [Prioritized implementation plan](IMPLEMENTATION_PLAN.md)
- [Private feedback ledger](judgment_ledger.py)
- [Standard-library tests](test_judgment_ledger.py)

## Why a judgment ledger?

Inspiration alone cannot tell an AI why the owner preferred one draft or rejected another. Explicit decision records can preserve the exact visual criticism, specific artifact and context. They are not automatic evidence that an AI's aesthetic choices have improved, and they do **not** update model weights.

## Quick start

Python 3.12+; no package install, database, browser, paid API, daemon or image embeddings. Run from the repository root:

```bash
python design-excellence/judgment_ledger.py record \
  --project faneqo-night \
  --id review-001 \
  --candidate night-concept-b-mobile \
  --decision REVISE --axis SPACE \
  --observation "The gallery sits too close to the hero photograph" \
  --because "The lead performance photo needs a stronger visual pause" \
  --next-move "Increase negative space and reduce repeated thumbnail density" \
  --evidence OWNER_FEEDBACK \
  --source "Human review; example only, replace with real source" \
  --context "390px mobile review"

python design-excellence/judgment_ledger.py brief --project faneqo-night
python design-excellence/judgment_ledger.py audit --project faneqo-night
python design-excellence/judgment_ledger.py list --project faneqo-night
```

The command above is an **illustrative example**, not a claim the owner actually said those words. Use `--evidence OWNER_FEEDBACK` only for faithful human review you actually received. Use `IMAGE_OBSERVED` for actually inspected pixels, `FLOW_TESTED` for a real interaction test, and `RESEARCH_HYPOTHESIS` for an untested assumption. Labels are author-provided, not authenticated.

Data is saved privately as `.cil-private/creative-judgment/<project>/records/<id>.json`; that directory is already in `.gitignore`. No user screenshot or visual reference is copied. Do not enter secrets, fan names, customer identifiers or other sensitive data even into private text fields.

### Correcting an opinion without rewriting history

```bash
python design-excellence/judgment_ledger.py record \
  --project faneqo-night \
  --id review-002 --supersedes review-001 \
  --candidate night-concept-b-mobile \
  --decision APPROVE --axis SPACE \
  --observation "The revised page now gives the hero room" \
  --because "The section pacing is calmer while the actions remain obvious" \
  --next-move "Keep the current spatial relationship for this concept" \
  --evidence OWNER_FEEDBACK --source "Owner review; illustrative example"
```

The old record remains on disk and shows up in `list`. The `brief` command includes only active records, **OWNER_FEEDBACK only by default**, up to eight recent examples. It doesn't infer generalized personality traits or run model training. To export machine-readable context:

```bash
python design-excellence/judgment_ledger.py brief --project faneqo-night --format json
```

For a research or design audit, `--include-nonowner` includes all explicitly labeled evidence types and still identifies their origins.

### Tests

```bash
python -m unittest discover -s design-excellence -p 'test_*.py' -v
```

Tests use temporary directories, not private production data. Do not mark as passed until they have actually run in an environment with this branch checked out.

## Integration contract

The owner approves all aesthetic decisions. This tool only remembers explicit feedback and exports a bounded briefing packet for future sessions. The other chat controls the Atlas's reference records and visual gallery. **Do not change or merge its work**, and do not add global v5.0 skill instructions until the active skill is located, its owner confirms a suitable integration point, and conflicts are checked.
