from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_biblical_codex_pointer_registry.py"
SPEC = importlib.util.spec_from_file_location("validate_biblical_codex_pointer_registry", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_boundary_codex_pointer_registry() -> None:
    result = MODULE.validate_registry()
    assert result["status"] == "valid"
    assert result["counts"]["catalog_roots"] >= 10
    assert result["counts"]["direct_witnesses"] >= 8
    assert result["mixed_witness_rows"] == result["counts"]["direct_witnesses"]
