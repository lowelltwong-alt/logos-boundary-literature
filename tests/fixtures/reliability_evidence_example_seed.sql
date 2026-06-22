-- object_type: sqlite_fixture
-- trust_zone: proposed
-- lifecycle_status: draft
-- provenance_note: Created 2026-06-22 as invented sample data for reliability evidence schema validation.
-- reason_for_inclusion: Exercise boundary/evidence table constraints without importing Scripture text, source text, or real catalog assertions.

PRAGMA foreign_keys = ON;

INSERT INTO boundary_source_work (
  boundary_work_id,
  work_title,
  material_class,
  author_label,
  author_tradition_scope,
  approximate_date_start,
  approximate_date_end,
  attribution_status,
  trust_level,
  tradition_scope,
  profile_scope,
  source_basis,
  provenance_note,
  review_status
) VALUES (
  'example_boundary_work_patristic_reception',
  'Example Patristic Reception Work',
  'patristic_reception',
  'Example ancient author label',
  'example_scope_only',
  NULL,
  NULL,
  'unreviewed',
  'example_only',
  'example_tradition_scope_only',
  'not_applicable',
  'invented fixture row; no source intake',
  'Example fixture created to validate table boundaries, not to assert historical content.',
  'unreviewed'
);

INSERT INTO boundary_source_access (
  boundary_source_access_id,
  boundary_work_id,
  source_locator,
  access_type,
  may_store_full_text,
  may_store_scripture_text,
  license_note,
  provenance_note,
  review_status
) VALUES (
  'example_boundary_source_access',
  'example_boundary_work_patristic_reception',
  'example locator only; not a real source locator',
  'bibliographic_reference',
  0,
  0,
  'Example fixture stores metadata only and grants no intake permission.',
  'Example fixture row; no source text or Scripture text is present.',
  'unreviewed'
);

INSERT INTO evidence_project (
  evidence_project_id,
  project_slug,
  project_title,
  project_scope,
  source_truth_repos,
  derived_artifact,
  canonical_authority_transferred,
  provenance_note,
  review_status
) VALUES (
  'example_evidence_project',
  'example-reliability-fixture',
  'Example Reliability Fixture',
  'Invented metadata-only project used to test schema separation.',
  'logos-scripture-graph references only; logos-boundary-literature metadata only',
  1,
  0,
  'Fixture project exists only to validate governance guardrails.',
  'draft'
);

