# Aurora / Flux Validation Manual v0.4

Status: working engineering validation manual  
Date: 2026-09-14

## Purpose

This manual keeps the Aurora / Flux program reality-first. It defines how to
separate software simulation, measured laboratory data, candidate anomalies,
and any future verified propulsion result.

The goal is not to tune a simulator until it prints a desired answer. The goal
is to determine whether a reproducible residual survives standard physics,
calibration, uncertainty, environmental-coupling checks, and momentum
accounting.

## Evidence states

### A. Simulation

Use for controller tests, software invariant sweeps, synthetic sensitivity
studies, conventional propulsion trade studies, and HIL replay.

A simulated force is not measured propulsion.

### B. Instrumented prototype

A physical test belongs here when it has calibrated force and reaction-force
channels, electrical measurements, temperature/environmental observations, and
a frozen analysis plan. Sham/device-off and orientation controls are required
before a residual can be treated as interesting.

### C. Candidate anomaly

A repeatable residual may enter this state only after ordinary coupling channels
have been bounded below the observed effect and the result exceeds the
predeclared uncertainty gate.

### D. Verified propulsion

This state remains unavailable until the complete physical acceptance gate in
`REVIEWER_EQUATION_SHEET_V0_3.md` passes and an independent operator reproduces
the result.

## Software validation gate

Before interpreting new data, run the repository's unit tests and submission
demo, followed by the million-trial synthetic reality audit:

```bash
python -m unittest discover -s tests -v
python tools/run_submission_demo.py
python tools/run_million_trial_reality_audit.py
```

A software regression freezes interpretation until resolved.

## Million-trial reality audit

The synthetic null-world harness exists to measure how easily ordinary artifact
channels can resemble thrust.

Reference run:

- trials: 1,000,000
- seed: 20260914
- physical propulsion proven: false

See `MILLION_TRIAL_REALITY_AUDIT_2026-09-14.md`.

## Candidate-signal promotion gate

A candidate signal advances only when all of the following are satisfied:

1. it exceeds the predeclared expanded uncertainty;
2. sham/device-off controls do not reproduce it;
3. reversed and perpendicular orientations follow a preregistered prediction;
4. thermal, magnetic, mechanical, acoustic, pressure, convection, buoyancy,
   radiation, and other declared channels are bounded below the effect size;
5. momentum accounting closes across the declared boundary;
6. the analysis version and exclusion rules were frozen before the decisive run;
7. an independent operator reproduces the result.

Failure of any item returns the result to artifact investigation.

## Scaling gate

Even a verified micro-newton residual would not automatically imply useful
vehicle propulsion. Before any vehicle-integration claim, require a measured,
predictive scaling law across relevant variables such as input power, geometry,
orientation, duty cycle, environment, device count, and thermal state.

The scaling law must predict blinded runs rather than merely fit completed data.

## Aurora mobility architecture

Aurora retains separate conventional mobility requirements for attitude
control, docking, station keeping, collision avoidance, abort capability, and
normal-space translation. The experimental Flux layer remains isolated behind
evidence gates until independently demonstrated.

## Near-term engineering target

The credible next target is not a city-scale vehicle. It is a
measurement-quality research program capable of distinguishing very small force
signals from ordinary experimental artifacts and of preserving an auditable
record of failures as well as successes.

## Claim language

Use:

- **simulation result** for software outputs;
- **measured residual** for unexplained instrument data;
- **candidate anomaly** only after controls fail to explain a repeatable
  residual;
- **verified propulsion** only after the full acceptance gate and independent
  replication.

Do not use `working Flux Drive`, `reactionless propulsion`, `warp drive`, or
`flight-capable Aurora` unless physical evidence establishes the claim.

## Current state

The software and evidence architecture is operational as a falsification,
measurement, and conventional trade-study program. No verified exotic
propulsion mechanism currently exists.

That is the correct engineering state from which to design the next decisive
experiment.
