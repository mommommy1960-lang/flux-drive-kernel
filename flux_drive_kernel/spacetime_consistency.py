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
