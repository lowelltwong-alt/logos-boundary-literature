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

---

## T004 Boundary Governance Stop Rules

- task_id: T004
- status: complete
- updated_by: Codex

### Files changed

- AI_FRONT_DOOR.md
- README.md
- .ai/control/boundary_material_routing.yaml
- .ai/control/contributor_review_policy.yaml
- .ai/control/PROJECT_STATUS.md
- .ai/handoffs/INITIAL_HANDOFF.md
- governance/BOUNDARY_GOVERNANCE_CONSTRAINTS.md
- governance/CONTAMINATION_CONTROLS.md
- governance/CROSS_REPO_CONTRACT_WITH_LOGOS_SCRIPTURE_GRAPH.md
- governance/RULES_REGISTRY.md
- governance/THREE_REPO_ROUTING_GUARDRAILS.md
- tests/test_boundary_governance_stop_rules.py

### Decisions made

- Added `BOUNDARY-GOV-001 - Governance Is Constraint, Not Obstacle`.
- Added `BOUNDARY-GOV-002 - Owner-Reserved Authorization for Boundary-Originated Higher-Layer Changes`.
- Boundary-originated requests that conflict with governance-layer policy, canonical Scripture
  authority, repository-link contracts, routing policy, trust hierarchy, or canonical scope must
  stop and be reviewed in the higher-authority repository.
- Only Lowell Wong, as project owner, may authorize boundary-originated changes to those
  higher-authority surfaces.
- Contributor consensus, contributor volume, automated recommendation, agent routing, and
  boundary-layer operational need are not sufficient authority.

### Validation performed

- `python -m pytest -q` passed: `17 passed`.
- YAML parse checks passed.
- `git diff --check` passed.

### Exact next action

Run validation and review T004. Do not import source texts, add real corpus records, create
boundary claims, or request higher-authority changes from this boundary layer.
