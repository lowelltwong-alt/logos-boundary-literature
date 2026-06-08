# T002 Handoff - Three-Repo Routing Guardrails

## Task

- task_id: T002
- title: Three-repo routing guardrails
- status: complete

## Agent

- agent_name: Codex
- mode: governance_docs
- stage: final

## Files read

- AI_FRONT_DOOR.md
- README.md
- .ai/control/PROJECT_STATUS.md
- governance/CANON_AND_AUTHORITY_POLICY.md
- governance/CONTAMINATION_CONTROLS.md
- governance/CROSS_REPO_CONTRACT_WITH_LOGOS_SCRIPTURE_GRAPH.md
- governance/RULES_REGISTRY.md
- governance/TRUST_HIERARCHY.md
- .ai/handoffs/INITIAL_HANDOFF.md
- .ai/tasks/T001_INITIAL_SCAFFOLD.task.yaml

## Files changed

- AI_FRONT_DOOR.md
- README.md
- .ai/control/PROJECT_STATUS.md
- .ai/control/boundary_material_routing.yaml
- governance/CANON_AND_AUTHORITY_POLICY.md
- governance/CONTAMINATION_CONTROLS.md
- governance/CROSS_REPO_CONTRACT_WITH_LOGOS_SCRIPTURE_GRAPH.md
- governance/RULES_REGISTRY.md
- governance/THREE_REPO_ROUTING_GUARDRAILS.md
- .ai/tasks/T002_THREE_REPO_ROUTING_GUARDRAILS.task.yaml
- .ai/handoffs/T002_THREE_REPO_ROUTING_GUARDRAILS.md
- tests/test_three_repo_routing_guardrails.py

## Decisions made

- `logos-boundary-literature` remains a support/background/reception/refutation repo, not canonical Scripture.
- `logos-scripture-graph` owns canonical 66-book Scripture truth.
- `logos-governance-architecture` owns cross-repo policy and authority contracts.
- Boundary claims require trust level, tradition scope, profile scope, and provenance.
- Boundary material must not override, contaminate, or become equal authority to canonical Scripture.
- No source texts, boundary corpus records, commentary corpus records, canonical records, or runtime ingestion pipelines were added.

## Validation performed

- `python -m pytest -q tests/test_three_repo_routing_guardrails.py` passed: `4 passed`.
- `python -m pytest -q` passed: `4 passed`.
- JSON schema parse with Python passed.
- `git diff --name-only -- data eval` returned no data/eval changes.

## Risks introduced

- Governance repo follow-up remains required.
- Boundary repo validation remains lightweight.

## Unresolved questions

- Should governance repo define a shared schema for the routing policy?

## Exact next action

Review T002. Do not import source texts. After the governance repo is clean, add the cross-repo authority contract there.
