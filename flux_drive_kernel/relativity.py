"""Educational general-relativity scale calculations.

These functions quantify black-hole scales. They are not a creation recipe,
propulsion model, or claim that a black hole is a traversable portal.
"""

from __future__ import annotations

import math

G_M3_KG_S2 = 6.67430e-11
C_M_S = 299_792_458.0
HBAR_J_S = 1.054571817e-34


def _positive_mass(mass_kg: float) -> float:
    if not math.isfinite(mass_kg) or mass_kg <= 0:
        raise ValueError("mass_kg must be finite and positive")
    return mass_kg


def schwarzschild_radius_m(mass_kg: float) -> float:
    """Return the Schwarzschild radius for an ideal non-rotating mass."""
    mass_kg = _positive_mass(mass_kg)
    return 2.0 * G_M3_KG_S2 * mass_kg / C_M_S**2


def rest_energy_joules(mass_kg: float) -> float:
    """Return E=mc² for the mass, as a scale comparison."""
    mass_kg = _positive_mass(mass_kg)
    return mass_kg * C_M_S**2


def hawking_lifetime_s(mass_kg: float) -> float:
    """Return the idealized, non-rotating Hawking evaporation lifetime."""
    mass_kg = _positive_mass(mass_kg)
    return 5120.0 * math.pi * G_M3_KG_S2**2 * mass_kg**3 / (HBAR_J_S * C_M_S**4)
