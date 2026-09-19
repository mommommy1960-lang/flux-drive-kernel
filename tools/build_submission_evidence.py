#!/usr/bin/env python3
"""Build a machine-readable, non-hardware submission evidence bundle."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INCLUDED_ROOTS = ("flux_drive_kernel", "tests", "tsphere", "schemas", "tools")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_manifest() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for root_name in INCLUDED_ROOTS:
        root = ROOT / root_name
        if not root.exists():
            continue
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            if "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            records.append(
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    return records


def run(command: list[str]) -> dict[str, object]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "command": command,
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def main() -> int:
    output = ROOT / "artifacts" / "submission_evidence_2026-09-11.json"
    output.parent.mkdir(exist_ok=True)
    checks = [
        run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]),
        run([sys.executable, "-m", "unittest", "discover", "-s", "tsphere/tests", "-v"]),
        run([sys.executable, "tools/run_submission_demo.py"]),
    ]
    files = source_manifest()
    aggregate = hashlib.sha256(
        "\n".join(f"{item['path']}:{item['sha256']}" for item in files).encode()
    ).hexdigest()
    bundle = {
        "schema": "aurora-flux-submission-evidence-v1",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "hardware_io": "disabled",
        "physical_propulsion_proven": False,
        "random_seeds": [],
        "runtime": {
            "python": sys.version,
            "platform": platform.platform(),
        },
        "source_manifest_sha256": aggregate,
        "source_files": files,
        "checks": checks,
        "all_checks_passed": all(check["exit_code"] == 0 for check in checks),
    }
    output.write_text(json.dumps(bundle, indent=2, sort_keys=True) + "\n")
    print(output.relative_to(ROOT))
    print(f"source_manifest_sha256={aggregate}")
    print(f"all_checks_passed={bundle['all_checks_passed']}")
    return 0 if bundle["all_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

