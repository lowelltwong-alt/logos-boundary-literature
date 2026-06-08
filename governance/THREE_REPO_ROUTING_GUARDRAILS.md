# Three-Repo Routing Guardrails

## Status

- Task: T002
- Mode: governance/routing documentation
- Status: complete
- Branch: `t002-three-repo-routing-guardrails`
- Text import: none
- Data mutation: none

## Authority Hierarchy

1. `logos-governance-architecture` owns cross-repo policy, authority contracts, update rules, and
   validation patterns.
2. `logos-scripture-graph` owns canonical 66-book Scripture truth.
3. `logos-boundary-literature` owns supporting boundary, noncanonical, deuterocanonical/apocrypha,
   heterodox, disputed, forged, commentary/reception, historical background, and supporting
   literature.

Boundary literature may interoperate with canonical Scripture, but it is hierarchically under, or at
minimum never above, canonical Scripture authority.

## Allowed Flow

- Scripture refs may point outward to boundary/reception materials as background or comparison.
- Boundary literature may reference Scripture.
- Commentary may discuss Scripture and boundary literature.
- Claims must remain scoped by trust level, tradition, profile, and provenance.

## Forbidden Flow

- Boundary claims must not become canonical Scripture claims.
- Noncanonical sources must not become default Scripture meaning.
- Commentary/reception claims must not mutate canonical Scripture records.
- Heterodox/forged/fake material must not enter canonical retrieval by default.
- Boundary repo material must not be treated as equal or superior authority to canonical Scripture.

If a task appears to require boundary material to modify canonical Scripture outputs, stop and
report.

## Boundary-Originated Higher-Layer Changes

Boundary-originated requests must not treat higher-authority governance as a surface to route
around. If a boundary task appears to require changing or bypassing governance-layer policy,
canonical Scripture authority, repository-link contracts, routing policy, trust hierarchy, or
canonical scope, stop and emit the required warning from
`governance/BOUNDARY_GOVERNANCE_CONSTRAINTS.md`.

Only Lowell Wong, as project owner, may authorize a boundary-originated request to change
higher-authority governance, canonical Scripture authority, repository-link contracts, canonical
scope, trust hierarchy, or cross-repo policy. Contributor consensus, contributor volume, automated
recommendation, agent routing, and boundary-layer operational need are not sufficient authority.

## Routing Table

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

## Machine-Readable Policy

Boundary-local policy:

- `.ai/control/boundary_material_routing.yaml`

Scripture-local policy:

- `logos-scripture-graph/.ai/control/boundary_material_routing.yaml`

Governance-repo follow-up is required because the local governance checkout had pre-existing dirty
work during T002/T327A1.

The governance registry is now live in `logos-governance-architecture`; this boundary repo mirrors
the stop rules locally for agents entering here first.
