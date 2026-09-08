#!/usr/bin/env python3
"""Run the non-hardware Aurora / Flux Drive submission checks."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATHS = tuple((ROOT / "schemas").glob("*.schema.json"))


def main() -> int:
    schema_candidates = [p.resolve() for p in SCHEMA_PATHS if p.exists()]
    for path in schema_candidates:
        json.loads(path.read_text(encoding="utf-8"))

    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        check=False,
    )
    print("\nAurora / Flux Drive submission demo")
    print("hardware_io=disabled")
    print(f"aurora_schemas_checked={len(schema_candidates)}")
    print(f"software_tests_exit={result.returncode}")
    print("physical_propulsion_proven=false")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
