#!/usr/bin/env python3
"""Run the declared Alpha Centauri coupled feasibility screen."""

import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flux_drive_kernel.relativistic_mission import (
    MissionInputs, find_fastest_passing_profile, simulate_mission,
)


def json_safe(metrics):
    return {
        key: (None if isinstance(value, float) and not math.isfinite(value) else value)
        for key, value in metrics.items()
    }


def main() -> None:
    inputs = MissionInputs()
    result = simulate_mission(inputs)
    fastest = find_fastest_passing_profile(inputs)
    print(json.dumps({
        "product": "MAGNUSPHERE",
        "model": "magnusphere-coupled-trajectory-environment-v0.1",
        "evidence_level": "screening simulation only",
        "passed": result.passed,
        "first_failure": result.first_failure,
        "gates": result.gates,
        "metrics": json_safe(result.metrics),
        "fastest_profile_passing_declared_gates": {
            "passed": fastest.passed,
            "first_failure": fastest.first_failure,
            "gates": fastest.gates,
            "metrics": json_safe(fastest.metrics),
        },
        "limitations": result.limitations,
        "physical_propulsion_proven": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
