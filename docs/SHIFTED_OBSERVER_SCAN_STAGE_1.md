# Shifted-shell observer scan: expanded spatial coverage

Date: 2026-09-19  
Status: preliminary numerical failure found; convergence and independent reproduction pending; no flight claim

## Model and sampling

- shell radii: 10 m to 20 m
- total shell mass: 4.49e27 kg
- shift parameter: beta = 0.02
- shift buffer: 0.5 m
- radial grid: 0.025 m
- density smoothing: span 171, four passes
- pressure smoothing: span 99, four passes
- observer directions per spacetime point: 100 null
- timelike observers per point: 100 directions times 10 speeds through 0.99c

## Six-axis scan

The first expanded pass sampled radii 8.5 m through 21.5 m at 0.5 m spacing on the six Cartesian axes, for 162 spatial points.

| finite-difference step | NEC minimum (Pa) | WEC minimum (Pa) | DEC minimum (Pa) | SEC minimum (Pa) |
|---:|---:|---:|---:|---:|
| 0.10 m | +3.4073e38 | +3.7501e39 | +1.4538e39 | +2.0013e39 |
| 0.05 m | +2.9141e38 | +3.7490e39 | +1.4534e39 | +2.0011e39 |

The weakest NEC sample occurred near radius 12 m on a transverse axis. This was more than an order of magnitude below the earlier x-axis-only minimum, demonstrating that a single-axis scan was insufficient.

## Focused spherical scan at 12 m

A 100-direction Fibonacci sampling of spatial locations on the radius-12 m sphere was combined with the full observer sweep.

| finite-difference step | NEC minimum (Pa) | WEC minimum (Pa) | DEC minimum (Pa) | SEC minimum (Pa) |
|---:|---:|---:|---:|---:|
| 0.10 m | +8.1699e37 | +5.4774e39 | +2.2180e39 | +1.4799e39 |
| 0.05 m | +4.4240e37 | +5.3336e39 | +2.1295e39 | +1.3332e39 |
| 0.025 m | +3.4113e37 | +5.2942e39 | +2.0902e39 | +1.2936e39 |

These radius-12 m samples were positive but not converged. They were retained as an intermediate result, not treated as a pass.

## Neighboring-radius refinement: sampled failure

The next pass sampled radii 11.00 m through 13.00 m at 0.25 m spacing, with 100 spatial orientations at each radius and the same observer sweep. It found the following minima:

| finite-difference step | NEC minimum (Pa) | WEC minimum (Pa) | DEC minimum (Pa) | SEC minimum (Pa) |
|---:|---:|---:|---:|---:|
| 0.05 m | -2.7968e37 | +3.6701e39 | -5.2643e38 | -6.0704e38 |
| 0.025 m | -3.6033e37 | +3.2690e39 | -1.0826e39 | -1.0084e39 |

The worst sampled point for NEC was at radius 12.25 m and spatial Fibonacci index 2, direction approximately (0.02730, -0.31105, 0.95000). The null-observer minimum occurred at observer-direction index 55. The timelike DEC and SEC failures occurred at speed 0.99c in the sampled grid.

This is a **preliminary numerical failure**, not yet an analytic theorem. However, the negative signs occur at both tested steps and the NEC magnitude increases under refinement. The current direct-g01 shifted-shell configuration therefore does **not** pass the sampled NEC, DEC, or SEC gate. WEC remained positive in this specific grid.

## Preserved numerical lessons

1. Linear interpolation previously produced false exterior stress; cubic interpolation restored the expected second-order decline under step halving.
2. An early DEC calculation compared quantities with inconsistent units (Pa against Pa-squared). It was corrected to the rest-frame margin energy minus spatial-energy-flux magnitude.
3. Expanding from one spatial axis to six axes, a sphere, and neighboring radii successively lowered the margins and ultimately exposed negative samples.
4. A positive result on a sparse slice must never be generalized to the full spacetime.

## Next falsification gates

1. Reproduce the radius-12.25 m failure with finer radial grid, curvature steps, spatial angles, and observer angles.
2. Separate interpolation, radial-grid, smoothing, and curvature-stencil errors.
3. Implement the independent 3+1 reconstruction and require agreement on the failure or its resolution.
4. Map the violation region over beta, buffer width, smoothing, and radius.
5. Complete causal, horizon, curvature-invariant, tidal, and stability checks.
6. Preserve every negative result and numerical artifact.

This document records a numerical research checkpoint. It is not evidence that a physical Flux Drive exists or can fly.
