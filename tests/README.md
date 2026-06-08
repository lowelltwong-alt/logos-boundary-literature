# Tests

No executable test suite exists yet.

Current scaffold validation should use:

```bash
python -c "import json, pathlib; [json.load(open(p, encoding='utf-8')) for p in pathlib.Path('schemas').glob('*.schema.json')]"
```

Future validation should check:

- schema parse and sample validation;
- data folders contain no source texts before intake approval;
- every source record has source status;
- every claim has provenance;
- every canon claim has tradition scope;
- no generic `related_to` relationships;
- no default canonical influence from boundary claims.
