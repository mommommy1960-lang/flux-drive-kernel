"""Direct paper-component shifted shell and Eulerian source projection."""

from __future__ import annotations

import math
from typing import Sequence

from .shell_cartesian import static_cartesian_metric
from .tensor4d import inverse4
from .warp_shift import (
    PUBLISHED_BETA_WARP,
    compact_shift_shape,
    shifted_g01,
)

G = 6.67430e-11
C = 299_792_458.0


def direct_g01_shifted_metric(
    radii_m: Sequence[float],
    e2a: Sequence[float],
    e2b: Sequence[float],
    *,
    inner_radius_m: float,
    outer_radius_m: float,
    buffer_m: float,
    beta_warp: float = PUBLISHED_BETA_WARP,
):
    """Apply paper Eq. (26) directly to g_01 in Cartesian coordinates.

    This freezes the direct component interpretation separately from a later
    independent 3+1 lapse/shift reconstruction.
    """
    base = static_cartesian_metric(radii_m, e2a, e2b)

    def metric(point):
        result = [row[:] for row in base(point)]
        _, x, y, z = point
        radius = math.sqrt(x * x + y * y + z * z)
        shape = compact_shift_shape(
            radius,
            inner_radius_m,
            outer_radius_m,
            buffer_m,
        )
        component = shifted_g01(result[0][1], shape, beta_warp)
        result[0][1] = component
        result[1][0] = component
        return result

    return metric


def eulerian_sources_from_einstein(metric_cov, einstein_cov):
    """Return epsilon, covariant momentum j_i, and coordinate stress S_ij.

    Values are SI energy-density/pressure units (J/m^3 = Pa) when coordinates
    use x0=c*t and spatial coordinates use metres.
    """
    inverse = inverse4(metric_cov)
    if inverse[0][0] >= 0.0:
        raise ValueError("constant-time hypersurface is not spacelike")
    alpha = 1.0 / math.sqrt(-inverse[0][0])
    normal = [-alpha * inverse[mu][0] for mu in range(4)]
    scale = C**4 / (8.0 * math.pi * G)
    stress_energy = [
        [scale * einstein_cov[mu][nu] for nu in range(4)]
        for mu in range(4)
    ]
    epsilon = sum(
        stress_energy[mu][nu] * normal[mu] * normal[nu]
        for mu in range(4)
        for nu in range(4)
    )
    momentum = [
        -sum(stress_energy[i][nu] * normal[nu] for nu in range(4))
        for i in range(1, 4)
    ]
    spatial_stress = [
        [stress_energy[i][j] for j in range(1, 4)]
        for i in range(1, 4)
    ]
    return epsilon, momentum, spatial_stress
