"""Independent SI reconstruction primitives for a static spherical shell.

This freezes rho as mass density [kg/m^3], pressure as [Pa], enclosed mass as
[kg], and metric exponents a,b as dimensionless. It implements the SI form of
the TOV equation and radial metric equations used in arXiv:2405.02709v1,
Eqs. (21), (24), and (25).
"""

from __future__ import annotations

import math
from typing import Sequence

G = 6.67430e-11
C = 299_792_458.0


def _profiles(radii: Sequence[float], *profiles: Sequence[float]) -> tuple[list[float], ...]:
    r = [float(x) for x in radii]
    if len(r) < 3 or r[0] < 0.0 or any(y <= x for x, y in zip(r, r[1:])):
        raise ValueError("radii must be nonnegative, strictly increasing, and length >= 3")
    result = [r]
    for profile in profiles:
        p = [float(x) for x in profile]
        if len(p) != len(r) or not all(math.isfinite(x) for x in p):
            raise ValueError("profiles must be finite and match radii")
        result.append(p)
    return tuple(result)


def cumulative_mass_kg(radii_m: Sequence[float], density_kg_m3: Sequence[float]) -> list[float]:
    r, rho = _profiles(radii_m, density_kg_m3)
    if any(x < 0.0 for x in rho):
        raise ValueError("density must be nonnegative")
    mass = [0.0]
    for i in range(1, len(r)):
        f0 = 4.0 * math.pi * r[i - 1] ** 2 * rho[i - 1]
        f1 = 4.0 * math.pi * r[i] ** 2 * rho[i]
        mass.append(mass[-1] + 0.5 * (f0 + f1) * (r[i] - r[i - 1]))
    return mass


def compactness(enclosed_mass_kg: float, radius_m: float) -> float:
    if radius_m == 0.0:
        return 0.0 if enclosed_mass_kg == 0.0 else math.inf
    return 2.0 * G * enclosed_mass_kg / (C * C * radius_m)


def tov_gradient_pa_m(radius_m: float, density_kg_m3: float, pressure_pa: float, mass_kg: float) -> float:
    """dP/dr in SI units for rho [kg/m^3], P [Pa], m [kg]."""
    if radius_m <= 0.0:
        raise ValueError("radius_m must be positive")
    if density_kg_m3 < 0.0 or pressure_pa < 0.0 or mass_kg < 0.0:
        raise ValueError("density, pressure, and mass must be nonnegative")
    horizon = 1.0 - compactness(mass_kg, radius_m)
    if horizon <= 0.0:
        raise ValueError("TOV equation is singular at or inside a horizon")
    inertial_density = density_kg_m3 + pressure_pa / (C * C)
    active_mass_over_r2 = mass_kg / (radius_m * radius_m) + 4.0 * math.pi * radius_m * pressure_pa / (C * C)
    return -G * inertial_density * active_mass_over_r2 / horizon


def integrate_tov_pressure_pa(
    radii_m: Sequence[float],
    density_kg_m3: Sequence[float],
    enclosed_mass_kg: Sequence[float],
    *,
    cavity_radius_m: float,
) -> list[float]:
    """Integrate inward from P(r_max)=0 using a midpoint predictor."""
    r, rho, mass = _profiles(radii_m, density_kg_m3, enclosed_mass_kg)
    if cavity_radius_m < 0.0 or cavity_radius_m >= r[-1]:
        raise ValueError("cavity_radius_m must lie inside the grid")
    if any(x < 0.0 for x in rho) or any(x < 0.0 for x in mass):
        raise ValueError("density and mass must be nonnegative")
    pressure = [0.0] * len(r)
    for i in range(len(r) - 2, -1, -1):
        if r[i] < cavity_radius_m:
            pressure[i] = 0.0
            continue
        dr = r[i + 1] - r[i]
        right_p = pressure[i + 1]
        g_right = tov_gradient_pa_m(r[i + 1], rho[i + 1], right_p, mass[i + 1])
        mid_p = max(0.0, right_p - 0.5 * dr * g_right)
        mid_r = 0.5 * (r[i] + r[i + 1])
        mid_rho = 0.5 * (rho[i] + rho[i + 1])
        mid_mass = 0.5 * (mass[i] + mass[i + 1])
        g_mid = tov_gradient_pa_m(mid_r, mid_rho, mid_p, mid_mass)
        pressure[i] = max(0.0, right_p - dr * g_mid)
    return pressure


