---
object_type: method_profile_plan
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created 2026-06-22 as a metadata-only method-profile plan for reliability evidence review."
reason_for_inclusion: "Prevent manuscript, dating, language, patristic, and apologetic claims from being promoted without an explicit review method."
---

# Reliability Evidence Method Profiles

## Purpose

Method profiles describe how a future evidence claim must be reviewed before it
can move beyond intake. They are not evidence records and do not import source
text, Scripture text, manuscript transcription, patristic text, commentary text,
or theologian text.

A method profile answers:

- what kind of review is needed;
- which evidence lane it governs;
- whether source-language expertise is required;
- whether dating, material, variant-method, citation-mode, or discovery-context
  review is required;
- which external source or scholarly method anchor should be consulted;
- whether AI-generated content may be promoted without review.

For this project, the default answer to AI promotion is always no.

An intake item may require several method profiles. For example, an early New
Testament fragment can require catalog review, palaeographic dating review,
material/image review, and source-language expertise before any claim about its
date or significance is promoted.

## Placement Decision

This file belongs in `logos-boundary-literature` because it governs source and
derived-evidence review. It may point future witness work toward
`logos-scripture-graph`, but it does not create canonical Scripture records,
manuscript witness records, variant records, or Scripture chunks.

## Method Profiles To Model

| Method Scope | Governs Lane | Review Requirement | Source Anchor |
|---|---|---|---|
| `source_catalog_metadata_review` | cross-lane | Confirm the source title, catalog locator, holding institution, license/access note, and whether the item is metadata only. | Catalogs such as NTVMR, CSNTM, Leon Levy DSS, and library records. |
| `palaeographic_dating_review` | DSS and NT witnesses | Keep dating as a source-anchored range; record method and dissent; do not narrow a date because it helps an argument. | Manchester Greek P 457 notes the dating is palaeographical and that recent research points nearer to 200 CE. |
| `material_and_image_review` | DSS and NT witnesses | Review material, image access, digitization, and whether the project may store only metadata or also derivative artifacts. | Leon Levy DSS and Codex Sinaiticus project pages show digital access and imaging/digitization context. |
| `textual_variant_method_review` | textual variants and copy abundance | Tie any reliability claim to a specific variant question, witness set, and method; never infer certainty from manuscript counts alone. | INTF describes New Testament textual history work across manuscript tradition, early translations, and patristic citations. |
| `patristic_citation_mode_review` | patristic reception and reconstruction | Classify quotation, varying citation, allusion, paraphrase, commentary reference, or reception motif before assigning text-critical value. | INTF patristic citation guidance emphasizes citation-mode and author-habit review. |
| `early_creed_tradition_review` | early creed and oral tradition | Separate a Scripture reference from a scholarly argument about formulaic tradition; track date range, argument basis, confidence, and dissent. | Scholarly books/articles must be added through intake before any "within months" claim is proposed. |
| `discovery_timeline_review` | discovery timeline | Separate ancient artifact date from modern discovery, acquisition, publication, digitization, redating, and debate milestones. | Museum, library, and project-history sources. |
| `source_language_expertise_review` | cross-lane | Require Greek, Hebrew, Aramaic, Syriac, Latin, Coptic, or other relevant expertise before promoting source-language claims. | INTF and manuscript/source catalogs provide language-scope anchors, but expert review is still required. |

## Source-Grounded Anchors

- [INTF](https://www.uni-muenster.de/INTF/en/) identifies its central task as
  researching New Testament textual history using manuscript tradition, early
  translations, and patristic citations.
- [INTF patristic citation guidance](https://ntvmr.uni-muenster.de/intfblog/-/blogs/patristic-citations-in-new-testament-textual-criticism)
  warns that patristic references need citation-mode and author-habit review.
- [Leon Levy Dead Sea Scrolls Digital Library](https://www.deadseascrolls.org.il/)
  provides digital access to scroll fragments and high-resolution images.
- [Codex Sinaiticus project](https://www.codexsinaiticus.org/en/project/)
  documents conservation, digitization, transcription, and dissemination work.
- [Manchester Greek P 457](https://www.digitalcollections.manchester.ac.uk/view/MS-GREEK-P-00457)
  is a source anchor for the need to preserve palaeographic date ranges and
  dating uncertainty.
- [CSNTM P52](https://manuscripts.csntm.org/manuscript/View/GA_P52) is a
  cross-check source for catalog metadata such as classification, date,
  location, shelf number, content, language, and material.

## Anti-Guessing Rules

Method profiles must stay unreviewed until a human or expert reviewer confirms
their scope. They do not permit any source import by themselves.

Stop if a method profile is used to:

- promote a candidate claim without source review;
- collapse a broad method into a specific passage, manuscript, or doctrine
  conclusion;
- infer Greek, Hebrew, Aramaic, or other source-language facts without expert
  review;
- hide dissent, date range, or method uncertainty;
- turn patristic reception into Scripture authority;
- store source text or Scripture text in this repo.

## Promotion Gates

A future evidence claim should not move past candidate status unless its linked
method requirements and review events show:

- source locator reviewed;
- source-language need assessed;
- dating basis recorded where relevant;
- material/image access reviewed where relevant;
- variant or citation method stated where relevant;
- discovery-context distinction preserved where relevant;
- confidence level explicit;
- provenance note present;
- review status no longer unreviewed.
