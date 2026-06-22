# AI Table Of Contents

This file is the navigation map for agents and maintainers entering
`logos-boundary-literature`.

## Start Here

- `AI_FRONT_DOOR.md` - authority boundary, routing table, hard prohibitions, and next tasks.
- `README.md` - human-facing summary of the scaffold and contamination controls.
- `.ai/control/boundary_material_routing.yaml` - machine-readable routing and stop triggers.
- `ROADMAP.md` - staged source-layer roadmap.

## Governance

- `governance/THREE_REPO_ROUTING_GUARDRAILS.md` - active three-repo routing rules.
- `governance/CROSS_REPO_CONTRACT_WITH_LOGOS_SCRIPTURE_GRAPH.md` - contract with Scripture Graph.
- `governance/CONTAMINATION_CONTROLS.md` - rules that keep boundary material out of canonical Scripture authority.
- `governance/TRUST_HIERARCHY.md` - trust levels for boundary material.
- `governance/SOURCE_INTAKE_POLICY.md` - source-intake controls before any real corpus work.
- `governance/ATTRIBUTION_AND_FORGERY_POLICY.md` - attribution, disputed status, and forgery controls.
- `governance/CANON_AND_AUTHORITY_POLICY.md` - canon and authority distinctions.
- `governance/BOUNDARY_GOVERNANCE_CONSTRAINTS.md` - P0 stop rules for boundary-originated pressure on higher-authority repos.

## Schemas And Database Planning

- `schemas/README.md` - schema index and source-ingestion warning.
- `schemas/reliability_evidence_database_plan.md` - Bible reliability/provenance evidence database plan.
- `schemas/reliability_evidence_source_spine.md` - starting source spine with confirmed metadata and candidate-claim separation.
- `schemas/reliability_evidence_intake_queue.md` - pre-evidence intake queue for source candidates, repo routing, and review gates.
- `schemas/reliability_evidence.sqlite.schema.sql` - SQLite scaffold for boundary and derived evidence metadata.

## Routing Summary

- Canonical 66-book Scripture text, chunks, manuscript witnesses, variants, and canonical Scripture records belong in `logos-scripture-graph`.
- Commentaries, church-father citations, patristic reception, theologian writings, attribution status, and reception-history metadata belong here.
- Denominational and theological development over time belongs in planned `logos-doctrine-genealogy` after governance registration.
- Unified evidence products are derived artifacts. They may join labels and references, but they must not transfer authority.
- Bible reliability/provenance database work starts here only as metadata and derived evidence planning. Actual Scripture manuscript, fragment, variant, and canonical evidence records belong in `logos-scripture-graph`.

## AI Rule

If a task would mix commentary, patristic, theologian, or denomination-profile data into canonical Scripture tables, canonical views, or default Scripture retrieval, stop and report.

If a boundary record lacks trust level, tradition/profile scope, provenance, or review status, keep it staged or unreviewed.
