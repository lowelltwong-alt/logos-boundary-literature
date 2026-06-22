---
object_type: timeline_checkpoint_plan
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created 2026-06-22 as a metadata-only discovery and knowledge-timeline scaffold for Bible reliability research."
reason_for_inclusion: "Model what was known when without importing source texts, creating canonical records, or promoting apologetic claims."
---

# Reliability Evidence Timeline Checkpoints

## Purpose

Timeline checkpoints model what was known, by whom, and when. They keep four
things separate:

- the ancient date range of an artifact, manuscript, tradition, or copied text;
- the modern discovery, acquisition, publication, cataloging, digitization, or
  redating event;
- the state of scholarly/public knowledge at that time;
- any later apologetic or historical claim that tries to use the event.

This matters because a discovery may change what can be argued, but the
discovery itself does not automatically prove a broader claim.

## Placement Decision

This scaffold belongs in `logos-boundary-literature` because it is derived
research metadata and claim-control work. It may refer to future
`logos-scripture-graph` witness records, but it does not create canonical
Scripture text, manuscript, fragment, variant, or Scripture passage records.

## Checkpoint Types

| Type | Question It Answers | Promotion Blocker |
|---|---|---|
| `artifact_copying_or_composition_range` | What ancient date range is claimed for the artifact or tradition? | Do not confuse artifact/copied-text date with modern discovery date. |
| `modern_discovery` | When was a manuscript, fragment, codex, or scroll found? | Do not infer textual reliability from discovery alone. |
| `acquisition_or_holding` | When did an institution acquire, hold, or identify the material? | Do not treat holding location as proof of provenance without review. |
| `cataloging_or_publication` | When did a catalog, edition, article, or institutional page make metadata available? | Do not treat publication as expert consensus unless the source supports that. |
| `digitization_or_public_access` | When did images, metadata, or a digital project become available? | Do not turn public access into a textual conclusion. |
| `redating_or_method_update` | When did new dating, imaging, or method work alter the discussion? | Do not narrow dates without method and dissent review. |
| `scholarly_debate_state` | What debate or uncertainty existed at a given time? | Do not say a debate was settled unless the source and scope prove it. |
| `apologetic_claim_boundary` | What later reliability claim is being attempted? | Keep candidate claims unreviewed until source, method, confidence, and review gates are complete. |

## Source-Grounded Starting Points

These are source anchors for later review, not imported records.

| Source | Confirmed Source Metadata To Check | Candidate Claims To Keep Unreviewed |
|---|---|---|
| [Israel Museum: The Dead Sea Scrolls](https://www.imj.org.il/en/wings/shrine-book/dead-sea-scrolls) | Discovery context for the first seven scrolls in 1947 near Khirbet Qumran and museum-level DSS framing. | Whether the DSS settle a specific prophecy, composition-date, or apologetic debate. |
| [Leon Levy Dead Sea Scrolls Digital Library](https://www.deadseascrolls.org.il/) | Digital access and metadata planning for Dead Sea Scrolls fragments. | Which exact scrolls or fragments support a particular reliability claim. |
| [Codex Sinaiticus project](https://www.codexsinaiticus.org/en/project/) | Project-history and digitization context, including conservation, digitization, transcription, and dissemination. | Whether digital reunification changes a particular text-critical conclusion. |
| [Manchester Digital Collections: Greek P 457](https://www.digitalcollections.manchester.ac.uk/view/MS-GREEK-P-00457) | P52/Greek P 457 catalog and dating-caution metadata, including palaeographic uncertainty. | Whether P52 is definitively earliest, how narrow the date can be, or how much apologetic force it carries. |
| [CSNTM P52](https://manuscripts.csntm.org/manuscript/View/GA_P52) | Cross-check catalog metadata for P52 as a manuscript witness reference. | Whether catalog metadata alone proves gospel composition, circulation, or textual reliability claims. |
| [INTF](https://www.uni-muenster.de/INTF/en/) | Textual-history method anchors involving manuscripts, early translations, and patristic citations. | Any broad reliability conclusion from one evidence class alone. |

## Required Fields

Each checkpoint should record:

- checkpoint type;
- knowledge scope;
- claim status;
- artifact date range where relevant;
- modern event date range where relevant;
- date precision;
- date basis;
- known-state summary;
- confirmed source metadata;
- candidate claim summary;
- source basis;
- method note;
- confidence level;
- provenance note;
- review status.

## Stop Rules

Stop and report if a checkpoint would:

- store Scripture text, manuscript transcription text, patristic text,
  commentary text, or theologian text;
- create or mutate `logos-scripture-graph` witness records;
- treat an artifact date as a modern discovery date, or the reverse;
- claim a debate was solved without a precise source, passage, method, and
  review status;
- promote a candidate apologetic claim because a source was discovered,
  digitized, or cataloged;
- hide uncertainty, dissent, date range, or source limitation.

## Example Use

A future Dead Sea Scrolls report may need one checkpoint for ancient manuscript
date range, a second checkpoint for modern discovery/publication, and a third
checkpoint for the later debate claim. Only the source metadata can move toward
review first; the debate claim remains candidate until the exact scroll,
passage, dating basis, scholarly source, and counterarguments are reviewed.
