"""Independent finite-difference 4D curvature engine.

Coordinates must share one length unit, with x0 = c*t for spacetime metrics.
The metric callback returns a symmetric 4x4 covariant metric.
"""

from __future__ import annotations

import math
from typing import Callable, Sequence

Matrix4 = list[list[float]]
MetricFunction = Callable[[tuple[float, float, float, float]], Sequence[Sequence[float]]]


def inverse4(matrix: Sequence[Sequence[float]]) -> Matrix4:
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        raise ValueError("matrix must be 4x4")
    augmented = [
        [float(matrix[i][j]) for j in range(4)]
        + [1.0 if i == j else 0.0 for j in range(4)]
        for i in range(4)
    ]
    for column in range(4):
        pivot = max(range(column, 4), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1.0e-15:
            raise ValueError("metric is singular")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(4):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                value - factor * source
                for value, source in zip(augmented[row], augmented[column])
            ]
    return [row[4:] for row in augmented]


def _metric(metric: MetricFunction, point: Sequence[float]) -> Matrix4:
    value = [[float(x) for x in row] for row in metric(tuple(point))]
    if len(value) != 4 or any(len(row) != 4 for row in value):
        raise ValueError("metric callback must return 4x4")
    if not all(math.isfinite(x) for row in value for x in row):
        raise ValueError("metric must be finite")
    if any(
        abs(value[i][j] - value[j][i]) > 1.0e-10
        for i in range(4)
        for j in range(4)
    ):
        raise ValueError("metric must be symmetric")
    return value


def _steps(steps: Sequence[float]) -> list[float]:
    result = [float(x) for x in steps]
    if len(result) != 4 or any(
        not math.isfinite(x) or x <= 0.0 for x in result
    ):
        raise ValueError("four finite positive steps are required")
    return result


def christoffel(
    metric: MetricFunction,
    point: Sequence[float],
    steps: Sequence[float],
) -> list[list[list[float]]]:
    x = [float(value) for value in point]
    if len(x) != 4:
        raise ValueError("point must have four coordinates")
    h = _steps(steps)
    g = _metric(metric, x)
    inverse = inverse4(g)
    derivative = [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
    for axis in range(4):
        plus = x.copy()
        plus[axis] += h[axis]
        minus = x.copy()
        minus[axis] -= h[axis]
        gp = _metric(metric, plus)
        gm = _metric(metric, minus)
        for mu in range(4):
            for nu in range(4):
                derivative[axis][mu][nu] = (
                    gp[mu][nu] - gm[mu][nu]
                ) / (2.0 * h[axis])
    gamma = [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
    for rho in range(4):
        for mu in range(4):
            for nu in range(4):
                gamma[rho][mu][nu] = 0.5 * sum(
                    inverse[rho][sigma]
                    * (
                        derivative[mu][sigma][nu]
                        + derivative[nu][sigma][mu]
                        - derivative[sigma][mu][nu]
                    )
                    for sigma in range(4)
                )
    return gamma


def einstein_tensor(
    metric: MetricFunction,
    point: Sequence[float],
    steps: Sequence[float],
) -> Matrix4:
    """Return covariant G_mu_nu using centered finite differences."""
    x = [float(value) for value in point]
    h = _steps(steps)
    g = _metric(metric, x)
    inverse = inverse4(g)
    gamma = christoffel(metric, x, h)
    dgamma = [
        [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
        for _ in range(4)
    ]
    for axis in range(4):
        plus = x.copy()
        plus[axis] += h[axis]
        minus = x.copy()
        minus[axis] -= h[axis]
        gp = christoffel(metric, plus, h)
        gm = christoffel(metric, minus, h)
        for rho in range(4):
            for mu in range(4):
                for nu in range(4):
                    dgamma[axis][rho][mu][nu] = (
                        gp[rho][mu][nu] - gm[rho][mu][nu]
                    ) / (2.0 * h[axis])
    ricci = [[0.0] * 4 for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            value = 0.0
            for rho in range(4):
                value += dgamma[rho][rho][mu][nu]
                value -= dgamma[nu][rho][mu][rho]
                for sigma in range(4):
                    value += (
                        gamma[rho][mu][nu] * gamma[sigma][rho][sigma]
                    )
                    value -= (
                        gamma[sigma][mu][rho] * gamma[rho][nu][sigma]
                    )
            ricci[mu][nu] = value
    scalar = sum(
        inverse[mu][nu] * ricci[mu][nu]
        for mu in range(4)
        for nu in range(4)
    )
    return [
        [
            ricci[mu][nu] - 0.5 * g[mu][nu] * scalar
            for nu in range(4)
        ]
        for mu in range(4)
    ]


def max_abs(values) -> float:
    """Return the largest absolute scalar in a nested tensor-like sequence."""
    found: list[float] = []

    def visit(value) -> None:
        if isinstance(value, (list, tuple)):
            for child in value:
                visit(child)
        else:
            found.append(abs(float(value)))

    visit(values)
    if not found:
        raise ValueError("tensor must contain at least one scalar")
    return max(found)
