"""Cartesian 4D metric adapter for radial static-shell profiles."""

from __future__ import annotations

import math
from typing import Sequence


def _interp(
    radii: Sequence[float],
    values: Sequence[float],
    radius: float,
) -> float:
    if radius <= radii[0]:
        return float(values[0])
    if radius >= radii[-1]:
        return float(values[-1])
    low, high = 0, len(radii) - 1
    while high - low > 1:
        middle = (low + high) // 2
        if radii[middle] <= radius:
            low = middle
        else:
            high = middle
    fraction = (radius - radii[low]) / (radii[high] - radii[low])
    return values[low] * (1.0 - fraction) + values[high] * fraction


def static_cartesian_metric(
    radii_m: Sequence[float],
    e2a: Sequence[float],
    e2b: Sequence[float],
):
    """Return g_mu_nu(x0,x,y,z) for a static radial metric."""
    radii = [float(x) for x in radii_m]
    lapse = [float(x) for x in e2a]
    radial = [float(x) for x in e2b]
    if (
        len(radii) < 3
        or len(lapse) != len(radii)
        or len(radial) != len(radii)
    ):
        raise ValueError("profiles must have equal length >= 3")
    if radii[0] != 0.0 or any(
        right <= left for left, right in zip(radii, radii[1:])
    ):
        raise ValueError("radial grid must start at zero and increase")
    if any(
        value <= 0.0 or not math.isfinite(value)
        for value in lapse + radial
    ):
        raise ValueError("metric profiles must be finite and positive")

    def metric(point):
        if len(point) != 4:
            raise ValueError("point must have four coordinates")
        _, x, y, z = point
        radius_m = math.sqrt(x * x + y * y + z * z)
        alpha2 = _interp(radii, lapse, radius_m)
        gamma_r = _interp(radii, radial, radius_m)
        result = [[0.0] * 4 for _ in range(4)]
        result[0][0] = -alpha2
        if radius_m == 0.0:
            for index in range(1, 4):
                result[index][index] = 1.0
            return result
        direction = [x / radius_m, y / radius_m, z / radius_m]
        for i in range(3):
            for j in range(3):
                result[i + 1][j + 1] = (
                    (1.0 if i == j else 0.0)
                    + (gamma_r - 1.0) * direction[i] * direction[j]
                )
        return result

    return metric
