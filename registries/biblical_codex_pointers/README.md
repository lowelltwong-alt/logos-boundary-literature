# Boundary And Non-Canonical Codex Digital-Pointer Registry

This is the separate directory requested for deuterocanonical, apocryphal,
pseudepigraphal, gnostic/heterodox, disputed, and other non-canonical manuscript
content. It contains metadata pointers only—no source text, transcription, images,
downloads, or ingestion runtime.

## Repository Boundary

- This repository owns `boundary_noncanonical` rows.
- `logos-scripture-graph` owns default-66 canonical rows.
- A mixed physical codex is split by content. The same `physical_witness_id` may
  occur in both repositories, while `companion_pointer_ids` preserve the relationship.
- Nothing here can change canonical Scripture, override Scripture, or enter default
  Scripture retrieval.

Every boundary row is forced by schema to declare `trust_level`, `tradition_scope`,
`profile_scope`, `provenance`, `canonical_claim: false`, and
`can_override_scripture: false`.

## Coverage

`boundary_noncanonical/catalog_roots.jsonl` is the extensive discovery layer. It
starts with NASSCAL e-Clavis—the strongest focused enumerating root for Christian
apocrypha—then adds official and scholarly portals needed for Coptic, Syriac,
Dead Sea Scrolls, deuterocanonical, fragment, and distributed institutional coverage.

`boundary_noncanonical/direct_witnesses.jsonl` is a curated seed for mixed codices
already represented in the canonical lane. It is deliberately non-exhaustive.
The manifest records known gaps and forbids a static 100-percent item claim.

## Rights And Use

All rows are pointers under `rights_status: not_reviewed_pointer_only` and
`download_authorized: false`. Cataloging a URL does not authorize downloading,
copying, redistribution, commercial use, or model training.

## Validation

```powershell
python scripts\validate_biblical_codex_pointer_registry.py
python scripts\validate_boundary_schema_controls.py
python -m pytest -q
```
