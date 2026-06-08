# Contamination Controls

Boundary texts may reference Scripture. Scripture records must not absorb boundary claims as
canonical truth.

`logos-boundary-literature` may interoperate with `logos-scripture-graph`, but it is hierarchically
under, or at minimum never above, canonical Scripture authority. Boundary claims must not override,
contaminate, or become equal authority to canonical Scripture.

## Core Controls

- No generic `related_to` links.
- Use typed relationships with authority scope.
- No default retrieval into canonical answers.
- No source without source status.
- No claim without provenance.
- No canon claim without tradition scope.
- No commentary or reception claim as canonical truth.
- No boundary source text copied into `logos-scripture-graph`.
- No boundary material used to mutate canonical Scripture records, chunks, evaluator inputs, or
  default Scripture retrieval.
- Stop and report if a task appears to require boundary material to modify canonical Scripture
  outputs.

## Typed Relationships

- `boundary_text_references_scripture`
- `scripture_referenced_by_boundary_text`
- `commentary_mentions_boundary_source`
- `commentary_interprets_passage_using_boundary_source`
- `boundary_text_parallel_to_scripture`
- `boundary_text_distorts_scripture`
- `boundary_text_preserves_reception_motif`
- `boundary_text_refuted_by_orthodox_source`
- `work_claims_false_attribution`
- `work_has_disputed_attribution`
- `work_is_known_forgery`
- `tradition_receives_as_canonical`
- `tradition_reads_for_edification`
- `tradition_rejects_as_canonical`

## Safe Pattern

```text
Boundary source B references Scripture passage S.
Record that B references S with source, tradition, trust, and review status.
Do not mutate S.
```

## Unsafe Pattern

```text
Scripture passage S means boundary claim C because boundary source B says it.
```

## Retrieval Boundary

Boundary material may be retrieved for background, reception, comparison, and refutation only after
review. It must not appear in canonical Scripture answers by default.

## Contributor Review Boundary

External contributor changes to cross-repo authority rules, boundary claim records,
commentary/reception claims, corpus records, trust hierarchy, canon status by tradition, source
intake, source text ingestion, or attribution/forgery labels require maintainer review before merge.

This review policy applies only to `logos-boundary-literature`. It does not apply to
`logos-scripture-graph` and does not change its rules, does not authorize source-text ingestion, and does not permit boundary
repo material to override or equal Scripture.
