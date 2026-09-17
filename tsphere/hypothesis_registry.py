"""Fail-closed registry for new macroscopic mechanism hypotheses.

This lets us be first to define and test a mechanism without pretending that a
proposal is already a discovery. A hypothesis is review-ready only when it
states its interaction, equations, observables, controls, and falsifiers.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MechanismHypothesis:
    name: str
    interaction: str
    governing_equations: str
    boundary_conditions: str
    predicted_observables: str
    required_controls: tuple[str, ...]
    falsifiers: str

    def review_status(self) -> dict[str, object]:
        fields = {
            "interaction": self.interaction,
            "governing_equations": self.governing_equations,
            "boundary_conditions": self.boundary_conditions,
            "predicted_observables": self.predicted_observables,
            "falsifiers": self.falsifiers,
        }
        missing = sorted(name for name, value in fields.items() if not value.strip())
        if not self.required_controls:
            missing.append("required_controls")
        return {
            "status": "READY_FOR_REVIEW" if not missing else "BLOCKED",
            "missing_fields": missing,
            "validated": False,
        }


def evaluate_evidence(
    hypothesis: MechanismHypothesis,
    *,
    repeated_trials: int,
    independent_replications: int,
    all_controls_passed: bool,
    measurements_within_uncertainty: bool,
) -> dict[str, object]:
    """Return a conservative evidence status for a proposed mechanism."""
    review = hypothesis.review_status()
    if review["status"] != "READY_FOR_REVIEW":
        return {**review, "reason": "mechanism packet is incomplete"}
    if repeated_trials < 3:
        return {"status": "NOT_VALIDATED", "validated": False,
                "reason": "fewer than three repeated trials"}
    if independent_replications < 1:
        return {"status": "NOT_VALIDATED", "validated": False,
                "reason": "no independent replication"}
    if not all_controls_passed:
        return {"status": "NOT_VALIDATED", "validated": False,
                "reason": "one or more controls failed"}
    if not measurements_within_uncertainty:
        return {"status": "NOT_VALIDATED", "validated": False,
                "reason": "measurements disagree with prediction"}
    return {"status": "VALIDATED_FOR_DEFINED_TEST", "validated": True,
            "reason": "all defined evidence gates passed"}
