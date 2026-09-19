# Frozen Metric Tensor and Parameter Scan — v0.2

## Frozen metric

The calculation fixes the zero-redshift Morris-Thorne ansatz

[
ds^2=-c^2dt^2+\frac{dr^2}{1-b(r)/r}+r^2d\Omega^2,
\qquad b(r)=\frac{r_0^2}{r}.
]

This choice is intentionally simple enough to audit analytically. It is not
selected because it is expected to be physically realizable.

## Complete orthonormal source

With (K=c^4/(8\pi G)), the nonzero diagonal stress-energy components are

[
\epsilon=K\frac{b'}{r^2},\qquad
p_r=-K\frac{b}{r^3},\qquad
p_t=\frac{K}{2}\frac{b-rb'}{r^3}.
]

The full orthonormal diagonal is
((\epsilon,p_r,p_t,p_t)); symmetry makes the off-diagonal components zero.

For (b=r_0^2/r):

[
\epsilon=p_r=-K\frac{r_0^2}{r^4},\qquad
p_t=+K\frac{r_0^2}{r^4}.
]

Therefore

[
\epsilon+p_r=-2K\frac{r_0^2}{r^4}<0.
]

The radial null energy condition is violated throughout this frozen model.
The tangential null combination is zero.

## Parameter scan

| Throat radius | Radius sampled | Energy density (J/m^3) | Radial NEC combination (J/m^3) |
|---:|---:|---:|---:|
| 1 m | 1 m | -4.81545e42 | -9.63091e42 |
| 1 m | 2 m | -3.00966e41 | -6.01932e41 |
| 10 m | 10 m | -4.81545e40 | -9.63091e40 |
| 100 m | 100 m | -4.81545e38 | -9.63091e38 |
| 1000 m | 1000 m | -4.81545e36 | -9.63091e36 |

At the throat the magnitude falls as (1/r_0^2); at fixed throat size it
falls radially as (1/r^4). Increasing the geometry does not change the sign
or provide a physical source.

## Horizon and stability boundary

The frozen redshift function is finite and constant, so this ansatz has no
event horizon from (g_{tt}). The coordinate behavior at the throat is handled
by the wormhole chart and is not by itself a proof of a physical passage.

Stability has **not** been established. The scan deliberately returns
`stability_assessed=false`. A perturbation operator, boundary conditions,
matter dynamics, and backreaction model are still absent.

## Test record

Local command:

    python -m unittest -v test_spacetime_consistency.py

Result, September 19, 2026:

- 12 tests run;
- 12 passed;
- 0 failures;
- 0 errors.

The tests verify tensor symmetry, signs, throat matching, radial and scale
power laws, profile limits, rejected inputs, and preservation of the unassessed
stability state.

## Decision

This frozen metric fails the “physically supportable source” gate because it
requires a negative radial null-energy combination and no realizable source has
been identified. The result remains valuable as a reference case and regression
test. It must not be promoted as a flight mechanism.

## Next research gate

1. Independent equation and SI-unit review.
2. Symbolic Christoffel/Ricci/Einstein derivation checked against the analytic
   diagonal above.
3. Perturbative stability formulation with declared matter dynamics.
4. Separate evaluation of a positive-energy warp proposal without transferring
   conclusions between inequivalent metrics.
5. CAL-00 proceeds independently; a bench force residual cannot be labeled
   curvature without a discriminating prediction.
