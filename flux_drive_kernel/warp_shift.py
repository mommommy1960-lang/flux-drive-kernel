"""Published compact radial shift profile from arXiv:2405.02709v1."""

from __future__ import annotations

import math

PUBLISHED_BETA_WARP = 0.02


def _sigmoid(value: float) -> float:
    if value >= 0.0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def compact_shift_shape(
    radius_m: float,
    inner_radius_m: float,
    outer_radius_m: float,
    buffer_m: float,
) -> float:
    """Paper Eqs. (27)-(28), evaluated with an overflow-safe sigmoid."""
    if not all(
        math.isfinite(x)
        for x in (radius_m, inner_radius_m, outer_radius_m, buffer_m)
    ):
        raise ValueError("inputs must be finite")
    if radius_m < 0.0 or inner_radius_m < 0.0 or outer_radius_m <= inner_radius_m:
        raise ValueError("invalid radii")
    if buffer_m <= 0.0 or 2.0 * buffer_m >= outer_radius_m - inner_radius_m:
        raise ValueError("buffer must be positive and leave a transition interval")
    if radius_m <= inner_radius_m + buffer_m:
        return 1.0
    if radius_m >= outer_radius_m - buffer_m:
        return 0.0
    exponent = (outer_radius_m - inner_radius_m) * (
        1.0 / (radius_m - outer_radius_m)
        + 1.0 / (radius_m - inner_radius_m)
    )
    return _sigmoid(exponent)


def shifted_g01(
    static_g01: float,
    shape: float,
    beta_warp: float = PUBLISHED_BETA_WARP,
) -> float:
    """Paper Eq. (26); static g01=0 gives -beta_warp inside."""
    if not all(math.isfinite(x) for x in (static_g01, shape, beta_warp)):
        raise ValueError("inputs must be finite")
    if not 0.0 <= shape <= 1.0 or abs(beta_warp) >= 1.0:
        raise ValueError("shape must be in [0,1] and beta_warp must be subluminal")
    return static_g01 - shape * (static_g01 + beta_warp)


def radial_causal_margin(
    lapse_squared: float,
    radial_metric: float,
    beta: float,
) -> float:
    """Return alpha^2-gamma_rr*beta^2 for a radial diagnostic.

    Positive values are a necessary local two-way radial-null accessibility
    check, not a complete global causal or horizon proof.
    """
    if lapse_squared <= 0.0 or radial_metric <= 0.0 or not all(
        math.isfinite(x) for x in (lapse_squared, radial_metric, beta)
    ):
        raise ValueError("metric inputs must be finite and positive")
    return lapse_squared - radial_metric * beta * beta
