from __future__ import annotations

import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "reliability_evidence.sqlite.schema.sql"
PLAN = ROOT / "schemas" / "reliability_evidence_database_plan.md"
SOURCE_SPINE = ROOT / "schemas" / "reliability_evidence_source_spine.md"


def load_schema() -> str:
    return SCHEMA.read_text(encoding="utf-8")


def schema_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.executescript(load_schema())
    return conn


def table_names(conn: sqlite3.Connection) -> set[str]:
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
    ).fetchall()
    return {row[0] for row in rows}


def column_names(conn: sqlite3.Connection, table: str) -> set[str]:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return {row[1] for row in rows}


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
