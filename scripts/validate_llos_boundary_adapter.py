#!/usr/bin/env python3
"""Validate the Boundary W2-8 LLOS v1 adapter and empty lesson-index bootstrap."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = Path("governance/LLOS_STANDARD_MIRROR.yaml")
INDEX_PATH = Path("governance/LLOS_LESSON_INDEX.yaml")
EXPECTED_PIN = "sha256:7870b7fa030a22607c202c061a073b86acff850573efbcefcf87c9532528e57d"
EXPECTED_CATEGORIES = {
    "boundary_intake",
    "reception_context",
    "source_rights",
    "boundary_validation",
}


def _load_yaml(root: Path, relative_path: Path) -> dict[str, Any]:
    path = root / relative_path
    documents = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    if not documents or not all(isinstance(document, dict) for document in documents):
        raise ValueError(f"{relative_path.as_posix()} must be a YAML mapping")
    data: dict[str, Any] = {}
    for document in documents:
        data.update(document)
    return data


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        adapter = _load_yaml(root, ADAPTER_PATH)
        index = _load_yaml(root, INDEX_PATH)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [str(exc)]

    if adapter.get("object_type") != "llos_standard_mirror":
        errors.append("LLOS adapter must identify as llos_standard_mirror")
    if adapter.get("owner_repo") != "logos-boundary-literature":
        errors.append("LLOS adapter owner_repo must be logos-boundary-literature")

    upstream = adapter.get("upstream_standard", {})
    if not isinstance(upstream, dict):
        errors.append("LLOS adapter upstream_standard must be a mapping")
    else:
        expected_upstream = {
            "repo": "logos-governance-architecture",
            "path": "governance/LOGOS_LEARNING_LOOP_OPERATING_STANDARD.yaml",
            "standard_id": "LLOS-v1",
            "surface_version": "1.0.0",
            "content_sha256": EXPECTED_PIN,
            "source_of_truth": True,
        }
        for key, expected in expected_upstream.items():
            if upstream.get(key) != expected:
                errors.append(f"LLOS adapter upstream_standard.{key} must be {expected!r}")

    local_adapter = adapter.get("local_adapter", {})
    if not isinstance(local_adapter, dict):
        errors.append("LLOS adapter local_adapter must be a mapping")
    else:
        if local_adapter.get("route") != "boundary":
            errors.append("LLOS adapter route must be boundary")
        if set(local_adapter.get("allowed_categories", [])) != EXPECTED_CATEGORIES:
            errors.append("LLOS adapter categories must match the governed boundary route")
        if local_adapter.get("lesson_index") != INDEX_PATH.as_posix():
            errors.append("LLOS adapter must reference the local lesson index")
        for key, expected in {
            "validator": "scripts/validate_llos_boundary_adapter.py",
            "test": "tests/test_llos_boundary_adapter.py",
        }.items():
            if local_adapter.get(key) != expected:
                errors.append(f"LLOS adapter local_adapter.{key} must be {expected!r}")

    authority = adapter.get("authority", {})
    if not isinstance(authority, dict):
        errors.append("LLOS adapter authority must be a mapping")
    else:
        for key in (
            "local_repo_may_override_upstream_standard",
            "adapter_is_authority",
            "authorizes_source_import",
            "authorizes_canonical_authority",
            "authorizes_runtime_ingestion",
            "authorizes_cross_repo_override",
            "authorizes_theology_claim",
        ):
            if authority.get(key) is not False:
                errors.append(f"LLOS adapter authority.{key} must be false")
        if authority.get("requires_human_review_for_lesson_admission") is not True:
            errors.append("LLOS adapter requires human review for lesson admission")

    bridge = adapter.get("dad_bridge", {})
    if not isinstance(bridge, dict):
        errors.append("LLOS adapter dad_bridge must be a mapping")
    else:
        for key in (
            "dad_may_write_inside_logos_repo",
            "dad_may_deliver_to_logos_inbox",
            "dad_may_mutate_logos_contract",
            "dad_may_mutate_logos_index",
        ):
            if bridge.get(key) is not False:
                errors.append(f"LLOS adapter dad_bridge.{key} must be false")
        for key in (
            "logos_local_may_write_own_outbox",
            "logos_local_may_read_dad_central_candidates",
            "dad_may_read_approved_metadata",
            "dad_may_read_approved_repo_outbox",
            "dad_may_write_central_dad_records",
            "approval_required_for_every_future_logos_write",
            "approval_must_be_fresh_and_explicit",
            "export_metadata_only",
        ):
            if bridge.get(key) is not True:
                errors.append(f"LLOS adapter dad_bridge.{key} must be true")
        if bridge.get("central_write_root") != "DAD_DATA_ROOT":
            errors.append("LLOS adapter DAD writes may only target DAD_DATA_ROOT")

    if index.get("object_type") != "llos_lesson_index":
        errors.append("LLOS lesson index must identify as llos_lesson_index")
    if index.get("owner_repo") != "logos-boundary-literature":
        errors.append("LLOS lesson index owner_repo must be logos-boundary-literature")
    if index.get("standard_adapter") != ADAPTER_PATH.as_posix():
        errors.append("LLOS lesson index must reference the local standard adapter")
    if index.get("lessons") != []:
        errors.append("LLOS lesson index bootstrap must remain empty")

    index_pin = index.get("upstream_standard_pin", {})
    if not isinstance(index_pin, dict) or index_pin.get("content_sha256") != EXPECTED_PIN:
        errors.append("LLOS lesson index must carry the adapter source pin")
    if isinstance(index_pin, dict):
        if index_pin.get("standard_id") != "LLOS-v1" or index_pin.get("surface_version") != "1.0.0":
            errors.append("LLOS lesson index must carry the LLOS v1 identity")

    index_authority = index.get("authority", {})
    if not isinstance(index_authority, dict):
        errors.append("LLOS lesson index authority must be a mapping")
    else:
        for key in (
            "index_is_authority",
            "authorizes_source_import",
            "authorizes_canonical_authority",
            "authorizes_runtime_ingestion",
            "authorizes_cross_repo_override",
            "authorizes_theology_claim",
        ):
            if index_authority.get(key) is not False:
                errors.append(f"LLOS lesson index authority.{key} must be false")
        if index_authority.get("records_local_lesson_metadata") is not True:
            errors.append("LLOS lesson index may only record local lesson metadata")
        if index_authority.get("requires_human_review_for_admission") is not True:
            errors.append("LLOS lesson index requires human review for admission")

    admission = index.get("admission_policy", {})
    if not isinstance(admission, dict):
        errors.append("LLOS lesson index admission_policy must be a mapping")
    else:
        for key in (
            "candidate_is_authority",
            "ai_may_admit",
            "dad_may_admit",
            "external_import_allowed",
            "raw_source_payload_allowed",
            "theology_claim_allowed",
        ):
            if admission.get(key) is not False:
                errors.append(f"LLOS lesson index admission_policy.{key} must be false")
        if admission.get("local_reauthoring_required") is not True:
            errors.append("LLOS lesson index requires local reauthoring")

    for path, phrases in {
        Path("AI_FRONT_DOOR.md"): [
            "LLOS v1 Local Adapter",
            "governance/LLOS_STANDARD_MIRROR.yaml",
            "new, explicit approval",
        ],
        Path("AI_TABLE_OF_CONTENTS.md"): [
            "governance/LLOS_STANDARD_MIRROR.yaml",
            "governance/LLOS_LESSON_INDEX.yaml",
            "scripts/validate_llos_boundary_adapter.py",
        ],
    }.items():
        try:
            text = (root / path).read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"missing LLOS navigation surface {path.as_posix()}: {exc}")
            continue
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{path.as_posix()} must mention {phrase!r}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print("Boundary W2-8 LLOS adapter validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
