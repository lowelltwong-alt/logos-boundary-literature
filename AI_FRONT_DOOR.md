# AI Front Door

This repository is `logos-boundary-literature`.

It is a governed scaffold for noncanonical, boundary, heterodox, disputed, forged,
reception-history, and supporting literature related to Scripture and Christian theological
interpretation.

## What This Repo Is

- A planning and metadata home for boundary literature.
- A future place for reviewed work records, source-status records, trust profiles, relationship
  contracts, and scoped claims.
- A companion repo that may reference Scripture by stable references.
- A contamination-control layer for background, reception, comparison, refutation, and
  source-tradition work.

## What This Repo Is Not

- It is not canonical Scripture.
- It is not the source of Scripture text, chunks, or canonical Scripture records.
- It is not a place to import full source-text corpora in this scaffold increment.
- It is not a place to declare theological conclusions as settled universal truth.
- It is not a place to flatten all noncanonical works into one trust category.

## Relation To `logos-scripture-graph`

`logos-scripture-graph` owns canonical Scripture records, chunking, and Scripture retrieval surfaces.
This repo owns boundary-literature metadata, scoped claims, source status, and contamination
controls.

This repo may point to Scripture references. It must not copy Scripture text or mutate Scripture
records. Claims from this repo may be used only as background, reception, comparison, refutation, or
tradition-scoped evidence unless a separate human review explicitly authorizes another use.

## Three-Repo Authority Hierarchy

`logos-governance-architecture` is the higher governance/control-plane repo for cross-repo policy,
authority contracts, update rules, and validation patterns.

`logos-scripture-graph` owns canonical Scripture truth for the 66-book Bible graph.

`logos-boundary-literature` supports canonical Scripture work with noncanonical,
deuterocanonical/apocrypha, boundary, heterodox, disputed, forged, commentary/reception, historical
background, and supporting literature.

This repo is hierarchically under, or at minimum never above, canonical Scripture authority. It may
provide background, comparison, reception history, refutation targets, commentary/reception claims,
and tradition-scoped claims. It must not override, contaminate, or become equal authority to
canonical Scripture.

If a task appears to require boundary material to modify canonical Scripture outputs, stop and
report.

Machine-readable local routing policy:
`.ai/control/boundary_material_routing.yaml`.

| User/task intent | Correct repo |
|---|---|
| 66-book Scripture passages/chunks | `logos-scripture-graph` |
| Apocrypha/deuterocanon/boundary literature | `logos-boundary-literature` |
| Gnostic/fake/forged texts | `logos-boundary-literature` |
| Commentary/reception claims | `logos-boundary-literature` |
| Cross-repo policy/authority/update rules | `logos-governance-architecture` |
| Canonical corpus correction | `logos-scripture-graph` |
| Boundary text source intake | `logos-boundary-literature` |
| Repository-link contract changes | `logos-governance-architecture` or coordinated PR |

## Hard Prohibitions

- Do not import full text corpora.
- Do not paste source texts.
- Do not download sources.
- Do not create canonical Scripture records.
- Do not treat boundary literature as Word of God.
- Do not classify all noncanonical literature as equally false.
- Do not normalize fake gospels, high-trust background, deuterocanon, and patristic reception into
  one bucket.
- Do not create runtime ingestion pipelines in this scaffold.
- Do not overwrite tradition-specific canon status.
- Do not create unscoped theological claims.
- Do not let boundary claims override, contaminate, or equal canonical Scripture authority.

## Contributor Review For Sensitive Changes

External contributor changes to sensitive governance, source, claim, corpus, trust, attribution, or
cross-repo authority surfaces require maintainer review before merge.

This applies to `logos-boundary-literature` only. It does not apply to `logos-scripture-graph` and
does not change its rules. It does not authorize importing source texts, creating real corpus records,
creating canonical Scripture records, or treating boundary claims as canonical truth.

Review is required for external contributor changes affecting:

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
templates remain governed by normal repository controls and validation.

Machine-readable contributor review policy:
`.ai/control/contributor_review_policy.yaml`.

## Next Tasks

1. Review governance docs.
2. Add lightweight validation for schema files and empty data directories.
3. Add dummy records only after review, using invented placeholder data rather than real source
   text.
4. Design source-intake review workflow before any real corpus or source metadata import.

## AI Behavior Here

AI agents must separate Confirmed, Inferred, Proposed, and Unknown. They must preserve authority
scope and must not smuggle boundary claims into canonical Scripture. When uncertain, fail closed:
mark records as `quarantine_unreviewed` or `requires_human_source_review`.
