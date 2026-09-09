# Flux Drive: Funder Evidence Brief

## The investable problem

Very small force claims are easy to mistake for propulsion. Thermal drift,
magnetic coupling, cable stiffness, vibration, buoyancy, convection, outgassing,
and center-of-mass motion can all create a convincing trace. Historical
closed-cavity and other propellantless-propulsion experiments have produced
conflicting or artifact-limited results, which makes the measurement problem
itself the first fundable engineering target.

## What exists now

The open Flux Drive Kernel provides:

- deterministic simulation;
- measured-channel CSV ingestion;
- safety trips and fail-closed behavior;
- force, impulse, voltage, current, temperature, and energy accounting;
- reaction-channel momentum closure;
- covariance-aware calibration and uncertainty propagation;
- radiation-momentum reference calculations;
- historical experiment reference data;
- relativity scale calculations that are explicitly separated from propulsion claims;
- an automated software test gate including a deterministic 100-case invariant sweep;
- a build-ready low-energy measurement-bench specification;
- a declared public/confidential boundary and evidence-gated claim language.

The software test count is intentionally not hard-coded in this funding brief;
the repository's CI result is the authoritative current count.

## What funding unlocks

Funding would purchase access to calibrated instrumentation and a supervised
test environment—not a promise of exotic propulsion. The first milestone is a
reproducible measurement campaign that can either identify an anomalous force
above the complete uncertainty budget or decisively bound the claim below it.

A null result is a valid outcome and does not make the measurement infrastructure
worthless. It produces reusable metrology, controls, and audit tooling for other
low-thrust experiments.

## Milestones

### M1 — Bench completion

Install the force, reaction, electrical, thermal, vibration, magnetic, acoustic,
pressure, orientation, and synchronized data channels. Verify independent
physical cutoff and calibration records.

### M2 — Controls

Run command-off, sham-device, reversed-orientation, perpendicular-orientation,
cable/feedthrough, magnetic-background, and thermal-drift controls before
testing any active article.

### M3 — Frozen analysis

Freeze the hardware configuration, calibration metadata, software commit, data
schema, uncertainty budget, covariance assumptions, system boundary, and
acceptance threshold before the powered run.

### M4 — Independent replication

Give the raw data and frozen analysis to a second operator. A result counts only
if the second operator can reproduce the reported force and uncertainty.

### M5 — Mechanism gate

Only if an anomaly survives M1–M4 should a mechanism study ask what external
momentum or field interaction could produce it. Flight sizing does not begin
before this gate.

## Success and failure are both valuable

A positive result would justify a larger replication campaign. A null result or
an identified artifact would still produce a valuable open metrology package
for advanced-propulsion research and prevent future teams from repeating the
same false-positive pathways.

## Current claim boundary

The project has not proven reactionless propulsion, a warp drive, a stable
black hole, a traversable wormhole, or a flight-ready city-ship. The credible
present-tense claim is:

> Flux Drive has an executable, reproducible measurement and falsification
> platform ready for a supervised low-energy physical bench campaign.

That is the claim a serious funder can evaluate immediately.
