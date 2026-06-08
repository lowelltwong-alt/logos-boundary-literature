# Project Status

Status: T002 three-repo routing guardrails complete.

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

## Next Recommended Task

Review source intake policy and add validation before any dummy records. Real source text import is
not allowed yet. Governance repo should receive a coordinated cross-repo authority contract update
after its local dirty work is resolved.
