"""Deterministic actuator-bench model with fail-closed safety interlocks.

This module models a controllable force-producing bench channel. It is useful
for controller development and HIL plumbing, but it deliberately does not
infer propulsion, reactionless force, or exotic physics from a command signal.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
import math
from typing import Dict, Optional


def _finite(name: str, value: float) -> float:
    if not math.isfinite(float(value)):
        raise ValueError(f"{name} must be finite")
    return float(value)


@dataclass(frozen=True)
class BenchConfig:
    mass_kg: float = 1.0
    max_command: float = 1.0
    max_force_N: float = 10.0
    supply_voltage_V: float = 24.0
    max_current_A: float = 5.0
    force_per_amp_N_A: float = 1.0
    ambient_temperature_C: float = 22.0
    max_temperature_C: float = 70.0
    thermal_resistance_C_W: float = 0.8
    thermal_time_constant_s: float = 12.0

    def __post_init__(self) -> None:
        values = {
            "mass_kg": self.mass_kg,
            "max_command": self.max_command,
            "max_force_N": self.max_force_N,
            "supply_voltage_V": self.supply_voltage_V,
            "max_current_A": self.max_current_A,
            "force_per_amp_N_A": self.force_per_amp_N_A,
            "ambient_temperature_C": self.ambient_temperature_C,
            "max_temperature_C": self.max_temperature_C,
            "thermal_resistance_C_W": self.thermal_resistance_C_W,
            "thermal_time_constant_s": self.thermal_time_constant_s,
        }
        for name, value in values.items():
            _finite(name, value)
        positive = {
            "mass_kg": self.mass_kg,
            "max_force_N": self.max_force_N,
            "supply_voltage_V": self.supply_voltage_V,
            "max_current_A": self.max_current_A,
            "force_per_amp_N_A": self.force_per_amp_N_A,
            "thermal_time_constant_s": self.thermal_time_constant_s,
        }
        for name, value in positive.items():
            if value <= 0:
                raise ValueError(f"{name} must be positive")
        if self.max_command <= 0 or self.max_command > 1:
            raise ValueError("max_command must be in (0, 1]")
        if self.max_temperature_C <= self.ambient_temperature_C:
            raise ValueError("max_temperature_C must exceed ambient_temperature_C")
        if self.thermal_resistance_C_W < 0:
            raise ValueError("thermal_resistance_C_W cannot be negative")


@dataclass
class BenchState:
    time_s: float = 0.0
    position_m: float = 0.0
    velocity_m_s: float = 0.0
    temperature_C: float = 22.0
    command: float = 0.0
    current_A: float = 0.0
    force_N: float = 0.0
    impulse_N_s: float = 0.0
    electrical_energy_J: float = 0.0
    safety_trip: Optional[str] = None

    def as_dict(self) -> Dict[str, object]:
        return asdict(self)


class FluxDriveBench:
    """A fail-closed software plant for bench and HIL development.

    The default simulated actuator uses a linear signed force law:

        |I| = |command| * I_max
        F = sign(command) * |I| * K_F

    where ``K_F`` is ``force_per_amp_N_A``. Thermal and electrical-energy
    calculations use current magnitude; force direction comes from command
    sign. Measured HIL force is preserved as an instrument channel and is never
    silently clipped to the simulated actuator limit.
    """

    def __init__(self, config: BenchConfig | None = None) -> None:
        self.config = config or BenchConfig()
        self.state = BenchState(
            temperature_C=self.config.ambient_temperature_C
        )

    @property
    def stopped(self) -> bool:
        return self.state.safety_trip is not None

    def emergency_stop(self, reason: str = "emergency_stop") -> None:
        self.state.safety_trip = reason
        self.state.command = 0.0
        self.state.current_A = 0.0
        self.state.force_N = 0.0

    def reset(self) -> None:
        self.state = BenchState(
            temperature_C=self.config.ambient_temperature_C
        )

    def step(
        self,
        command: float,
        dt_s: float = 0.01,
        measured_force_N: float | None = None,
        measured_current_A: float | None = None,
        measured_temperature_C: float | None = None,
        measured_voltage_V: float | None = None,
    ) -> BenchState:
        """Advance one timestep using simulated or measured HIL channels.

        ``dt_s=0`` is permitted for an initial sampled state. It updates the
        instantaneous measured/model channels without inventing impulse or
        energy before the first real time interval.
        """
        command = _finite("command", command)
        dt_s = _finite("dt_s", dt_s)
        if dt_s < 0:
            raise ValueError("dt_s must be nonnegative")
        if self.stopped:
            return self.state

        if measured_force_N is not None:
            measured_force_N = _finite("measured_force_N", measured_force_N)
        if measured_current_A is not None:
            measured_current_A = _finite("measured_current_A", measured_current_A)
        if measured_temperature_C is not None:
            measured_temperature_C = _finite("measured_temperature_C", measured_temperature_C)
        if measured_voltage_V is not None:
            measured_voltage_V = _finite("measured_voltage_V", measured_voltage_V)

        command = max(-self.config.max_command, min(self.config.max_command, command))
        current_magnitude = (
            abs(measured_current_A)
            if measured_current_A is not None
            else abs(command) * self.config.max_current_A
        )
        voltage = self.config.supply_voltage_V if measured_voltage_V is None else measured_voltage_V
        if voltage < 0:
            raise ValueError("measured_voltage_V cannot be negative")
        temperature = (
            measured_temperature_C
            if measured_temperature_C is not None
            else self._temperature_step(current_magnitude, dt_s)
        )

        if current_magnitude > self.config.max_current_A:
            self.emergency_stop("over_current")
            return self.state
        if temperature >= self.config.max_temperature_C:
            self.emergency_stop("over_temperature")
            return self.state

        if measured_force_N is not None:
            # Instrument data are evidence, not a simulated control output.
            # Preserve the measured value rather than clipping it to max_force_N.
            force = measured_force_N
        elif command == 0.0:
            force = 0.0
        else:
            direction = 1.0 if command > 0.0 else -1.0
            force = direction * current_magnitude * self.config.force_per_amp_N_A
            force = max(-self.config.max_force_N, min(self.config.max_force_N, force))

        acceleration = force / self.config.mass_kg
        self.state.velocity_m_s += acceleration * dt_s
        self.state.position_m += self.state.velocity_m_s * dt_s
        self.state.time_s += dt_s
        self.state.temperature_C = temperature
        self.state.command = command
        self.state.current_A = current_magnitude
        self.state.force_N = force
        self.state.impulse_N_s += force * dt_s
        self.state.electrical_energy_J += voltage * current_magnitude * dt_s
        return self.state

    def _temperature_step(self, current_A: float, dt_s: float) -> float:
        power_W = self.config.supply_voltage_V * current_A
        equilibrium = self.config.ambient_temperature_C + (
            power_W * self.config.thermal_resistance_C_W
        )
        alpha = min(1.0, dt_s / self.config.thermal_time_constant_s)
        return self.state.temperature_C + alpha * (
            equilibrium - self.state.temperature_C
        )
