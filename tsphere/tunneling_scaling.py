"""Order-of-magnitude tunneling scaling for the T-Sphere hypothesis.

This is the rectangular-barrier WKB exponent for one coherent degree of
freedom. It is a screening calculation, not a model of a macroscopic robot.
The point is to expose how barrier width and mass enter the probability.
"""

from __future__ import annotations

import math


HBAR_J_S = 1.054_571_817e-34
EV_J = 1.602_176_634e-19
ELECTRON_MASS_KG = 9.109_383_7015e-31


def log10_transmission(mass_kg: float, barrier_height_ev: float, width_m: float) -> float:
    """Return log10 of the WKB transmission estimate.

    Assumes E is below a rectangular barrier by ``barrier_height_ev``. The
    result is intentionally logarithmic because direct probabilities underflow.
    """
    if mass_kg <= 0 or barrier_height_ev <= 0 or width_m < 0:
        raise ValueError("mass, barrier height, and width must be positive")
    delta_e = barrier_height_ev * EV_J
    kappa = math.sqrt(2.0 * mass_kg * delta_e) / HBAR_J_S
    return -2.0 * kappa * width_m / math.log(10.0)


def mass_scaling_ratio(mass_a_kg: float, mass_b_kg: float) -> float:
    """Return sqrt(mass_a/mass_b), the ratio of WKB exponents."""
    if mass_a_kg <= 0 or mass_b_kg <= 0:
        raise ValueError("masses must be positive")
    return math.sqrt(mass_a_kg / mass_b_kg)


if __name__ == "__main__":
    for label, mass in (("electron", ELECTRON_MASS_KG), ("one gram", 1e-3), ("one kg", 1.0)):
        print(label, log10_transmission(mass, barrier_height_ev=1.0, width_m=0.01))
