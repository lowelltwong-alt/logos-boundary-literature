from __future__ import annotations

import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "reliability_evidence.sqlite.schema.sql"
PLAN = ROOT / "schemas" / "reliability_evidence_database_plan.md"
SOURCE_SPINE = ROOT / "schemas" / "reliability_evidence_source_spine.md"
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
