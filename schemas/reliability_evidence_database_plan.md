---
object_type: database_scaffold_plan
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created 2026-06-22 as a metadata-only scaffold for Bible reliability, provenance, manuscript-evidence, reception, and apologetics research."
reason_for_inclusion: "Plan a SQLite evidence database without importing Scripture text, manuscript transcriptions, commentary corpora, or canonical Scripture records."
---

# Reliability Evidence Database Plan

## Purpose

This plan defines a metadata-only SQLite scaffold for future Bible reliability,
provenance, manuscript-evidence, reception-history, and apologetics research.

It is intentionally not a corpus import. It does not store Scripture text,
manuscript transcription text, patristic source text, commentary text, or
theologian text.

## Placement Decision

This scaffold starts in `logos-boundary-literature` because it is a derived
evidence and source/reception planning surface.

Actual canonical Scripture records belong elsewhere:

- canonical Scripture text, chunks, passage IDs, manuscript witnesses,
  fragments, variants, and canonical textual-evidence records belong in
  `logos-scripture-graph`;
- patristic citations, church-father reception, commentary metadata,
  theologian-writing metadata, attribution status, and reception-history source
  records belong in `logos-boundary-literature`;
- doctrine progression, denomination/profile lineage, and theologian-to-theologian
  influence belong in planned `logos-doctrine-genealogy` after governance
  registration.

Unified reports may join these layers only as derived artifacts. Authority does
not transfer across the join.

## Database Namespace Rule

This boundary repo may define `boundary_*` and `evidence_*` tables for its own
metadata and derived evidence products.

A future unified database may attach or consume read-only `scripture_*` records
from `logos-scripture-graph`, but this repo must not define or own those tables.

Never create a `canonical_*` table or view for this project.

## Initial Research Lanes

### Manuscript And Fragment Evidence

Goal: plan references to oldest fragments, manuscript witnesses, codices,
scrolls, and discovery events without storing the underlying text.

Required fields:

- owning repo or external catalog;
- witness or fragment reference ID;
- date range and dating method;
- material, language, and script;
- location or holding institution;
- passage coverage as references only;
- confidence level;
- source/provenance;
- review status.

### Dead Sea Scrolls And Old Testament Witnesses

Goal: record what the project should eventually ask about the Dead Sea Scrolls,
Qumran discoveries, biblical manuscript dating, and their relevance to Old
Testament textual history.

Do not assert that a discovery "proves" a prophecy argument until the exact
manuscript, dating, passage, claim, and scholarly source are reviewed.

### New Testament Papyri And Codices

Goal: reference New Testament papyri, majuscule codices, catalog IDs, and
discovery/provenance records through external scholarly catalogs or future
Scripture Graph witness records.

### Textual Variant And Copy-Abundance Evidence

Goal: model how multiple witnesses help identify variants, scribal changes,
copying errors, and reconstruction confidence.

Do not collapse "many copies exist" into a single reliability conclusion. Store
the claim, the witness set, the method, and the review status separately.

### Early Creed And Oral-Tradition Evidence

Goal: model claims about early creedal or formulaic material, such as the
tradition referenced in `1 Corinthians 15:3-8`, with explicit date ranges,
argument basis, confidence, and scholarly disagreement.

Do not store biblical text here. Store Scripture references and research
questions only.

### Patristic Citation And Reception Evidence

Goal: model church-father citations, allusions, paraphrases, and reception
patterns as boundary/reception evidence.

A patristic citation may be text-critical evidence, but it is not Scripture
authority. The record must distinguish direct quotation, paraphrase, allusion,
commentary, reception motif, and doctrinal use.

### Discovery Timeline

Goal: show what was known when by recording discovery, publication,
digitization, cataloging, and scholarly-debate events.

This lane is important because apologetic or historical claims often depend on
whether a manuscript was known before or after a debate.

## Anti-Guessing Rules

Every future record or claim must declare:

- source basis;
- source URL, catalog ID, or bibliographic citation;
- method;
- scope;
- confidence level;
- review status;
- provenance note;
- whether the record is confirmed, inferred, proposed, or unknown.

AI output may generate candidate rows or review queues. It must not become
reviewed evidence merely because it sounds fluent, cites Greek or Hebrew, or
appears near a passage in vector search.

## Initial Source Spine

These sources are starting points for metadata design and review. They are not
imported as data.

- [Leon Levy Dead Sea Scrolls Digital Library](https://www.deadseascrolls.org.il/) -
  digital access to Dead Sea Scrolls fragments and related metadata.
- [Israel Museum: The Dead Sea Scrolls](https://www.imj.org.il/en/wings/shrine-book/dead-sea-scrolls) -
  museum-level overview of the Qumran discoveries.
- [New Testament Virtual Manuscript Room](https://ntvmr.uni-muenster.de/) -
  INTF manuscript research environment for Greek New Testament manuscripts.
- [INTF](https://www.uni-muenster.de/INTF/en/) - institute-level source for
  New Testament textual history, manuscript tradition, early translations, and
  patristic citations.
- [Codex Sinaiticus](https://www.codexsinaiticus.org/) - official digital
  project for Codex Sinaiticus.
- [British Library Codex Sinaiticus project page](https://support.bl.uk/page/codex-sinaiticus) -
  project and holding-location overview.
- [Manchester Digital Collections: Greek P 457](https://www.digitalcollections.manchester.ac.uk/view/MS-GREEK-P-00457) -
  John Rylands fragment metadata.
- [CSNTM P52 record](https://manuscripts.csntm.org/manuscript/View/GA_P52) -
  catalog metadata for P52.
- [BiblIndex](https://www.biblindex.org/) - index of biblical references in
  early and medieval Christian literature.
- [INTF blog on patristic citations](https://ntvmr.uni-muenster.de/intfblog/-/blogs/patristic-citations-in-new-testament-textual-criticism) -
  cautionary framing for direct quotations, imprecise quotation, allusion, and
  paraphrase.
- [SBL Textual Criticism journal](https://www.sbl-site.org/sbl-press/browse-journals/textual-criticism/) -
  open-access scholarly venue for textual-criticism research.

## Next Safe Step

The next safe implementation step is to create invented sample rows in a
separate fixture or eval file, not real source records. Real rows should wait
until source-intake review decides which catalogs, licenses, and scholarly
editions may be used.