def metric_a_gradient_per_m(radius_m: float, pressure_pa: float, mass_kg: float) -> float:
    """da/dr from paper Eq. (25), with a dimensionless and r in metres."""
    if radius_m <= 0.0:
        raise ValueError("radius_m must be positive")
    if pressure_pa < 0.0 or mass_kg < 0.0:
        raise ValueError("pressure and mass must be nonnegative")
    horizon = 1.0 - compactness(mass_kg, radius_m)
    if horizon <= 0.0:
        raise ValueError("metric gradient is singular at or inside a horizon")
    return G * (
        mass_kg / (C * C * radius_m * radius_m)
        + 4.0 * math.pi * radius_m * pressure_pa / C**4
    ) / horizon


def radial_metric(
    radii_m: Sequence[float],
    pressure_pa: Sequence[float],
    enclosed_mass_kg: Sequence[float],
) -> tuple[list[float], list[float]]:
    """Return exp(2a), exp(2b), anchored to exterior Schwarzschild at r_max."""
    r, pressure, mass = _profiles(radii_m, pressure_pa, enclosed_mass_kg)
    if any(x < 0.0 for x in pressure) or any(x < 0.0 for x in mass):
        raise ValueError("pressure and mass must be nonnegative")
    e2b: list[float] = []
    for radius, m in zip(r, mass):
        q = compactness(m, radius)
        if q >= 1.0:
            raise ValueError("metric contains a horizon")
        e2b.append(1.0 / (1.0 - q))
    q_outer = compactness(mass[-1], r[-1])
    a = [0.0] * len(r)
    a[-1] = 0.5 * math.log1p(-q_outer)
    for i in range(len(r) - 2, 0, -1):
        dr = r[i + 1] - r[i]
        mid_r = 0.5 * (r[i] + r[i + 1])
        mid_p = 0.5 * (pressure[i] + pressure[i + 1])
        mid_m = 0.5 * (mass[i] + mass[i + 1])
        a[i] = a[i + 1] - dr * metric_a_gradient_per_m(mid_r, mid_p, mid_m)
    a[0] = a[1]
    return [math.exp(2.0 * x) for x in a], e2b


def tangential_pressure_pa(
    radii_m: Sequence[float],
    density_kg_m3: Sequence[float],
    radial_pressure_pa: Sequence[float],
    enclosed_mass_kg: Sequence[float],
) -> list[float]:
    """Infer tangential pressure from static anisotropic stress conservation."""
    r, rho, pr, mass = _profiles(radii_m, density_kg_m3, radial_pressure_pa, enclosed_mass_kg)
    derivative = [0.0] * len(r)
    derivative[0] = (pr[1] - pr[0]) / (r[1] - r[0])
    derivative[-1] = (pr[-1] - pr[-2]) / (r[-1] - r[-2])
    for i in range(1, len(r) - 1):
        derivative[i] = (pr[i + 1] - pr[i - 1]) / (r[i + 1] - r[i - 1])
    pt = [pr[0]]
    for i in range(1, len(r)):
        a_prime = metric_a_gradient_per_m(r[i], pr[i], mass[i])
        epsilon = rho[i] * C * C
        pt.append(pr[i] + 0.5 * r[i] * (derivative[i] + (epsilon + pr[i]) * a_prime))
    return pt


def energy_condition_margins_pa(
    energy_density_pa: float,
    radial_pressure_pa: float,
    tangential_pressure_pa: float,
) -> dict[str, float]:
    """Return minimum diagonal-frame margins; negative means violation."""
    eps, pr, pt = energy_density_pa, radial_pressure_pa, tangential_pressure_pa
    return {
        "NEC": min(eps + pr, eps + pt),
        "WEC": min(eps, eps + pr, eps + pt),
        "DEC": min(eps - abs(pr), eps - abs(pt)),
        "SEC": min(eps + pr, eps + pt, eps + pr + 2.0 * pt),
    }


def diagonal_energy_conditions(
    energy_density_pa: float,
    radial_pressure_pa: float,
    tangential_pressure_pa: float,
) -> dict[str, bool]:
    values = (energy_density_pa, radial_pressure_pa, tangential_pressure_pa)
    if not all(math.isfinite(x) for x in values):
        return {name: False for name in ("NEC", "WEC", "DEC", "SEC")}
    return {name: margin >= 0.0 for name, margin in energy_condition_margins_pa(*values).items()}
