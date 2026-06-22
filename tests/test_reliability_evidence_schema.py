from __future__ import annotations

import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "reliability_evidence.sqlite.schema.sql"
PLAN = ROOT / "schemas" / "reliability_evidence_database_plan.md"
SOURCE_SPINE = ROOT / "schemas" / "reliability_evidence_source_spine.md"
INTAKE_QUEUE = ROOT / "schemas" / "reliability_evidence_intake_queue.md"
METHOD_PROFILES = ROOT / "schemas" / "reliability_evidence_method_profiles.md"
TIMELINE_CHECKPOINTS = ROOT / "schemas" / "reliability_evidence_timeline_checkpoints.md"
FIXTURE = ROOT / "tests" / "fixtures" / "reliability_evidence_example_seed.sql"


def load_schema() -> str:
    return SCHEMA.read_text(encoding="utf-8")


def schema_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.executescript(load_schema())
    return conn


def fixture_connection() -> sqlite3.Connection:
    conn = schema_connection()
    conn.executescript(FIXTURE.read_text(encoding="utf-8"))
    return conn


def table_names(conn: sqlite3.Connection) -> set[str]:
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
    ).fetchall()
    return {row[0] for row in rows}


def column_names(conn: sqlite3.Connection, table: str) -> set[str]:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return {row[1] for row in rows}


def primary_key_columns(conn: sqlite3.Connection, table: str) -> list[str]:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return [row[1] for row in rows if row[5]]


def test_reliability_schema_executes_as_sqlite() -> None:
    conn = schema_connection()
    assert "evidence_project" in table_names(conn)


def test_reliability_schema_uses_only_boundary_or_evidence_tables() -> None:
    conn = schema_connection()
    tables = table_names(conn)
    assert tables
    assert all(name.startswith(("boundary_", "evidence_")) for name in tables)
    assert not any(name.startswith("canonical_") for name in tables)
    assert not any(name.startswith("scripture_") for name in tables)
    assert not any(name.startswith("doctrine_") for name in tables)


def test_reliability_schema_does_not_store_source_text_or_scripture_text() -> None:
    sql = load_schema().lower()
    forbidden_tokens = [
        "canonical_text",
        "scripture_text_body",
        "source_text_body",
        "full_text_body",
        "manuscript_transcription_text",
        "commentary_text",
        "patristic_text",
        "theologian_text",
    ]
    for token in forbidden_tokens:
        assert token not in sql

    conn = schema_connection()
    for table in table_names(conn):
        columns = column_names(conn, table)
        assert "scripture_text" not in columns
        assert "source_text" not in columns
        assert "canonical_text" not in columns


def test_reliability_schema_requires_anti_guessing_fields() -> None:
    conn = schema_connection()
    for table in [
        "evidence_method_profile",
        "evidence_intake_method_requirement",
        "evidence_research_intake_queue",
        "evidence_timeline_checkpoint",
        "evidence_manuscript_witness_ref",
        "evidence_textual_question_ref",
        "evidence_claim_candidate",
        "boundary_patristic_citation_candidate",
    ]:
        columns = column_names(conn, table)
        assert "source_basis" in columns
        assert "confidence_level" in columns
        assert "provenance_note" in columns
        assert "review_status" in columns

    audit_columns = column_names(conn, "evidence_anti_guessing_audit")
    assert {
        "has_source_basis",
        "has_scope",
        "has_method",
        "has_confidence",
        "has_provenance",
        "has_review_status",
        "may_promote",
    }.issubset(audit_columns)


def test_reliability_schema_has_source_intake_queue_guardrails() -> None:
    conn = schema_connection()
    columns = column_names(conn, "evidence_research_intake_queue")
    assert {
        "evidence_lane",
        "evidence_method_profile_id",
        "source_locator",
        "proposed_target_repo",
        "proposed_record_namespace",
        "intake_claim_status",
        "confirmed_fact_summary",
        "candidate_claim_summary",
        "stores_source_text",
        "stores_scripture_text",
        "stores_transcription_text",
        "requires_license_review",
        "requires_expert_review",
        "source_basis",
        "method_note",
        "confidence_level",
        "provenance_note",
        "review_status",
    }.issubset(columns)

    sql = load_schema()
    for lane in [
        "dead_sea_scrolls_ot_witness",
        "nt_papyri_codices",
        "textual_variants_copy_abundance",
        "early_creed_oral_tradition",
        "patristic_reception_reconstruction",
        "discovery_timeline",
        "method_bibliography",
    ]:
        assert lane in sql

    assert "'scripture_*'" in sql
    assert "'boundary_*'" in sql
    assert "'evidence_*'" in sql
    assert "'canonical_*'" not in sql


