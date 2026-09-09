# Flux Drive Kernel

The repository test gate runs on every push and pull request.

This repository contains the first executable, testable layer of the Commons
Flux Drive project: a safe actuator-bench and hardware-in-the-loop reference
kernel.

It is not a warp-drive implementation and it does not claim reactionless
propulsion, zero-point-energy extraction, faster-than-light travel, or
spacetime curvature control. Those claims require evidence that does not yet
exist. The kernel therefore enforces a strict boundary between:

- **simulation**: deterministic plant and controller models;
- **prototype instrumentation**: measured voltage, current, temperature, and
  force channels;
- **verified propulsion**: a future status that may be assigned only after an
  independently calibrated force measurement closes momentum and energy
  accounting and survives controlled replication.

## What works now

- deterministic actuator-bench simulation with an explicitly linear signed
  command/current/force model;
- command limiting and emergency-stop behavior;
- over-current and over-temperature trips;
- force, impulse, electrical energy, and telemetry accounting;
- hardware-in-the-loop measured-channel API and JSON output;
- CSV replay with automatic validation and pass/fail reporting;
- strict reaction-force momentum-closure mode;
- covariance-aware calibration and uncertainty propagation for measurement-grade data;
- radiation-momentum reference calculations covering emitted/absorbed and ideal reflected cases;
- GitHub Actions continuous integration on every push and pull request;
- a deterministic 100-case software invariant sweep in addition to the unit tests.

Run a short simulation from the repository root:

```bash
python -m flux_drive_kernel --seconds 2 --command 0.25
```

Audit measured channels from a CSV (no external actuation is enabled):

```bash
python -m flux_drive_kernel --hil-csv data/run001.csv
```

Require the reaction channel for a strict closure test:

```bash
python -m flux_drive_kernel --hil-csv data/run001.csv --require-momentum
```

The CSV must contain `timestamp_s`, `command`, `measured_voltage_V`,
`measured_current_A`, `measured_temperature_C`, and `measured_force_N`.
The report includes measured impulse, electrical energy, peak channels, safety
trips, and validation errors. `momentum_closure_status` remains
`not_assessed` until an independent reaction/momentum channel is recorded.
Strict mode fails closed when `reaction_force_N` is absent or when the signed
force impulses do not close within the declared tolerance.

Run the tests:

```bash
python -m unittest discover -s tests -v
```

The current CI result, rather than a manually copied test-count number in a
document, is the authoritative software-gate status.

## Measurement boundary

The default model represents a bench actuator. A command produces a modeled
externally applied force; it does not establish a reactionless drive. A real
experiment must use independently calibrated force and reaction measurements,
isolated power measurement, thermal/environment monitoring, and a declared
momentum-accounting boundary. Do not connect this software directly to
high-voltage, high-current, vacuum, laser, cryogenic, or propulsion hardware
without a qualified engineer, an independent safety review, and a physical
emergency disconnect.

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
for what is established prior art, what is an integration contribution, and what
must not be called novel without a dedicated search.

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
