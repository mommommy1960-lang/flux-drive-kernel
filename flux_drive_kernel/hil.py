"""Replay measured bench data through the fail-closed Flux Drive kernel."""

from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

from .bench import BenchConfig, FluxDriveBench
from .metrology import is_consistent_with_zero, momentum_closure

REQUIRED_COLUMNS = (
    "timestamp_s", "command", "measured_voltage_V", "measured_current_A",
    "measured_temperature_C", "measured_force_N",
)
MOMENTUM_COLUMNS = ("reaction_force_N",)
ENVIRONMENT_COLUMNS = (
    "vibration_x_m_s2", "vibration_y_m_s2", "vibration_z_m_s2",
    "magnetic_field_uT", "acoustic_pressure_Pa", "ambient_pressure_Pa",
    "orientation_deg",
)


@dataclass(frozen=True)
class HILReport:
    status: str
    rows: int
    duration_s: float
    measured_impulse_N_s: float
    measured_electrical_energy_J: float
    peak_abs_force_N: float
    peak_current_A: float
    peak_temperature_C: float
    safety_trip: str | None
    missing_columns: tuple[str, ...] = ()
    validation_errors: tuple[str, ...] = ()
    reaction_impulse_N_s: float | None = None
    momentum_residual_N_s: float | None = None
    data_completeness_status: str = "basic_channels_only"
    momentum_closure_status: str = "not_assessed"
    propulsion_verdict: str = "not_assessed"
    integration_method: str = "trapezoidal"
    measured_absolute_electrical_energy_J: float = 0.0
    momentum_expanded_uncertainty_N_s: float | None = None
    momentum_coverage_factor: float | None = None
    momentum_closure_method: str = "not_assessed"

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _number(row: Mapping[str, str], name: str, line: int) -> float:
    try:
        value = float(row[name])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"line {line}: {name} must be numeric") from exc
    if not math.isfinite(value):
        raise ValueError(f"line {line}: {name} must be finite")
    return value


def _validate_optional_uncertainty(
    force_standard_uncertainty_N_s: float | None,
    reaction_standard_uncertainty_N_s: float | None,
    covariance_N2_s2: float,
    coverage_factor: float,
) -> None:
    paired = (force_standard_uncertainty_N_s is None) == (
        reaction_standard_uncertainty_N_s is None
    )
    if not paired:
        raise ValueError(
            "force and reaction impulse standard uncertainties must be supplied together"
        )
    if not math.isfinite(covariance_N2_s2):
        raise ValueError("force_reaction_covariance_N2_s2 must be finite")
    if not math.isfinite(coverage_factor) or coverage_factor <= 0:
        raise ValueError("coverage_factor must be finite and positive")
    if force_standard_uncertainty_N_s is not None:
        for name, value in {
            "force_impulse_standard_uncertainty_N_s": force_standard_uncertainty_N_s,
            "reaction_impulse_standard_uncertainty_N_s": reaction_standard_uncertainty_N_s,
        }.items():
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{name} must be finite and nonnegative")


