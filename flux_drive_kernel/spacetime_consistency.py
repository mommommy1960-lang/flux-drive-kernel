"""Conservative checks for speculative spacetime geometries.

These functions evaluate declared mathematical conditions. They do not model a
constructible device or establish transport, propulsion, or FTL.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

G_M3_KG_S2 = 6.67430e-11
C_M_S = 299_792_458.0


def _finite(name: str, value: float) -> float:
    if not math.isfinite(value):
        raise ValueError(name + " must be finite")
    return value


@dataclass(frozen=True)
class WormholeThroatAssessment:
    radius_matches: bool
    finite_redshift: bool
    flares_out: bool
    radial_nec_j_m3: float

    @property
    def geometric_throat_conditions_pass(self) -> bool:
        return self.radius_matches and self.finite_redshift and self.flares_out

    @property
    def radial_nec_is_violated(self) -> bool:
        return self.radial_nec_j_m3 < 0.0


def assess_morris_thorne_throat(
    throat_radius_m: float,
    shape_at_throat_m: float,
    shape_derivative: float,
    redshift_at_throat: float,
    *,
    relative_tolerance: float = 1e-9,
) -> WormholeThroatAssessment:
    """Evaluate necessary throat conditions for a Morris-Thorne ansatz.

    radial_nec_j_m3 is the orthonormal radial null-energy combination
    rho_energy + p_r at the throat:
    c^4 (b'(r0)-1) / (8 pi G r0^2).

    A negative value is an energy-condition problem, not a source prescription.
    Passing the geometric checks is necessary but nowhere near sufficient.
    """

    r0 = _finite("throat_radius_m", throat_radius_m)
    b0 = _finite("shape_at_throat_m", shape_at_throat_m)
    bp = _finite("shape_derivative", shape_derivative)
    phi = _finite("redshift_at_throat", redshift_at_throat)
    tol = _finite("relative_tolerance", relative_tolerance)
    if r0 <= 0.0:
        raise ValueError("throat_radius_m must be positive")
    if tol < 0.0:
        raise ValueError("relative_tolerance must be nonnegative")

    radial_nec = C_M_S**4 * (bp - 1.0) / (8.0 * math.pi * G_M3_KG_S2 * r0**2)
    return WormholeThroatAssessment(
        radius_matches=math.isclose(b0, r0, rel_tol=tol, abs_tol=tol * r0),
        finite_redshift=math.isfinite(phi),
        flares_out=bp < 1.0,
        radial_nec_j_m3=radial_nec,
    )


def alcubierre_top_hat_shape(radius_m: float, bubble_radius_m: float, sigma_per_m: float) -> float:
    """Return Alcubierre's smooth top-hat profile at radial distance."""

    r = _finite("radius_m", radius_m)
    radius = _finite("bubble_radius_m", bubble_radius_m)
    sigma = _finite("sigma_per_m", sigma_per_m)
    if r < 0.0 or radius <= 0.0 or sigma <= 0.0:
        raise ValueError("radius must be nonnegative; bubble radius and sigma must be positive")
    denominator = 2.0 * math.tanh(sigma * radius)
    return (
        math.tanh(sigma * (r + radius))
        - math.tanh(sigma * (r - radius))
    ) / denominator


def required_average_speed_m_s(distance_m: float, transit_time_s: float) -> float:
    """Return distance/time as a reporting check, not a prediction."""

    distance = _finite("distance_m", distance_m)
    duration = _finite("transit_time_s", transit_time_s)
    if distance < 0.0 or duration <= 0.0:
        raise ValueError("distance must be nonnegative and transit_time_s positive")
    return distance / duration

@dataclass(frozen=True)
class OrthonormalStressEnergy:
    """Diagonal orthonormal stress-energy components, all in J/m^3."""

    energy_density_j_m3: float
    radial_pressure_j_m3: float
    tangential_pressure_j_m3: float

    @property
    def radial_nec_j_m3(self) -> float:
        return self.energy_density_j_m3 + self.radial_pressure_j_m3

    @property
    def tangential_nec_j_m3(self) -> float:
        return self.energy_density_j_m3 + self.tangential_pressure_j_m3

    def tensor_diagonal_j_m3(self) -> tuple[float, float, float, float]:
        return (
            self.energy_density_j_m3,
            self.radial_pressure_j_m3,
            self.tangential_pressure_j_m3,
            self.tangential_pressure_j_m3,
        )


@dataclass(frozen=True)
class ZeroTidalScanPoint:
    throat_radius_m: float
    radius_m: float
    shape_m: float
    shape_derivative: float
    horizon_free_at_point: bool
    stress_energy: OrthonormalStressEnergy
    stability_assessed: bool = False


def zero_tidal_shape_m(radius_m: float, throat_radius_m: float) -> float:
    """Return b(r)=r0^2/r for the frozen zero-redshift metric."""
    r = _finite("radius_m", radius_m)
    r0 = _finite("throat_radius_m", throat_radius_m)
    if r0 <= 0.0 or r < r0:
        raise ValueError("require throat_radius_m > 0 and radius_m >= throat_radius_m")
    return r0**2 / r


def zero_tidal_shape_derivative(radius_m: float, throat_radius_m: float) -> float:
    """Return db/dr for b(r)=r0^2/r."""
    r = _finite("radius_m", radius_m)
    r0 = _finite("throat_radius_m", throat_radius_m)
    if r0 <= 0.0 or r < r0:
        raise ValueError("require throat_radius_m > 0 and radius_m >= throat_radius_m")
    return -(r0**2) / r**2


def zero_tidal_stress_energy(radius_m: float, throat_radius_m: float) -> OrthonormalStressEnergy:
    """Return the complete diagonal source for the frozen metric.

    Frozen ansatz:
        ds^2 = -c^2 dt^2 + dr^2/(1-b/r) + r^2 dOmega^2
        b(r) = r0^2/r

    In an orthonormal frame and SI energy-density units:
        epsilon = (c^4/8 pi G) b'/r^2
        p_r     = -(c^4/8 pi G) b/r^3
        p_t     = (c^4/16 pi G) (b-r b')/r^3

    Symmetry makes all off-diagonal components zero. This derives a required
    source; it does not identify matter capable of producing it.
    """
    r = _finite("radius_m", radius_m)
    r0 = _finite("throat_radius_m", throat_radius_m)
    b = zero_tidal_shape_m(r, r0)
    bp = zero_tidal_shape_derivative(r, r0)
    scale = C_M_S**4 / (8.0 * math.pi * G_M3_KG_S2)
    epsilon = scale * bp / r**2
    radial_pressure = -scale * b / r**3
    tangential_pressure = 0.5 * scale * (b - r * bp) / r**3
    return OrthonormalStressEnergy(epsilon, radial_pressure, tangential_pressure)


def scan_zero_tidal_metric(
    throat_radius_m: float, radius_multipliers: tuple[float, ...]
) -> tuple[ZeroTidalScanPoint, ...]:
    """Evaluate the frozen metric at declared multiples of the throat radius."""
    r0 = _finite("throat_radius_m", throat_radius_m)
    if r0 <= 0.0:
        raise ValueError("throat_radius_m must be positive")
    if not radius_multipliers:
        raise ValueError("radius_multipliers must not be empty")
    points = []
    for multiplier in radius_multipliers:
        value = _finite("radius_multiplier", multiplier)
        if value < 1.0:
            raise ValueError("every radius multiplier must be at least 1")
        radius = value * r0
        shape = zero_tidal_shape_m(radius, r0)
        points.append(
            ZeroTidalScanPoint(
                throat_radius_m=r0,
                radius_m=radius,
                shape_m=shape,
                shape_derivative=zero_tidal_shape_derivative(radius, r0),
                horizon_free_at_point=True,
                stress_energy=zero_tidal_stress_energy(radius, r0),
            )
        )
    return tuple(points)

