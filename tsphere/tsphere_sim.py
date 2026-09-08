"""Deterministic, hardware-neutral T-Sphere control demonstrator."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List


class Mode(str, Enum):
    SAFE = "SAFE"
    ROAM = "ROAM"
    MORPH = "MORPH"
    INSPECT = "INSPECT"
    HANDOFF = "HANDOFF"


@dataclass
class Telemetry:
    sequence: int
    mode: Mode
    radius_mm: float
    battery_v: float
    temperature_c: float
    emergency_stop: bool
    barrier_side: str
    note: str = ""


@dataclass
class TSphere:
    radius_mm: float = 45.0
    min_radius_mm: float = 30.0
    max_radius_mm: float = 50.0
    battery_v: float = 7.4
    temperature_c: float = 22.0
    barrier_side: str = "A"
    mode: Mode = Mode.SAFE
    emergency_stop: bool = False
    sequence: int = 0
    telemetry: List[Telemetry] = field(default_factory=list)

    def _record(self, note: str = "") -> Telemetry:
        self.sequence += 1
        item = Telemetry(
            self.sequence, self.mode, self.radius_mm, self.battery_v,
            self.temperature_c, self.emergency_stop, self.barrier_side, note
        )
        self.telemetry.append(item)
        return item

    def command(self, name: str, **kwargs: object) -> Telemetry:
        if self.emergency_stop and name != "reset":
            return self._record("command_denied: emergency_stop")
        if name == "reset":
            self.emergency_stop = False
            self.mode = Mode.SAFE
            return self._record("reset")
        if name == "stop":
            self.mode = Mode.SAFE
            return self._record("safe_stop")
        if name == "roam":
            self.mode = Mode.ROAM
            return self._record("roam")
        if name == "morph":
            target = float(kwargs["radius_mm"])
            if not self.min_radius_mm <= target <= self.max_radius_mm:
                self.emergency_stop = True
                self.mode = Mode.SAFE
                return self._record("reject: radius_limit")
            self.radius_mm = target
            self.mode = Mode.MORPH
            return self._record("morph_complete")
        if name == "inspect":
            self.mode = Mode.INSPECT
            return self._record("sensor_only_inspection")
        if name == "handoff":
            side = str(kwargs["barrier_side"])
            if side not in {"A", "B"}:
                self.emergency_stop = True
                self.mode = Mode.SAFE
                return self._record("reject: unknown_barrier_side")
            self.barrier_side = side
            self.mode = Mode.HANDOFF
            return self._record("telemetry_handoff")
        self.emergency_stop = True
        self.mode = Mode.SAFE
        return self._record("reject: unknown_command")


def demo() -> Dict[str, object]:
    sphere = TSphere()
    sphere.command("roam")
    sphere.command("morph", radius_mm=32)
    sphere.command("inspect")
    sphere.command("handoff", barrier_side="B")
    sphere.command("stop")
    return {
        "final_mode": sphere.mode.value,
        "barrier_side": sphere.barrier_side,
        "telemetry_rows": len(sphere.telemetry),
        "last_note": sphere.telemetry[-1].note,
    }


if __name__ == "__main__":
    print(demo())
