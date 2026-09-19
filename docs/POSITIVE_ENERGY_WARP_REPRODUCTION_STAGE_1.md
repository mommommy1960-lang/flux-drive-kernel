# Positive-Energy Warp Baseline Reproduction — Stage 1

## Frozen source

Fuchs et al., *Constant Velocity Physical Warp Drive Solution*,
arXiv:2405.02709, accessed September 19, 2026.

This stage reproduces only the analytic unsmoothed matter-shell foundation in
paper equations (19)-(20). It does not reproduce the later smoothing iteration,
anisotropic stress solution, numerical metric, shift vector, or energy-condition
optimization.

## Reproduced equations

For inner radius R1, outer radius R2, and total mass M:

[
\rho'(r)=\frac{3M}{4\pi(R_2^3-R_1^3)}
]

inside the shell and zero in the cavity/exterior. The cumulative mass is

[
m'(r)=M\frac{r^3-R_1^3}{R_2^3-R_1^3}
]

inside the shell, with zero in the cavity and M outside.

## Implemented checks

- shell volume and SI density;
- exact piecewise density;
- exact piecewise cumulative mass;
- monotonic enclosed mass;
- exterior ADM-mass baseline;
- compactness 2Gm/(c^2r);
- pointwise horizon-free check;
- invalid geometry/value rejection.

## Validation

Command:

    python -m unittest -v test_positive_energy_shell.py test_spacetime_consistency.py

Result:

- 19 total tests;
- 19 passed;
- 0 failures;
- 0 errors.

## Interpretation

This reproduces ordinary positive-mass spherical-shell bookkeeping. It is not
yet a warp-drive reproduction. The paper's transport behavior arises only after
constructing the smoothed anisotropic shell metric and adding the bounded shift
vector, followed by numerical all-observer energy-condition evaluation.

## Next stage

1. Freeze the smoothing function and numerical parameters from the paper.
2. Reproduce smoothed density and pressure inputs.
3. Solve the shell metric functions and compare exterior Schwarzschild limits.
4. Recompute the Eulerian stress-energy tensor.
5. Only then add the shift vector and test the stated velocity threshold.