def test_reliability_schema_has_method_profile_guardrails() -> None:
    conn = schema_connection()
    columns = column_names(conn, "evidence_method_profile")
    assert {
        "method_scope",
        "method_title",
        "source_locator",
        "source_kind",
        "governs_evidence_lane",
        "requires_source_language_review",
        "requires_dating_review",
        "requires_material_review",
        "requires_citation_mode_review",
        "requires_variant_method_review",
        "requires_discovery_context_review",
        "prohibits_ai_promotion",
        "source_basis",
        "method_note",
        "confidence_level",
        "provenance_note",
        "review_status",
    }.issubset(columns)

    sql = load_schema()
    for method_scope in [
        "source_catalog_metadata_review",
        "palaeographic_dating_review",
        "material_and_image_review",
        "textual_variant_method_review",
        "patristic_citation_mode_review",
        "early_creed_tradition_review",
        "discovery_timeline_review",
        "source_language_expertise_review",
    ]:
        assert method_scope in sql

    assert "prohibits_ai_promotion INTEGER NOT NULL DEFAULT 1" in sql


def test_reliability_schema_has_method_requirement_guardrails() -> None:
    conn = schema_connection()
    columns = column_names(conn, "evidence_intake_method_requirement")
    assert {
        "evidence_intake_id",
        "evidence_method_profile_id",
        "requirement_role",
        "required_before_status",
        "satisfied",
        "source_basis",
        "method_note",
        "confidence_level",
        "provenance_note",
        "review_status",
    }.issubset(columns)

    sql = load_schema()
    for role in [
        "primary_method",
        "additional_review",
        "blocking_review",
        "source_access_review",
        "language_review",
        "dating_review",
        "citation_mode_review",
        "discovery_context_review",
    ]:
        assert role in sql
    assert "satisfied INTEGER NOT NULL DEFAULT 0 CHECK (satisfied = 0)" in sql


def test_reliability_schema_has_timeline_checkpoint_guardrails() -> None:
    conn = schema_connection()
    columns = column_names(conn, "evidence_timeline_checkpoint")
    assert {
        "checkpoint_type",
        "knowledge_scope",
        "knowledge_claim_status",
        "artifact_date_start",
        "artifact_date_end",
        "modern_event_date_start",
        "modern_event_date_end",
        "date_precision",
        "date_basis",
        "known_state_summary",
        "confirmed_fact_summary",
        "candidate_claim_summary",
        "separates_artifact_date_from_discovery_date",
        "stores_source_text",
        "stores_scripture_text",
        "stores_transcription_text",
        "source_basis",
        "method_note",
        "confidence_level",
        "provenance_note",
        "review_status",
    }.issubset(columns)

    sql = load_schema()
    for checkpoint_type in [
        "artifact_copying_or_composition_range",
        "modern_discovery",
        "acquisition_or_holding",
        "cataloging_or_publication",
        "digitization_or_public_access",
        "redating_or_method_update",
        "scholarly_debate_state",
        "apologetic_claim_boundary",
    ]:
        assert checkpoint_type in sql
    assert "separates_artifact_date_from_discovery_date INTEGER NOT NULL DEFAULT 1" in sql


def test_reliability_plan_declares_repo_placement_and_source_spine() -> None:
    text = PLAN.read_text(encoding="utf-8")
    assert "This scaffold starts in `logos-boundary-literature`" in text
    assert "canonical Scripture text, chunks, passage IDs, manuscript witnesses" in text
    assert "`logos-scripture-graph`" in text
    assert "Never create a `canonical_*` table or view" in text
    assert "Initial Source Spine" in text
    assert "New Testament Virtual Manuscript Room" in text
    assert "BiblIndex" in text


def test_reliability_source_spine_separates_confirmed_and_candidate_claims() -> None:
    text = SOURCE_SPINE.read_text(encoding="utf-8")
    assert "Confirmed From Source" in text
    assert "Candidate Claims Not Yet Asserted" in text
    assert "Leon Levy Dead Sea Scrolls Digital Library" in text
    assert "New Testament Virtual Manuscript Room" in text
    assert "Codex Sinaiticus" in text
    assert "Manchester Digital Collections: Greek P 457" in text
    assert "BiblIndex" in text
    assert "Patristic Citation Caution" in text
    assert "No source-spine entry may become a reviewed row merely because a model found it" in text


def test_reliability_intake_queue_plan_declares_lanes_and_stop_rules() -> None:
    text = INTAKE_QUEUE.read_text(encoding="utf-8")
    assert "pre-evidence holding area" in text
    assert "`dead_sea_scrolls_ot_witness`" in text
    assert "`nt_papyri_codices`" in text
    assert "`textual_variants_copy_abundance`" in text
    assert "`early_creed_oral_tradition`" in text
    assert "`patristic_reception_reconstruction`" in text
    assert "`discovery_timeline`" in text
    assert "`method_bibliography`" in text
    assert "Confirmed Metadata Vs Candidate Claims" in text
    assert "No \"within months\" dating claim may be promoted" in text
    assert "store Scripture text, manuscript transcription text" in text
    assert "https://www.deadseascrolls.org.il/" in text
    assert "https://www.uni-muenster.de/INTF/en/" in text
    assert "https://manuscripts.csntm.org/manuscript/View/GA_P52" in text


