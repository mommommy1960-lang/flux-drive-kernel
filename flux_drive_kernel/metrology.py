"""Traceable calibration and uncertainty calculations for bench measurements."""

from __future__ import annotations

import math
from dataclasses import dataclass


def _finite(name: str, value: float) -> float:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


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
    coverage_factor: float = 2.0,
) -> CalibratedMeasurement:
    """Convert a raw channel with a linear calibration and RSS uncertainty.

    The calibration certificate must supply the slope/offset uncertainties and
    the raw channel uncertainty. Correlations are not assumed; if a certificate
    supplies covariance, it must be handled by a future covariance-aware path.
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
    value = slope * raw_value + offset
    standard = math.sqrt(
        (slope * raw_standard_uncertainty) ** 2
        + (raw_value * slope_standard_uncertainty) ** 2
        + offset_standard_uncertainty**2
    )
    return CalibratedMeasurement(value, standard, coverage_factor * standard, coverage_factor)


def momentum_closure(
    force_impulse_N_s: float,
    reaction_impulse_N_s: float,
    *,
    force_standard_uncertainty_N_s: float,
    reaction_standard_uncertainty_N_s: float,
    coverage_factor: float = 2.0,
) -> CalibratedMeasurement:
    """Evaluate signed impulse closure with an uncertainty interval."""
    for name, value in {
        "force_impulse_N_s": force_impulse_N_s,
        "reaction_impulse_N_s": reaction_impulse_N_s,
        "force_standard_uncertainty_N_s": force_standard_uncertainty_N_s,
        "reaction_standard_uncertainty_N_s": reaction_standard_uncertainty_N_s,
    }.items():
        _finite(name, value)
    if min(force_standard_uncertainty_N_s, reaction_standard_uncertainty_N_s) < 0:
        raise ValueError("standard uncertainties cannot be negative")
    if coverage_factor <= 0:
        raise ValueError("coverage_factor must be positive")
    standard = math.hypot(force_standard_uncertainty_N_s, reaction_standard_uncertainty_N_s)
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
