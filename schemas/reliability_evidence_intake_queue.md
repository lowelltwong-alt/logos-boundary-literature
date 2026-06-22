---
object_type: database_intake_queue_plan
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created 2026-06-22 as a metadata-only intake queue plan for Bible reliability and provenance research."
reason_for_inclusion: "Define how future source candidates enter review without importing source text, Scripture text, or canonical records."
---

# Reliability Evidence Intake Queue

## Purpose

The intake queue is a pre-evidence holding area. It records what a future
researcher or AI agent wants to investigate before any row becomes a source
record, manuscript witness, textual question, patristic citation, or reliability
claim.

The queue exists to prevent fluent but unreviewed summaries from becoming
evidence. A queue item may point to an official catalog, museum page, academic
project, peer-reviewed article, scholarly book, or primary-source reference, but
it still remains unreviewed until source, method, scope, confidence, license,
and expert-review gates are satisfied.

## Placement Decision

This queue belongs in `logos-boundary-literature` because it is a boundary and
derived-evidence workbench. It may route a future item to another repo, but it
does not create that repo's records.

- `logos-scripture-graph` remains the target for canonical Scripture text,
  canonical chunks, manuscript witnesses, variants, fragments, and Scripture
  evidence records.
- `logos-boundary-literature` remains the target for commentary, church-father,
  patristic, theologian, reception, and source-access metadata.
- Planned `logos-doctrine-genealogy` remains the target for denomination,
  doctrine-lineage, and theologian-influence development.

## Intake Lanes

| Lane | Typical Source Locator | Correct First Question | Promotion Blocker |
|---|---|---|---|
| `dead_sea_scrolls_ot_witness` | Leon Levy Dead Sea Scrolls Digital Library, Israel Museum, scholarly DSS publications | What source metadata is confirmed, and which Scripture Graph record would own the witness later? | No prophecy or dating claim may be promoted without identifying the exact scroll/fragment, passage, date basis, and scholarly source. |
| `nt_papyri_codices` | NTVMR, CSNTM, Codex Sinaiticus project, holding-library pages | Which catalog facts are confirmed, and which witness metadata belongs in Scripture Graph later? | No "earliest" or apologetic force claim may be promoted without catalog cross-check and date-method review. |
| `textual_variants_copy_abundance` | INTF, ECM, SBL Textual Criticism, peer-reviewed textual-criticism work | What variant question is being asked, and which witness set/method is required? | No broad reliability conclusion may be promoted from manuscript counts alone. |
| `early_creed_oral_tradition` | Scholarly books/articles on formulaic tradition, Pauline studies, early Christian origins | Is the item a source fact, a scholarly argument, or a candidate apologetic claim? | No "within months" dating claim may be promoted without exact source, argument basis, confidence, and dissent notes. |
| `patristic_reception_reconstruction` | BiblIndex, INTF patristic citation guidance, critical editions, source-access records | Is the reference a quotation, varying citation, allusion, paraphrase, commentary reference, or reception motif? | No reconstruction claim may be promoted without citation-mode review and edition/source review. |
| `discovery_timeline` | Museum/catalog pages, publication histories, digitization projects | What was discovered, acquired, published, digitized, re-dated, or debated, and when was it known? | No "this solved the debate" claim may be promoted without tying the debate to the source event and scholarly discussion. |
| `method_bibliography` | Handbooks, peer-reviewed articles, institute guidance, source-intake policy | Which method governs a future claim? | No method note may be treated as evidence for a specific manuscript, passage, or doctrine by itself. |

## Confirmed Metadata Vs Candidate Claims

Each intake item must split source metadata from candidate claims.

Confirmed metadata can include:

- source title;
- source URL or catalog locator;
- holding institution or publisher;
- broad catalog date range as stated by the source;
- material, language, or fragment status as stated by the source;
- whether the source is a catalog, museum page, academic project, scholarly
  article, book, or primary-source reference.

Candidate claims include:

- a manuscript or fragment is the earliest surviving witness;
- a discovery settles a prophecy-dating or composition-date debate;
- copy abundance proves a specific reliability conclusion;
- an early creed dates to months after the resurrection;
- church-father citations can reconstruct a specified corpus or percentage.

Candidate claims remain unreviewed until source, scope, method, confidence,
provenance, license, and expert-review gates are complete.

## Source-Grounded Starting Points

These are starting points for intake review, not imported records.

- [Leon Levy Dead Sea Scrolls Digital Library](https://www.deadseascrolls.org.il/):
  official IAA digital library for Dead Sea Scrolls fragments and public
  high-resolution access.
- [Israel Museum Dead Sea Scrolls page](https://www.imj.org.il/en/wings/shrine-book/dead-sea-scrolls):
  museum-level discovery and Shrine of the Book context.
- [New Testament Virtual Manuscript Room](https://ntvmr.uni-muenster.de/) and
  [INTF](https://www.uni-muenster.de/INTF/en/): manuscript research,
  cataloging, textual history, early translations, and patristic citation
  method.
- [Codex Sinaiticus project](https://www.codexsinaiticus.org/en/project/):
  digitization, conservation, transcription, and virtual reunification planning
  for the manuscript.
- [Manchester Digital Collections Greek P 457](https://www.digitalcollections.manchester.ac.uk/view/MS-GREEK-P-00457)
  and [CSNTM P52](https://manuscripts.csntm.org/manuscript/View/GA_P52):
  cross-check examples for an early New Testament papyrus fragment.
- [BiblIndex](https://www.biblindex.org/) and
  [INTF patristic citation guidance](https://ntvmr.uni-muenster.de/intfblog/-/blogs/patristic-citations-in-new-testament-textual-criticism):
  starting points for patristic reference indexing and citation-mode caution.

## Required Review Gates

Before an intake item can become a proposed evidence record:

- source locator must be reviewed;
- source access/license must be reviewed;
- target repo and namespace must be confirmed;
- confirmed metadata and candidate claims must be split;
- method note must identify how the claim would be evaluated;
- confidence level must be explicit;
- provenance note must explain where the queue item came from;
- review status must move through a human or expert review event.

## Stop Rules

Stop and report if an intake item would:

- store Scripture text, manuscript transcription text, patristic text,
  commentary text, or theologian text;
- create `canonical_*` tables or views;
- place commentary, patristic, theologian, or denomination data into
  Scripture Graph records;
- promote an AI-generated claim because it sounds expert;
- treat one denomination's reading as universal without scope;
- bypass `logos-governance-architecture` to change cross-repo authority rules.
