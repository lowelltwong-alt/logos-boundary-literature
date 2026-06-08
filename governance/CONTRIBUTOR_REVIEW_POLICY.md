# Contributor Review Policy

## Status

- Policy id: `BOUNDARY-CONTRIBUTOR-REVIEW-v1`
- Repository: `logos-boundary-literature`
- Status: active policy

This is public contributor-review governance for sensitive boundary-literature changes.

## Named Rule

`BOUNDARY-CONTRIB-001 — External Contributor Review Required`

Importance:

- P1 normally.
- P0 when source ingestion, trust hierarchy, canon status, attribution/forgery policy, boundary
  claims, corpus records, or cross-repo authority is affected.

## Rule

External contributor changes to trust hierarchy, canon-status policy, source-intake policy,
attribution/forgery policy, source text ingestion, boundary claim records, commentary/reception
claim records, corpus records, or cross-repo authority rules require maintainer review before merge.

## Applies To

This policy applies to `logos-boundary-literature`.

External contributor changes require maintainer review when they affect:

- trust hierarchy;
- canon status by tradition;
- source intake;
- attribution and forgery labels;
- source text ingestion;
- boundary claim records;
- commentary/reception claims;
- corpus records;
- cross-repo authority rules.

Routine maintainer-controlled changes to docs, scaffolding, planning, schema drafts, tests, and
templates are governed by normal repository controls and validation.

## Non-Authorization

This policy does not:

- apply to `logos-scripture-graph` or change its rules;
- authorize importing source texts;
- authorize real corpus records;
- authorize boundary claims as canonical truth;
- allow boundary repo material to override Scripture;
- allow boundary repo material to equal Scripture authority.

This policy does not authorize real corpus records.
This policy does not authorize boundary claims as canonical truth.
This policy does not permit boundary repo material to override or equal Scripture.

## Relationship To Existing Controls

This policy complements:

- `governance/SOURCE_INTAKE_POLICY.md`
- `governance/CONTAMINATION_CONTROLS.md`
- `governance/CANON_AND_AUTHORITY_POLICY.md`
- `governance/ATTRIBUTION_AND_FORGERY_POLICY.md`
- `governance/CROSS_REPO_CONTRACT_WITH_LOGOS_SCRIPTURE_GRAPH.md`
- `.ai/control/boundary_material_routing.yaml`

All source, claim, corpus, trust, attribution, and cross-repo authority changes remain subject to
the stricter applicable governance rule.
