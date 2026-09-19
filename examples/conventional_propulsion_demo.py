"""Safe, dimensioned conventional-propulsion reference calculations.

This is a sandbox model only. It does not model reactionless propulsion.
"""
from __future__ import annotations

import math


def exhaust_thrust(mass_flow_kg_s: float, exhaust_velocity_m_s: float) -> float:
    return mass_flow_kg_s * exhaust_velocity_m_s


def photon_thrust(power_w: float) -> float:
    return power_w / 299_792_458.0


def impulse(force_n: float, duration_s: float) -> float:
    return force_n * duration_s


def main() -> None:
    mdot = 1.0e-6
    exhaust_velocity = 10_000.0
    duration = 10.0
    power = 100.0

    exhaust_force = exhaust_thrust(mdot, exhaust_velocity)
    photon_force = photon_thrust(power)

    print("CONVENTIONAL PROPULSION SANDBOX")
    print(f"exhaust force N: {exhaust_force:.9g}")
    print(f"exhaust impulse N*s: {impulse(exhaust_force, duration):.9g}")
    print(f"100 W photon force N: {photon_force:.9g}")
    print(f"100 W photon impulse N*s: {impulse(photon_force, duration):.9g}")
    print("reactionless propulsion proven: false")
    print("physical validation: pending")


if __name__ == "__main__":
    main()
