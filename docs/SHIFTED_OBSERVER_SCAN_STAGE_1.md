# Shifted-shell observer scan: expanded spatial coverage

Date: 2026-09-19  
Status: preliminary; not converged; no flight claim

## Model and sampling

- shell radii: 10 m to 20 m
- total shell mass: (4.49\times10^{27}) kg
- shift parameter: (eta=0.02)
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
| 0.10 m | (3.4073\times10^{38}) | (3.7501\times10^{39}) | (1.4538\times10^{39}) | (2.0013\times10^{39}) |
| 0.05 m | (2.9141\times10^{38}) | (3.7490\times10^{39}) | (1.4534\times10^{39}) | (2.0011\times10^{39}) |

The weakest NEC sample occurred near radius 12 m on a transverse axis. This is more than an order of magnitude below the earlier x-axis-only minimum, demonstrating that a single-axis scan was insufficient.

## Focused spherical scan at 12 m

A 100-direction Fibonacci sampling of spatial locations on the radius-12 m sphere was then combined with the full observer sweep.

| finite-difference step | NEC minimum (Pa) | WEC minimum (Pa) | DEC minimum (Pa) | SEC minimum (Pa) |
|---:|---:|---:|---:|---:|
| 0.10 m | (8.1699\times10^{37}) | (5.4774\times10^{39}) | (2.2180\times10^{39}) | (1.4799\times10^{39}) |
| 0.05 m | (4.4240\times10^{37}) | (5.3336\times10^{39}) | (2.1295\times10^{39}) | (1.3332\times10^{39}) |
| 0.025 m | (3.4113\times10^{37}) | (5.2942\times10^{39}) | (2.0902\times10^{39}) | (1.2936\times10^{39}) |

All reported sampled margins are positive, but the NEC minimum changes substantially under step refinement. It therefore **cannot yet be reported as a converged pass**. The energy-condition/error-bound checkbox remains open.

## Preserved numerical lessons

1. Linear interpolation previously produced false exterior stress; cubic interpolation restored the expected second-order decline under step halving.
2. An early DEC calculation compared quantities with inconsistent units (Pa against Pa-squared). It was corrected to the rest-frame margin (\epsilon-|q|).
3. Expanding from one spatial axis to six axes and then a sphere substantially reduced the weakest NEC margin. This is evidence that broad directional coverage is essential.

## Next falsification gates

1. Refine spatial angle, radius, observer angle, and finite-difference step near the current NEC minimum.
2. Separate interpolation, radial-grid, and curvature-stencil errors.
3. Implement the independent 3+1 reconstruction and require agreement.
4. Complete causal, horizon, curvature-invariant, tidal, and stability checks.
5. Preserve every negative result and numerical artifact.

This document records a numerical research checkpoint. It is not evidence that a physical Flux Drive exists or can fly.
