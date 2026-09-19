"""Directional null and timelike energy-condition contractions."""

from __future__ import annotations

import math
from typing import Sequence

from .tensor4d import inverse4


def _inner(metric, left, right):
    return sum(
        metric[i][j] * left[i] * right[j]
        for i in range(4)
        for j in range(4)
    )


def _normal_and_triad(metric):
    inverse = inverse4(metric)
    if inverse[0][0] >= 0.0:
        raise ValueError("constant-time hypersurface is not spacelike")
    alpha = 1.0 / math.sqrt(-inverse[0][0])
    normal = [-alpha * inverse[mu][0] for mu in range(4)]
    triad = []
    for axis in range(1, 4):
        vector = [0.0, 0.0, 0.0, 0.0]
        vector[axis] = 1.0
        for basis in triad:
            projection = _inner(metric, vector, basis)
            vector = [
                value - projection * component
                for value, component in zip(vector, basis)
            ]
        norm = _inner(metric, vector, vector)
        if norm <= 0.0:
            raise ValueError("spatial metric is not positive definite")
        triad.append([value / math.sqrt(norm) for value in vector])
    return normal, triad, inverse


def fibonacci_directions(count: int):
    if isinstance(count, bool) or not isinstance(count, int) or count < 4:
        raise ValueError("direction count must be an integer >= 4")
    golden = math.pi * (3.0 - math.sqrt(5.0))
    result = []
    for index in range(count):
        z = 1.0 - 2.0 * (index + 0.5) / count
        radius = math.sqrt(max(0.0, 1.0 - z * z))
        phi = golden * index
        result.append(
            (radius * math.cos(phi), radius * math.sin(phi), z)
        )
    return result


def observer_energy_condition_margins(
    metric_cov: Sequence[Sequence[float]],
    stress_energy_cov: Sequence[Sequence[float]],
    *,
    direction_count: int = 100,
    speed_count: int = 10,
    maximum_speed: float = 0.99,
):
    """Return worst sampled NEC/WEC/DEC/SEC margins in energy-density units."""
    if speed_count < 2 or not 0.0 < maximum_speed < 1.0:
        raise ValueError(
            "speed_count >= 2 and 0 < maximum_speed < 1 required"
        )
    metric = [[float(x) for x in row] for row in metric_cov]
    stress = [[float(x) for x in row] for row in stress_energy_cov]
    normal, triad, inverse = _normal_and_triad(metric)
    trace = sum(
        inverse[i][j] * stress[i][j]
        for i in range(4)
        for j in range(4)
    )
    directions = fibonacci_directions(direction_count)
    minima = {
        "NEC": math.inf,
        "WEC": math.inf,
        "DEC": math.inf,
        "SEC": math.inf,
    }
    argmin = {name: None for name in minima}

    def contraction(left, right):
        return sum(
            stress[i][j] * left[i] * right[j]
            for i in range(4)
            for j in range(4)
        )

    for direction_index, direction in enumerate(directions):
        spatial = [
            sum(
                direction[axis] * triad[axis][mu]
                for axis in range(3)
            )
            for mu in range(4)
        ]
        null = [
            normal[mu] + spatial[mu]
            for mu in range(4)
        ]
        nec = contraction(null, null)
        if nec < minima["NEC"]:
            minima["NEC"] = nec
            argmin["NEC"] = (direction_index, 1.0)
        for speed_index in range(speed_count):
            speed = maximum_speed * speed_index / (speed_count - 1)
            gamma = 1.0 / math.sqrt(1.0 - speed * speed)
            observer = [
                gamma * (normal[mu] + speed * spatial[mu])
                for mu in range(4)
            ]
            energy = contraction(observer, observer)
            sec = energy + 0.5 * trace
            mixed_action = [
                sum(
                    inverse[mu][alpha]
                    * stress[alpha][nu]
                    * observer[nu]
                    for alpha in range(4)
                    for nu in range(4)
                )
                for mu in range(4)
            ]
            flux = [-value for value in mixed_action]
            spatial_flux = [
                flux[mu] - energy * observer[mu]
                for mu in range(4)
            ]
            spatial_flux_squared = max(
                0.0,
                _inner(metric, spatial_flux, spatial_flux),
            )
            dec = energy - math.sqrt(spatial_flux_squared)
            for name, value in (
                ("WEC", energy),
                ("SEC", sec),
                ("DEC", dec),
            ):
                if value < minima[name]:
                    minima[name] = value
                    argmin[name] = (direction_index, speed)
    return {
        "minima": minima,
        "argmin": argmin,
        "null_samples": direction_count,
        "timelike_samples": direction_count * speed_count,
    }
