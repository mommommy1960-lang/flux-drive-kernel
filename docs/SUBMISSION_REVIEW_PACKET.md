# Aurora / Flux Drive Reviewer Packet

## One-page request

We are requesting an independent technical feasibility review of a simulation-
defined Aurora vessel architecture and Flux Drive propulsion hypothesis.

Please assess:

1. whether the proposed governing equations are dimensionally and physically
   coherent;
2. whether the proposed acoustic and electromagnetic architecture has a
   measurable external momentum channel;
3. whether the force-measurement plan can distinguish thrust from vibration,
   thermal drift, magnetic coupling, cable forces, and acoustic coupling;
4. what minimum controlled experiment would justify further work; and
5. what result would falsify the propulsion claim.

## What is included

- Aurora command and telemetry schemas;
- deterministic replay and tamper-detection tests;
- simulation-only Aurora-to-Flux Drive bridge;
- force, momentum, and power bookkeeping checks;
- preliminary lab-vessel safety envelope;
- pre-submission technical audit;
- non-confidential system boundary and source reconciliation.

## What is not claimed

- no demonstrated net propulsion;
- no flight certification;
- no human-rated life-support design;
- no stable black-hole or wormhole generator;
- no autonomous authority over physical actuators.

## Requested reviewer output

Please return one of:

- **Proceed to controlled bench experiment**;
- **Revise model or measurement design**; or
- **Stop: claim is not physically supported**.

The review should identify the equations, measurements, or assumptions that
drive its conclusion.

## Reproducibility

From the repository root, run:

```text
python tools/run_submission_demo.py
```

The command validates the JSON schemas, executes the local test suite, and
prints the software-only status. It does not activate RF, acoustic, power, or
propulsion hardware.
