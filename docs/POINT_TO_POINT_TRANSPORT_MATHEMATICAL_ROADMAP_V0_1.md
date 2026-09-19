# Flux Drive Point-to-Point Transport — Mathematical Roadmap v0.1

## Design intent and present status

The long-range design intent is push-button transport from point A to point B by controlled spacetime geometry. Earlier concept language sometimes described this as creating or harnessing a miniature black hole ahead of Aurora. That phrase records the aspiration but does not supply a valid mechanism.

A black hole is not a traversable two-way portal. The only mathematically relevant point-to-point branches are candidate traversable-wormhole geometries or warp-like spacetime metrics. Neither branch currently has a demonstrated source, stable device, safe control law, or experimental transport evidence. The present Flux bench program therefore remains separate.

## Governing equation

Every spacetime proposal begins with the Einstein field equation:

[
G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}.
]

Specifying a desired metric (g_{\mu\nu}) is not enough. The project must derive the required stress-energy tensor (T_{\mu\nu}), test conservation (
abla_\mu T^{\mu\nu}=0), identify a physically realizable source, and show stability, controllability, causal consistency, tolerable curvature, and safe geodesics.

## Branch A — Black-hole scale calculations

For an ideal non-rotating black hole:

[
r_s=\frac{2GM}{c^2},\qquad E=Mc^2.
]

This branch is limited to scale and hazard analysis. It is falsified as a transport mechanism because an event horizon is not a controllable exit to a chosen destination. No bench residual may be labeled a black-hole effect.

## Branch B — Traversable-wormhole consistency study

A standard static spherical ansatz is:

[
ds^2=-e^{2\Phi(r)}c^2dt^2+\frac{dr^2}{1-b(r)/r}+r^2d\Omega^2.
]

At a candidate throat (r_0), the model must at minimum check:

- (b(r_0)=r_0);
- finite (Phi(r)), avoiding an event horizon;
- the flaring-out condition (b'(r_0)<1);
- curvature invariants and tidal acceleration along traveler geodesics;
- the required (T_{\mu\nu}) and all relevant energy conditions;
- quantum-energy-inequality restrictions;
- linear/nonlinear stability and backreaction;
- a causal construction and shutdown procedure.

A symbolic solution that violates these checks or requires no physically identified source is a mathematical example, not an engine.

## Branch C — Warp-metric consistency study

Use a declared 3+1/ADM metric:

[
ds^2=-\alpha^2c^2dt^2+\gamma_{ij}(dx^i+\beta^i cdt)(dx^j+\beta^j cdt).
]

For each lapse (alpha), spatial metric (gamma_{ij}), and shift (eta^i), calculate rather than assume:

1. the complete Einstein tensor and implied stress-energy;
2. local and integrated energy density for specified observers;
3. null, weak, dominant, and strong energy-condition behavior;
4. horizons, causal accessibility, and whether the bubble can be created or controlled from inside;
5. curvature, traveler tidal load, and boundary gradients;
6. conservation, initial-data constraints, stability, and radiation;
7. source-field compatibility and total energy/power;
8. subluminal limits before any superluminal interpretation.

Positive coordinate energy density in one ansatz is not sufficient. The full stress-energy, constraints, sourceability, stability, and causal control must all close.

## Branch D — Flux residual experiment

The bench hypothesis is deliberately independent:

[
J_{res}=J_{device}+J_{reaction}+J_{environment}.
]

An interesting residual must exceed preregistered combined uncertainty, survive sham and orientation controls, obey a frozen scaling prediction, close energy/momentum accounting, and replicate independently. Even then it is only evidence of an unexplained interaction. It does not become evidence of curvature, a wormhole, a warp bubble, or point-to-point travel without additional discriminating predictions.

## Computation package required next

The legitimate “paper proof” deliverable is a reproducible notebook or code module that:

- defines one metric and coordinate convention;
- derives (G_{\mu\nu}) and (T_{\mu\nu}) symbolically;
- verifies units, limits, conservation, and constraint equations;
- computes curvature invariants and geodesics;
- maps energy-condition violations over parameter space;
- tests perturbative stability;
- publishes failing parameter regions as well as surviving ones;
- contains no fitted transport claim.

## Promotion rule

[
	ext{consistent metric}\not\Rightarrow	ext{physical source}\not\Rightarrow
	ext{stable device}\not\Rightarrow	ext{transport}.
]

The point-to-point objective becomes credible only after every implication is separately demonstrated. Until then, the repository may truthfully say the mathematics is being tested—not that a push-button drive exists.

## Primary research starting points

- Miguel Alcubierre, *The warp drive: hyper-fast travel within general relativity*.
- Alexey Bobrick and Gianni Martire, *Introducing physical warp drives*.
- Erik Lentz, *Breaking the warp barrier: hyper-fast solitons in Einstein-Maxwell-plasma theory*.
- Eleni-Alexandra Kontou, *Wormhole restrictions from quantum energy inequalities*.
- The repository's [black-hole and wormhole boundary](BLACK_HOLES_AND_WORMHOLES_BOUNDARY.md).
