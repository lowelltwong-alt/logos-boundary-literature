# Canon And Authority Policy

Canonical Scripture remains in `logos-scripture-graph`.

This repository models boundary, noncanonical, disputed, heterodox, forged, reception-history, and
supporting literature. Presence here does not imply canonical authority.

`logos-boundary-literature` is hierarchically under, or at minimum never above, canonical Scripture
authority. `logos-governance-architecture` may define cross-repo policy and authority contracts, but
boundary literature must not override, contaminate, or become equal authority to canonical
Scripture.

## Required Distinctions

- Tradition-scoped canon status must be modeled explicitly.
- A text can be canonical in one tradition, noncanonical in another, and still valuable
  historically.
- High-value background is not the same as Word of God.
- Commentary and reception claims are not canonical claims.
- Heterodox/gnostic texts must be represented accurately and scoped as heterodox/gnostic.
- Known forgeries are preserved only for identification, quarantine, comparison, and refutation.
- Boundary claims must remain scoped by trust level, tradition, profile, and provenance.

## 1 Enoch Statement

1 Enoch may be high-value background, especially for Second Temple context and Jude reception. It is
not treated as Word of God in the default Logos Scripture Graph scope.

## Deuterocanonical Statement

Deuterocanonical and apocrypha status is tradition-scoped. A work may be received differently by
Protestant, Roman Catholic, Eastern Orthodox, and other traditions. This repository must not
overwrite or flatten that distinction.

## Authority Defaults

```text
canonical_claim: false
canonical_influence_allowed: false
tradition_scope: required when canon status is discussed
profile_scope: required when an interpretive profile is used
can_override_scripture: false
can_equal_scripture_authority: false
```

## Prohibited Claims

- "This boundary source is Scripture for all users."
- "This work is false because it is noncanonical."
- "This high-trust background text is Word of God."
- "This tradition-specific canon decision is universal."
- "This fake or forged text can be retrieved as trusted spiritual background."
