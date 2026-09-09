"""Conventional spacecraft-propulsion reference calculations for Aurora.

These are standard ideal relations used for mission trade studies. They do not
select hardware, authorize construction, or validate the experimental Flux
Drive. Real propulsion sizing requires qualified design work, losses, margins,
thermal limits, structural loads, propellant storage/feed systems, lifetime,
EMC, controls, and mission-specific constraints.
"""

from __future__ import annotations

import math

G0_M_S2 = 9.80665


def _finite_positive(name: str, value: float) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def _finite_nonnegative(name: str, value: float) -> float:
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return value


def exhaust_velocity_m_s(specific_impulse_s: float) -> float:
    """Convert specific impulse to effective exhaust velocity, v_e = Isp*g0."""
    return _finite_positive("specific_impulse_s", specific_impulse_s) * G0_M_S2


def specific_impulse_s(exhaust_velocity_m_s_value: float) -> float:
    """Convert effective exhaust velocity to specific impulse."""
    return _finite_positive("exhaust_velocity_m_s", exhaust_velocity_m_s_value) / G0_M_S2


def ideal_rocket_delta_v_m_s(
    initial_mass_kg: float,
    final_mass_kg: float,
    specific_impulse_s_value: float,
) -> float:
    """Ideal Tsiolkovsky delta-v for a reaction-mass propulsion stage."""
    m0 = _finite_positive("initial_mass_kg", initial_mass_kg)
    mf = _finite_positive("final_mass_kg", final_mass_kg)
    if mf > m0:
        raise ValueError("final_mass_kg cannot exceed initial_mass_kg")
    ve = exhaust_velocity_m_s(specific_impulse_s_value)
    return ve * math.log(m0 / mf)


def mass_ratio_for_delta_v(
    delta_v_m_s: float,
    specific_impulse_s_value: float,
) -> float:
    """Ideal initial/final mass ratio required for nonnegative delta-v."""
    dv = _finite_nonnegative("delta_v_m_s", delta_v_m_s)
    ve = exhaust_velocity_m_s(specific_impulse_s_value)
    exponent = dv / ve
    try:
        return math.exp(exponent)
    except OverflowError as exc:
        raise ValueError("requested delta-v implies an unrepresentable mass ratio") from exc


def propellant_fraction_for_delta_v(
    delta_v_m_s: float,
    specific_impulse_s_value: float,
) -> float:
    """Ideal propellant fraction relative to initial mass, ignoring tank/engine mass."""
    ratio = mass_ratio_for_delta_v(delta_v_m_s, specific_impulse_s_value)
    return 1.0 - 1.0 / ratio


def thrust_from_mass_flow_N(
    propellant_mass_flow_kg_s: float,
    specific_impulse_s_value: float,
) -> float:
    """Ideal thrust F = m_dot * v_e, neglecting pressure-thrust terms."""
    mdot = _finite_nonnegative("propellant_mass_flow_kg_s", propellant_mass_flow_kg_s)
    return mdot * exhaust_velocity_m_s(specific_impulse_s_value)


def mass_flow_for_thrust_kg_s(
    thrust_N: float,
    specific_impulse_s_value: float,
) -> float:
    """Ideal propellant mass flow needed for a specified nonnegative thrust."""
    thrust = _finite_nonnegative("thrust_N", thrust_N)
    return thrust / exhaust_velocity_m_s(specific_impulse_s_value)


def ideal_electric_thrust_from_power_N(
    input_power_W: float,
    specific_impulse_s_value: float,
    *,
    jet_power_efficiency: float = 1.0,
) -> float:
    """Ideal electric-propulsion thrust from kinetic jet power.

    Uses P_jet = 0.5*m_dot*v_e^2 and F = m_dot*v_e, giving
    F = 2*eta*P_input/v_e. This is a reference ceiling for the declared
    efficiency, not a hardware performance guarantee.
    """
    power = _finite_nonnegative("input_power_W", input_power_W)
    if not math.isfinite(jet_power_efficiency) or not (0 < jet_power_efficiency <= 1):
        raise ValueError("jet_power_efficiency must be finite and in (0, 1]")
    ve = exhaust_velocity_m_s(specific_impulse_s_value)
    return 2.0 * jet_power_efficiency * power / ve


def acceleration_from_thrust_m_s2(thrust_N: float, vehicle_mass_kg: float) -> float:
    """Return ideal instantaneous acceleration from net thrust and vehicle mass."""
    thrust = _finite_nonnegative("thrust_N", thrust_N)
    mass = _finite_positive("vehicle_mass_kg", vehicle_mass_kg)
    return thrust / mass
