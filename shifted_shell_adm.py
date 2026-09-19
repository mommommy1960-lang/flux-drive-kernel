"""Independent 3+1 reconstruction of the shifted spherical shell.

This module does not edit a single covariant metric component.  It freezes the
static lapse and spatial metric, prescribes a contravariant shift along the
Cartesian x direction, and reconstructs the complete four-metric from

    g_00 = -alpha**2 + gamma_ij beta**i beta**j
    g_0i = gamma_ij beta**j
    g_ij = gamma_ij.

That makes it an intentionally independent convention check on the direct-g01
implementation in shifted_shell.py.
"""

from __future__ import annotations

import math
from typing import Sequence

from shell_cartesian import static_cartesian_metric
from warp_shift import PUBLISHED_BETA_WARP, compact_shift_shape


def adm_shifted_metric(
    radii_m: Sequence[float],
    e2a: Sequence[float],
    e2b: Sequence[float],
    *,
    inner_radius_m: float,
    outer_radius_m: float,
    buffer_m: float,
    beta_warp: float = PUBLISHED_BETA_WARP,
):
    """Return a four-metric reconstructed from lapse, 3-metric, and shift.

    The static lapse and spatial metric are retained.  The prescribed
    contravariant shift is beta^i=(-beta_warp*f(r),0,0).
    """
    if not math.isfinite(beta_warp) or abs(beta_warp) >= 1.0:
        raise ValueError("beta_warp must be finite and subluminal")
    base = static_cartesian_metric(radii_m, e2a, e2b)

    def metric(point):
        static = base(point)
        _, x, y, z = point
        radius = math.sqrt(x*x + y*y + z*z)
        shape = compact_shift_shape(
            radius, inner_radius_m, outer_radius_m, buffer_m
        )
        beta_contra = (-beta_warp * shape, 0.0, 0.0)
        gamma = [[static[i + 1][j + 1] for j in range(3)] for i in range(3)]
        beta_cov = [
            sum(gamma[i][j] * beta_contra[j] for j in range(3))
            for i in range(3)
        ]
        alpha_squared = -static[0][0]
        beta_squared = sum(beta_cov[i] * beta_contra[i] for i in range(3))
        result = [[0.0] * 4 for _ in range(4)]
        result[0][0] = -alpha_squared + beta_squared
        for i in range(3):
            result[0][i + 1] = beta_cov[i]
            result[i + 1][0] = beta_cov[i]
            for j in range(3):
                result[i + 1][j + 1] = gamma[i][j]
        return result

    return metric