INSERT INTO evidence_research_intake_queue (
  evidence_intake_id,
  evidence_project_id,
  evidence_lane,
  source_locator,
  source_kind,
  proposed_target_repo,
  proposed_record_namespace,
  intake_claim_status,
  confirmed_fact_summary,
  candidate_claim_summary,
  stores_source_text,
  stores_scripture_text,
  stores_transcription_text,
  requires_license_review,
  requires_expert_review,
  source_basis,
  method_note,
  confidence_level,
  tradition_scope,
  profile_scope,
  provenance_note,
  review_status
) VALUES
(
  'example_intake_dead_sea_scrolls',
  'example_evidence_project',
  'dead_sea_scrolls_ot_witness',
  'example DSS source locator only',
  'official_catalog',
  'logos-scripture-graph',
  'scripture_*',
  'candidate_claim',
  'none_reviewed',
  'Example-only question about which future Scripture Graph witness record would own a DSS item.',
  0,
  0,
  0,
  1,
  1,
  'invented fixture row; no source intake',
  'Queue item asks for source and date review before any witness or prophecy-related claim.',
  'unknown',
  'not_applicable',
  'not_applicable',
  'Fixture intake row routes a future canonical witness question without creating canonical data.',
  'unreviewed'
),
(
  'example_intake_nt_papyri_codices',
  'example_evidence_project',
  'nt_papyri_codices',
  'example NT papyrus catalog locator only',
  'academic_project',
  'logos-scripture-graph',
  'scripture_*',
  'mixed_requires_split',
  'Example-only catalog metadata would be separated from any earliest-fragment claim.',
  'Example-only candidate claim requires catalog cross-check and dating-method review.',
  0,
  0,
  0,
  1,
  1,
  'invented fixture row; no source intake',
  'Queue item verifies that source facts and apologetic claims must be split.',
  'unknown',
  'not_applicable',
  'not_applicable',
  'Fixture intake row does not assert real papyrus metadata.',
  'unreviewed'
),
(
  'example_intake_textual_variants',
  'example_evidence_project',
  'textual_variants_copy_abundance',
  'example textual-criticism method source only',
  'peer_reviewed_article',
  'logos-boundary-literature',
  'evidence_*',
  'candidate_claim',
  'none_reviewed',
  'Example-only question about how witness abundance should be evaluated for a specific variant question.',
  0,
  0,
  0,
  1,
  1,
  'invented fixture row; no source intake',
  'Queue item blocks broad reliability conclusions from manuscript counts alone.',
  'unknown',
  'not_applicable',
  'not_applicable',
  'Fixture intake row remains an unreviewed method question.',
  'unreviewed'
),
(
  'example_intake_early_creed',
  'example_evidence_project',
  'early_creed_oral_tradition',
  'example early-tradition bibliography locator only',
  'scholarly_book',
  'logos-boundary-literature',
  'evidence_*',
  'candidate_claim',
  'none_reviewed',
  'Example-only question about dating a formulaic tradition without storing Scripture text.',
  0,
  0,
  0,
  1,
  1,
  'invented fixture row; no source intake',
  'Queue item requires source, argument basis, confidence, and dissent notes before promotion.',
  'unknown',
  'not_applicable',
  'not_applicable',
  'Fixture intake row does not assert a real creed date.',
  'unreviewed'
),
(
  'example_intake_patristic_reception',
  'example_evidence_project',
  'patristic_reception_reconstruction',
  'example patristic citation index locator only',
  'academic_project',
  'logos-boundary-literature',
  'boundary_*',
  'mixed_requires_split',
  'Example-only source metadata would be separate from reconstruction claims.',
  'Example-only reconstruction claim requires citation-mode and edition review.',
  0,
  0,
  0,
  1,
  1,
  'invented fixture row; no source intake',
  'Queue item verifies that patristic references stay reception evidence, not Scripture authority.',
  'unknown',
  'example_tradition_scope_only',
  'not_applicable',
  'Fixture intake row stores no patristic text and makes no reconstruction assertion.',
  'unreviewed'
),
(
  'example_intake_discovery_timeline',
  'example_evidence_project',
  'discovery_timeline',
  'example discovery-history locator only',
  'museum_or_library_record',
  'logos-boundary-literature',
  'evidence_*',
  'candidate_claim',
  'none_reviewed',
  'Example-only question about what was known when and whether a debate milestone is actually linked.',
  0,
  0,
  0,
  1,
  1,
  'invented fixture row; no source intake',
  'Queue item separates discovery events from later apologetic interpretations.',
  'unknown',
  'not_applicable',
  'not_applicable',
  'Fixture intake row does not assert a real discovery event.',
  'unreviewed'
),
(
  'example_intake_method_bibliography',
  'example_evidence_project',
  'method_bibliography',
  'example method bibliography locator only',
  'scholarly_book',
  'logos-boundary-literature',
  'evidence_*',
  'confirmed_source_metadata',
  'Example-only method bibliography metadata can be queued without becoming evidence for a claim.',
  'none',
  0,
  0,
  0,
  1,
  1,
  'invented fixture row; no source intake',
  'Queue item keeps method sources separate from manuscript, passage, or doctrine claims.',
  'unknown',
  'not_applicable',
  'not_applicable',
  'Fixture intake row does not promote any method source as decisive evidence.',
  'unreviewed'
);

INSERT INTO evidence_external_source (
  evidence_source_id,
  source_title,
  source_url,
  source_kind,
  publisher_or_institution,
  access_date,
  source_trust_level,
  license_or_access_note,
  provenance_note,
  review_status
) VALUES (
  'example_evidence_external_source',
  'Example External Catalog Record',
  'https://example.test/catalog/example-witness',
  'official_catalog',
  'Example institution',
  '2026-06-22',
  'requires_review',
  'Example URL only; does not authorize source ingestion.',
  'Invented source row for schema testing; not a real catalog assertion.',
  'unreviewed'
);

INSERT INTO evidence_scripture_reference (
  evidence_scripture_ref_id,
  owning_repo,
  scripture_reference,
  passage_id_ref,
  stores_scripture_text,
  source_basis,
  provenance_note,
  review_status
) VALUES (
  'example_evidence_scripture_ref',
  'logos-scripture-graph',
  'John 18:31-38',
  'example_passage_ref_only',
  0,
  'reference_only',
  'Fixture stores a reference string only and no Scripture text.',
  'unreviewed'
);

INSERT INTO boundary_patristic_citation_candidate (
  boundary_citation_id,
  boundary_work_id,
  scripture_reference_id,
  citation_mode,
  citation_text_stored,
  source_basis,
  method_note,
  confidence_level,
  tradition_scope,
  profile_scope,
  provenance_note,
  review_status
) VALUES (
  'example_boundary_citation_candidate',
  'example_boundary_work_patristic_reception',
  'example_evidence_scripture_ref',
  'allusion_candidate',
  0,
  'invented fixture row; no citation text stored',
  'Used only to verify that citation candidates can point at references without becoming Scripture authority.',
  'unknown',
  'example_tradition_scope_only',
  'not_applicable',
  'Fixture row is not reviewed evidence and cannot be promoted as a historical claim.',
  'unreviewed'
);