def audit_rows(
    rows: Iterable[Mapping[str, str]],
    config: BenchConfig | None = None,
    *,
    require_momentum_channels: bool = False,
    require_environment_channels: bool = False,
    momentum_tolerance_N_s: float = 1e-6,
    force_impulse_standard_uncertainty_N_s: float | None = None,
    reaction_impulse_standard_uncertainty_N_s: float | None = None,
    force_reaction_covariance_N2_s2: float = 0.0,
    coverage_factor: float = 2.0,
    require_uncertainty_for_momentum: bool = False,
) -> HILReport:
    """Audit measured rows without converting a residual into a propulsion claim.

    Momentum closure uses expanded uncertainty when both impulse standard
    uncertainties are supplied. The fixed ``momentum_tolerance_N_s`` path is
    retained as a legacy/software check only. Measurement-grade interpretation
    should set ``require_uncertainty_for_momentum=True`` and supply calibrated
    uncertainty inputs.
    """
    if not math.isfinite(momentum_tolerance_N_s) or momentum_tolerance_N_s < 0:
        raise ValueError("momentum_tolerance_N_s must be finite and nonnegative")
    _validate_optional_uncertainty(
        force_impulse_standard_uncertainty_N_s,
        reaction_impulse_standard_uncertainty_N_s,
        force_reaction_covariance_N2_s2,
        coverage_factor,
    )

    momentum_required = (
        require_momentum_channels
        or require_uncertainty_for_momentum
        or force_impulse_standard_uncertainty_N_s is not None
    )

    materialized = list(rows)
    present = set(materialized[0]) if materialized else set()
    missing = [column for column in REQUIRED_COLUMNS if column not in present]
    if momentum_required:
        missing.extend(column for column in MOMENTUM_COLUMNS if column not in present)
    if require_environment_channels:
        missing.extend(column for column in ENVIRONMENT_COLUMNS if column not in present)
    if missing:
        return HILReport(
            status="FAIL", rows=0, duration_s=0.0,
            measured_impulse_N_s=0.0, measured_electrical_energy_J=0.0,
            measured_absolute_electrical_energy_J=0.0,
            peak_abs_force_N=0.0, peak_current_A=0.0, peak_temperature_C=0.0,
            safety_trip=None, missing_columns=tuple(dict.fromkeys(missing)),
            data_completeness_status="incomplete",
            propulsion_verdict=(
                "uncertainty_required"
                if require_uncertainty_for_momentum
                and force_impulse_standard_uncertainty_N_s is None
                else "not_assessed"
            ),
        )

    bench = FluxDriveBench(config)
    errors: list[str] = []
    count = 0
    first_timestamp: float | None = None
    previous_timestamp: float | None = None
    previous_force: float | None = None
    previous_power: float | None = None
    previous_abs_power: float | None = None
    previous_reaction: float | None = None
    measured_impulse = 0.0
    measured_energy = 0.0
    measured_abs_energy = 0.0
    reaction_impulse = 0.0 if "reaction_force_N" in present else None
    peak_force = 0.0
    peak_current = 0.0
    peak_temperature = float("-inf")

    for line, row in enumerate(materialized, start=2):
        count += 1
        try:
            timestamp = _number(row, "timestamp_s", line)
            command = _number(row, "command", line)
            voltage = _number(row, "measured_voltage_V", line)
            current = _number(row, "measured_current_A", line)
            temperature = _number(row, "measured_temperature_C", line)
            force = _number(row, "measured_force_N", line)
            reaction = (
                _number(row, "reaction_force_N", line)
                if reaction_impulse is not None
                else None
            )
            for column in ENVIRONMENT_COLUMNS:
                if column in present:
                    _number(row, column, line)

            if voltage < 0:
                raise ValueError(f"line {line}: measured_voltage_V cannot be negative")
            if previous_timestamp is not None and timestamp <= previous_timestamp:
                raise ValueError(f"line {line}: timestamps must increase strictly")

            dt = 0.0 if previous_timestamp is None else timestamp - previous_timestamp
            instantaneous_power = voltage * current
            instantaneous_abs_power = abs(instantaneous_power)

            bench.step(
                command,
                dt_s=dt,
                measured_force_N=force,
                measured_current_A=current,
                measured_temperature_C=temperature,
                measured_voltage_V=voltage,
            )

            if previous_timestamp is not None:
                measured_impulse += 0.5 * (previous_force + force) * dt
                measured_energy += 0.5 * (previous_power + instantaneous_power) * dt
                measured_abs_energy += 0.5 * (
                    previous_abs_power + instantaneous_abs_power
                ) * dt
                if reaction_impulse is not None:
                    reaction_impulse += 0.5 * (previous_reaction + reaction) * dt

            if first_timestamp is None:
                first_timestamp = timestamp
            previous_timestamp = timestamp
            previous_force = force
            previous_power = instantaneous_power
            previous_abs_power = instantaneous_abs_power
            previous_reaction = reaction
            peak_force = max(peak_force, abs(force))
            peak_current = max(peak_current, abs(current))
            peak_temperature = max(peak_temperature, temperature)
        except ValueError as exc:
            errors.append(str(exc))

    duration = (
        0.0
        if first_timestamp is None or previous_timestamp is None
        else previous_timestamp - first_timestamp
    )
    residual = None if reaction_impulse is None else measured_impulse + reaction_impulse

    expanded_uncertainty = None
    reported_coverage_factor = None
    closure_method = "not_assessed"

    if reaction_impulse is None:
        closure = "not_assessed"
        verdict = "not_assessed"
    elif errors or bench.state.safety_trip is not None:
        closure = "not_assessed"
        verdict = "not_assessed"
    elif force_impulse_standard_uncertainty_N_s is not None:
        closure_measurement = momentum_closure(
            measured_impulse,
            reaction_impulse,
            force_standard_uncertainty_N_s=force_impulse_standard_uncertainty_N_s,
            reaction_standard_uncertainty_N_s=reaction_impulse_standard_uncertainty_N_s,
            force_reaction_covariance_N2_s2=force_reaction_covariance_N2_s2,
            coverage_factor=coverage_factor,
        )
        expanded_uncertainty = closure_measurement.expanded_uncertainty
        reported_coverage_factor = closure_measurement.coverage_factor
        closure_method = "expanded_uncertainty"
        if is_consistent_with_zero(closure_measurement):
            closure = "pass"
            verdict = "recorded_channels_close_no_propulsion_inference"
        else:
            closure = "fail"
            verdict = "momentum_not_closed"
    elif require_uncertainty_for_momentum:
        closure = "not_assessed"
        verdict = "uncertainty_required"
        closure_method = "uncertainty_required"
    elif abs(residual) <= momentum_tolerance_N_s:
        closure = "pass"
        verdict = "recorded_channels_close_no_propulsion_inference"
        closure_method = "fixed_tolerance_software_check"
    else:
        closure = "fail"
        verdict = "momentum_not_closed"
        closure_method = "fixed_tolerance_software_check"

    environment_complete = all(column in present for column in ENVIRONMENT_COLUMNS)
    if reaction_impulse is not None and environment_complete:
        complete = "reaction_and_environment_channels"
    elif reaction_impulse is not None:
        complete = "reaction_channel_present"
    elif environment_complete:
        complete = "environment_channels_present"
    else:
        complete = "basic_channels_only"

    status = "PASS" if count and not errors and bench.state.safety_trip is None else "FAIL"
    if momentum_required and closure != "pass":
        status = "FAIL"
    if require_environment_channels and not environment_complete:
        status = "FAIL"

    return HILReport(
        status=status,
        rows=count,
        duration_s=duration,
        measured_impulse_N_s=measured_impulse,
        measured_electrical_energy_J=measured_energy,
        measured_absolute_electrical_energy_J=measured_abs_energy,
        peak_abs_force_N=peak_force,
        peak_current_A=peak_current,
        peak_temperature_C=peak_temperature if count else 0.0,
        safety_trip=bench.state.safety_trip,
        validation_errors=tuple(errors),
        reaction_impulse_N_s=reaction_impulse,
        momentum_residual_N_s=residual,
        data_completeness_status=complete,
        momentum_closure_status=closure,
        propulsion_verdict=verdict,
        momentum_expanded_uncertainty_N_s=expanded_uncertainty,
        momentum_coverage_factor=reported_coverage_factor,
        momentum_closure_method=closure_method,
    )


