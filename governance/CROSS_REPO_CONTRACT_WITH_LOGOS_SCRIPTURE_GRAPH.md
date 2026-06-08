# Cross-Repo Contract With `logos-scripture-graph`

## Ownership

`logos-governance-architecture` owns cross-repo policy, authority contracts, update rules, and
validation patterns.

`logos-scripture-graph` owns:

- canonical Scripture records;
- Scripture chunks;
- Scripture references;
- Scripture retrieval contracts;
- Scripture canonical metadata.

`logos-boundary-literature` owns:

- boundary literature metadata;
- source status records;
- trust profiles;
- attribution and forgery status;
- scoped boundary claims;
- reception/background/refutation relationships.

Authority hierarchy:

```text
logos-governance-architecture
  -> cross-repo policy and authority contracts
  -> logos-scripture-graph
     -> canonical 66-book Scripture truth
     -> logos-boundary-literature
        -> scoped supporting/background/reception/refutation material
```

Boundary material is under, or at minimum never above, canonical Scripture authority.

## Reference Direction

This repo may point to Scripture refs. It must not copy Scripture text.

`logos-scripture-graph` may point to this repo as reception/background only. It must not absorb this
repo's claims as canonical truth.

## Cross-Repo Rule

Claims from this repo cannot become canonical Scripture claims without explicit tradition/profile
review.

Claims from this repo must not override, contaminate, or become equal authority to canonical
Scripture. If a task appears to require boundary material to modify canonical Scripture outputs,
stop and report.

## Contract Fields For Future Relationships

- source repo;
- target repo;
- source record ID;
- target Scripture ref;
- relationship type;
- trust level;
- tradition scope;
- profile scope;
- assertion mode;
- review status;
- provenance.

## Forbidden

- copying boundary source text into `logos-scripture-graph`;
- copying Scripture text into this repo;
- using generic `related_to`;
- defaulting boundary claims into canonical answers;
- hiding tradition scope.
