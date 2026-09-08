"""First-pass screening equations for proposed T-Sphere mechanisms.

These calculations do not claim phasing. They quantify ordinary interactions
and expose the requirements a new mechanism would have to exceed.
"""

from __future__ import annotations

import math


C_LIGHT_M_S = 299_792_458.0


def photon_pressure_force(power_w: float, area_m2: float, reflection: float = 1.0) -> float:
    """Upper-bound radiation-pressure force for a normally illuminated target."""
    if power_w < 0 or area_m2 < 0 or not 0 <= reflection <= 1:
        raise ValueError("power, area, and reflection are out of range")
    return (1.0 + reflection) * power_w / C_LIGHT_M_S


def acoustic_pressure_force(rms_pressure_pa: float, projected_area_m2: float) -> float:
    """Pressure-force scale; this is not a reactionless-thrust equation."""
    if rms_pressure_pa < 0 or projected_area_m2 < 0:
        raise ValueError("pressure and area must be non-negative")
    return rms_pressure_pa * projected_area_m2


def required_force_for_acceleration(mass_kg: float, acceleration_m_s2: float) -> float:
    if mass_kg < 0 or acceleration_m_s2 < 0:
        raise ValueError("mass and acceleration must be non-negative")
    return mass_kg * acceleration_m_s2


def force_gap_ratio(required_n: float, available_n: float) -> float:
    """How many times larger the desired force is than a measured bound."""
    if required_n < 0 or available_n <= 0:
        raise ValueError("invalid force values")
    return required_n / available_n


def classify_candidate(*, predicted_force_n: float, measured_force_n: float,
                       control_residual_n: float, uncertainty_n: float) -> str:
    """Return a conservative evidence label for a force-producing candidate."""
    if uncertainty_n <= 0 or measured_force_n < 0 or control_residual_n < 0:
        raise ValueError("invalid measurement values")
    if measured_force_n - control_residual_n <= uncertainty_n:
        return "NOT_RESOLVED"
    if predicted_force_n <= 0:
        return "MODEL_INVALID"
    if measured_force_n - control_residual_n >= predicted_force_n - uncertainty_n:
        return "CONSISTENT_WITH_MODEL"
    return "INCONSISTENT_WITH_MODEL"


if __name__ == "__main__":
    mass = 0.10
    desired_acceleration = 0.01
    required = required_force_for_acceleration(mass, desired_acceleration)
    optical_bound = photon_pressure_force(10.0, 0.01)
    acoustic_scale = acoustic_pressure_force(1.0, 0.01)
    print({
        "required_force_N": required,
        "10W_radiation_pressure_N": optical_bound,
        "1Pa_acoustic_pressure_over_0.01m2_N": acoustic_scale,
        "radiation_force_gap": force_gap_ratio(required, optical_bound),
    })
