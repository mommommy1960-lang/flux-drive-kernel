# T-Sphere Phase-Effect Demonstrator v0.1

This package turns the older Quantum Flux Drive sphere/synchronizer concept
into a safe, testable robotics demonstrator.

## What it can demonstrate now

- A small rolling inspection sphere with a morphing outer shell.
- A command/telemetry state machine with fail-closed limits.
- Navigation through a constrained maze and through existing openings.
- Wireless telemetry and handoff to a second unit on the far side of a barrier.
- Non-destructive sensing behind a barrier when an approved radar or ultrasonic
  sensor is fitted.

## What it does not claim

The current design does not make matter pass through an intact wall. No
validated mechanism for that exists in the source material or in the current
prototype. The words “phase effect” refer to a measurable system demonstration:
the device disappears from one instrumented zone, the barrier-side sensor
tracks it or receives its telemetry, and the unit reappears through a known
opening or through a second synchronized unit.

## Run the deterministic software demo

```text
python tsphere/tsphere_sim.py
python -m unittest discover -s tsphere/tests -v
```

The software is deliberately hardware-neutral. Physical motors, RF, radar,
ultrasound, batteries, and enclosures remain separate engineering items and
must be reviewed before energizing.
