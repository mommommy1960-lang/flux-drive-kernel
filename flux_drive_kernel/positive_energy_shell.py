"""Stage-one reproduction of the positive-mass shell in arXiv:2405.02709.

This implements the paper's unsmoothed equations (19)-(20) in SI units. It is
the conventional shell baseline, not the later numerical warp-shell solution.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

G_M3_KG_S2 = 6.67430e-11
C_M_S = 299_792_458.0


def _finite_positive(name: str, value: float, *, allow_zero: bool = False) -> float:
    if not math.isfinite(value) or value < 0.0 or (value == 0.0 and not allow_zero):
        qualifier = "nonnegative" if allow_zero else "positive"
        raise ValueError(name + " must be finite and " + qualifier)
    return value


@dataclass(frozen=True)
class ConstantDensityShell:
    inner_radius_m: float
    outer_radius_m: float
    total_mass_kg: float

    def __post_init__(self) -> None:
        r1 = _finite_positive("inner_radius_m", self.inner_radius_m, allow_zero=True)
        r2 = _finite_positive("outer_radius_m", self.outer_radius_m)
        _finite_positive("total_mass_kg", self.total_mass_kg)
        if r2 <= r1:
            raise ValueError("outer_radius_m must exceed inner_radius_m")

    @property
    def volume_m3(self) -> float:
        return 4.0 * math.pi * (self.outer_radius_m**3 - self.inner_radius_m**3) / 3.0

    @property
    def density_kg_m3(self) -> float:
        return self.total_mass_kg / self.volume_m3

    def density_at_radius_kg_m3(self, radius_m: float) -> float:
        radius = _finite_positive("radius_m", radius_m, allow_zero=True)
        if self.inner_radius_m <= radius <= self.outer_radius_m:
            return self.density_kg_m3
        return 0.0

    def enclosed_mass_kg(self, radius_m: float) -> float:
        """Return the exact piecewise cumulative mass from paper equation (20)."""
        radius = _finite_positive("radius_m", radius_m, allow_zero=True)
        if radius <= self.inner_radius_m:
            return 0.0
        if radius >= self.outer_radius_m:
            return self.total_mass_kg
        numerator = radius**3 - self.inner_radius_m**3
        denominator = self.outer_radius_m**3 - self.inner_radius_m**3
        return self.total_mass_kg * numerator / denominator

    def compactness(self, radius_m: float) -> float:
        """Return 2 G m(r)/(c^2 r), with the regular center defined as zero."""
        radius = _finite_positive("radius_m", radius_m, allow_zero=True)
        if radius == 0.0:
            return 0.0
        return 2.0 * G_M3_KG_S2 * self.enclosed_mass_kg(radius) / (C_M_S**2 * radius)

    def horizon_free_at(self, radius_m: float) -> bool:
        return self.compactness(radius_m) < 1.0

    @property
    def exterior_adm_mass_kg(self) -> float:
        return self.total_mass_kg
