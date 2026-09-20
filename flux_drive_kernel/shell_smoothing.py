"""Stage-two numerical primitives for the Fuchs et al. shell reproduction.

Paper source: arXiv:2405.02709v1, equations (22)-(25) and footnotes 6-8.

The paper specifies moving-average smoothing, four repeated passes, and a
density-span/pressure-span ratio of approximately 1.72. It does not publish the
absolute spans. Consequently these routines require the span explicitly and do
not claim to reproduce the authors' final numerical metric by themselves.
"""

from __future__ import annotations

import math
from typing import Iterable, Sequence


PUBLISHED_SPAN_RATIO = 1.72
PUBLISHED_SMOOTHING_PASSES = 4


def _finite_sequence(name: str, values: Iterable[float]) -> list[float]:
    result = [float(value) for value in values]
    if not result:
        raise ValueError(name + " must not be empty")
    if not all(math.isfinite(value) for value in result):
        raise ValueError(name + " must contain only finite values")
    return result


def _valid_span(span: int, size: int) -> int:
    if isinstance(span, bool) or not isinstance(span, int):
        raise ValueError("span must be an integer")
    if span < 1 or span > size or span % 2 == 0:
        raise ValueError("span must be odd and between 1 and the profile length")
    return span


def moving_average(values: Sequence[float], span: int) -> list[float]:
    """Centered moving average with shortened endpoint windows.

    Interior filter coefficients are 1/span, matching the paper's description
    and MATLAB's moving-average convention. Endpoint windows shrink rather than
    injecting zero-valued samples outside the numerical domain.
    """
    profile = _finite_sequence("values", values)
    width = _valid_span(span, len(profile))
    radius = width // 2
    smoothed: list[float] = []
    for index in range(len(profile)):
        lower = max(0, index - radius)
        upper = min(len(profile), index + radius + 1)
        window = profile[lower:upper]
        smoothed.append(sum(window) / len(window))
    return smoothed


def repeated_moving_average(
    values: Sequence[float],
    span: int,
    passes: int = PUBLISHED_SMOOTHING_PASSES,
) -> list[float]:
    if isinstance(passes, bool) or not isinstance(passes, int) or passes < 1:
        raise ValueError("passes must be a positive integer")
    result = _finite_sequence("values", values)
    _valid_span(span, len(result))
    for _ in range(passes):
        result = moving_average(result, span)
    return result


def pressure_span_for_density_span(
    density_span: int,
    *,
    ratio: float = PUBLISHED_SPAN_RATIO,
) -> int:
    """Return the nearest positive odd pressure span for s_rho/s_P ~= ratio."""
    if isinstance(density_span, bool) or not isinstance(density_span, int):
        raise ValueError("density_span must be an integer")
    if density_span < 1 or density_span % 2 == 0:
        raise ValueError("density_span must be a positive odd integer")
    if not math.isfinite(ratio) or ratio <= 0.0:
        raise ValueError("ratio must be finite and positive")
    target = density_span / ratio
    lower = max(1, int(math.floor(target)))
    candidates = [n for n in range(max(1, lower - 3), lower + 5) if n % 2 == 1]
    return min(candidates, key=lambda n: (abs(n - target), n))


def spherical_shell_mass_kg(
    radii_m: Sequence[float],
    density_kg_m3: Sequence[float],
) -> float:
    """Trapezoidal integral of 4*pi*r^2*rho(r) over a radial grid."""
    radii = _finite_sequence("radii_m", radii_m)
    density = _finite_sequence("density_kg_m3", density_kg_m3)
    if len(radii) != len(density) or len(radii) < 2:
        raise ValueError("radii and density must have equal length of at least two")
    if radii[0] < 0.0 or any(b <= a for a, b in zip(radii, radii[1:])):
        raise ValueError("radii must be nonnegative and strictly increasing")
    if any(value < 0.0 for value in density):
        raise ValueError("density must be nonnegative")
    integrand = [4.0 * math.pi * radius**2 * rho for radius, rho in zip(radii, density)]
    return sum(
        0.5 * (left + right) * (r1 - r0)
        for left, right, r0, r1 in zip(
            integrand, integrand[1:], radii, radii[1:]
        )
    )


def rescale_density_to_mass(
    radii_m: Sequence[float],
    density_kg_m3: Sequence[float],
    target_mass_kg: float,
) -> list[float]:
    """Optional numerical normalization, explicitly separate from paper smoothing."""
    if not math.isfinite(target_mass_kg) or target_mass_kg <= 0.0:
        raise ValueError("target_mass_kg must be finite and positive")
    density = _finite_sequence("density_kg_m3", density_kg_m3)
    current = spherical_shell_mass_kg(radii_m, density)
    if current <= 0.0:
        raise ValueError("density profile must have positive integrated mass")
    scale = target_mass_kg / current
    return [value * scale for value in density]
