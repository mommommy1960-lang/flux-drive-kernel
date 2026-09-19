# What the “moving belt” means

## Short version

The moving belt is **not a physical conveyor belt inside the craft**. It is a plain-language picture for the metric's **shift field**: the off-diagonal time-space term (g_{01}), directed along the proposed travel axis.

Think of spacetime as graph paper with a small arrow at every point. The arrow says how the spatial coordinates are carried from one time slice to the next.

- Inside the bubble, the arrow is approximately constant.
- Outside the bubble, the arrow is zero.
- Across the shell, the arrow smoothly changes between those values.

A constant arrow in the cabin can be locally flat: passengers need not feel ordinary acceleration merely because the coordinate shift is nonzero. The transition region is where derivatives of the shift appear. Those derivatives create curvature and momentum-density terms in the Einstein tensor, so the shell—not the empty cabin—is the difficult physical part.

## Frozen implementation

The current research branch implements the published direct-component interpretation

[
g_{01}=g^{\rm static}_{01}-f(r)\left(g^{\rm static}_{01}+\beta\right),
]

with (eta=0.02) and a compact radial shape (f(r)). This is Implementation A only. An independent 3+1 lapse/shift reconstruction is still required.

## What it does not prove

A coordinate shift is not automatically propulsion. The present calculation does not show that matter can generate the metric, that the shell is stable, that a bubble can be started or stopped, or that a craft can travel nearly instantaneously. It asks a narrower falsification question: for a frozen metric, what stress-energy tensor does general relativity require, and do sampled observers see energy-condition failures?

“Positive in the sampled grid” is not the same as a proof. Numerical convergence, complete spatial coverage, an independent implementation, causal/horizon checks, stability, tidal checks, and physical source feasibility remain open.
