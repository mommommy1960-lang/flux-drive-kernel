"""Auditable Aurora system bookkeeping.

This module performs design-accounting checks only. It does not control
actuators and cannot establish physical propulsion.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


G0 = 9.80665


def _finite_nonnegative(name: str, value: float) -> float:
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return value


@dataclass(frozen=True)
class Budget:
    """Electrical power-flow ledger for a declared design interval.

    ``input_power_w`` is power entering from generation or an upstream bus.
    ``storage_discharge_power_w`` is an additional source from batteries or
    other storage; ``storage_charge_power_w`` is a sink into storage.

    ``thermal_power_w`` means *active thermal-management electrical load*
    (fans, pumps, chillers, heaters, etc.). It must not be used for heat already
    represented by actuator/control/loss power, or energy would be double-
    counted. Heat generation/rejection belongs in ``ThermalBudget``.
    """

    mass_kg: float
    input_power_w: float
    actuator_power_w: float
    control_power_w: float
    thermal_power_w: float
    losses_power_w: float
    exported_power_w: float = 0.0
    storage_charge_power_w: float = 0.0
    storage_discharge_power_w: float = 0.0

    @property
    def source_power_w(self) -> float:
        return self.input_power_w + self.storage_discharge_power_w

    @property
    def accounted_power_w(self) -> float:
        return (
            self.actuator_power_w
            + self.control_power_w
            + self.thermal_power_w
            + self.losses_power_w
            + self.exported_power_w
            + self.storage_charge_power_w
        )

    @property
    def power_residual_w(self) -> float:
        return self.source_power_w - self.accounted_power_w

    @property
    def net_storage_power_w(self) -> float:
        """Positive when storage is charging; negative when discharging."""
        return self.storage_charge_power_w - self.storage_discharge_power_w

    def validate(self) -> None:
        if not math.isfinite(self.mass_kg) or self.mass_kg <= 0:
            raise ValueError("mass_kg must be finite and positive")
        for name, value in {
            "input_power_w": self.input_power_w,
            "actuator_power_w": self.actuator_power_w,
            "control_power_w": self.control_power_w,
            "thermal_power_w": self.thermal_power_w,
            "losses_power_w": self.losses_power_w,
            "exported_power_w": self.exported_power_w,
            "storage_charge_power_w": self.storage_charge_power_w,
            "storage_discharge_power_w": self.storage_discharge_power_w,
        }.items():
            _finite_nonnegative(name, value)
        tolerance = max(1e-9, abs(self.source_power_w) * 1e-9)
        if abs(self.power_residual_w) > tolerance:
            raise ValueError("electrical power-flow ledger does not close")


@dataclass(frozen=True)
class ThermalBudget:
    """First-law thermal power balance for a declared control volume.

    Positive ``stored_heat_rate_w`` means internal thermal energy is increasing.
    The balance is:

        heat_generated + heat_absorbed_external
        = heat_rejected + stored_heat_rate

    This is bookkeeping only; radiator sizing still requires temperatures,
    emissivity, geometry, view factors, coolant behavior, and mission boundary
    conditions.
    """

    heat_generated_w: float
    heat_absorbed_external_w: float
    heat_rejected_w: float
    stored_heat_rate_w: float = 0.0

    @property
    def thermal_residual_w(self) -> float:
        return (
            self.heat_generated_w
            + self.heat_absorbed_external_w
            - self.heat_rejected_w
            - self.stored_heat_rate_w
        )

    def validate(self) -> None:
        for name, value in {
            "heat_generated_w": self.heat_generated_w,
            "heat_absorbed_external_w": self.heat_absorbed_external_w,
            "heat_rejected_w": self.heat_rejected_w,
        }.items():
            _finite_nonnegative(name, value)
        if not math.isfinite(self.stored_heat_rate_w):
            raise ValueError("stored_heat_rate_w must be finite")
        scale = max(
            1.0,
            self.heat_generated_w,
            self.heat_absorbed_external_w,
            self.heat_rejected_w,
            abs(self.stored_heat_rate_w),
        )
        if abs(self.thermal_residual_w) > 1e-9 * scale:
            raise ValueError("thermal power ledger does not close")


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
    value describes commanded downward acceleration rather than lift. This
    near-surface equation is not an orbital-flight model.
    """
    return required_net_force(mass_kg, G0 + vertical_acceleration_m_s2)


def momentum_residual(vehicle_delta_p: float, exhaust_delta_p: float,
                      radiation_delta_p: float, environment_delta_p: float) -> float:
    """Return the signed momentum-accounting residual for a declared boundary."""
    values = (vehicle_delta_p, exhaust_delta_p, radiation_delta_p, environment_delta_p)
    if not all(math.isfinite(float(v)) for v in values):
        raise ValueError("momentum terms must be finite")
    return sum(values)
