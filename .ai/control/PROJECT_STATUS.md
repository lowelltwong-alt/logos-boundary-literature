# Project Status

Status: T005 boundary schema controls and authority crosswalk proposed.

This repository is `logos-boundary-literature`, a governed boundary/noncanonical/reception
literature scaffold. It is not canonical Scripture and contains no source text corpus.

## Current Scope

- Governance docs created.
- JSON Schema scaffolds created.
- Empty data directories created with `.gitkeep` only.
- No source ingestion.
- No runtime pipelines.
- No canonical Scripture records.
- Three-repo routing guardrails added:
  - `logos-governance-architecture` owns cross-repo policy and authority contracts.
  - `logos-scripture-graph` owns canonical 66-book Scripture truth.
  - `logos-boundary-literature` owns boundary/supporting literature under, or never above,
    canonical Scripture authority.
  - Boundary material must not override, contaminate, or become equal authority to canonical
    Scripture.
- Contributor review policy added:
  - external contributor changes to sensitive governance, source, claim, corpus, trust,
    attribution, or cross-repo authority surfaces require maintainer review before merge;
  - the policy applies only to `logos-boundary-literature`;
  - it does not authorize source-text ingestion, real corpus records, canonical Scripture records,
    or boundary claims as canonical truth.
- Boundary governance stop rules added:
  - `BOUNDARY-GOV-001 - Governance Is Constraint, Not Obstacle`;
  - `BOUNDARY-GOV-002 - Owner-Reserved Authorization for Boundary-Originated Higher-Layer Changes`;
  - boundary-originated requests must stop if they conflict with governance-layer policy, canonical
    Scripture authority, repository-link contracts, routing policy, trust hierarchy, or canonical
    scope;
  - only Lowell Wong, as project owner, may authorize boundary-originated changes to those
    higher-authority surfaces;
  - contributor consensus, contributor volume, automated recommendation, agent routing, and
    boundary-layer operational need are not sufficient authority.
- Boundary schema controls proposed:
  - `scripts/validate_boundary_schema_controls.py` checks the four JSON Schemas as Draft 2020-12
    schemas;
  - trust-tier vocabulary is locked across schema and documentation surfaces;
  - contamination lint emits warn-level findings for suspected verse-length quoted strings in data
    files;
  - `governance/AUTHORITY_LADDER_CROSSWALK.md` keeps boundary trust tiers separate from S0-S7
    doctrine authority rungs.

## Next Recommended Task

After T005 lands, review source intake policy and add validation before any dummy records. Real
source text import is not allowed yet. Any boundary-originated request that targets
higher-authority governance or canonical Scripture layers must stop and be reviewed in the
higher-authority repository.
