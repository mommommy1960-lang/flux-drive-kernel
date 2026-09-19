# Positive-Energy Warp Baseline — Stages 2B–2D

Date: September 19, 2026  
Branch: `point-to-point-consistency-v0-1`  
Frozen paper: Fuchs et al., arXiv:2405.02709v1

## Purpose

Continue the published baseline reproduction through the static shell metric and
the paper's bounded shift profile while keeping every distinction between:

- input matter profiles;
- a static spherical Einstein solution;
- a constant-velocity shifted metric;
- acceleration or controllable transportation;
- and a physical device.

## SI convention audit

The implementation freezes:

- mass density `rho`: kg/m^3;
- energy density `epsilon = rho*c^2`: J/m^3 = Pa;
- pressure: Pa;
- enclosed mass: kg;
- radius: m;
- metric exponents `a` and `b`: dimensionless.

The TOV equation is implemented as

[
rac{dP}{dr}
=
-rac{G(ho+P/c^2)(m/r^2+4pi rP/c^2)}
       {1-2Gm/(c^2r)}.
]

A regression test verifies its Newtonian limit,
`dP/dr -> -G*rho*m/r^2`, preventing an unnoticed extra or missing factor of
`c^2`.

## Implemented gates

### 1. Declared grid and spans

A reproducible research trial uses:

- domain: 0–40 m;
- representative grid: `dr = 0.05 m`;
- density span: 85 samples (4.25 m);
- pressure span: 49 samples (2.45 m);
- four smoothing passes;
- span ratio: `85/49 = 1.7347`, close to the published approximately 1.72.

These are declared research parameters. They are **not** represented as the
authors' unpublished absolute spans.

### 2. Initial TOV pressure

The unsmoothed constant-density shell is integrated inward from `P(r_max)=0`.
The interior cavity pressure is explicitly set to zero before the pressure
profile is smoothed, following the paper's stated construction order.

### 3. Smoothed cumulative mass

Density is smoothed separately from pressure. The mass profile is recomputed
from `4*pi*r^2*rho`. Optional normalization restores the declared ADM mass
`M = 4.49e27 kg` and is labeled as an explicit numerical choice.

### 4. Static metric functions

The implementation computes

[
e^{2b} = left(1-rac{2Gm}{c^2r}ight)^{-1}
]

and integrates `a(r)` using paper equation (25), anchored to the exterior
Schwarzschild solution at the outer boundary.

### 5. Horizon and exterior gates

The published outer-edge compactness is approximately 0.3334 and is below one.
For the declared smoothed trial, the maximum sampled compactness is
approximately 0.2832. Any sampled compactness at or above one raises an error.

Exterior `e^{2a}` and `e^{2b}` are regression-tested against their
Schwarzschild values.

### 6. Independent Einstein-source reconstruction

The metric is differentiated independently to reconstruct energy density,
radial pressure, and tangential pressure from the static spherical Einstein
equations. Interior density and radial-pressure reconstruction are compared
against the input profiles with numerical tolerances.

Tangential pressure is also computed independently through anisotropic stress
conservation for comparison.

### 7. Static all-direction energy-condition gate

For the diagonal static Type-I stress tensor, the code evaluates the exact
principal-pressure margins for NEC, WEC, DEC, and SEC. This covers all null and
timelike observer directions for that diagonal static tensor; it does not cover
the later off-diagonal shifted tensor.

The declared 0.05 m / 85 / 49 trial produced nonnegative sampled static margins.

A required falsification test using `dr = 0.025 m`, density span 21, and
pressure span 13 produced a negative DEC margin of approximately
`-4.38e39 Pa`. That parameter set is preserved as **FAIL**, demonstrating that
the gate rejects inadequately smoothed profiles.

### 8. Published bounded shift profile

Paper equations (26)–(28) are implemented with:

- compact interior-to-exterior radial transition;
- overflow-safe evaluation;
- published `beta_warp = 0.02`;
- boundedness and monotonicity tests;
- strict subluminal input rejection;
- a local radial causal-margin diagnostic.

The causal diagnostic is necessary but not a complete global horizon proof.

## Validation boundary

The static Einstein reconstruction is now implemented. The **shifted** 4D
Einstein tensor and its off-diagonal momentum flux have not yet been
independently reconstructed in this repository. Therefore the paper's final
shifted all-observer energy-condition result has not yet been reproduced.

Nothing here establishes creation, acceleration, steering, stopping,
point-to-point control, nearly instantaneous travel, material realizability, or
physical flight.

## Next work

1. Add a second, algebraically independent shifted 4D Einstein-tensor
   implementation.
2. Compare both implementations on Minkowski and Schwarzschild regression
   metrics before evaluating the warp shell.
3. Evaluate shifted NEC/WEC/DEC/SEC across the paper's observer sampling.
4. Sweep grid spacing, physical smoothing widths, buffer size, and beta.
5. Preserve every violation, horizon, divergence, and nonconvergent region.
6. Separate constant velocity from acceleration and momentum export.
7. Continue CAL-00 physical force-measurement preparation in parallel.