INSERT INTO evidence_manuscript_witness_ref (
  evidence_witness_ref_id,
  owning_repo_or_catalog,
  external_witness_id,
  witness_label,
  corpus_scope,
  language_scope,
  material_type,
  approximate_date_start,
  approximate_date_end,
  dating_method,
  stores_transcription_text,
  source_basis,
  confidence_level,
  provenance_note,
  review_status
) VALUES (
  'example_evidence_witness_ref',
  'example_catalog_reference_only',
  'example_external_witness_id',
  'Example Witness Label',
  'new_testament',
  'example_language_scope_only',
  'example_material_type',
  NULL,
  NULL,
  'unknown',
  0,
  'invented fixture row; catalog metadata only',
  'unknown',
  'Fixture witness reference is not a real manuscript record and stores no transcription.',
  'unreviewed'
);

INSERT INTO evidence_textual_question_ref (
  evidence_question_id,
  evidence_scripture_ref_id,
  question_type,
  question_summary,
  no_reading_text_stored,
  source_basis,
  method_note,
  confidence_level,
  provenance_note,
  review_status
) VALUES (
  'example_evidence_textual_question',
  'example_evidence_scripture_ref',
  'witness_attestation_question',
  'Example-only question about how a witness reference would be linked to a passage reference.',
  1,
  'invented fixture row; no variant reading text stored',
  'The fixture validates method/provenance fields without making textual-critical claims.',
  'unknown',
  'Fixture question is not a reviewed textual question.',
  'draft'
);

INSERT INTO evidence_discovery_event (
  evidence_discovery_event_id,
  evidence_witness_ref_id,
  event_type,
  event_date_start,
  event_date_end,
  event_location,
  event_summary,
  evidence_source_id,
  provenance_note,
  review_status
) VALUES (
  'example_evidence_discovery_event',
  'example_evidence_witness_ref',
  'cataloging',
  NULL,
  NULL,
  'example location only',
  'Example-only event showing where discovery or cataloging metadata would be modeled.',
  'example_evidence_external_source',
  'Fixture discovery event is invented and not a historical assertion.',
  'unreviewed'
);

INSERT INTO evidence_claim_candidate (
  evidence_claim_id,
  evidence_project_id,
  claim_scope,
  claim_summary,
  claim_status,
  source_basis,
  method_note,
  confidence_level,
  tradition_scope,
  profile_scope,
  provenance_note,
  review_status
) VALUES (
  'example_evidence_claim_candidate',
  'example_evidence_project',
  'apologetics_report',
  'Example-only candidate showing how a report claim can link manuscript and reception metadata with clear labels.',
  'candidate',
  'invented fixture row; requires real source review before any promotion',
  'This fixture verifies joins and anti-guessing review gates without asserting reliability evidence.',
  'unknown',
  'not_applicable',
  'not_applicable',
  'Fixture claim remains candidate/unreviewed and transfers no Scripture authority.',
  'unreviewed'
);

INSERT INTO evidence_claim_source_link (
  evidence_claim_source_link_id,
  evidence_claim_id,
  evidence_source_id,
  evidence_witness_ref_id,
  boundary_citation_id,
  support_role,
  provenance_note,
  review_status
) VALUES (
  'example_evidence_claim_source_link',
  'example_evidence_claim_candidate',
  'example_evidence_external_source',
  'example_evidence_witness_ref',
  'example_boundary_citation_candidate',
  'requires_review',
  'Fixture link demonstrates labeled joins without source authority promotion.',
  'unreviewed'
);

INSERT INTO evidence_review_event (
  evidence_review_event_id,
  reviewed_object_type,
  reviewed_object_id,
  reviewer_role,
  review_decision,
  review_note
) VALUES (
  'example_evidence_review_event',
  'evidence_claim_candidate',
  'example_evidence_claim_candidate',
  'fixture_validation',
  'keep_candidate',
  'Fixture review keeps the example claim as a candidate.'
);

INSERT INTO evidence_anti_guessing_audit (
  evidence_audit_id,
  audited_object_type,
  audited_object_id,
  has_source_basis,
  has_scope,
  has_method,
  has_confidence,
  has_provenance,
  has_review_status,
  may_promote,
  audit_note
) VALUES (
  'example_evidence_anti_guessing_audit',
  'evidence_claim_candidate',
  'example_evidence_claim_candidate',
  1,
  1,
  1,
  1,
  1,
  1,
  0,
  'Even complete fixture metadata cannot be promoted because the row is invented and unreviewed.'
);
