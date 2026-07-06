---
object_type: authority_ladder_crosswalk
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created 2026-07-06 by Codex for Fable PR-6 boundary repo hardening after governance PRs #72-#78 landed."
reason_for_inclusion: "Map boundary trust tiers to the doctrine-genealogy S0-S7 authority ladder without collapsing contamination/retrieval utility into doctrinal authority."
---

# Authority Ladder Crosswalk

This crosswalk connects `logos-boundary-literature` trust tiers to the future doctrine-genealogy
authority ladder recorded in
`logos-governance-architecture/docs/governance/doctrine-genealogy-vocabulary.md`.

It is a routing and validation aid only. It does not create doctrine records, promote boundary
sources, authorize source-text ingestion, or change canonical Scripture authority.

## Core Distinction

Boundary trust tiers answer a contamination and retrieval question:

```text
How may this source be stored, found, quarantined, compared, or used as scoped background without
contaminating canonical Scripture?
```

Doctrine-genealogy authority rungs answer a doctrinal-authority-weight question:

```text
What kind of source is being cited, and how much authority may it carry in a scoped doctrine
genealogy claim?
```

Neither system collapses into the other. A source may have high historical or reception utility and
still carry no canonical or binding doctrinal authority.

## Crosswalk

| Boundary trust tier | Closest authority-rung handling | Crosswalk rule |
|---|---|---|
| `canonical_scripture_reference_only` | S0 `canonical_scripture` by reference only | This repo may store stable Scripture references only. It does not own S0 text, chunks, variants, or canonical truth. |
| `deuterocanonical_tradition_scoped` | No automatic S0 mapping | Canon status is tradition-scoped. In the default Logos 66-book scope, this tier never becomes S0. Any doctrine-genealogy use must record tradition scope and authority basis. |
| `high_trust_noncanonical_background` | S6-adjacent utility, sometimes evidence utility only | Historical or background value does not create doctrinal authority. Utility flags may be high; authority remains noncanonical. |
| `historical_context_source` | S6 `scholarly_analysis` or historical/textual utility | May inform historical, linguistic, attribution, or textual fields after review. It may not set orthodoxy status or canonical meaning. |
| `patristic_reception` | S4 `patristic_and_doctor_witness` | Strong reception evidence, never binding by itself and never canonical Scripture. |
| `heterodox_or_gnostic` | S7 `adversarial_or_heterodox_source` | Comparison, refutation, and boundary-recognition use only. It must not be normalized into Christian canon or default doctrine. |
| `disputed_attribution` | Source-specific after attribution review | Disputed attribution is a warning state, not an authority rung. A reviewed source may later route to S4, S5, S6, or S7 depending on content and provenance. |
| `known_forgery_or_fake` | S7 `adversarial_or_heterodox_source` | Identification, quarantine, comparison, and refutation only. Forgery/fake status cannot become trusted background by retrieval convenience. |
| `quarantine_unreviewed` | No authority rung until reviewed | Triage only. Do not ingest, retrieve as evidence, route into doctrine genealogy, or use for interpretation before review. |

## Non-Promotion Rules

- Retrieval value never raises authority rung.
- Historical value never makes a source canonical.
- Reception value never makes a source binding by itself.
- A patristic, commentary, theologian, heterodox, or forged source may not mutate Scripture chunks,
  canonical passage records, Scripture retrieval truth, or default canonical answers.
- S0 canonical Scripture remains owned by `logos-scripture-graph` only.
- S1 boundary-instrument membership remains owner-reserved in `logos-governance-architecture`.
- S6 scholarly analysis may inform historical, linguistic, attribution, or textual fields only.
- S7 adversarial or heterodox sources are comparison and refutation targets only.

## Safe Use Pattern

```text
Boundary source B has trust tier T.
If a future doctrine-genealogy artifact references B, it records:
- boundary source ID;
- trust tier T;
- proposed authority rung or explicit no-rung status;
- tradition/profile scope where relevant;
- evidence utility flags;
- provenance;
- review status.

No authority is transferred merely because B is useful.
```

## Stop Conditions

Stop and report if a task asks this repo to:

- treat boundary trust level as equivalent to doctrinal authority rung;
- raise a source's rung because it has high retrieval, reception, historical, or apologetic value;
- use boundary material to change canonical Scripture text, chunking, evaluator behavior, or graph
  truth;
- make a universal canon claim from a tradition-scoped source;
- use S6 scholarship or S7 adversarial material to set orthodoxy status.
