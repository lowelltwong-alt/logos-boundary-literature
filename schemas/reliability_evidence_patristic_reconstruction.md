---
object_type: patristic_reconstruction_plan
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created 2026-06-22 as a metadata-only scaffold for patristic reconstruction questions in Bible reliability research."
reason_for_inclusion: "Plan how church-father citations may serve as reception/textual evidence without treating them as Scripture or importing patristic/source text."
---

# Reliability Evidence Patristic Reconstruction

## Purpose

This scaffold models questions about whether patristic citations and reception
evidence could help reconstruct a passage, section, corpus subset, or scoped
claim if direct manuscript evidence were missing.

It does not assert that the Bible can be reconstructed from church fathers. It
does not store patristic text, commentary text, theologian text, Scripture text,
or manuscript transcriptions. It creates a review shape for future work.

## Placement Decision

This belongs in `logos-boundary-literature` because church-father citations,
patristic reception, commentary references, source-access metadata, attribution
status, and reconstruction questions are boundary literature evidence.

Canonical Scripture text, variants, manuscript witnesses, fragments, and
canonical passage records remain in `logos-scripture-graph`.

## Source-Grounded Starting Points

| Source | Confirmed Source Metadata To Check | Candidate Claims To Keep Unreviewed |
|---|---|---|
| [BiblIndex overview](https://www.biblindex.org/en/overview) | BiblIndex is a project for indexing biblical quotations and allusions in early Christian literature. | Whether BiblIndex coverage proves a passage, corpus, or whole-canon reconstruction claim. |
| [BiblIndex project blog](https://biblindex-en.hypotheses.org/page/2) | The project describes itself as an online index of biblical references in Jewish and Christian literature and late-antique/early-medieval texts. | Whether an indexed reference is a direct quotation, allusion, paraphrase, or reliable textual witness. |
| [INTF patristic citation guidance](https://ntvmr.uni-muenster.de/intfblog/-/blogs/patristic-citations-in-new-testament-textual-criticism) | INTF treats patristic citations as potentially significant witnesses while emphasizing that citation treatment and author habits must be reviewed. | Any blanket claim that the church fathers alone reconstruct the New Testament or settle a variant. |
| [INTF](https://www.uni-muenster.de/INTF/en/) | INTF frames textual-history work across manuscript tradition, early translations, and patristic citations. | Any claim that patristic evidence can replace manuscript and versional evidence. |

## Reconstruction Scopes

| Scope | Meaning | Required Caution |
|---|---|---|
| `passage_reference` | A question about one passage reference or small reference cluster. | Store references only; no Scripture text or citation text. |
| `book_or_section` | A question about coverage for a book, chapter group, or section. | Require coverage limits and source-corpus boundaries. |
| `corpus_subset` | A question about a subset such as Gospel citations in a defined patristic corpus. | Require corpus selection rules and edition/source review. |
| `canon_wide_candidate` | A candidate question about broad reconstruction claims. | Must remain candidate until coverage, modes, editions, languages, and dissent are reviewed. |
| `essential_doctrine_reference` | A question about whether references support a doctrinally important Scripture passage or theme. | Must not become doctrine authority or Scripture authority. |
| `method_only` | A method question about how reconstruction should be evaluated. | Cannot be used as evidence for a passage by itself. |

## Citation-Mode Requirements

Future reconstruction work must distinguish:

- direct quotation;
- varying or loose quotation;
- paraphrase;
- allusion;
- commentary reference;
- reception motif;
- doctrinal use.

Only a reviewed source, edition, attribution, language, and citation-mode
analysis can move a reconstruction question beyond candidate status.

## Stop Rules

Stop and report if a reconstruction question would:

- store patristic text, commentary text, theologian text, Scripture text, or
  manuscript transcription text;
- treat church fathers as Scripture authority;
- merge patristic material into canonical Scripture tables or views;
- assert a whole-canon or percentage reconstruction claim without corpus,
  edition, citation-mode, language, method, confidence, and dissent review;
- use a translated citation as if it were the source-language wording;
- hide uncertainty about attribution, date, location, edition, or author habit.

## Promotion Gates

A patristic reconstruction question cannot move beyond candidate unless it has:

- source corpus boundary;
- citation-mode policy;
- critical-edition or source-access basis;
- translation/source-language basis;
- attribution/date/location review where relevant;
- coverage summary;
- candidate claim summary;
- source basis;
- method note;
- confidence level;
- provenance note;
- review status beyond unreviewed.
