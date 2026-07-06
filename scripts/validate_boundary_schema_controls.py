#!/usr/bin/env python3
"""Validate boundary schema controls and warn on suspected copied source text."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    from jsonschema import Draft202012Validator, exceptions
except ImportError as exc:  # pragma: no cover - exercised only in missing-dependency envs.
    print(
        "Boundary schema controls validation failed: install jsonschema to validate schemas.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schemas"
DATA_DIR = ROOT / "data"
EVAL_DIR = ROOT / "eval"
TRUST_HIERARCHY = ROOT / "governance" / "TRUST_HIERARCHY.md"
README = ROOT / "README.md"

SCHEMA_FILES = {
    "work": SCHEMA_DIR / "work.schema.json",
    "source_status": SCHEMA_DIR / "source_status.schema.json",
    "trust_profile": SCHEMA_DIR / "trust_profile.schema.json",
    "boundary_claim": SCHEMA_DIR / "boundary_claim.schema.json",
}

RECORD_TARGETS = {
    "work": ("data/works/**/*.json", "data/works/*.json"),
    "source_status": ("data/source_statuses/**/*.json", "data/source_statuses/*.json"),
    "trust_profile": ("data/trust_profiles/**/*.json", "data/trust_profiles/*.json"),
    "boundary_claim": ("data/claims/**/*.json", "data/claims/*.json"),
}

TRUST_LEVELS = (
    "canonical_scripture_reference_only",
    "deuterocanonical_tradition_scoped",
    "high_trust_noncanonical_background",
    "historical_context_source",
    "patristic_reception",
    "heterodox_or_gnostic",
    "disputed_attribution",
    "known_forgery_or_fake",
    "quarantine_unreviewed",
)

SCAN_SUFFIXES = {".json", ".jsonl", ".yaml", ".yml", ".md", ".txt", ".sql"}
QUOTED_STRING = re.compile(r"""(?P<quote>["'])(?P<text>(?:\\.|(?!\1)[^"'\n]){120,})(?P=quote)""")
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")
MIN_SUSPECT_WORDS = 25


class BoundarySchemaControlsError(ValueError):
    """Raised when a boundary schema control is invalid."""


@dataclass(frozen=True)
class ContaminationWarning:
    """Warn-level suspected source-text copy finding."""

    path: Path
    line: int
    word_count: int
    excerpt: str


def _rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BoundarySchemaControlsError(f"{_rel(path)} is not valid JSON: {exc}") from exc


def load_schemas() -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for name, path in SCHEMA_FILES.items():
        if not path.exists():
            raise BoundarySchemaControlsError(f"Missing schema file: {_rel(path)}")
        schema = _read_json(path)
        if not isinstance(schema, dict):
            raise BoundarySchemaControlsError(f"{_rel(path)} must be a JSON object")
        try:
            Draft202012Validator.check_schema(schema)
        except exceptions.SchemaError as exc:
            raise BoundarySchemaControlsError(f"{_rel(path)} is not a valid Draft 2020-12 schema: {exc.message}") from exc
        schemas[name] = schema
    return schemas


def _enum_at(schema: dict[str, Any], *keys: str) -> list[str]:
    value: Any = schema
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            raise BoundarySchemaControlsError(f"Missing schema key path: {'.'.join(keys)}")
        value = value[key]
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise BoundarySchemaControlsError(f"Schema key path must be a string enum: {'.'.join(keys)}")
    return value


def validate_trust_level_vocabulary(schemas: dict[str, dict[str, Any]]) -> None:
    expected = list(TRUST_LEVELS)
    work_levels = _enum_at(schemas["work"], "properties", "trust_level", "enum")
    profile_levels = _enum_at(schemas["trust_profile"], "properties", "trust_level", "enum")
    if work_levels != expected:
        raise BoundarySchemaControlsError("schemas/work.schema.json trust_level enum drifted from approved trust levels")
    if profile_levels != expected:
        raise BoundarySchemaControlsError("schemas/trust_profile.schema.json trust_level enum drifted from approved trust levels")

    for doc in (TRUST_HIERARCHY, README):
        text = doc.read_text(encoding="utf-8")
        missing = [level for level in TRUST_LEVELS if level not in text]
        if missing:
            raise BoundarySchemaControlsError(f"{_rel(doc)} missing trust level(s): {missing}")


def validate_existing_records(schemas: dict[str, dict[str, Any]]) -> None:
    for schema_name, patterns in RECORD_TARGETS.items():
        validator = Draft202012Validator(schemas[schema_name])
        files = sorted({path for pattern in patterns for path in ROOT.glob(pattern)})
        for path in files:
            record = _read_json(path)
            errors = sorted(validator.iter_errors(record), key=lambda err: list(err.path))
            if errors:
                first = errors[0]
                location = ".".join(str(part) for part in first.path) or "<root>"
                raise BoundarySchemaControlsError(
                    f"{_rel(path)} does not conform to {SCHEMA_FILES[schema_name].name} at {location}: {first.message}"
                )


def iter_scan_files(paths: Iterable[Path]) -> Iterable[Path]:
    for root in paths:
        if not root.exists():
            continue
        if root.is_file():
            if root.suffix.lower() in SCAN_SUFFIXES:
                yield root
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in SCAN_SUFFIXES:
                yield path


def find_contamination_warnings(paths: Iterable[Path]) -> list[ContaminationWarning]:
    warnings: list[ContaminationWarning] = []
    for path in iter_scan_files(paths):
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in QUOTED_STRING.finditer(text):
            quoted_text = match.group("text")
            words = WORD.findall(quoted_text)
            if len(words) < MIN_SUSPECT_WORDS:
                continue
            line = text.count("\n", 0, match.start()) + 1
            excerpt = " ".join(quoted_text.split())[:160]
            warnings.append(
                ContaminationWarning(
                    path=path,
                    line=line,
                    word_count=len(words),
                    excerpt=excerpt,
                )
            )
    return warnings


def validate_boundary_schema_controls() -> list[ContaminationWarning]:
    schemas = load_schemas()
    validate_trust_level_vocabulary(schemas)
    validate_existing_records(schemas)
    return find_contamination_warnings((DATA_DIR, EVAL_DIR))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fail-on-contamination-warning",
        action="store_true",
        help="Treat warn-level suspected source-text findings as errors.",
    )
    args = parser.parse_args(argv)

    try:
        warnings = validate_boundary_schema_controls()
    except BoundarySchemaControlsError as exc:
        print(f"Boundary schema controls validation failed: {exc}", file=sys.stderr)
        return 1

    if warnings:
        print("Boundary contamination lint warnings (warn-only):", file=sys.stderr)
        for warning in warnings:
            print(
                f"- {_rel(warning.path)}:{warning.line}: suspected verse-length quoted string "
                f"({warning.word_count} words): {warning.excerpt!r}",
                file=sys.stderr,
            )
        if args.fail_on_contamination_warning:
            return 1

    print("Boundary schema controls validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
