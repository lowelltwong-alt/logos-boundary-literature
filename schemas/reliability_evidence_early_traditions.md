---
object_type: early_tradition_question_plan
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created 2026-06-22 as a metadata-only scaffold for early creed and oral-tradition reliability questions."
reason_for_inclusion: "Plan how early tradition claims can be reviewed without storing Scripture text, creed wording, or overpromoting apologetic date claims."
---

# Reliability Evidence Early Traditions

## Purpose

This scaffold models questions about early creeds, formulaic traditions, oral
tradition, and early devotion patterns. It is designed for claims such as
whether a tradition behind a Scripture reference may be pre-Pauline or unusually
early.

It does not store Scripture wording, creed wording, source text, manuscript
transcriptions, or theological conclusions.

It does not assert that a creed dates within months of the resurrection.

It creates a review shape so those claims can stay candidate until source,
method, language, context, dissent, and confidence are reviewed.

## Placement Decision

This belongs in `logos-boundary-literature` as derived evidence and historical
method planning. It stores Scripture references only. Canonical Scripture text,
canonical chunks, canonical passage IDs, and canonical Scripture authority
remain in `logos-scripture-graph`.

## Source-Grounded Starting Points

| Source | Confirmed Source Metadata To Check | Candidate Claims To Keep Unreviewed |
|---|---|---|
| [N. T. Wright: Early Traditions and the Origins of Christianity](https://ntwrightpage.com/2016/04/05/early-traditions-and-the-origins-of-christianity/) | Wright treats `1 Corinthians 15:1-7` as a very early tradition Paul describes as common among Christians. | Exact date range; whether the tradition dates within months; which parts are pre-Pauline; how much evidential force follows. |
| [Larry Hurtado: The Origins of Devotion to Jesus in its Ancient Context](https://larryhurtado.wordpress.com/2019/08/23/the-origins-of-devotion-to-jesus-in-its-ancient-context/) | Hurtado points readers to scholarly work on earliest devotion to Jesus and early Christian origins. | Whether a specific formula is fixed, how early it is, and whether it supports a resurrection-evidence report. |
| [Ehrman blog caution on pre-Pauline language](https://ehrmanblog.org/one-of-our-earliest-statements-of-belief-in-jesus/) | The public post distinguishes "pre-Pauline" from proving circulation immediately after Jesus' death. | Any automatic move from "pre-Pauline" to "within months" or "first couple of years." |

These sources are anchors for review planning only. They are not imported rows,
and their claims are not promoted by this scaffold.

## Early Tradition Question Types

| Type | Meaning | Promotion Blocker |
|---|---|---|
| `pre_pauline_creed_candidate` | A candidate question that a formula or tradition predates Paul's letter or use of it. | Must not be narrowed to months or years without source, method, context, and dissent review. |
| `formulaic_tradition_candidate` | A candidate question based on formulaic, rhythmic, or tradition-marker arguments. | Requires source-language and literary-form review. |
| `oral_tradition_question` | A question about whether material circulated orally before being written. | Requires transmission model and historical-context review. |
| `early_devotion_pattern` | A question about early devotional practice or belief patterns. | Must not become doctrine authority or Scripture authority. |
| `method_only` | A method question about how early tradition should be evaluated. | Cannot serve as evidence for a date or event by itself. |

## Required Review Fields

Each future early-tradition row must track:

- Scripture reference only, not Scripture text;
- tradition type;
- evidence scope;
- dating claim status;
- earliest and latest possible date ranges where reviewed;
- date precision and basis;
- linguistic or formulaic signal status;
- source-language scope;
- confirmed fact summary;
- candidate claim summary;
- dissent summary;
- source basis;
- method note;
- confidence level;
- provenance note;
- review status.

## Stop Rules

Stop and report if a row would:

- store Scripture text, creed wording, source text, or manuscript transcription;
- assert a "within months" date without reviewed source and method evidence;
- treat a pre-Pauline label as equivalent to immediate post-resurrection origin;
- claim resurrection proof from tradition age alone;
- hide dissent or uncertainty about linguistic, formulaic, or historical
  arguments;
- treat an early tradition claim as Scripture authority.

## Promotion Gates

An early-tradition question cannot move beyond candidate unless it has:

- reviewed source basis;
- reviewed date basis;
- source-language or linguistic review where relevant;
- historical-context review;
- dissent review;
- explicit confidence level;
- provenance note;
- review status beyond unreviewed.
