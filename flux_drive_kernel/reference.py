"""Compare published propulsion observations against physical reference limits."""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

SPEED_OF_LIGHT_M_S = 299_792_458.0


@dataclass(frozen=True)
class ReferenceObservation:
    experiment_id: str
    input_power_W: float
    reported_force_N: float | None
    source_url: str
    result_class: str
    calibration_status: str


def photon_pressure_force_N(input_power_W: float) -> float:
    if not math.isfinite(input_power_W) or input_power_W < 0:
        raise ValueError("input_power_W must be finite and nonnegative")
    return input_power_W / SPEED_OF_LIGHT_M_S


def force_to_power_N_W(force_N: float, input_power_W: float) -> float:
    if not math.isfinite(force_N) or not math.isfinite(input_power_W):
        raise ValueError("force and power must be finite")
    if input_power_W <= 0:
        raise ValueError("input_power_W must be positive")
    return force_N / input_power_W


def load_reference_csv(path: str | Path) -> list[ReferenceObservation]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"experiment_id", "input_power_W", "reported_force_N", "source_url", "result_class", "calibration_status"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"missing reference columns: {sorted(missing)}")
        observations = []
        for line, row in enumerate(reader, start=2):
            try:
                force_text = (row["reported_force_N"] or "").strip()
                force = None if not force_text else float(force_text)
                power = float(row["input_power_W"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"line {line}: invalid reference number") from exc
            if power <= 0 or (force is not None and not math.isfinite(force)):
                raise ValueError(f"line {line}: invalid reference value")
            observations.append(ReferenceObservation(
                row["experiment_id"], power, force, row["source_url"],
                row["result_class"], row["calibration_status"],
            ))
        return observations
