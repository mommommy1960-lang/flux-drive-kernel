# Point-to-Point Transport Progress Record — 2026-09-19

## Objective

Long-range objective: controlled transport from point A to point B with transit
time far below conventional propulsion, while preserving causality, traveler
safety, conservation laws, controllability, and an independently testable
physical source.

This is an objective, not a present capability.

## Stage 1 — consistency foundation

PR #17 first added:

- Morris-Thorne throat checks;
- radial null-energy-condition calculation;
- Alcubierre smooth top-hat profile;
- requested average-speed reporting;
- strict input validation;
- explicit scientific non-claims.

Initial local result: 7 tests passed, 0 failed.

## Stage 2 — frozen metric source calculation

The branch then froze the zero-redshift Morris-Thorne metric with

[
b(r)=r_0^2/r.
]

It added:

- the complete orthonormal diagonal stress-energy tensor;
- SI energy-density conversion;
- radial and tangential NEC tests;
- throat-size and radial parameter scans;
- horizon-condition tracking;
- lateral traveler tidal-acceleration calculation;
- an explicit `stability_assessed=false` state.

Current local result: 13 tests passed, 0 failed.

## Preserved falsification result

For this frozen metric,

[
\epsilon=p_r=-\frac{c^4}{8\pi G}\frac{r_0^2}{r^4},
\qquad
p_t=+\frac{c^4}{8\pi G}\frac{r_0^2}{r^4},
]

and therefore

[
\epsilon+p_r=-\frac{c^4}{4\pi G}\frac{r_0^2}{r^4}<0.
]

At a one-meter throat the radial NEC combination has magnitude approximately
(9.63\times10^{42},mathrm{J/m^3}). Larger throats reduce the magnitude but
do not change the sign or identify a realizable source.

Decision: this metric is retained as a failed physical-supportability reference
and regression test. It is not a candidate Flux engine.

## Independent review

Issue #18 requests external verification of the metric, Einstein/stress-energy
components, SI units, scaling, omitted conditions, and claim boundary. Internal
tests do not satisfy independent review.

## Next candidate class

The next target is not another relabeling of the failed wormhole. It is the
published constant-velocity, subluminal positive-energy warp-drive class.

Candidate starting points:

1. Bobrick and Martire, *Introducing Physical Warp Drives*,
   arXiv:2102.06824.
2. Helmerich et al., *Analyzing Warp Drive Spacetimes with Warp Factory*,
   arXiv:2404.03095.
3. Fuchs et al., *Constant Velocity Physical Warp Drive Solution*,
   arXiv:2405.02709.
4. Le, *Steering a Warp Drive without Exotic Matter*,
   arXiv:2606.22531.

The papers do not establish nearly instantaneous travel. The positive-energy
constructions are subluminal/constant-velocity or require ordinary momentum
and energy export for steering. Bobrick and Martire's central physical boundary
is preserved: a warp shell still requires propulsion.

## Acceptance gates for the next reproduction

- freeze the paper version, metric, coordinates, grid, and boundary conditions;
- reproduce the stress-energy tensor numerically;
- test all-observer energy conditions, not only one observer;
- verify ADM/Bondi mass and asymptotic behavior;
- calculate horizons, causal accessibility, curvature, and traveler tidal load;
- distinguish constant velocity from acceleration/steering;
- calculate the propulsion and energy budget needed to create and move the shell;
- run convergence and independent-code checks;
- preserve every failing parameter region;
- prohibit any inference of instant travel from a subluminal solution.

## Parallel physical gate

CAL-00 remains independent of this relativity track. It asks whether a calibrated
force residual survives ordinary momentum accounting, uncertainty, controls,
and replication. A residual cannot be called spacetime curvature without a
preregistered discriminating prediction.

Current state remains:

`physical_propulsion_proven=false`
