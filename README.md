# Logos Boundary Literature

`logos-boundary-literature` is a governed repository scaffold for noncanonical, boundary,
heterodox, disputed, forged, reception-history, and supporting literature related to Scripture and
Christian theological interpretation.

Presence in this repo does not imply authority.

## Purpose

Canonical Scripture remains in `logos-scripture-graph`. Boundary, noncanonical, heterodox,
disputed, forged, reception-history, and supporting literature belongs here so it can be modeled
without contaminating Scripture records.

This scaffold defines governance, trust hierarchy, schemas, and cross-repo contracts. It does not
include source texts.

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

## Repository Structure

```text
governance/      Trust, canon, source intake, attribution, rules, contamination controls.
schemas/         Proposed JSON Schemas for metadata and scoped claims.
data/            Empty scaffold folders only; no source text yet.
eval/            Placeholder for future validation and review artifacts.
tests/           Placeholder for future validation tests.
.ai/             Project status, task, and handoff scaffolding.
```

## Contamination Controls

- Boundary texts may reference Scripture.
- Scripture records must not absorb boundary claims as canonical truth.
- Do not use generic `related_to` relationships.
- Use typed relationships with source, tradition, profile, and review status.
- Do not retrieve boundary material into canonical answers by default.
- Do not create a claim without provenance.
- Do not create a canon claim without tradition scope.

## No Text Import Yet

The `data/` folders are intentionally empty except `.gitkeep`. No full source text corpus,
copyrighted text, public-domain text, commentary text, or boundary text is imported in this
scaffold.
