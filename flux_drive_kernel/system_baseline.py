"""Auditable Aurora system bookkeeping.

This module performs design-accounting checks only. It does not control
actuators and cannot establish physical propulsion.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


G0 = 9.80665


@dataclass(frozen=True)
class Budget:
    """Electrical input-power ledger for the current design interval.

    ``thermal_power_w`` means *active thermal-management electrical load*
    (fans, pumps, chillers, heaters, etc.). It must not be used for heat that is
    already represented by actuator/control/loss power, or that energy would be
    double-counted. Heat rejection is a separate thermal-balance calculation.
    """

    mass_kg: float
    input_power_w: float
    actuator_power_w: float
    control_power_w: float
    thermal_power_w: float
    losses_power_w: float
    exported_power_w: float = 0.0

    @property
    def accounted_power_w(self) -> float:
        return (
            self.actuator_power_w
            + self.control_power_w
            + self.thermal_power_w
            + self.losses_power_w
            + self.exported_power_w
        )

    @property
    def power_residual_w(self) -> float:
        return self.input_power_w - self.accounted_power_w

    def validate(self) -> None:
        values = (
            self.mass_kg,
            self.input_power_w,
            self.actuator_power_w,
            self.control_power_w,
            self.thermal_power_w,
            self.losses_power_w,
            self.exported_power_w,
        )
        if not all(math.isfinite(float(v)) for v in values):
            raise ValueError("budget values must be finite")
        if self.mass_kg <= 0 or any(v < 0 for v in values[1:]):
            raise ValueError("mass must be positive and power terms non-negative")
        tolerance = max(1e-9, abs(self.input_power_w) * 1e-9)
        if abs(self.power_residual_w) > tolerance:
            raise ValueError("electrical input-power ledger does not close")


def required_net_force(mass_kg: float, acceleration_m_s2: float) -> float:
    """Return F = m*a for the explicitly defined inertial frame."""
    if not math.isfinite(mass_kg) or not math.isfinite(acceleration_m_s2):
        raise ValueError("mass and acceleration must be finite")
    if mass_kg <= 0:
        raise ValueError("mass must be positive")
    return mass_kg * acceleration_m_s2


def required_vertical_lift(mass_kg: float, vertical_acceleration_m_s2: float = 0.0) -> float:
    """Actuator force for hover/upward acceleration near Earth's surface.

    Positive ``vertical_acceleration_m_s2`` is upward. A sufficiently negative
    value describes commanded downward acceleration rather than lift.
    """
    return required_net_force(mass_kg, G0 + vertical_acceleration_m_s2)


def momentum_residual(vehicle_delta_p: float, exhaust_delta_p: float,
                      radiation_delta_p: float, environment_delta_p: float) -> float:
    """Return the signed momentum-accounting residual for a declared boundary."""
    values = (vehicle_delta_p, exhaust_delta_p, radiation_delta_p, environment_delta_p)
    if not all(math.isfinite(float(v)) for v in values):
        raise ValueError("momentum terms must be finite")
    return sum(values)
