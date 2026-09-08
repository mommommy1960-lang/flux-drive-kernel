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
    momentum_closure_status: str = "not_assessed"

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _number(row: Mapping[str, str], name: str, line: int) -> float:
    try:
        value = float(row[name])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"line {line}: {name} must be numeric") from exc
    if not value == value:
        raise ValueError(f"line {line}: {name} must be finite")
    return value


def audit_rows(rows: Iterable[Mapping[str, str]], config: BenchConfig | None = None) -> HILReport:
    bench = FluxDriveBench(config)
    errors: list[str] = []
    count = 0
    first_timestamp: float | None = None
    previous_timestamp: float | None = None
    peak_force = 0.0
    peak_current = 0.0
    peak_temperature = float("-inf")

    for line, row in enumerate(rows, start=2):
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
            if voltage < 0:
                errors.append(f"line {line}: measured_voltage_V cannot be negative")
            bench.step(command, dt_s=max(dt, 1e-9), measured_force_N=force,
                       measured_current_A=current, measured_temperature_C=temperature)
            peak_force = max(peak_force, abs(force))
            peak_current = max(peak_current, abs(current))
            peak_temperature = max(peak_temperature, temperature)
        except ValueError as exc:
            errors.append(str(exc))

    duration = 0.0 if first_timestamp is None or previous_timestamp is None else previous_timestamp - first_timestamp
    status = "PASS" if count and not errors and bench.state.safety_trip is None else "FAIL"
    return HILReport(
        status=status, rows=count, duration_s=duration,
        measured_impulse_N_s=bench.state.impulse_N_s,
        measured_electrical_energy_J=bench.state.electrical_energy_J,
        peak_abs_force_N=peak_force, peak_current_A=peak_current,
        peak_temperature_C=peak_temperature if count else 0.0,
        safety_trip=bench.state.safety_trip, validation_errors=tuple(errors),
    )


def audit_csv(path: str | Path, config: BenchConfig | None = None) -> HILReport:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = tuple(column for column in REQUIRED_COLUMNS if column not in (reader.fieldnames or []))
        if missing:
            return HILReport("FAIL", 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, None, missing_columns=missing)
        return audit_rows(reader, config)


def report_json(report: HILReport) -> str:
    return json.dumps(report.as_dict(), indent=2, sort_keys=True)
