# Direct-g01 versus full 3+1 reconstruction

Date: 2026-09-19  
Status: preliminary convention discrepancy; sampled comparison only; no flight claim

## Question

Does the shifted shell have the same stress-energy behavior when the shift is implemented by directly replacing one covariant component, g01, versus reconstructing the entire four-metric from independently frozen 3+1 variables?

## Two implementations

### Implementation A: direct g01

The existing implementation applies the paper-component expression directly to g01 while preserving the static g00 and spatial components.

### Implementation B: full ADM reconstruction

The new independent implementation freezes the static lapse alpha and spatial metric gamma_ij, prescribes the contravariant Cartesian shift

beta^i = (-beta_warp f(r), 0, 0),

and reconstructs

g00 = -alpha^2 + gamma_ij beta^i beta^j,

g0i = gamma_ij beta^j,

gij = gamma_ij.

These are not algebraically identical conventions. In particular, Implementation B changes g00 by the shift norm. At off-axis points in a curved radial spatial metric, it may also produce nonzero g0y and g0z even though the prescribed contravariant shift points along x.

## Pointwise comparison at the direct-method failure point

Point: radius 12.25 m, spatial direction approximately (0.0272987, -0.3110543, 0.95).

| method | step (m) | NEC (Pa) | WEC (Pa) | DEC (Pa) | SEC (Pa) |
|---|---:|---:|---:|---:|---:|
| direct g01 | 0.1000 | +4.2298e36 | +5.2713e39 | +1.3312e39 | +9.9532e38 |
| direct g01 | 0.0500 | -2.7968e37 | +3.6701e39 | -5.2643e38 | -6.0704e38 |
| direct g01 | 0.0250 | -3.6033e37 | +3.2690e39 | -1.0826e39 | -1.0084e39 |
| direct g01 | 0.0125 | -3.8050e37 | +3.1687e39 | -1.2267e39 | -1.1088e39 |
| full ADM | 0.1000 | +9.6207e37 | +5.6520e39 | +2.2561e39 | +1.6706e39 |
| full ADM | 0.0500 | +6.4845e37 | +5.5299e39 | +2.1942e39 | +1.5482e39 |
| full ADM | 0.0250 | +5.6990e37 | +5.4993e39 | +2.1581e39 | +1.5176e39 |
| full ADM | 0.0125 | +5.5025e37 | +5.4916e39 | +2.1489e39 | +1.5099e39 |

The direct method trends toward negative NEC, DEC, and SEC at this point. The ADM reconstruction remains positive and is stabilizing under stencil refinement.

## Regional comparison for Implementation B

The ADM version was scanned over radii 11.00–13.00 m in 0.25 m increments, with 100 spatial Fibonacci orientations at each radius. Every point used 100 null directions and 100 directions times 10 timelike speeds through 0.99c.

| step (m) | minimum NEC (Pa) | minimum WEC (Pa) | minimum DEC (Pa) | minimum SEC (Pa) |
|---|---:|---:|---:|---:|
| 0.050 | +6.4845e37 | +5.5299e39 | +2.1350e39 | +1.5482e39 |
| 0.025 | +5.6990e37 | +5.4969e39 | +2.1215e39 | +1.5176e39 |

This sampled region contains no negative margin for Implementation B. That is not an all-observer proof and does not establish a globally admissible metric.

## Interpretation

A consequential convention mismatch has been identified: “set g01” and “prescribe a 3+1 shift while retaining lapse and spatial metric” define different four-metrics. Energy-condition conclusions can therefore differ.

Before claiming either implementation represents the published construction, the project must trace the paper's coordinate and ADM conventions line by line and compare against author code or data. The result may be:

1. Implementation A is the intended metric and its failure is physical;
2. Implementation B is the intended metric and the direct-component reading was incomplete;
3. both are legitimate but different ansatzes;
4. another lapse/shift convention is required.

## Remaining gates

- hosted CI for the new tests;
- frame-independent Hawking–Ellis classification;
- global spatial coverage, not only radii 11–13 m;
- radial-grid, smoothing, interpolation, angular, and stencil error separation;
- source conservation and complete Einstein-constraint residuals;
- causal, horizon, curvature, tidal, and stability checks;
- independent expert review.

No physical propulsion, FTL travel, or realizable matter source is established.