def test_reliability_method_profiles_plan_declares_review_methods() -> None:
    text = METHOD_PROFILES.read_text(encoding="utf-8")
    assert "Method profiles describe how a future evidence claim must be reviewed" in text
    assert "`source_catalog_metadata_review`" in text
    assert "`palaeographic_dating_review`" in text
    assert "`textual_variant_method_review`" in text
    assert "`patristic_citation_mode_review`" in text
    assert "`early_creed_tradition_review`" in text
    assert "`discovery_timeline_review`" in text
    assert "`source_language_expertise_review`" in text
    assert "For this project, the default answer to AI promotion is always no" in text
    assert "An intake item may require several method profiles" in text
    assert "https://www.uni-muenster.de/INTF/en/" in text
    assert "https://www.digitalcollections.manchester.ac.uk/view/MS-GREEK-P-00457" in text


def test_reliability_timeline_checkpoints_plan_declares_date_separation() -> None:
    text = TIMELINE_CHECKPOINTS.read_text(encoding="utf-8")
    assert "Timeline checkpoints model what was known, by whom, and when" in text
    assert "`artifact_copying_or_composition_range`" in text
    assert "`modern_discovery`" in text
    assert "`digitization_or_public_access`" in text
    assert "`redating_or_method_update`" in text
    assert "`scholarly_debate_state`" in text
    assert "`apologetic_claim_boundary`" in text
    assert "Do not confuse artifact/copied-text date with modern discovery date" in text
    assert "Confirmed Source Metadata To Check" in text
    assert "Candidate Claims To Keep Unreviewed" in text
    assert "https://www.imj.org.il/en/wings/shrine-book/dead-sea-scrolls" in text
    assert "https://www.codexsinaiticus.org/en/project/" in text


def test_reliability_fixture_loads_as_example_only_metadata() -> None:
    conn = fixture_connection()
    tables = table_names(conn)
    assert tables
    assert all(name.startswith(("boundary_", "evidence_")) for name in tables)

    for table in tables:
        for column in primary_key_columns(conn, table):
            rows = conn.execute(f"SELECT {column} FROM {table}").fetchall()
            assert rows, f"{table} has no fixture rows"
            assert all(row[0].startswith("example_") for row in rows)


def test_reliability_fixture_keeps_text_storage_disabled() -> None:
    conn = fixture_connection()
    fixture_sql = FIXTURE.read_text(encoding="utf-8").lower()
    forbidden_tokens = [
        "canonical_text",
        "scripture_text_body",
        "source_text_body",
        "full_text_body",
        "manuscript_transcription_text",
        "commentary_text",
        "patristic_text",
        "theologian_text",
    ]
    for token in forbidden_tokens:
        assert token not in fixture_sql

    assert conn.execute(
        "SELECT may_store_full_text, may_store_scripture_text FROM boundary_source_access"
    ).fetchall() == [(0, 0)]
    assert set(
        conn.execute(
            """
            SELECT stores_source_text, stores_scripture_text, stores_transcription_text
            FROM evidence_research_intake_queue
            """
        ).fetchall()
    ) == {(0, 0, 0)}
    assert set(
        conn.execute(
            """
            SELECT stores_source_text, stores_scripture_text, stores_transcription_text
            FROM evidence_timeline_checkpoint
            """
        ).fetchall()
    ) == {(0, 0, 0)}
    assert conn.execute(
        "SELECT citation_text_stored FROM boundary_patristic_citation_candidate"
    ).fetchall() == [(0,)]
    assert conn.execute(
        "SELECT stores_scripture_text FROM evidence_scripture_reference"
    ).fetchall() == [(0,)]
    assert conn.execute(
        "SELECT stores_transcription_text FROM evidence_manuscript_witness_ref"
    ).fetchall() == [(0,)]
    assert conn.execute(
        "SELECT no_reading_text_stored FROM evidence_textual_question_ref"
    ).fetchall() == [(1,)]


