from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / ".ai" / "control" / "contributor_review_policy.yaml"
DOC = ROOT / "governance" / "CONTRIBUTOR_REVIEW_POLICY.md"
FRONT_DOOR = ROOT / "AI_FRONT_DOOR.md"
README = ROOT / "README.md"
RULES = ROOT / "governance" / "RULES_REGISTRY.md"
SOURCE = ROOT / "governance" / "SOURCE_INTAKE_POLICY.md"
CONTROLS = ROOT / "governance" / "CONTAMINATION_CONTROLS.md"
STATUS = ROOT / ".ai" / "control" / "PROJECT_STATUS.md"
HANDOFF = ROOT / ".ai" / "handoffs" / "INITIAL_HANDOFF.md"

PUBLIC_SURFACES = [
    POLICY,
    DOC,
    FRONT_DOOR,
    README,
    RULES,
    SOURCE,
    CONTROLS,
    STATUS,
    HANDOFF,
]

REVIEW_REQUIRED_FOR = {
    "trust_hierarchy",
    "canon_status_policy",
    "source_intake_policy",
    "attribution_forgery_policy",
    "source_text_ingestion",
    "boundary_claim_records",
    "commentary_reception_claims",
    "corpus_records",
    "cross_repo_authority_rules",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def policy() -> dict:
    return yaml.safe_load(read(POLICY))


def test_contributor_review_policy_yaml() -> None:
    data = policy()
    assert data["policy_id"] == "BOUNDARY-CONTRIBUTOR-REVIEW-v1"
    assert data["repo"] == "logos-boundary-literature"
    assert data["status"] == "active_policy"
    assert data["named_rule"]["id"] == "BOUNDARY-CONTRIB-001"
    assert data["named_rule"]["title"] == "External Contributor Review Required"
    assert data["named_rule"]["importance_default"] == "P1"
    assert data["named_rule"]["importance_sensitive"] == "P0"
    assert set(data["external_contributor_review_required_for"]) == REVIEW_REQUIRED_FOR


def test_policy_is_non_authorizing_and_does_not_relax_scripture_graph() -> None:
    data = policy()
    assert "logos-scripture-graph" in data["canonical_repos_not_relaxed"]
    for value in [
        "source_text_import_without_source_review",
        "canonical_scripture_claims",
        "cross_repo_contamination",
        "overriding_scripture",
        "equal_authority_to_scripture",
    ]:
        assert value in data["never_authorized_by_this_policy"]
    for value in [
        "source_text_ingestion",
        "real_corpus_records",
        "boundary_claims_as_canonical_truth",
        "boundary_repo_override_of_scripture",
        "boundary_repo_equal_authority_to_scripture",
    ]:
        assert value in data["does_not_authorize"]


def test_public_docs_contain_required_rule_language() -> None:
    combined = "\n".join(read(path) for path in PUBLIC_SURFACES)
    assert "BOUNDARY-CONTRIB-001 - External Contributor Review Required" in combined
    assert "External contributor changes" in combined
    assert "maintainer review before merge" in combined
    assert "trust hierarchy" in combined
    assert "canon status" in combined
    assert "source intake" in combined
    assert "attribution" in combined
    assert "boundary claim" in combined
    assert "commentary/reception" in combined
    assert "cross-repo authority" in combined


def test_policy_does_not_authorize_text_or_canonical_claims() -> None:
    combined = "\n".join(read(path) for path in [DOC, FRONT_DOOR, README, SOURCE, CONTROLS])
    assert "does not authorize importing source texts" in combined
    assert "does not authorize real corpus records" in combined
    assert "does not authorize boundary claims as canonical truth" in combined
    assert "does not apply to `logos-scripture-graph`" in combined
    assert "does not change its rules" in combined
    assert "does not permit boundary repo material to override or equal Scripture" in combined


def test_prohibited_public_language_is_absent() -> None:
    combined = "\n".join(read(path) for path in PUBLIC_SURFACES).lower()
    forbidden = [
        "fast" + " path",
        "private owner" + " workflow",
        "ai" + "-assisted",
        "relaxed" + " rules",
        "relax `logos-scripture-graph`",
        "relax logos-scripture-graph",
    ]
    for phrase in forbidden:
        assert phrase not in combined


def test_no_text_corpus_or_claim_records_were_added() -> None:
    files = [
        path
        for dirname in ["data", "eval"]
        for path in (ROOT / dirname).rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    ]
    assert files == []
