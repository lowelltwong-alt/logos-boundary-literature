---
object_type: source_spine_scaffold
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created 2026-06-22 as a source-spine scaffold for Bible reliability, provenance, manuscript-evidence, and reception-history research."
reason_for_inclusion: "Separate confirmed source metadata from candidate apologetic or historical claims before any source import or database seeding."
---

# Reliability Evidence Source Spine

## Purpose

This source spine identifies starting sources for the future reliability
evidence database. It is not a data import, claim promotion, or apologetic
conclusion.

The document separates:

- confirmed source facts that may guide schema and source-intake planning;
- candidate research claims that require review before they can become
  evidence records;
- stop rules that keep source metadata from becoming Scripture authority.

## Placement

This source spine belongs in `logos-boundary-literature` because it covers
source/reception metadata, patristic citation planning, discovery history, and
derived evidence reports.

Canonical manuscript, fragment, variant, and Scripture passage records still
belong in `logos-scripture-graph`. This file may reference those future records
but must not define them.

## Source Spine Table

| Source | Evidence Lane | Confirmed From Source | Candidate Claims Not Yet Asserted |
|---|---|---|---|
| [Leon Levy Dead Sea Scrolls Digital Library](https://www.deadseascrolls.org.il/) | Dead Sea Scrolls and Old Testament witness planning | Official digital library for Dead Sea Scrolls fragments and related metadata. Useful for source locator, fragment/cave, image, and catalog planning. | Which scrolls should be linked to which reliability claims; whether a specific debate is answered by a specific fragment; any claim about prophecy dating. |
| [Israel Museum: The Dead Sea Scrolls](https://www.imj.org.il/en/wings/shrine-book/dead-sea-scrolls) | Discovery timeline and museum-level context | Museum overview states the scrolls were discovered between 1947 and 1956 in eleven caves near Khirbet Qumran. | What each discovery changed in a particular scholarly debate; whether a later apologetic claim is warranted. |
| [New Testament Virtual Manuscript Room](https://ntvmr.uni-muenster.de/) | New Testament manuscript catalog planning | INTF-hosted workspace for Greek New Testament manuscript research and manuscript-resource discovery. | Which manuscripts should be selected as earliest or most relevant for a given reliability report. |
| [INTF](https://www.uni-muenster.de/INTF/en/) | Textual criticism method and source classes | INTF describes its work as researching New Testament textual history using manuscript tradition, early translations, and patristic citations. | Any simplified count or confidence claim about reconstructing the New Testament from one evidence class alone. |
| [Codex Sinaiticus](https://www.codexsinaiticus.org/) | Major codex and digitization planning | Official project for Codex Sinaiticus, a major Greek Christian Bible manuscript and one of the most important witnesses for the history of the Bible text and book. | How Sinaiticus should be weighted in a specific variant or reliability claim. |
| [British Library Codex Sinaiticus project page](https://support.bl.uk/page/codex-sinaiticus) | Holding-location and project history | British Library page describes the online reunification project and notes the manuscript pages/fragments are held in multiple institutions. | Whether the digital reunification changes a specific text-critical conclusion. |
| [Manchester Digital Collections: Greek P 457](https://www.digitalcollections.manchester.ac.uk/view/MS-GREEK-P-00457) | Early New Testament fragment planning | Manchester record identifies Greek P 457 as a papyrus fragment of John 18:31-33 and 18:37-38. | Whether P52 is the earliest surviving New Testament fragment; the exact date range; what it implies for dating John's Gospel. |
| [CSNTM P52 record](https://manuscripts.csntm.org/manuscript/View/GA_P52) | New Testament papyrus metadata cross-check | CSNTM catalog record classifies P52 as a second-century papyrus fragment located at John Rylands University Library. | Whether the dating should be narrowed beyond the catalog range; how much apologetic force the fragment carries. |
| [BiblIndex](https://www.biblindex.org/) | Patristic citation and reception planning | BiblIndex indexes biblical references in early and medieval Christian literature. | Whether patristic citations can reconstruct a whole text; which citations are direct quotations versus allusions or paraphrases. |
| [INTF: Patristic Citations in New Testament Textual Criticism](https://ntvmr.uni-muenster.de/intfblog/-/blogs/patristic-citations-in-new-testament-textual-criticism) | Patristic evidence method | INTF blog explains that patristic citations can be important for textual criticism, but citation mode and author treatment must be evaluated. | Any blanket claim that church-father writings alone recover the entire New Testament. |
| [SBL Textual Criticism](https://www.sbl-site.org/sbl-press/browse-journals/textual-criticism/) | Scholarly review queue | Open-access scholarly venue for textual-criticism articles, notes, reports, and reviews. | Which articles should be adopted as source basis for a future row or claim. |
| [N. T. Wright: Early Traditions and the Origins of Christianity](https://ntwrightpage.com/2016/04/05/early-traditions-and-the-origins-of-christianity/) | Early creed and oral tradition planning | Wright treats 1 Corinthians 15:1-7 as an early tradition Paul describes as common to Christians. | Exact dating of the tradition to months or a small number of years after the resurrection; confidence level for each dating argument. |
| [Larry Hurtado: The Origins of Devotion to Jesus in its Ancient Context](https://larryhurtado.wordpress.com/2019/08/23/the-origins-of-devotion-to-jesus-in-its-ancient-context/) | Early devotion and pre-Pauline tradition planning | Hurtado discusses early Christian devotional practices and Pauline evidence for early beliefs about Jesus. | Whether a given formula is a fixed creed, how early it is, and how it should be linked to a resurrection-evidence report. |

## Evidence Classes To Model Later

### Confirmed Metadata

Confirmed metadata may become future source records after source-intake review.

Examples:

- source title;
- source institution or publisher;
- source URL;
- catalog ID;
- broad date range stated by source;
- holding institution;
- evidence lane;
- access or license note.

### Candidate Evidence Claims

Candidate claims must stay candidate until reviewed.

Examples:

- "this is the earliest surviving New Testament fragment";
- "this manuscript settles a specific Old Testament dating debate";
- "copy abundance makes a particular reading secure";
- "a creed dates within months of the resurrection";
- "patristic citations can reconstruct a specified percentage of the New
  Testament."

Each candidate claim needs source basis, method, scope, confidence, provenance,
and review status before promotion.

## Discovery Timeline Questions

The future database should track both ancient dates and modern discovery dates.

Initial timeline questions:

- What was known before the Dead Sea Scrolls discoveries of 1947-1956?
- Which biblical manuscripts were known before and after major digitization
  projects?
- Which fragments or codices were known before a specific scholarly debate?
- When was a source discovered, acquired, cataloged, published, photographed,
  digitized, re-dated, or reinterpreted?

## Patristic Citation Caution

Patristic citations are useful, but they need careful classification.

A future row should distinguish:

- direct quotation;
- paraphrase;
- allusion;
- commentary reference;
- reception motif;
- doctrinal use.

Do not turn "the fathers quote Scripture often" into a reconstruction claim
without checking citation mode, edition quality, author date/location, and
whether later scribes or editors adjusted the quoted biblical wording.

## Anti-Guessing Rule

No source-spine entry may become a reviewed row merely because a model found it,
summarized it fluently, or linked it to a Bible passage.

Every future promoted record must include:

- source basis;
- scope;
- method;
- dating basis where applicable;
- confidence level;
- provenance note;
- review status.

## Next Safe Step

Create invented sample rows that exercise the schema shape without importing
real source data. Real records should wait for source-intake review, licensing
review, and expert review rules.
