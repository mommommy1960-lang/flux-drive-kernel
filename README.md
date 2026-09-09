# Flux Drive Kernel

This repository contains the executable, testable layer of the Commons Flux
Drive research program and Aurora reference architecture: a safe actuator-bench,
hardware-in-the-loop audit path, metrology utilities, and conventional
spacecraft-propulsion trade-study equations.

It is not a warp-drive implementation and it does not claim reactionless
propulsion, zero-point-energy extraction, faster-than-light travel, or
spacetime curvature control. Those claims require evidence that does not yet
exist. The kernel enforces a strict boundary between:

- **simulation**: deterministic plant and controller models;
- **prototype instrumentation**: measured voltage, current, temperature, force,
  reaction, and environmental channels;
- **verified propulsion**: a future status that may be assigned only after an
  independently calibrated physical result survives the complete uncertainty
  budget, control conditions, momentum/energy accounting, and independent
  replication.

## What works now

- deterministic actuator-bench simulation with an explicitly linear signed
  command/current/force model;
- measured-force preservation: instrument readings are never clipped to a
  simulation force limit;
- zero-duration first-sample handling so HIL replay does not invent impulse or
  energy before the first measured interval;
- command limiting and latching emergency-stop behavior;
- over-current and over-temperature trips;
- trapezoidal force/impulse and electrical-energy integration;
- separate signed net electrical energy and absolute energy-throughput reports;
- CSV replay with automatic validation and pass/fail reporting;
- reaction-channel momentum closure with a legacy fixed-tolerance software
  check and a measurement-grade expanded-uncertainty path;
- covariance-aware calibration and uncertainty propagation;
- radiation-momentum references covering emitted/absorbed and ideal reflected
  cases;
- storage-aware electrical power-flow bookkeeping and a separate thermal power
  balance;
- standard ideal conventional-propulsion references: Isp/exhaust velocity,
  Tsiolkovsky delta-v, mass ratio, propellant fraction, thrust/mass flow, and an
  electric-propulsion power/thrust reference;
- a deterministic 100-case software invariant sweep in addition to unit tests.

## Quick software checks

Run a short simulation from the repository root:

```bash
python -m flux_drive_kernel --seconds 2 --command 0.25
```

Audit measured channels from a CSV with no external actuation enabled by the
software:

```bash
python -m flux_drive_kernel --hil-csv data/run001.csv
```

Require the reaction channel for the software closure check:

```bash
python -m flux_drive_kernel --hil-csv data/run001.csv --require-momentum
```

For a measurement-grade momentum assessment, supply calibrated impulse
uncertainties and require uncertainty-based closure:

```bash
python -m flux_drive_kernel \
  --hil-csv data/run001.csv \
  --require-momentum \
  --measurement-grade-momentum \
  --force-impulse-std-uncertainty <N_s> \
  --reaction-impulse-std-uncertainty <N_s> \
  --coverage-factor 2
```

The fixed `--momentum-tolerance` path is a software/legacy gate only. It is not
sufficient evidence for a physical propulsion claim.

The CSV must contain `timestamp_s`, `command`, `measured_voltage_V`,
`measured_current_A`, `measured_temperature_C`, and `measured_force_N`.
Measurement-grade momentum analysis additionally requires `reaction_force_N`.
Environmental strict mode can require the declared environmental channels.

Run the tests:

```bash
python -m unittest discover -s tests -v
```

See [`docs/ENGINEERING_AUDIT_V0_3.md`](docs/ENGINEERING_AUDIT_V0_3.md) for the
current audit record, repeated local validation, and hosted-CI status. A hosted
CI badge or run result must not be described as green unless GitHub actually
executes and passes the test steps.

## Measurement boundary

The default model represents a bench actuator. A command produces a modeled
externally applied force; it does not establish a reactionless drive. A real
experiment must use independently calibrated force and reaction measurements,
isolated power measurement, thermal/environment monitoring, and a declared
momentum-accounting boundary. Do not connect this software directly to
high-voltage, high-current, vacuum, laser, cryogenic, or propulsion hardware
without a qualified engineer, an independent safety review, and a physical
emergency disconnect.

## Aurora architecture

Aurora separates four mobility layers:

1. modular assembly and emplacement;
2. conventional normal-space translation and mission propulsion;
3. attitude control, docking, station-keeping, collision avoidance, and abort
   mobility; and
4. the experimental Flux Drive research layer, isolated behind evidence and
   safety gates.

The city-ship concept is not baselined as a vehicle that launches intact from
Earth. Modular in-space assembly is the more credible requirements path for a
structure of that scale. See
[`docs/AURORA_PROPULSION_ARCHITECTURE_V0_1.md`](docs/AURORA_PROPULSION_ARCHITECTURE_V0_1.md).

## Governance

The repository's `GOVERNANCE.md` is part of the engineering specification:
external actuation must remain independently interruptible, consequential
actions must be attributable and auditable, and simulation/prototype/verified
implementation/speculation must remain separately labeled.

See [`docs/MEASUREMENT_GRADE_BUILD_PACKAGE.md`](docs/MEASUREMENT_GRADE_BUILD_PACKAGE.md)
for the controlled bench architecture, declared system boundary, uncertainty
budget, run sequence, force-instrument stages, and acceptance criteria.

See [`docs/REVIEWER_EQUATION_SHEET_V0_3.md`](docs/REVIEWER_EQUATION_SHEET_V0_3.md)
for governing equations, variables, units, assumptions, and falsification gates.

See [`docs/NOVELTY_AND_PRIOR_ART_BOUNDARY.md`](docs/NOVELTY_AND_PRIOR_ART_BOUNDARY.md)
for what is established prior art, what may be an integration contribution, and
what must not be called novel without a dedicated prior-art search.

The concrete first-build materials and assembly sequence are in
[`docs/LOW_ENERGY_BENCH_MATERIALS_LIST.md`](docs/LOW_ENERGY_BENCH_MATERIALS_LIST.md).

Historical published observations are registered in
[`data/literature_reference_experiments.csv`](data/literature_reference_experiments.csv)
and explained in [`docs/HISTORICAL_EXPERIMENT_REGISTER.md`](docs/HISTORICAL_EXPERIMENT_REGISTER.md).

For a concise, evidence-bounded funding case, see
[`docs/FUNDER_EVIDENCE_BRIEF.md`](docs/FUNDER_EVIDENCE_BRIEF.md).

## Aurora submission checks

Run the full non-hardware reproducibility package from the repository root:

```bash
python tools/run_submission_demo.py
```

It validates the local Aurora schemas and runs the current software gate. It
prints `physical_propulsion_proven=false` by design. See
[`docs/PRE_SUBMISSION_TECHNICAL_AUDIT.md`](docs/PRE_SUBMISSION_TECHNICAL_AUDIT.md),
[`docs/SUBMISSION_REVIEW_PACKET.md`](docs/SUBMISSION_REVIEW_PACKET.md), and
[`docs/PUBLIC_CONFIDENTIAL_BOUNDARY.md`](docs/PUBLIC_CONFIDENTIAL_BOUNDARY.md)
before sending the project for independent review.
