from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / ".ai" / "control" / "boundary_material_routing.yaml"
FRONT_DOOR = ROOT / "AI_FRONT_DOOR.md"
CONTRACT = ROOT / "governance" / "CROSS_REPO_CONTRACT_WITH_LOGOS_SCRIPTURE_GRAPH.md"
GUARDRAILS = ROOT / "governance" / "THREE_REPO_ROUTING_GUARDRAILS.md"
DATA_DIR = ROOT / "data"


def load_policy() -> dict:
    return yaml.safe_load(POLICY.read_text(encoding="utf-8"))


def test_boundary_policy_records_authority_hierarchy() -> None:
    data = load_policy()
    assert data["routing_policy_id"] == "BOUNDARY-MATERIAL-ROUTING-v1"
    assert data["owner_repo"] == "logos-boundary-literature"
    assert data["canonical_authority_repo"] == "logos-scripture-graph"
    assert data["governance_authority_repo"] == "logos-governance-architecture"
    assert data["authority_hierarchy"]["boundary_repo_can_override_scripture"] is False
    assert data["authority_hierarchy"]["boundary_repo_can_equal_scripture_authority"] is False
    assert data["canonical_scope"]["canonical_claims_owned_here"] is False


def test_boundary_policy_routes_scripture_and_governance_work_away() -> None:
    data = load_policy()
    assert "canonical_66_scripture_passages" in data["route_to_scripture_graph"]
    assert "canonical_scripture_chunks" in data["route_to_scripture_graph"]
    assert "cross_repo_authority_policy" in data["route_to_governance_repo"]
    assert "repository_link_contracts" in data["route_to_governance_repo"]
    assert "boundary_claims_overriding_scripture" in data["forbidden_in_boundary_repo"]
    assert "theologian_or_commentary_claims_as_scripture_authority" in data["forbidden_in_boundary_repo"]
    assert "scripture_references_without_scripture_text" in data["allowed_in_boundary_repo"]
    assert "church_father_citation_metadata" in data["allowed_in_boundary_repo"]
    assert "theologian_writing_source_metadata" in data["allowed_in_boundary_repo"]
    assert set(data["boundary_claims_require_scope"]) == {
        "trust_level",
        "tradition_scope",
        "profile_scope",
        "provenance",
    }


def test_front_door_and_contract_state_stop_rule() -> None:
    text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [FRONT_DOOR, CONTRACT, GUARDRAILS]
    )
    assert "logos-governance-architecture" in text
    assert "logos-scripture-graph" in text
    assert "hierarchically under, or at minimum never above" in text
    assert "must not override, contaminate, or become equal authority" in text
    assert "stop and report" in text
    assert "Church-father citations/patristic reception" in text
    assert "Denominational/theological development over time" in text


def test_unified_evidence_namespace_controls_are_boundary_scoped() -> None:
    data = load_policy()
    guardrails = data["data_flow_guardrails"]
    assert guardrails["scripture_text_stored_here"] is False
    assert guardrails["unified_evidence_products_are_derived_artifacts"] is True
    assert guardrails["canonical_tables_may_include_boundary_data"] is False
    assert guardrails["canonical_tables_may_include_commentary_data"] is False
    assert guardrails["canonical_tables_may_include_patristic_data"] is False
    assert guardrails["canonical_tables_may_include_theologian_data"] is False
    assert guardrails["canonical_tables_may_include_denominational_profile_data"] is False
    assert set(guardrails["derived_database_allowed_prefixes"]) == {"boundary_", "evidence_"}


def test_no_text_corpus_was_imported() -> None:
    files = [
        path
        for path in DATA_DIR.rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    ]
    assert files == []
