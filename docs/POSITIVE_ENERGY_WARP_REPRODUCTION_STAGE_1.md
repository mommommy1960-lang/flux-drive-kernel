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

## Hosted-CI reconciliation

GitHub Actions run 35459011481 tested intermediate commit `65bec85` and failed
during test discovery because `tests/test_positive_energy_shell.py` was present
before `flux_drive_kernel/positive_energy_shell.py` became reachable from that
intermediate branch head. The reported exception was:

    ModuleNotFoundError: No module named 'flux_drive_kernel.positive_energy_shell'

This was a commit-order/integration failure, not a failed equation assertion.
The branch was then verified to contain the module, test, and this report.
A new sequential reconciliation commit was created to trigger hosted validation
against the complete file set. The failed run remains preserved and must not be
described as green.

Hosted reconciliation result: GitHub Actions run 35459407455 completed
successfully against commit `132eb89d48ebc85a33874f3073a0168964b24e3d`.
All workflow steps, including the unit-test step, passed. This successful run
closes the integration-order fault; it does not change the scientific
non-claims above.
