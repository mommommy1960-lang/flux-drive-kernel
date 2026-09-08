"""Validated, hardware-neutral macroscopic thrust mechanism.

This module models ordinary reaction-mass propulsion. It is a real,
macroscopic mechanism because the force is the measured change in momentum of
the working fluid plus the pressure-area correction. It does not model or
claim matter phasing through an intact barrier.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ThrustInputs:
    """One-dimensional propulsion control-volume inputs in SI units."""

    exit_mass_flow_kg_s: float
    exit_velocity_m_s: float
    inlet_mass_flow_kg_s: float = 0.0
    inlet_velocity_m_s: float = 0.0
    exit_pressure_pa: float = 0.0
    ambient_pressure_pa: float = 0.0
    exit_area_m2: float = 0.0


def thrust_newton(inputs: ThrustInputs) -> float:
    """Return ideal control-volume thrust from momentum flux and pressure."""
    if inputs.exit_mass_flow_kg_s < 0 or inputs.inlet_mass_flow_kg_s < 0:
        raise ValueError("mass flow cannot be negative")
    if inputs.exit_area_m2 < 0:
        raise ValueError("exit area cannot be negative")
    if inputs.exit_pressure_pa < 0 or inputs.ambient_pressure_pa < 0:
        raise ValueError("pressure cannot be negative")
    return (
        inputs.exit_mass_flow_kg_s * inputs.exit_velocity_m_s
        - inputs.inlet_mass_flow_kg_s * inputs.inlet_velocity_m_s
        + inputs.exit_area_m2
        * (inputs.exit_pressure_pa - inputs.ambient_pressure_pa)
    )


def validate_thrust_measurement(
    *,
    predicted_n: float,
    measured_n: float,
    uncertainty_n: float,
    repeated_trials: int,
    independent_replications: int,
) -> dict[str, object]:
    """Apply a conservative validation gate to a measured thrust result.

    VALIDATED_FOR_DEFINED_TEST means the declared measurement agrees with
    the model, repeats, and has independent replication. It does not validate
    a reactionless drive or any untested scale, environment, or hardware.
    """
    if predicted_n < 0 or measured_n < 0 or uncertainty_n <= 0:
        raise ValueError("invalid force or uncertainty")
    residual_n = measured_n - predicted_n
    if abs(residual_n) > uncertainty_n:
        status = "NOT_VALIDATED"
        reason = "measurement is outside declared uncertainty"
    elif repeated_trials < 3:
        status = "NOT_VALIDATED"
        reason = "fewer than three repeated trials"
    elif independent_replications < 1:
        status = "NOT_VALIDATED"
        reason = "no independent replication"
    else:
        status = "VALIDATED_FOR_DEFINED_TEST"
        reason = "model, repeated trials, and independent replication agree"
    return {
        "status": status,
        "predicted_force_n": predicted_n,
        "measured_force_n": measured_n,
        "residual_n": residual_n,
        "uncertainty_n": uncertainty_n,
        "reason": reason,
    }
