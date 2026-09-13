from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = {
    "run_id",
    "software_commit",
    "apparatus_config_hash",
    "operator_id",
    "condition",
    "calibration_record_id",
    "timestamp_source",
    "channels",
    "expanded_uncertainty_impulse_N_s",
    "acceptance",
}

ALLOWED_CONDITIONS = {"NULL", "KNOWN_POS", "KNOWN_NEG", "SHAM", "ARTIFACT"}


def evaluate(record: dict) -> tuple[str, list[str]]:
    reasons: list[str] = []
    missing = sorted(REQUIRED - set(record))
    if missing:
        reasons.append("missing fields: " + ", ".join(missing))

    if record.get("condition") not in ALLOWED_CONDITIONS:
        reasons.append("invalid condition")

    u = record.get("expanded_uncertainty_impulse_N_s")
    if not isinstance(u, (int, float)) or u <= 0:
        reasons.append("expanded uncertainty must be positive")

    acceptance = record.get("acceptance")
    if not isinstance(acceptance, dict):
        reasons.append("acceptance must be an object")
    else:
        explicit_fail = [
            name
            for name in ("known_force_recovery", "null_discrimination", "reversal_consistent")
            if acceptance.get(name) is False
        ]
        if explicit_fail:
            return "FAIL", ["failed checks: " + ", ".join(explicit_fail)]

        pending = [
            name
            for name in ("known_force_recovery", "null_discrimination", "reversal_consistent")
            if acceptance.get(name) is not True
        ]
        if pending:
            reasons.append("checks not yet established: " + ", ".join(pending))

    if reasons:
        return "INDETERMINATE", reasons
    return "PASS", ["manifest satisfies the CAL-00 evidence gate"]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/cal00_manifest_check.py manifest.json", file=sys.stderr)
        return 2
    record = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    status, reasons = evaluate(record)
    print(json.dumps({"status": status, "reasons": reasons}, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
