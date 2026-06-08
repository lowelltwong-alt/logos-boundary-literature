# Initial Handoff

## Task

- task_id: T001_INITIAL_SCAFFOLD
- title: Scaffold boundary literature governance repo
- status: complete

## Agent

- agent_name: Codex
- mode: scaffold
- stage: final

## Files changed

- AI_FRONT_DOOR.md
- README.md
- LICENSE_POLICY.md
- governance/
- schemas/
- data/*/.gitkeep
- eval/.gitkeep
- tests/README.md
- tests/.gitkeep
- .ai/control/PROJECT_STATUS.md
- .ai/handoffs/INITIAL_HANDOFF.md
- .ai/tasks/T001_INITIAL_SCAFFOLD.task.yaml

## Decisions made

- This repo is not canonical Scripture.
- No source texts were imported.
- Data folders remain empty except `.gitkeep`.
- Trust hierarchy distinguishes deuterocanonical, high-trust background, historical context,
  patristic reception, heterodox/gnostic, disputed attribution, known forgery/fake, and quarantine
  material.
- Cross-repo references to `logos-scripture-graph` must not contaminate canonical Scripture.

## Validation performed

- File tree checked.
- JSON schemas parsed with Python.

## Risks introduced

- Governance is scaffold-only; no automated data validation exists yet.
- Schemas have no sample records yet.

## Unresolved questions

- Which validation runner should be introduced first.
- Whether dummy placeholder records should be added before source intake workflow.

## Exact next action

Claude review the scaffold. Do not import source texts. Next task should add source intake
validation or invented dummy records, not real corpus import.

---

## T003 Contributor Review Policy Update

- task_id: T003
- status: complete
- updated_by: Codex

### Files changed

- AI_FRONT_DOOR.md
- README.md
- governance/RULES_REGISTRY.md
- governance/SOURCE_INTAKE_POLICY.md
- governance/CONTAMINATION_CONTROLS.md
- governance/CONTRIBUTOR_REVIEW_POLICY.md
- .ai/control/PROJECT_STATUS.md
- .ai/control/contributor_review_policy.yaml
- .ai/handoffs/INITIAL_HANDOFF.md
- tests/test_contributor_review_policy.py

### Decisions made

- Added `BOUNDARY-CONTRIB-001 — External Contributor Review Required`.
- External contributor changes to sensitive governance, source, claim, corpus, trust, attribution,
  or cross-repo authority surfaces require maintainer review before merge.
- The policy applies only to `logos-boundary-literature`.
- The policy does not apply to `logos-scripture-graph` and does not change its rules.
- The policy does not authorize source-text ingestion, real corpus records, canonical Scripture
  records, or boundary claims as canonical truth.

### Validation performed

- `python -m pytest -q tests/test_contributor_review_policy.py` passed: `6 passed`.
- `python -m pytest -q` passed: `10 passed`.
- JSON schema parse with Python passed.

### Exact next action

Review T003. Do not import source texts, add real corpus records, or create boundary claims.
