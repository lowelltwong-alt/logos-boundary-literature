# AI Front Door

This repository is `logos-boundary-literature`.

It is a governed scaffold for noncanonical, boundary, heterodox, disputed, forged,
reception-history, and supporting literature related to Scripture and Christian theological
interpretation.

## What This Repo Is

- A planning and metadata home for boundary literature.
- A future place for reviewed work records, source-status records, trust profiles, relationship
  contracts, and scoped claims.
- A companion repo that may reference Scripture by stable references.
- A contamination-control layer for background, reception, comparison, refutation, and
  source-tradition work.

## What This Repo Is Not

- It is not canonical Scripture.
- It is not the source of Scripture text, chunks, or canonical Scripture records.
- It is not a place to import full source-text corpora in this scaffold increment.
- It is not a place to declare theological conclusions as settled universal truth.
- It is not a place to flatten all noncanonical works into one trust category.

## Relation To `logos-scripture-graph`

`logos-scripture-graph` owns canonical Scripture records, chunking, and Scripture retrieval surfaces.
This repo owns boundary-literature metadata, scoped claims, source status, and contamination
controls.

This repo may point to Scripture references. It must not copy Scripture text or mutate Scripture
records. Claims from this repo may be used only as background, reception, comparison, refutation, or
tradition-scoped evidence unless a separate human review explicitly authorizes another use.

## Hard Prohibitions

- Do not import full text corpora.
- Do not paste source texts.
- Do not download sources.
- Do not create canonical Scripture records.
- Do not treat boundary literature as Word of God.
- Do not classify all noncanonical literature as equally false.
- Do not normalize fake gospels, high-trust background, deuterocanon, and patristic reception into
  one bucket.
- Do not create runtime ingestion pipelines in this scaffold.
- Do not overwrite tradition-specific canon status.
- Do not create unscoped theological claims.

## Next Tasks

1. Review governance docs.
2. Add lightweight validation for schema files and empty data directories.
3. Add dummy records only after review, using invented placeholder data rather than real source
   text.
4. Design source-intake review workflow before any real corpus or source metadata import.

## AI Behavior Here

AI agents must separate Confirmed, Inferred, Proposed, and Unknown. They must preserve authority
scope and must not smuggle boundary claims into canonical Scripture. When uncertain, fail closed:
mark records as `quarantine_unreviewed` or `requires_human_source_review`.
