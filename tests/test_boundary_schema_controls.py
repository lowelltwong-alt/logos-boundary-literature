from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_boundary_schema_controls import (  # noqa: E402
    TRUST_LEVELS,
    find_contamination_warnings,
    load_schemas,
    validate_trust_level_vocabulary,
)


def test_boundary_schema_controls_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_boundary_schema_controls.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Boundary schema controls validation passed." in result.stdout


def test_four_json_schemas_are_draft_2020_12_valid() -> None:
    schemas = load_schemas()
    assert set(schemas) == {"work", "source_status", "trust_profile", "boundary_claim"}


def test_trust_level_vocabulary_is_closed_across_schema_and_docs() -> None:
    schemas = load_schemas()
    validate_trust_level_vocabulary(schemas)

    work_levels = schemas["work"]["properties"]["trust_level"]["enum"]
    profile_levels = schemas["trust_profile"]["properties"]["trust_level"]["enum"]
    assert tuple(work_levels) == TRUST_LEVELS
    assert tuple(profile_levels) == TRUST_LEVELS


def test_contamination_lint_flags_verse_length_quoted_text_without_failing(tmp_path: Path) -> None:
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    data_file = data_dir / "sample.json"
    data_file.write_text(
        '{"quote": "'
        "These words are intentionally long enough to look like a copied passage rather than a "
        "metadata summary, and the warning should help future agents stop before storing source "
        "or Scripture text in the boundary repository"
        '"}',
        encoding="utf-8",
    )

    warnings = find_contamination_warnings((data_dir,))
    assert len(warnings) == 1
    assert warnings[0].path == data_file
    assert warnings[0].word_count >= 25
