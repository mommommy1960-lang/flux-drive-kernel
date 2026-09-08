"""Evidence gate for a macroscopic barrier-transit claim.

This does not detect phasing. It prevents incomplete evidence from being
reported as phasing.
"""

from dataclasses import dataclass
from typing import Iterable, Tuple


REQUIRED_CONTROLS = {
    "empty",
    "powered_off",
    "ordinary_opening",
    "matched_dummy",
    "telemetry_relay",
    "sham_field",
    "reversed_orientation",
    "sealed_barrier",
}


@dataclass(frozen=True)
class Evidence:
    object_continuity: bool
    optical_coverage: bool
    no_barrier_damage: bool
    no_unobserved_path: bool
    conservation_within_uncertainty: bool
    randomized_repeatability: bool
    independent_replication: bool
    controls_completed: Tuple[str, ...]

    def evaluate(self) -> dict:
        controls = set(self.controls_completed)
        missing = sorted(REQUIRED_CONTROLS - controls)
        passed = all(
            (
                self.object_continuity,
                self.optical_coverage,
                self.no_barrier_damage,
                self.no_unobserved_path,
                self.conservation_within_uncertainty,
                self.randomized_repeatability,
                self.independent_replication,
            )
        ) and not missing
        return {
            "status": "DEMONSTRATED" if passed else "NOT_DEMONSTRATED",
            "missing_controls": missing,
            "reason": "all evidence gates passed" if passed else "one or more evidence gates failed",
        }


def evaluate_run(evidence: Evidence) -> dict:
    return evidence.evaluate()


if __name__ == "__main__":
    example = Evidence(
        object_continuity=False,
        optical_coverage=True,
        no_barrier_damage=True,
        no_unobserved_path=True,
        conservation_within_uncertainty=True,
        randomized_repeatability=False,
        independent_replication=False,
        controls_completed=tuple(sorted(REQUIRED_CONTROLS)),
    )
    print(evaluate_run(example))
