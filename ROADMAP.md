# Boundary Literature Roadmap

This roadmap stages future work for commentary, patristic, theologian-writing,
and reception-history material without importing source texts in the current
scaffold.

## Phase 1: Navigation And Governance

- Keep `AI_FRONT_DOOR.md`, `AI_TABLE_OF_CONTENTS.md`, `README.md`, and
  `.ai/control/boundary_material_routing.yaml` aligned.
- Maintain contamination controls that prevent boundary material from becoming
  canonical Scripture authority.
- Keep data folders empty until source-intake review permits scoped records.

## Phase 2: Source Metadata Before Text

- Define metadata-only records for works, authors, dates, attribution status,
  tradition/profile scope, trust level, provenance, and review status.
- Store Scripture references only, not Scripture text.
- Track whether a source is public domain, copyrighted, licensed, disputed, or
  unavailable.
- Develop the reliability/provenance evidence database scaffold as metadata
  planning only. It may reference future `scripture_*` records from
  `logos-scripture-graph`, but this repo owns only `boundary_*` and `evidence_*`
  tables.

## Phase 3: Patristic And Early Reception

- Add reviewed metadata patterns for church-father citations and patristic
  reception.
- Distinguish quotation, paraphrase, allusion, commentary, reception motif, and
  doctrinal use.
- Keep claims scoped by tradition/profile and review status.

## Phase 4: Commentary And Theologian Source Layers

- Add metadata patterns for ancient, medieval, Reformation, modern, and
  contemporary theologian writings.
- Track attribution, edition, translation, provenance, and source reliability.
- Preserve the difference between source/reception evidence and doctrine
  lineage.

## Phase 5: Derived Evidence Exports

- Support future derived reports that show Scripture evidence, boundary
  reception, and doctrine lineage with clear labels.
- Use `boundary_*` and `evidence_*` namespaces for boundary-derived data.
- Never create canonical Scripture tables or views from commentary, patristic,
  theologian, or denomination-profile data.
- Add discovery-timeline and reliability-report views only after the source
  records, confidence fields, and review gates exist.

## Phase 6: Doctrine Genealogy Handoff

- When `logos-doctrine-genealogy` is created by governance registration, expose
  reviewed boundary source references for lineage work.
- Do not move commentary corpora or theologian source records into the doctrine
  repo by default.
- Doctrine lineage should reference boundary source IDs, not absorb this repo's
  source ownership.

## Stop Conditions

Stop and report if:

- commentary or theologian claims are treated as Scripture authority;
- Scripture text is requested for storage in this repo;
- a boundary record lacks trust level, tradition/profile scope, provenance, or
  review status;
- denomination/profile claims are presented as universal truth without scope;
- a unified report hides whether data came from Scripture, boundary literature,
  or doctrine lineage.
- a reliability/provenance record stores Scripture text, manuscript
  transcription text, commentary text, patristic text, or theologian text before
  source-intake review.
