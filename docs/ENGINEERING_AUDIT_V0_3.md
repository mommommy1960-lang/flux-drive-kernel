# Aurora / Flux Drive Engineering Audit v0.3

## Scope

This audit records software and documentation corrections made before further
technical outreach. It is an engineering-quality review of the current model,
data-audit path, and architecture boundaries. It is not physical validation of
the Flux Drive.

## Corrections completed

1. **Actuator reference law** — removed unintended quadratic command scaling.
   The simulated force law is now explicitly linear and signed below saturation:
   `F_model = u I_max K_F`.
2. **Measured-force preservation** — measured HIL force is no longer clipped to
   the simulation force limit.
3. **First-sample integration** — zero-duration first samples are supported so
   replay does not invent an initial impulse or energy interval.
4. **Numerical integration** — HIL impulse and energy use an explicit
   trapezoidal rule.
5. **Electrical sign convention** — HIL reports signed net electrical energy and
   absolute energy throughput separately.
6. **Uncertainty propagation** — linear calibration and momentum closure support
   first-order covariance terms with covariance-bound validation.
7. **Measurement-grade closure** — momentum closure can be evaluated against
   expanded uncertainty with an explicit coverage factor. The fixed absolute
   tolerance remains only a software/legacy check.
8. **Fail-closed HIL mode** — requesting measurement-grade momentum evaluation,
   or supplying momentum uncertainty inputs, now implicitly requires the
   reaction channel even if the caller omits the separate reaction-channel flag.
9. **Radiation momentum** — the `P/c` reference is retained but generalized with
   an explicit 0–2 normal momentum-transfer factor for simple absorption/emission
   and ideal reflection reference cases.
10. **Electrical power bookkeeping** — active thermal-management load is
    distinguished from dissipated heat; charge/discharge power for storage is
    represented explicitly in the source/sink ledger.
11. **Thermal bookkeeping** — a separate first-law thermal power balance tracks
    generated, absorbed, rejected, and stored heat rate.
12. **Force instrumentation** — single-axis measurement is limited to screening;
    six-axis force/torque measurement is required before promoting a candidate
    anomaly to propulsion evidence.
13. **Experimental boundary** — fixture/support, cables/feedthroughs, mass flow,
    acoustic, RF/radiation, magnetic, electrostatic, atmospheric, buoyancy,
    convection, vibration, tilt, and center-of-mass pathways are explicitly
    identified as channels to measure or bound.
14. **Conventional propulsion** — Aurora now has a separate software reference
    layer for standard reaction-mass/electric-propulsion trade calculations so
    normal-space mobility is not architecturally dependent on the Flux Drive.
15. **Aurora mobility architecture** — assembly/emplacement, normal-space
    propulsion, local/attitude/abort mobility, and experimental Flux Drive are
    separate layers. A city-sized Aurora is not baselined as launching intact
    from Earth's surface.
16. **Claim boundary** — documents no longer rely on copied test counts as proof
    and do not label a software result, unexplained force residual, or simulated
    value as physical propulsion.

## Local validation record

The corrected core suite was executed locally after the final HIL and
conventional-propulsion changes.

- One complete discovery run: **56 tests passed**.
- The complete 56-test suite was then repeated **100 times** with zero failed
  iterations: **5,600 test-method executions**.
- Each suite includes a deterministic randomized invariant test containing 100
  subcases, giving **10,000 invariant subcases** across the 100 repeated suites.
- An additional **10,000 randomized numerical/adversarial cases** exercised the
  actuator linearity invariants and conventional-propulsion reference equations.
- `compileall` completed successfully for the core package and tests.

These results validate software invariants only. They do not establish a
physical force, a new propulsion mechanism, a warp field, or flight readiness.

## Hosted GitHub Actions status

The repository's hosted GitHub Actions runs are currently reporting failure
before any test step is exposed by the GitHub API. The latest inspected job has
no returned step list or usable test log. Therefore:

- local software validation is clean as recorded above;
- hosted CI must **not** be described as green;
- the hosted-run problem remains an infrastructure/account/workflow-execution
  issue to diagnose separately from the code audit;
- no physical or software-validation claim depends on a failed-to-start hosted
  runner.

## Remaining evidence gates

### Software / review

- independent code review;
- hosted CI successfully executing the same test suite;
- external review of equation assumptions and sign conventions;
- formal prior-art/patent search before making patent-novelty claims.

### Physical measurement

- calibrated force and reaction instrumentation;
- complete calibration metadata and uncertainty budget;
- declared measurement boundary and environmental channels;
- sham, off, orientation, cable-routing, thermal, magnetic, acoustic, pressure,
  vibration, and other preregistered controls;
- frozen analysis and acceptance threshold before the decisive run;
- independent replication.

### Aurora city-ship

- itemized dry/wet mass model;
- structure/load cases;
- pressure/habitat and population assumptions;
- life support and food/agriculture model;
- generation, storage, distribution, and thermal-rejection closure;
- radiation shielding/dose model;
- GNC, communications, maintenance, spares, and manufacturing architecture;
- conventional propulsion/propellant trade;
- modular assembly and logistics study;
- human-rating and independent safety pathway.

## Current technical claim

The defensible present-tense claim is:

> Aurora / Flux Drive has a corrected, auditable software and measurement
> architecture that is ready for skeptical independent review and a supervised
> low-energy measurement campaign. It does not yet demonstrate reactionless
> propulsion, a warp drive, or a flight-capable city-ship.
