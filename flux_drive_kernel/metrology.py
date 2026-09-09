"""Traceable calibration and uncertainty calculations for bench measurements."""

from __future__ import annotations

import math
from dataclasses import dataclass


def _finite(name: str, value: float) -> float:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def _validate_covariance(name: str, covariance: float, u_a: float, u_b: float) -> None:
    _finite(name, covariance)
    bound = u_a * u_b
    tolerance = max(1e-30, bound * 1e-12)
    if abs(covariance) > bound + tolerance:
        raise ValueError(f"{name} exceeds the Cauchy-Schwarz covariance bound")


@dataclass(frozen=True)
class CalibratedMeasurement:
    value: float
    standard_uncertainty: float
    expanded_uncertainty: float
    coverage_factor: float

    @property
    def interval(self) -> tuple[float, float]:
        return (
            self.value - self.expanded_uncertainty,
            self.value + self.expanded_uncertainty,
        )


def calibrate_linear(
    raw_value: float,
    *,
    slope: float,
    offset: float = 0.0,
    raw_standard_uncertainty: float = 0.0,
    slope_standard_uncertainty: float = 0.0,
    offset_standard_uncertainty: float = 0.0,
    covariance_raw_slope: float = 0.0,
    covariance_raw_offset: float = 0.0,
    covariance_slope_offset: float = 0.0,
    coverage_factor: float = 2.0,
) -> CalibratedMeasurement:
    """Convert a raw channel with a linear calibration and first-order GUM uncertainty.

    For ``y = slope * raw_value + offset``, the variance includes the full
    first-order covariance terms. Set covariance arguments to zero only when
    independence is justified by the calibration model or certificate.
    """
    for name, value in {
        "raw_value": raw_value,
        "slope": slope,
        "offset": offset,
        "raw_standard_uncertainty": raw_standard_uncertainty,
        "slope_standard_uncertainty": slope_standard_uncertainty,
        "offset_standard_uncertainty": offset_standard_uncertainty,
        "coverage_factor": coverage_factor,
    }.items():
        _finite(name, value)
    if slope == 0:
        raise ValueError("slope must be nonzero")
    if min(raw_standard_uncertainty, slope_standard_uncertainty, offset_standard_uncertainty) < 0:
        raise ValueError("standard uncertainties cannot be negative")
    if coverage_factor <= 0:
        raise ValueError("coverage_factor must be positive")

    _validate_covariance(
        "covariance_raw_slope",
        covariance_raw_slope,
        raw_standard_uncertainty,
        slope_standard_uncertainty,
    )
    _validate_covariance(
        "covariance_raw_offset",
        covariance_raw_offset,
        raw_standard_uncertainty,
        offset_standard_uncertainty,
    )
    _validate_covariance(
        "covariance_slope_offset",
        covariance_slope_offset,
        slope_standard_uncertainty,
        offset_standard_uncertainty,
    )

    value = slope * raw_value + offset
    variance = (
        (slope * raw_standard_uncertainty) ** 2
        + (raw_value * slope_standard_uncertainty) ** 2
        + offset_standard_uncertainty**2
        + 2.0 * slope * raw_value * covariance_raw_slope
        + 2.0 * slope * covariance_raw_offset
        + 2.0 * raw_value * covariance_slope_offset
    )
    tolerance = 1e-24 * max(1.0, abs(value) ** 2)
    if variance < -tolerance:
        raise ValueError("uncertainty covariance matrix yields negative propagated variance")
    standard = math.sqrt(max(0.0, variance))
    return CalibratedMeasurement(value, standard, coverage_factor * standard, coverage_factor)


def momentum_closure(
    force_impulse_N_s: float,
    reaction_impulse_N_s: float,
    *,
    force_standard_uncertainty_N_s: float,
    reaction_standard_uncertainty_N_s: float,
    force_reaction_covariance_N2_s2: float = 0.0,
    coverage_factor: float = 2.0,
) -> CalibratedMeasurement:
    """Evaluate signed impulse closure with covariance-aware uncertainty."""
    for name, value in {
        "force_impulse_N_s": force_impulse_N_s,
        "reaction_impulse_N_s": reaction_impulse_N_s,
        "force_standard_uncertainty_N_s": force_standard_uncertainty_N_s,
        "reaction_standard_uncertainty_N_s": reaction_standard_uncertainty_N_s,
        "coverage_factor": coverage_factor,
    }.items():
        _finite(name, value)
    if min(force_standard_uncertainty_N_s, reaction_standard_uncertainty_N_s) < 0:
        raise ValueError("standard uncertainties cannot be negative")
    if coverage_factor <= 0:
        raise ValueError("coverage_factor must be positive")

    _validate_covariance(
        "force_reaction_covariance_N2_s2",
        force_reaction_covariance_N2_s2,
        force_standard_uncertainty_N_s,
        reaction_standard_uncertainty_N_s,
    )
    variance = (
        force_standard_uncertainty_N_s**2
        + reaction_standard_uncertainty_N_s**2
        + 2.0 * force_reaction_covariance_N2_s2
    )
    if variance < -1e-30:
        raise ValueError("momentum-closure covariance yields negative variance")
    standard = math.sqrt(max(0.0, variance))
    return CalibratedMeasurement(
        force_impulse_N_s + reaction_impulse_N_s,
        standard,
        coverage_factor * standard,
        coverage_factor,
    )


def is_consistent_with_zero(measurement: CalibratedMeasurement) -> bool:
    """Return true only when the expanded interval contains zero."""
    low, high = measurement.interval
    return low <= 0.0 <= high
