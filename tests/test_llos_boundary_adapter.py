from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from scripts import validate_llos_boundary_adapter as validator


ROOT = Path(__file__).resolve().parents[1]


def test_dad_repo_write_policy_is_fail_closed_without_standing_approval() -> None:
    policy = json.loads((ROOT / ".digital-asset/dad-write-policy.json").read_text(encoding="utf-8"))
    assert policy["dad_write_allowed"] is False
    assert policy["approved_explicit_approval_ids"] == []
    assert policy["logos_local_outbox_write_allowed"] is True
    assert policy["logos_local_dad_central_read_allowed"] is True
    assert policy["dad_push_or_inbox_write_allowed"] is False
    assert policy["rollout_approval_is_standing_write_permission"] is False


def test_llos_boundary_adapter_validates() -> None:
    assert validator.validate(ROOT) == []


def test_empty_lesson_bootstrap_and_dad_write_denial_are_explicit() -> None:
    adapter = validator._load_yaml(ROOT, validator.ADAPTER_PATH)
    index = validator._load_yaml(ROOT, validator.INDEX_PATH)

    assert index["lessons"] == []
    assert adapter["authority"]["authorizes_source_import"] is False
    assert adapter["authority"]["authorizes_canonical_authority"] is False
    assert adapter["authority"]["authorizes_runtime_ingestion"] is False
    assert adapter["authority"]["authorizes_cross_repo_override"] is False
    assert adapter["dad_bridge"]["logos_local_may_write_own_outbox"] is True
    assert adapter["dad_bridge"]["logos_local_may_read_dad_central_candidates"] is True
    assert adapter["dad_bridge"]["dad_may_read_approved_repo_outbox"] is True
    assert adapter["dad_bridge"]["dad_may_write_central_dad_records"] is True
    assert adapter["dad_bridge"]["dad_may_write_inside_logos_repo"] is False
    assert adapter["dad_bridge"]["dad_may_deliver_to_logos_inbox"] is False
    assert adapter["dad_bridge"]["approval_required_for_every_future_logos_write"] is True
    assert adapter["dad_bridge"]["approval_must_be_fresh_and_explicit"] is True


def test_llos_boundary_adapter_command_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_llos_boundary_adapter.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Boundary W2-8 LLOS adapter validation passed." in result.stdout
