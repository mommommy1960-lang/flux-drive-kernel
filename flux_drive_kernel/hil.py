"""Replay measured bench data through the fail-closed Flux Drive kernel."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

from .bench import BenchConfig, FluxDriveBench

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

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _number(row: Mapping[str, str], name: str, line: int) -> float:
    try:
        value = float(row[name])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"line {line}: {name} must be numeric") from exc
    if not value == value or value in (float("inf"), float("-inf")):
        raise ValueError(f"line {line}: {name} must be finite")
    return value


def audit_rows(
    rows: Iterable[Mapping[str, str]],
    config: BenchConfig | None = None,
    *,
    require_momentum_channels: bool = False,
    require_environment_channels: bool = False,
    momentum_tolerance_N_s: float = 1e-6,
) -> HILReport:
    materialized = list(rows)
    present = set(materialized[0]) if materialized else set()
    missing = [column for column in REQUIRED_COLUMNS if column not in present]
    if require_momentum_channels:
        missing.extend(column for column in MOMENTUM_COLUMNS if column not in present)
    if require_environment_channels:
        missing.extend(column for column in ENVIRONMENT_COLUMNS if column not in present)
    if missing:
        return HILReport(
            status="FAIL", rows=0, duration_s=0.0,
            measured_impulse_N_s=0.0, measured_electrical_energy_J=0.0,
            peak_abs_force_N=0.0, peak_current_A=0.0, peak_temperature_C=0.0,
            safety_trip=None, missing_columns=tuple(dict.fromkeys(missing)),
            data_completeness_status="incomplete",
        )

    bench = FluxDriveBench(config)
    errors: list[str] = []
    count = 0
    first_timestamp: float | None = None
    previous_timestamp: float | None = None
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
            if first_timestamp is None:
                first_timestamp = timestamp
            if previous_timestamp is not None and timestamp <= previous_timestamp:
                errors.append(f"line {line}: timestamps must increase strictly")
                continue
            dt = 0.0 if previous_timestamp is None else timestamp - previous_timestamp
            previous_timestamp = timestamp
            bench.step(command, dt_s=max(dt, 1e-9), measured_force_N=force,
                       measured_current_A=current, measured_temperature_C=temperature,
                       measured_voltage_V=voltage)
            if reaction_impulse is not None:
                reaction_impulse += _number(row, "reaction_force_N", line) * dt
            for column in ENVIRONMENT_COLUMNS:
                if column in present:
                    _number(row, column, line)
            peak_force = max(peak_force, abs(force))
            peak_current = max(peak_current, abs(current))
            peak_temperature = max(peak_temperature, temperature)
        except ValueError as exc:
            errors.append(str(exc))

    duration = 0.0 if first_timestamp is None or previous_timestamp is None else previous_timestamp - first_timestamp
    residual = None if reaction_impulse is None else bench.state.impulse_N_s + reaction_impulse
    if reaction_impulse is None:
        closure = "not_assessed"
        verdict = "not_assessed"
    elif errors or bench.state.safety_trip is not None:
        closure = "not_assessed"
        verdict = "not_assessed"
    elif abs(residual) <= momentum_tolerance_N_s:
        closure = "pass"
        verdict = "momentum_closed_for_recorded_channels"
    else:
        closure = "fail"
        verdict = "momentum_not_closed"
    complete = "complete_channels" if reaction_impulse is not None else "basic_channels_only"
    status = "PASS" if count and not errors and bench.state.safety_trip is None else "FAIL"
    return HILReport(
        status=status, rows=count, duration_s=duration,
        measured_impulse_N_s=bench.state.impulse_N_s,
        measured_electrical_energy_J=bench.state.electrical_energy_J,
        peak_abs_force_N=peak_force, peak_current_A=peak_current,
        peak_temperature_C=peak_temperature if count else 0.0,
        safety_trip=bench.state.safety_trip, validation_errors=tuple(errors),
        reaction_impulse_N_s=reaction_impulse, momentum_residual_N_s=residual,
        data_completeness_status=complete,
        momentum_closure_status=closure, propulsion_verdict=verdict,
    )


def audit_csv(
    path: str | Path,
    config: BenchConfig | None = None,
    *,
    require_momentum_channels: bool = False,
    require_environment_channels: bool = False,
    momentum_tolerance_N_s: float = 1e-6,
) -> HILReport:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return audit_rows(
            reader, config,
            require_momentum_channels=require_momentum_channels,
            require_environment_channels=require_environment_channels,
            momentum_tolerance_N_s=momentum_tolerance_N_s,
        )


def report_json(report: HILReport) -> str:
    return json.dumps(report.as_dict(), indent=2, sort_keys=True)
