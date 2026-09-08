# Flux Drive Kernel

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
  accounting.

## What works now

- deterministic actuator-bench simulation;
- command limiting and emergency-stop behavior;
- over-current and over-temperature trips;
- force, impulse, electrical energy, and telemetry accounting;
- CSV hardware-in-the-loop input and JSON output;
- standard-library-only tests.

Run a short simulation from the repository root:

```bash
python -m flux_drive_kernel --seconds 2 --command 0.25
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Measurement boundary

The default model represents a bench actuator. A command produces an
externally applied force in the model; it does not establish a reactionless
drive. A real experiment must use an independently calibrated force sensor,
isolated power measurement, thermal monitoring, and a documented momentum
accounting model. Do not connect this software directly to high-voltage,
high-current, vacuum, laser, cryogenic, or propulsion hardware without a
qualified engineer, an independent safety review, and a physical emergency
disconnect.

## Governance

The repository's `GOVERNANCE.md` is part of the engineering specification:
external actuation must remain independently interruptible, consequential
actions must be attributable and auditable, and simulation/prototype/verified
implementation/speculation must remain separately labeled.

