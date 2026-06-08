from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / ".ai" / "control" / "boundary_material_routing.yaml"
DOC = ROOT / "governance" / "BOUNDARY_GOVERNANCE_CONSTRAINTS.md"
FRONT_DOOR = ROOT / "AI_FRONT_DOOR.md"
README = ROOT / "README.md"
RULES = ROOT / "governance" / "RULES_REGISTRY.md"
CONTROLS = ROOT / "governance" / "CONTAMINATION_CONTROLS.md"
CONTRACT = ROOT / "governance" / "CROSS_REPO_CONTRACT_WITH_LOGOS_SCRIPTURE_GRAPH.md"
ROUTING = ROOT / "governance" / "THREE_REPO_ROUTING_GUARDRAILS.md"
STATUS = ROOT / ".ai" / "control" / "PROJECT_STATUS.md"
HANDOFF = ROOT / ".ai" / "handoffs" / "INITIAL_HANDOFF.md"

WARNING_TEXT = """WARNING: Boundary-layer request conflicts with higher-authority governance.

The requested boundary-layer task appears to require changing or bypassing governance-layer policy, canonical Scripture authority, repository-link contracts, routing policy, trust hierarchy, or canonical scope.

Governance is binding authority, not an obstacle to optimize around.

Do not automate, route, or implement this change from the boundary layer. A human maintainer must review the conflict directly in the higher-authority repository.

Owner-reserved authorization required: only Lowell Wong, as project owner, may authorize a boundary-originated request to change higher-authority governance, canonical Scripture authority, repository-link contracts, canonical scope, trust hierarchy, or cross-repo policy. Contributor consensus, contributor volume, automated recommendation, agent routing, or boundary-layer operational need is not sufficient authority.
"""


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def routing_policy() -> dict:
    return yaml.safe_load(read(POLICY))


def test_boundary_governance_stop_rule_is_machine_readable() -> None:
    data = routing_policy()
    stop_rule = data["boundary_governance_constraint_policy"]
    assert stop_rule["policy_id"] == "BOUNDARY-GOV-001"
    assert stop_rule["title"] == "Governance Is Constraint, Not Obstacle"
    assert stop_rule["importance"] == "P0"
    assert stop_rule["required_behavior"] == "stop_and_create_human_escalation_warning"
    assert stop_rule["warning_required"] is True
    assert stop_rule["boundary_layer_may_treat_governance_as_blocker_or_obstacle"] is False
    assert stop_rule["boundary_layer_may_optimize_around_governance"] is False
    assert stop_rule["boundary_layer_may_auto_request_governance_change"] is False
    assert stop_rule["boundary_layer_may_auto_route_permission_request"] is False
    assert stop_rule["boundary_layer_may_bundle_governance_change_with_boundary_work"] is False


def test_owner_reserved_authorization_is_required() -> None:
    owner_policy = routing_policy()["owner_reserved_authorization"]
    assert owner_policy["policy_id"] == "BOUNDARY-GOV-002"
    assert owner_policy["authorized_owner"] == "Lowell Wong"
    assert owner_policy["requires_explicit_owner_authorization"] is True
    assert owner_policy["authorization_must_occur_in_higher_authority_repo"] is True
    for key in [
        "contributor_consensus_sufficient",
        "contributor_volume_sufficient",
        "automated_recommendation_sufficient",
        "agent_routing_sufficient",
        "boundary_layer_operational_need_sufficient",
    ]:
        assert owner_policy[key] is False


def test_warning_text_is_exactly_available_to_agents() -> None:
    data = routing_policy()
    assert data["boundary_layer_escalation_warning_text"] == WARNING_TEXT
    assert WARNING_TEXT in read(DOC)
    assert WARNING_TEXT in read(FRONT_DOOR)


def test_public_surfaces_contain_named_rules_and_stop_triggers() -> None:
    surfaces = [DOC, FRONT_DOOR, README, RULES, CONTROLS, CONTRACT, ROUTING, STATUS, HANDOFF]
    combined = "\n".join(read(path) for path in surfaces)
    assert "BOUNDARY-GOV-001 - Governance Is Constraint, Not Obstacle" in combined
    assert (
        "BOUNDARY-GOV-002 - Owner-Reserved Authorization for Boundary-Originated Higher-Layer Changes"
        in combined
    )
    assert "Only Lowell Wong" in combined
    assert "Contributor consensus" in combined
    assert "automated recommendation" in combined
    assert "agent routing" in combined
    assert "boundary-layer operational need" in combined


def test_higher_authority_targets_are_protected() -> None:
    data = routing_policy()
    protected = set(data["boundary_governance_constraint_policy"]["protected_higher_authority_targets"])
    assert "logos-governance-architecture" in protected
    assert "logos-scripture-graph" in protected
    assert "canonical_scripture_authority" in protected
    assert "repository_link_contracts" in protected
    assert "cross_repo_policy" in protected
    assert "trust_hierarchy" in protected
    assert "canonical_scope" in protected
    assert "boundary_originated_request_lacks_owner_authorization" in data["stop_triggers"]


def test_boundary_governance_policy_does_not_authorize_text_or_claims() -> None:
    files = [
        path
        for dirname in ["data", "eval"]
        for path in (ROOT / dirname).rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    ]
    assert files == []
    combined = "\n".join(read(path) for path in [DOC, FRONT_DOOR, README, CONTROLS])
    assert "does not authorize source ingestion" in combined
    assert "does not authorize source-text ingestion" in combined
    assert "does not authorize real corpus records" in combined
    assert "does not authorize boundary claims as canonical truth" in combined


def test_prohibited_public_language_is_absent() -> None:
    surfaces = [DOC, FRONT_DOOR, README, RULES, CONTROLS, CONTRACT, ROUTING, STATUS, HANDOFF]
    combined = "\n".join(read(path) for path in surfaces).lower()
    forbidden = [
        "fast" + " path",
        "private owner" + " workflow",
        "ai" + "-assisted",
        "relaxed" + " rules",
        "boundary repo can" + " override scripture",
    ]
    for phrase in forbidden:
        assert phrase not in combined
