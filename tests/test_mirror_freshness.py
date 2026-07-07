from __future__ import annotations

import shutil
from pathlib import Path

from scripts import validate_mirror_freshness as validator


ROOT = Path(__file__).resolve().parents[1]


def copy_repo(tmp_path: Path) -> Path:
    target = tmp_path / "repo"
    shutil.copytree(
        ROOT,
        target,
        ignore=shutil.ignore_patterns(".git", ".pytest_cache", "__pycache__"),
    )
    return target


def seed_source_repo(child_repo: Path) -> Path:
    source_root = child_repo.parent / "logos-governance-architecture"
    for rel in validator.REQUIRED_UPSTREAM_PATHS:
        target = source_root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("fixture\n", encoding="utf-8")
    return source_root


def test_mirror_freshness_passes() -> None:
    assert validator.validate(ROOT) == []


def test_mirror_freshness_can_require_local_source(tmp_path: Path) -> None:
    repo = copy_repo(tmp_path)

    errors = validator.validate(repo, require_local_source=True)

    assert any("local source repo missing" in error for error in errors)


def test_mirror_freshness_fails_when_upstream_control_missing(tmp_path: Path) -> None:
    repo = copy_repo(tmp_path)
    source_root = seed_source_repo(repo)
    (source_root / "governance/CROSS_REPO_REFERENCE_MANIFEST.yaml").unlink()

    errors = validator.validate(repo)

    assert any("missing upstream governance control" in error for error in errors)


def test_mirror_freshness_fails_when_token_missing(tmp_path: Path) -> None:
    repo = copy_repo(tmp_path)
    mirror = repo / ".ai/control/governance_dependency_map_mirror.yaml"
    mirror.write_text(
        mirror.read_text(encoding="utf-8").replace("  staleness_budget_days: 14\n", ""),
        encoding="utf-8",
    )

    errors = validator.validate(repo)

    assert any("staleness_budget_days" in error for error in errors)
