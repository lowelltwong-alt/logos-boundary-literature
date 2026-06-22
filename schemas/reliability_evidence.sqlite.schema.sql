-- object_type: sqlite_schema_scaffold
-- trust_zone: proposed
-- lifecycle_status: draft
-- provenance_note: Created 2026-06-22 as a metadata-only reliability evidence schema scaffold.
-- reason_for_inclusion: Define table boundaries for derived Bible reliability evidence without importing source texts or canonical Scripture records.

PRAGMA foreign_keys = ON;

CREATE TABLE boundary_source_work (
  boundary_work_id TEXT PRIMARY KEY,
  work_title TEXT NOT NULL,
  material_class TEXT NOT NULL CHECK (
    material_class IN (
      'patristic_reception',
      'church_father_citation',
      'commentary_metadata',
      'theologian_writing_metadata',
      'historical_context_source',
      'attribution_or_forgery_source'
    )
  ),
  author_label TEXT,
  author_tradition_scope TEXT NOT NULL DEFAULT 'unknown',
  approximate_date_start INTEGER,
  approximate_date_end INTEGER,
  attribution_status TEXT NOT NULL DEFAULT 'unreviewed',
  trust_level TEXT NOT NULL,
  tradition_scope TEXT NOT NULL,
  profile_scope TEXT NOT NULL DEFAULT 'not_applicable',
  source_basis TEXT NOT NULL,
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE boundary_source_access (
  boundary_source_access_id TEXT PRIMARY KEY,
  boundary_work_id TEXT NOT NULL REFERENCES boundary_source_work(boundary_work_id),
  source_locator TEXT NOT NULL,
  access_type TEXT NOT NULL CHECK (
    access_type IN (
      'catalog_record',
      'public_domain_source',
      'licensed_source',
      'bibliographic_reference',
      'restricted_or_unavailable',
      'unknown'
    )
  ),
  may_store_full_text INTEGER NOT NULL DEFAULT 0 CHECK (may_store_full_text = 0),
  may_store_scripture_text INTEGER NOT NULL DEFAULT 0 CHECK (may_store_scripture_text = 0),
  license_note TEXT NOT NULL,
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE boundary_patristic_citation_candidate (
  boundary_citation_id TEXT PRIMARY KEY,
  boundary_work_id TEXT NOT NULL REFERENCES boundary_source_work(boundary_work_id),
  scripture_reference_id TEXT NOT NULL,
  citation_mode TEXT NOT NULL CHECK (
    citation_mode IN (
      'direct_quotation_candidate',
      'paraphrase_candidate',
      'allusion_candidate',
      'commentary_reference',
      'reception_motif',
      'unknown'
    )
  ),
  citation_text_stored INTEGER NOT NULL DEFAULT 0 CHECK (citation_text_stored = 0),
  source_basis TEXT NOT NULL,
  method_note TEXT NOT NULL,
  confidence_level TEXT NOT NULL DEFAULT 'unknown',
  tradition_scope TEXT NOT NULL,
  profile_scope TEXT NOT NULL DEFAULT 'not_applicable',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE evidence_project (
  evidence_project_id TEXT PRIMARY KEY,
  project_slug TEXT NOT NULL UNIQUE,
  project_title TEXT NOT NULL,
  project_scope TEXT NOT NULL,
  source_truth_repos TEXT NOT NULL,
  derived_artifact INTEGER NOT NULL DEFAULT 1 CHECK (derived_artifact = 1),
  canonical_authority_transferred INTEGER NOT NULL DEFAULT 0 CHECK (canonical_authority_transferred = 0),
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'draft'
);

CREATE TABLE evidence_method_profile (
  evidence_method_profile_id TEXT PRIMARY KEY,
  method_scope TEXT NOT NULL CHECK (
    method_scope IN (
      'source_catalog_metadata_review',
      'palaeographic_dating_review',
      'material_and_image_review',
      'textual_variant_method_review',
      'patristic_citation_mode_review',
      'early_creed_tradition_review',
      'discovery_timeline_review',
      'source_language_expertise_review'
    )
  ),
  method_title TEXT NOT NULL,
  source_locator TEXT NOT NULL,
  source_kind TEXT NOT NULL CHECK (
    source_kind IN (
      'official_catalog',
      'museum_or_library_record',
      'academic_project',
      'peer_reviewed_article',
      'scholarly_book',
      'primary_source_reference',
      'other'
    )
  ),
  governs_evidence_lane TEXT NOT NULL CHECK (
    governs_evidence_lane IN (
      'dead_sea_scrolls_ot_witness',
      'nt_papyri_codices',
      'textual_variants_copy_abundance',
      'early_creed_oral_tradition',
      'patristic_reception_reconstruction',
      'discovery_timeline',
      'method_bibliography',
      'cross_lane'
    )
  ),
  requires_source_language_review INTEGER NOT NULL DEFAULT 0 CHECK (requires_source_language_review IN (0, 1)),
  requires_dating_review INTEGER NOT NULL DEFAULT 0 CHECK (requires_dating_review IN (0, 1)),
  requires_material_review INTEGER NOT NULL DEFAULT 0 CHECK (requires_material_review IN (0, 1)),
  requires_citation_mode_review INTEGER NOT NULL DEFAULT 0 CHECK (requires_citation_mode_review IN (0, 1)),
  requires_variant_method_review INTEGER NOT NULL DEFAULT 0 CHECK (requires_variant_method_review IN (0, 1)),
  requires_discovery_context_review INTEGER NOT NULL DEFAULT 0 CHECK (requires_discovery_context_review IN (0, 1)),
  prohibits_ai_promotion INTEGER NOT NULL DEFAULT 1 CHECK (prohibits_ai_promotion = 1),
  source_basis TEXT NOT NULL,
  method_note TEXT NOT NULL,
  confidence_level TEXT NOT NULL DEFAULT 'unknown',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE evidence_research_intake_queue (
  evidence_intake_id TEXT PRIMARY KEY,
  evidence_project_id TEXT NOT NULL REFERENCES evidence_project(evidence_project_id),
  evidence_lane TEXT NOT NULL CHECK (
    evidence_lane IN (
      'dead_sea_scrolls_ot_witness',
      'nt_papyri_codices',
      'textual_variants_copy_abundance',
      'early_creed_oral_tradition',
      'patristic_reception_reconstruction',
      'discovery_timeline',
      'method_bibliography'
    )
  ),
  evidence_method_profile_id TEXT REFERENCES evidence_method_profile(evidence_method_profile_id),
  source_locator TEXT NOT NULL,
  source_kind TEXT NOT NULL CHECK (
    source_kind IN (
      'official_catalog',
      'museum_or_library_record',
      'academic_project',
      'peer_reviewed_article',
      'scholarly_book',
      'primary_source_reference',
      'other'
    )
  ),
  proposed_target_repo TEXT NOT NULL CHECK (
    proposed_target_repo IN (
      'logos-boundary-literature',
      'logos-scripture-graph',
      'logos-doctrine-genealogy',
      'external_catalog_only',
      'undecided'
    )
  ),
  proposed_record_namespace TEXT NOT NULL CHECK (
    proposed_record_namespace IN (
      'boundary_*',
      'evidence_*',
      'scripture_*',
      'doctrine_*',
      'external_catalog_only',
      'undecided'
    )
  ),
  intake_claim_status TEXT NOT NULL CHECK (
    intake_claim_status IN (
      'confirmed_source_metadata',
      'candidate_claim',
      'mixed_requires_split',
      'unknown_requires_review'
    )
  ),
  confirmed_fact_summary TEXT NOT NULL DEFAULT 'none_reviewed',
  candidate_claim_summary TEXT NOT NULL DEFAULT 'none',
  stores_source_text INTEGER NOT NULL DEFAULT 0 CHECK (stores_source_text = 0),
  stores_scripture_text INTEGER NOT NULL DEFAULT 0 CHECK (stores_scripture_text = 0),
  stores_transcription_text INTEGER NOT NULL DEFAULT 0 CHECK (stores_transcription_text = 0),
  requires_license_review INTEGER NOT NULL DEFAULT 1 CHECK (requires_license_review IN (0, 1)),
  requires_expert_review INTEGER NOT NULL DEFAULT 1 CHECK (requires_expert_review IN (0, 1)),
  source_basis TEXT NOT NULL,
  method_note TEXT NOT NULL,
  confidence_level TEXT NOT NULL DEFAULT 'unknown',
  tradition_scope TEXT NOT NULL DEFAULT 'not_applicable',
  profile_scope TEXT NOT NULL DEFAULT 'not_applicable',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE evidence_intake_method_requirement (
  evidence_intake_method_requirement_id TEXT PRIMARY KEY,
  evidence_intake_id TEXT NOT NULL REFERENCES evidence_research_intake_queue(evidence_intake_id),
  evidence_method_profile_id TEXT NOT NULL REFERENCES evidence_method_profile(evidence_method_profile_id),
  requirement_role TEXT NOT NULL CHECK (
    requirement_role IN (
      'primary_method',
      'additional_review',
      'blocking_review',
      'source_access_review',
      'language_review',
      'dating_review',
      'citation_mode_review',
      'discovery_context_review'
    )
  ),
  required_before_status TEXT NOT NULL CHECK (
    required_before_status IN (
      'source_intake',
      'candidate_to_proposed',
      'proposed_to_reviewed',
      'any_promotion'
    )
  ),
  satisfied INTEGER NOT NULL DEFAULT 0 CHECK (satisfied = 0),
  source_basis TEXT NOT NULL,
  method_note TEXT NOT NULL,
  confidence_level TEXT NOT NULL DEFAULT 'unknown',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE evidence_external_source (
  evidence_source_id TEXT PRIMARY KEY,
  source_title TEXT NOT NULL,
  source_url TEXT,
  source_kind TEXT NOT NULL CHECK (
    source_kind IN (
      'official_catalog',
      'museum_or_library_record',
      'academic_project',
      'peer_reviewed_article',
      'scholarly_book',
      'primary_source_reference',
      'other'
    )
  ),
  publisher_or_institution TEXT,
  access_date TEXT,
  source_trust_level TEXT NOT NULL DEFAULT 'requires_review',
  license_or_access_note TEXT NOT NULL,
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE evidence_scripture_reference (
  evidence_scripture_ref_id TEXT PRIMARY KEY,
  owning_repo TEXT NOT NULL DEFAULT 'logos-scripture-graph',
  scripture_reference TEXT NOT NULL,
  passage_id_ref TEXT,
  stores_scripture_text INTEGER NOT NULL DEFAULT 0 CHECK (stores_scripture_text = 0),
  source_basis TEXT NOT NULL DEFAULT 'reference_only',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE evidence_manuscript_witness_ref (
  evidence_witness_ref_id TEXT PRIMARY KEY,
  owning_repo_or_catalog TEXT NOT NULL,
  external_witness_id TEXT NOT NULL,
  witness_label TEXT NOT NULL,
  corpus_scope TEXT NOT NULL CHECK (
    corpus_scope IN (
      'old_testament_or_hebrew_bible',
      'new_testament',
      'septuagint_or_ancient_version',
      'patristic_or_reception',
      'unknown'
    )
  ),
  language_scope TEXT NOT NULL DEFAULT 'unknown',
  material_type TEXT,
  approximate_date_start INTEGER,
  approximate_date_end INTEGER,
  dating_method TEXT NOT NULL DEFAULT 'unknown',
  stores_transcription_text INTEGER NOT NULL DEFAULT 0 CHECK (stores_transcription_text = 0),
  source_basis TEXT NOT NULL,
  confidence_level TEXT NOT NULL DEFAULT 'unknown',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE evidence_textual_question_ref (
  evidence_question_id TEXT PRIMARY KEY,
  evidence_scripture_ref_id TEXT NOT NULL REFERENCES evidence_scripture_reference(evidence_scripture_ref_id),
  question_type TEXT NOT NULL CHECK (
    question_type IN (
      'variant_unit_reference',
      'witness_attestation_question',
      'dating_question',
      'provenance_question',
      'copy_abundance_question',
      'translation_history_question',
      'early_creed_or_oral_tradition_question'
    )
  ),
  question_summary TEXT NOT NULL,
  no_reading_text_stored INTEGER NOT NULL DEFAULT 1 CHECK (no_reading_text_stored = 1),
  source_basis TEXT NOT NULL,
  method_note TEXT NOT NULL,
  confidence_level TEXT NOT NULL DEFAULT 'unknown',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'draft'
);

CREATE TABLE evidence_discovery_event (
  evidence_discovery_event_id TEXT PRIMARY KEY,
  evidence_witness_ref_id TEXT REFERENCES evidence_manuscript_witness_ref(evidence_witness_ref_id),
  event_type TEXT NOT NULL CHECK (
    event_type IN (
      'discovery',
      'acquisition',
      'cataloging',
      'publication',
      'digitization',
      'redating',
      'debate_milestone'
    )
  ),
  event_date_start INTEGER,
  event_date_end INTEGER,
  event_location TEXT,
  event_summary TEXT NOT NULL,
  evidence_source_id TEXT REFERENCES evidence_external_source(evidence_source_id),
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE evidence_claim_candidate (
  evidence_claim_id TEXT PRIMARY KEY,
  evidence_project_id TEXT NOT NULL REFERENCES evidence_project(evidence_project_id),
  claim_scope TEXT NOT NULL CHECK (
    claim_scope IN (
      'manuscript_provenance',
      'textual_variant_detection',
      'copy_abundance',
      'old_testament_witness_history',
      'new_testament_witness_history',
      'early_creed_or_oral_tradition',
      'patristic_reception',
      'apologetics_report'
    )
  ),
  claim_summary TEXT NOT NULL,
  claim_status TEXT NOT NULL DEFAULT 'candidate' CHECK (
    claim_status IN ('candidate', 'proposed', 'reviewed', 'rejected')
  ),
  source_basis TEXT NOT NULL,
  method_note TEXT NOT NULL,
  confidence_level TEXT NOT NULL DEFAULT 'unknown',
  tradition_scope TEXT NOT NULL DEFAULT 'not_applicable',
  profile_scope TEXT NOT NULL DEFAULT 'not_applicable',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE evidence_timeline_checkpoint (
  evidence_timeline_checkpoint_id TEXT PRIMARY KEY,
  evidence_project_id TEXT NOT NULL REFERENCES evidence_project(evidence_project_id),
  evidence_intake_id TEXT REFERENCES evidence_research_intake_queue(evidence_intake_id),
  evidence_source_id TEXT REFERENCES evidence_external_source(evidence_source_id),
  evidence_witness_ref_id TEXT REFERENCES evidence_manuscript_witness_ref(evidence_witness_ref_id),
  evidence_question_id TEXT REFERENCES evidence_textual_question_ref(evidence_question_id),
  evidence_discovery_event_id TEXT REFERENCES evidence_discovery_event(evidence_discovery_event_id),
  evidence_claim_id TEXT REFERENCES evidence_claim_candidate(evidence_claim_id),
  checkpoint_type TEXT NOT NULL CHECK (
    checkpoint_type IN (
      'artifact_copying_or_composition_range',
      'modern_discovery',
      'acquisition_or_holding',
      'cataloging_or_publication',
      'digitization_or_public_access',
      'redating_or_method_update',
      'scholarly_debate_state',
      'apologetic_claim_boundary'
    )
  ),
  knowledge_scope TEXT NOT NULL CHECK (
    knowledge_scope IN (
      'source_community',
      'holding_institution',
      'scholarly_publication',
      'public_digital_access',
      'project_internal_review',
      'unknown'
    )
  ),
  knowledge_claim_status TEXT NOT NULL CHECK (
    knowledge_claim_status IN (
      'confirmed_source_metadata',
      'candidate_claim',
      'mixed_requires_split',
      'unknown_requires_review'
    )
  ),
  artifact_date_start INTEGER,
  artifact_date_end INTEGER,
  modern_event_date_start INTEGER,
  modern_event_date_end INTEGER,
  date_precision TEXT NOT NULL DEFAULT 'unknown' CHECK (
    date_precision IN (
      'exact_year',
      'year_range',
      'century_range',
      'unknown',
      'not_applicable'
    )
  ),
  date_basis TEXT NOT NULL,
  known_state_summary TEXT NOT NULL,
  confirmed_fact_summary TEXT NOT NULL DEFAULT 'none_reviewed',
  candidate_claim_summary TEXT NOT NULL DEFAULT 'none',
  separates_artifact_date_from_discovery_date INTEGER NOT NULL DEFAULT 1 CHECK (separates_artifact_date_from_discovery_date = 1),
  stores_source_text INTEGER NOT NULL DEFAULT 0 CHECK (stores_source_text = 0),
  stores_scripture_text INTEGER NOT NULL DEFAULT 0 CHECK (stores_scripture_text = 0),
  stores_transcription_text INTEGER NOT NULL DEFAULT 0 CHECK (stores_transcription_text = 0),
  source_basis TEXT NOT NULL,
  method_note TEXT NOT NULL,
  confidence_level TEXT NOT NULL DEFAULT 'unknown',
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE evidence_claim_source_link (
  evidence_claim_source_link_id TEXT PRIMARY KEY,
  evidence_claim_id TEXT NOT NULL REFERENCES evidence_claim_candidate(evidence_claim_id),
  evidence_source_id TEXT REFERENCES evidence_external_source(evidence_source_id),
  evidence_witness_ref_id TEXT REFERENCES evidence_manuscript_witness_ref(evidence_witness_ref_id),
  boundary_citation_id TEXT REFERENCES boundary_patristic_citation_candidate(boundary_citation_id),
  support_role TEXT NOT NULL CHECK (
    support_role IN (
      'primary_support',
      'background_context',
      'counterpoint',
      'dating_support',
      'catalog_support',
      'requires_review'
    )
  ),
  provenance_note TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE evidence_review_event (
  evidence_review_event_id TEXT PRIMARY KEY,
  reviewed_object_type TEXT NOT NULL,
  reviewed_object_id TEXT NOT NULL,
  reviewer_role TEXT NOT NULL,
  review_decision TEXT NOT NULL CHECK (
    review_decision IN (
      'keep_candidate',
      'promote_to_proposed',
      'promote_to_reviewed',
      'reject',
      'needs_source_review',
      'needs_expert_language_review',
      'needs_textual_criticism_review'
    )
  ),
  review_note TEXT NOT NULL,
  reviewed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE evidence_anti_guessing_audit (
  evidence_audit_id TEXT PRIMARY KEY,
  audited_object_type TEXT NOT NULL,
  audited_object_id TEXT NOT NULL,
  has_source_basis INTEGER NOT NULL CHECK (has_source_basis IN (0, 1)),
  has_scope INTEGER NOT NULL CHECK (has_scope IN (0, 1)),
  has_method INTEGER NOT NULL CHECK (has_method IN (0, 1)),
  has_confidence INTEGER NOT NULL CHECK (has_confidence IN (0, 1)),
  has_provenance INTEGER NOT NULL CHECK (has_provenance IN (0, 1)),
  has_review_status INTEGER NOT NULL CHECK (has_review_status IN (0, 1)),
  may_promote INTEGER NOT NULL DEFAULT 0 CHECK (may_promote IN (0, 1)),
  audit_note TEXT NOT NULL,
  audited_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