def test_reliability_fixture_claims_cannot_promote_or_transfer_authority() -> None:
    conn = fixture_connection()

    assert conn.execute(
        "SELECT derived_artifact, canonical_authority_transferred FROM evidence_project"
    ).fetchall() == [(1, 0)]
    assert conn.execute(
        "SELECT claim_status, review_status FROM evidence_claim_candidate"
    ).fetchall() == [("candidate", "unreviewed")]
    assert conn.execute(
        "SELECT review_decision FROM evidence_review_event"
    ).fetchall() == [("keep_candidate",)]
    assert conn.execute(
        "SELECT may_promote FROM evidence_anti_guessing_audit"
    ).fetchall() == [(0,)]
    assert set(
        conn.execute(
            "SELECT prohibits_ai_promotion, review_status FROM evidence_method_profile"
        ).fetchall()
    ) == {(1, "unreviewed")}
    assert set(
        conn.execute(
            "SELECT satisfied, review_status FROM evidence_intake_method_requirement"
        ).fetchall()
    ) == {(0, "unreviewed")}
    assert set(
        conn.execute(
            """
            SELECT separates_artifact_date_from_discovery_date, review_status
            FROM evidence_timeline_checkpoint
            """
        ).fetchall()
    ) == {(1, "unreviewed")}


def test_reliability_fixture_intake_queue_covers_all_lanes_without_promotion() -> None:
    conn = fixture_connection()
    lanes = {
        row[0]
        for row in conn.execute(
            "SELECT evidence_lane FROM evidence_research_intake_queue"
        ).fetchall()
    }
    assert lanes == {
        "dead_sea_scrolls_ot_witness",
        "nt_papyri_codices",
        "textual_variants_copy_abundance",
        "early_creed_oral_tradition",
        "patristic_reception_reconstruction",
        "discovery_timeline",
        "method_bibliography",
    }

    rows = conn.execute(
        """
        SELECT proposed_target_repo, proposed_record_namespace, intake_claim_status, review_status
        FROM evidence_research_intake_queue
        """
    ).fetchall()
    assert all(row[3] == "unreviewed" for row in rows)
    assert any(row[0] == "logos-scripture-graph" and row[1] == "scripture_*" for row in rows)
    assert any(row[1] == "boundary_*" for row in rows)
    assert any(row[2] == "candidate_claim" for row in rows)
    assert any(row[2] == "mixed_requires_split" for row in rows)


def test_reliability_fixture_method_profiles_cover_review_needs() -> None:
    conn = fixture_connection()
    method_scopes = {
        row[0]
        for row in conn.execute("SELECT method_scope FROM evidence_method_profile").fetchall()
    }
    assert method_scopes == {
        "source_catalog_metadata_review",
        "palaeographic_dating_review",
        "material_and_image_review",
        "textual_variant_method_review",
        "patristic_citation_mode_review",
        "early_creed_tradition_review",
        "discovery_timeline_review",
        "source_language_expertise_review",
    }

    assert conn.execute(
        """
        SELECT COUNT(*)
        FROM evidence_research_intake_queue
        WHERE evidence_method_profile_id IS NULL
        """
    ).fetchone() == (0,)
    assert conn.execute(
        """
        SELECT COUNT(*)
        FROM evidence_method_profile
        WHERE requires_source_language_review = 1
        """
    ).fetchone()[0] >= 4
    assert conn.execute(
        """
        SELECT COUNT(*)
        FROM evidence_method_profile
        WHERE requires_citation_mode_review = 1
        """
    ).fetchone()[0] == 1
    assert conn.execute(
        """
        SELECT COUNT(*)
        FROM evidence_method_profile
        WHERE requires_discovery_context_review = 1
        """
    ).fetchone()[0] == 1
    assert conn.execute(
        """
        SELECT COUNT(DISTINCT evidence_intake_id)
        FROM evidence_intake_method_requirement
        """
    ).fetchone()[0] == 7
    assert conn.execute(
        """
        SELECT COUNT(*)
        FROM evidence_intake_method_requirement
        WHERE requirement_role = 'language_review'
        """
    ).fetchone()[0] >= 3


def test_reliability_fixture_timeline_checkpoints_cover_knowledge_states() -> None:
    conn = fixture_connection()
    checkpoint_types = {
        row[0]
        for row in conn.execute(
            "SELECT checkpoint_type FROM evidence_timeline_checkpoint"
        ).fetchall()
    }
    assert checkpoint_types == {
        "artifact_copying_or_composition_range",
        "modern_discovery",
        "cataloging_or_publication",
        "digitization_or_public_access",
        "redating_or_method_update",
        "scholarly_debate_state",
        "apologetic_claim_boundary",
    }

    rows = conn.execute(
        """
        SELECT knowledge_claim_status, date_precision, review_status
        FROM evidence_timeline_checkpoint
        """
    ).fetchall()
    assert all(row[2] == "unreviewed" for row in rows)
    assert any(row[0] == "confirmed_source_metadata" for row in rows)
    assert any(row[0] == "candidate_claim" for row in rows)
    assert any(row[0] == "mixed_requires_split" for row in rows)
    assert set(row[1] for row in rows) == {"unknown"}
