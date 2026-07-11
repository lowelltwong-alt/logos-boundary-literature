# AI Table Of Contents

This file is the navigation map for agents and maintainers entering
`logos-boundary-literature`.

## Start Here

- `AI_FRONT_DOOR.md` - authority boundary, routing table, hard prohibitions, and next tasks.
- `README.md` - human-facing summary of the scaffold and contamination controls.
- `.ai/control/boundary_material_routing.yaml` - machine-readable routing and stop triggers.
- `ROADMAP.md` - staged source-layer roadmap.

## Governance

- `.ai/control/governance_dependency_map_mirror.yaml` - local mirror of the upstream `logos-governance-architecture/governance/GOVERNANCE_DEPENDENCY_MAP.yaml` GD-014 governance-map update gate.
- `scripts/validate_governance_dependency_map_mirror.py` - local validator for the governance dependency-map mirror.
- `scripts/validate_mirror_freshness.py` - tags: `mirror-freshness`, `upstream-drift`, `w2-2`; checks upstream W2-1 governance controls and recorded commit freshness when a local governance checkout is available.
- `governance/LLOS_STANDARD_MIRROR.yaml` - source-pinned LLOS v1 metadata-only adapter; preserves governance ownership and DAD's no-write boundary.
- `governance/LLOS_LESSON_INDEX.yaml` - intentionally empty local lesson-index bootstrap; future lessons require local re-authoring and human admission.
- `scripts/validate_llos_boundary_adapter.py` - tags: `llos`, `w2-8`, `metadata-only`, `dad-no-write`; validates the adapter, empty index, and navigation wiring.
- `governance/THREE_REPO_ROUTING_GUARDRAILS.md` - active three-repo routing rules.
- `governance/CROSS_REPO_CONTRACT_WITH_LOGOS_SCRIPTURE_GRAPH.md` - contract with Scripture Graph.
- `governance/CONTAMINATION_CONTROLS.md` - rules that keep boundary material out of canonical Scripture authority.
- `governance/TRUST_HIERARCHY.md` - trust levels for boundary material.
- `governance/AUTHORITY_LADDER_CROSSWALK.md` - trust-tier to S0-S7 authority-ladder crosswalk; keeps retrieval/contamination utility separate from doctrine authority.
- `governance/SOURCE_INTAKE_POLICY.md` - source-intake controls before any real corpus work.
- `governance/ATTRIBUTION_AND_FORGERY_POLICY.md` - attribution, disputed status, and forgery controls.
- `governance/CANON_AND_AUTHORITY_POLICY.md` - canon and authority distinctions.
- `governance/BOUNDARY_GOVERNANCE_CONSTRAINTS.md` - P0 stop rules for boundary-originated pressure on higher-authority repos.

## Schemas And Database Planning

- `schemas/README.md` - schema index and source-ingestion warning.
- `schemas/reliability_evidence_database_plan.md` - Bible reliability/provenance evidence database plan.
- `schemas/reliability_evidence_source_spine.md` - starting source spine with confirmed metadata and candidate-claim separation.
- `schemas/reliability_evidence_intake_queue.md` - pre-evidence intake queue for source candidates, repo routing, and review gates.
- `schemas/reliability_evidence_method_profiles.md` - review-method profiles for dating, language, variants, patristic citations, and discovery context.
- `schemas/reliability_evidence_timeline_checkpoints.md` - discovery and knowledge-timeline checkpoints for what was known when.
- `schemas/reliability_evidence_patristic_reconstruction.md` - patristic reconstruction question scaffold with citation-mode guardrails.
- `schemas/reliability_evidence_early_traditions.md` - early creed, oral tradition, and early devotion question scaffold.
- `schemas/reliability_evidence.sqlite.schema.sql` - SQLite scaffold for boundary and derived evidence metadata.
- `scripts/validate_boundary_schema_controls.py` - JSON Schema conformance, closed trust-tier vocabulary, and warn-level source-text contamination lint.

## Routing Summary

- Canonical 66-book Scripture text, chunks, manuscript witnesses, variants, and canonical Scripture records belong in `logos-scripture-graph`.
- Commentaries, church-father citations, patristic reception, theologian writings, attribution status, and reception-history metadata belong here.
- Denominational and theological development over time belongs in planned `logos-doctrine-genealogy` after governance registration.
- Unified evidence products are derived artifacts. They may join labels and references, but they must not transfer authority.
- Bible reliability/provenance database work starts here only as metadata and derived evidence planning. Actual Scripture manuscript, fragment, variant, and canonical evidence records belong in `logos-scripture-graph`.

## AI Rule

If a task would mix commentary, patristic, theologian, or denomination-profile data into canonical Scripture tables, canonical views, or default Scripture retrieval, stop and report.

If a boundary record lacks trust level, tradition/profile scope, provenance, or review status, keep it staged or unreviewed.
