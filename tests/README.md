# Tests

Current scaffold validation uses pytest plus JSON Schema parse checks:

```bash
python -c "import json, pathlib; [json.load(open(p, encoding='utf-8')) for p in pathlib.Path('schemas').glob('*.schema.json')]"
python -m pytest -q
```

Current executable checks cover:

- SQLite reliability-evidence schema execution;
- namespace separation for `boundary_*` and `evidence_*` tables;
- pre-evidence intake queue lanes, repo routing, text-storage flags, and review gates;
- invented reliability-evidence fixture loading;
- text-storage flags staying disabled;
- candidate claims staying unpromoted and non-authoritative.

Future validation should check:

- broader schema parse and sample validation;
- data folders contain no source texts before intake approval;
- every source record has source status;
- every claim has provenance;
- every canon claim has tradition scope;
- no generic `related_to` relationships;
- no default canonical influence from boundary claims.
