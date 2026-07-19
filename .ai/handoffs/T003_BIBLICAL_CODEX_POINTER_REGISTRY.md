# T003 Handoff — Boundary Biblical Codex Pointer Registry

## Task

- task_id: T003
- title: Boundary and non-canonical biblical codex digital-pointer registry
- status: complete

## Agent

- agent_name: Codex
- mode: metadata_build
- stage: final

## Files read

- `AI_FRONT_DOOR.md`
- `ROADMAP.md`
- `.ai/control/PROJECT_STATUS.md`
- `.ai/control/boundary_material_routing.yaml`
- `governance/CANON_AND_AUTHORITY_POLICY.md`
- `schemas/reliability_evidence_source_spine.md`
- `scripts/validate_boundary_schema_controls.py`
- paired T518 Scripture registry artifacts

## Files changed

- `.ai/tasks/T003_BIBLICAL_CODEX_POINTER_REGISTRY.task.yaml`
- `.ai/handoffs/T003_BIBLICAL_CODEX_POINTER_REGISTRY.md`
- `.ai/control/PROJECT_STATUS.md`
- `registries/biblical_codex_pointers/README.md`
- `registries/biblical_codex_pointers/manifest.json`
- `registries/biblical_codex_pointers/boundary_noncanonical/catalog_roots.jsonl`
- `registries/biblical_codex_pointers/boundary_noncanonical/direct_witnesses.jsonl`
- `schemas/biblical_codex_pointer.schema.json`
- `scripts/validate_biblical_codex_pointer_registry.py`
- `tests/test_biblical_codex_pointer_registry.py`

## Decisions made

- Boundary/non-canonical pointers belong in `logos-boundary-literature`; default-66 pointers remain in `logos-scripture-graph`.
- The final top-level `registries/` namespace preserves the repository's enforced empty-`data/` invariant.
- Mixed physical codices share `physical_witness_id` values but use separate content-lane records and cross-repository companion IDs.
- Catalog-root coverage is extensive; direct-witness coverage is curated and explicitly non-exhaustive.
- Every row denies canonical override, download authority, and unreviewed rights inference.

## Validation performed

- `python scripts\validate_biblical_codex_pointer_registry.py` — passed: 12 roots, 8 direct, 20 total, 8 mixed.
- `python scripts\validate_boundary_schema_controls.py` — passed.
- `python -m pytest -q` — passed: 58 tests.
- `git diff --check` — passed.
- Independent checker — PASS; all cross-lane IDs resolved with matching physical witness identities; schema snapshots byte-identical.

## Risks introduced

- Direct witness rows remain a curated seed; NASSCAL and Nag Hammadi item-level enumeration is future work.
- Either single-repo validator checks nonempty companion IDs but does not itself dereference the opposite repository.
- Licensing and rights remain intentionally unreviewed at object level.

## Unresolved questions

- When the governance repository has a clean worktree, should it adopt the shared schema as a governed cross-repository contract?

## Exact next action

Review the T003 and paired T518 diffs together. Do not import texts or download images; if accepted, publish each branch through its repository's normal PR lifecycle.
