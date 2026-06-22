# Logos Boundary Literature

`logos-boundary-literature` is a governed repository scaffold for noncanonical, boundary,
heterodox, disputed, forged, reception-history, commentary, patristic, theologian-writing, and
supporting literature related to Scripture and Christian theological interpretation.

Presence in this repo does not imply authority.

## Purpose

Canonical Scripture remains in `logos-scripture-graph`. Boundary, noncanonical, heterodox,
disputed, forged, reception-history, commentary, patristic, church-father citation, and
theologian-writing material belongs here so it can be modeled without contaminating Scripture
records.

This scaffold defines governance, trust hierarchy, schemas, and cross-repo contracts. It does not
include source texts.

## Three-Repo Routing

`logos-governance-architecture` owns cross-repo policy, authority contracts, update rules, and
validation patterns.

`logos-scripture-graph` owns canonical 66-book Scripture truth, canonical passage records,
canonical chunking, canonical Scripture gold/evaluator surfaces, and canonical Scripture graph
outputs.

`logos-boundary-literature` owns boundary literature metadata, source status, trust profiles,
tradition-scoped claims, commentary/reception claims, and comparison/refutation/background
relationships. It is hierarchically under, or at minimum never above, canonical Scripture authority.

Commentaries, church-father citations, patristic reception, and ancient or modern theologian
writings route here as source and reception metadata. This repo stores Scripture references, not
Scripture text.

Future doctrine-development and denomination/profile lineage belongs in the planned
`logos-doctrine-genealogy` repo after governance registration. This repo may hold source records
that doctrine lineage later references, but it does not own doctrine-genealogy truth.

Boundary material must not override, contaminate, or become equal authority to canonical Scripture.
If a task appears to require boundary material to modify canonical Scripture outputs, stop and
report.

Boundary-originated requests that conflict with higher-authority governance must also stop and be
reviewed in the higher-authority repository. `logos-boundary-literature` must not automate, route,
or implement changes to governance-layer policy, canonical Scripture authority, repository-link
contracts, routing policy, trust hierarchy, or canonical scope. Only Lowell Wong, as project owner,
may authorize a boundary-originated request to change those higher-authority surfaces.

## Trust Hierarchy

1. `canonical_scripture_reference_only`
2. `deuterocanonical_tradition_scoped`
3. `high_trust_noncanonical_background`
4. `historical_context_source`
5. `patristic_reception`
6. `heterodox_or_gnostic`
7. `disputed_attribution`
8. `known_forgery_or_fake`
9. `quarantine_unreviewed`

A boundary source can be useful, historically important, high-trust for background, or important
for reception history without being canonical Scripture.

## Required Examples

- 1 Enoch may be high-value background, especially for Second Temple context and Jude reception, but
  is not treated as Word of God in the default Logos Scripture Graph scope.
- Fake gospels and known forgeries are preserved only so the system can recognize, quarantine,
  compare, and refute them.
- Heterodox/gnostic texts should be represented accurately but scoped as heterodox/gnostic, not
  normalized into Christian canon.
- A text can be canonical in one tradition, noncanonical in another, and still valuable
  historically.
- Church-father or commentary citations can help show reception history and textual continuity, but
  they are never canonical Scripture.
- Ancient and modern theologian writings can be source or reception evidence, but their claims
  require trust, tradition/profile scope, provenance, and review status.

## Repository Structure

```text
governance/      Trust, canon, source intake, attribution, rules, contamination controls.
schemas/         Proposed JSON Schemas for metadata and scoped claims.
data/            Empty scaffold folders only; no source text yet.
eval/            Placeholder for future validation and review artifacts.
tests/           Placeholder for future validation tests.
.ai/             Project status, task, and handoff scaffolding.
AI_TABLE_OF_CONTENTS.md  AI navigation map for this repo.
ROADMAP.md       Source-layer roadmap for patristic, commentary, theologian, and denominational reception.
```

The first reliability/provenance database scaffold lives under `schemas/` as a planning artifact.
It defines only metadata and derived-evidence table boundaries; it does not import source texts or
canonical Scripture records.

## Contamination Controls

- Boundary texts may reference Scripture.
- Scripture records must not absorb boundary claims as canonical truth.
- Do not use generic `related_to` relationships.
- Use typed relationships with source, tradition, profile, and review status.
- Do not retrieve boundary material into canonical answers by default.
- Do not create a claim without provenance.
- Do not create a canon claim without tradition scope.
- Do not place commentary, patristic, theologian, or denomination-profile data in canonical
  Scripture tables or default Scripture retrieval.
- Use `boundary_*` or clearly derived `evidence_*` namespaces for future unified reports.
- Future reliability/provenance reports may reference `scripture_*` records from
  `logos-scripture-graph`, but this repo must not define or own those records.

## Contributor Review

External contributor changes to sensitive governance, source, claim, corpus, trust, attribution, or
cross-repo authority surfaces require maintainer review before merge.

This public policy applies only to `logos-boundary-literature`. It does not apply to
`logos-scripture-graph` and does not change its rules, does not authorize source-text ingestion, does not authorize real corpus
records, and does not allow boundary material to override or equal canonical Scripture authority.

See [`governance/CONTRIBUTOR_REVIEW_POLICY.md`](governance/CONTRIBUTOR_REVIEW_POLICY.md) and
[`.ai/control/contributor_review_policy.yaml`](.ai/control/contributor_review_policy.yaml).

## Boundary Governance Constraints

`BOUNDARY-GOV-001 - Governance Is Constraint, Not Obstacle` and `BOUNDARY-GOV-002 -
Owner-Reserved Authorization for Boundary-Originated Higher-Layer Changes` prevent boundary-layer
tasks from treating governance, canonical Scripture authority, repository-link contracts, routing
policy, trust hierarchy, or canonical scope as surfaces to route around.

See [`governance/BOUNDARY_GOVERNANCE_CONSTRAINTS.md`](governance/BOUNDARY_GOVERNANCE_CONSTRAINTS.md)
and [`.ai/control/boundary_material_routing.yaml`](.ai/control/boundary_material_routing.yaml).

## No Text Import Yet

The `data/` folders are intentionally empty except `.gitkeep`. No full source text corpus,
copyrighted text, public-domain text, commentary text, theologian text, patristic text, or boundary
text is imported in this scaffold.
