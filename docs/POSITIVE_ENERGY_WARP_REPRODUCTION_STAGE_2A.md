# Positive-Energy Warp Baseline Reproduction — Stage 2A

## Frozen source

Fuchs et al., *Constant Velocity Physical Warp Drive Solution*,
arXiv:2405.02709v1 (submitted May 4, 2024), equations (22)-(25) and
footnotes 6-8. Source inspected September 19, 2026.

This stage implements only the published smoothing primitives and numerical
invariants. It does not yet claim reproduction of the final shell metric,
stress-energy tensor, all-observer energy conditions, or warp transport.

## What the paper specifies

The construction starts with the constant-density shell and TOV pressure
profile from Stage 1, then:

1. applies moving-average smoothing to density and pressure;
2. uses low-pass coefficients equal to the reciprocal of the averaging span;
3. applies smoothing four times;
4. uses a density-span to pressure-span ratio of approximately 1.72;
5. recomputes the cumulative mass from the smoothed density;
6. solves the radial metric functions and checks all energy conditions;
7. later adds a compact shift profile with the reported value
   `beta_warp = 0.02`.

Published baseline parameters are `R1 = 10 m`, `R2 = 20 m`, and
`M = 4.49e27 kg`.

## Reproducibility boundary

The paper does **not** publish the absolute density or pressure window spans.
Footnote 7 states that the setup numbers were found by trial and error.
Therefore the absolute span remains a frozen input to the implementation.
No unpublished span is fitted or presented as the authors' value.

The paper points to MATLAB's `smooth` function for the moving-average
convention. The implementation uses a centered uniform window with shortened
endpoint windows. This convention is explicit and tested.

## Added implementation

`flux_drive_kernel/shell_smoothing.py` adds:

- centered moving-average smoothing;
- the published default of four passes;
- explicit span validation;
- conversion from density span to the nearest odd pressure span at ratio 1.72;
- spherical `4*pi*r^2*rho` mass integration;
- optional mass renormalization, clearly separated from the paper's raw
  smoothing operation.

`tests/test_shell_smoothing.py` checks:

- exact centered-window behavior;
- nonnegative smoothed density;
- reduction of a step-boundary jump;
- constant-profile invariance;
- the published 43/25 = 1.72 representative span ratio;
- spherical mass recovery after explicit normalization;
- invalid parameter rejection.

## Evidence boundary and next gate

Stage 2A is a reproducible numerical foundation, not a positive-energy warp
metric reproduction. The next gate is to freeze a radial grid and an explicit
span pair, reproduce the initial TOV pressure profile, compute equations
(23)-(25), and sweep span/grid choices while preserving every failure.
The final energy-condition claim must be evaluated from the Einstein tensor
for the constructed metric across the specified null and timelike observers.

Constant-velocity metric mathematics does not establish creation,
acceleration, steering, stopping, nearly instantaneous travel, or a physical
device.