def audit_csv(
    path: str | Path,
    config: BenchConfig | None = None,
    *,
    require_momentum_channels: bool = False,
    require_environment_channels: bool = False,
    momentum_tolerance_N_s: float = 1e-6,
    force_impulse_standard_uncertainty_N_s: float | None = None,
    reaction_impulse_standard_uncertainty_N_s: float | None = None,
    force_reaction_covariance_N2_s2: float = 0.0,
    coverage_factor: float = 2.0,
    require_uncertainty_for_momentum: bool = False,
) -> HILReport:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return audit_rows(
            reader,
            config,
            require_momentum_channels=require_momentum_channels,
            require_environment_channels=require_environment_channels,
            momentum_tolerance_N_s=momentum_tolerance_N_s,
            force_impulse_standard_uncertainty_N_s=force_impulse_standard_uncertainty_N_s,
            reaction_impulse_standard_uncertainty_N_s=reaction_impulse_standard_uncertainty_N_s,
            force_reaction_covariance_N2_s2=force_reaction_covariance_N2_s2,
            coverage_factor=coverage_factor,
            require_uncertainty_for_momentum=require_uncertainty_for_momentum,
        )


def report_json(report: HILReport) -> str:
    return json.dumps(report.as_dict(), indent=2, sort_keys=True)
