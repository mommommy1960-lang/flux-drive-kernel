# CAL-00 Experiment Zero — Flux Checkpoint (2026-09-12)

## Status boundary

The Flux corpus supports a reproducible measurement/falsification platform ready for a supervised low-energy physical bench campaign. It does **not** demonstrate propulsion, reactionless thrust, inertia modification, vacuum-energy extraction, warp, faster-than-light travel, or instantaneous transportation.

## Frozen acceptance contract

Define measured impulse:

\[
J = \int_{t_0}^{t_1} F(t)\,dt
\]

Each blinded trial reports measured impulse \(J_m\), expected injected impulse \(J_k\), expanded uncertainty \(U_J\), and classification.

- Known-force PASS: \(|J_m-J_k|\le U_J\)
- Null PASS: \(|J_m|\le U_J\)
- Reversal: \(J_+\approx -J_-\) within combined uncertainty
- Deliberate artifacts must be identified by auxiliary channels or cause run rejection; they must not be relabeled as Flux.

## CAL-00 campaign

CAL-00 is Experiment Zero and contains randomized NULL, KNOWN+, KNOWN−, SHAM, and ARTIFACT trials. The analyst receives anonymous run IDs. The condition key remains sealed until calibration constants, exclusions, analysis code, and uncertainty calculations are frozen.

CAL-00 uses only conventional, independently calculable forces. Its purpose is to validate known-force recovery, null discrimination, reversal behavior, artifact rejection, and the uncertainty budget before FRU-01 inherits the apparatus.

Required controls include command-off, sham, reversed/perpendicular orientation, cable/feedthrough, thermal, vibration, acoustic, electromagnetic, environmental, calibration, drift, and timing controls, with synchronized force/reaction, voltage, current, temperature, and environmental telemetry.

## FRU-01 decision rule

For each active trial:

\[
R_J = J_{\\text{article}} + J_{\\text{reaction}} + J_{\\text{known external}}
\]

A candidate residual requires \(|R_J|>U_R\), preregistered behavior, and no correlation with identified conventional artifact channels. One positive run is insufficient.

Promotion states are:

1. CANDIDATE — repeatable residual.
2. CANDIDATE—REPLICATED INTERNALLY — successful blinded internal replication.
3. INDEPENDENT CANDIDATE — different apparatus and/or operator.
4. External laboratory reproduction.

No state may be renamed “warp drive” or treated as engineering proof.

## Immediate real-world action

Use the existing Test Operator Outreach Packet to contact a qualified university, metrology, or instrumentation partner capable of calibrated force measurement, reaction/momentum closure, synchronized electrical/thermal logging, environmental monitoring, blinded controls, and signed run records.

Funding purchases calibrated instrumentation and supervised testing, not promised exotic propulsion. A null result remains valuable reusable metrology infrastructure.

## Synchronization checkpoint

- VERIFIED: executable simulation/HIL/metrology framework exists; physical propulsion is unproven.
- FROZEN: CAL-00 precedes FRU-01; known-force recovery, null discrimination, reversal, and artifact rejection are mandatory.
- PRIMARY OBSERVABLE: momentum residual after measured reaction and external channels plus uncertainty.
- NEXT PHYSICAL ACTION: obtain an independently instrumented low-energy CAL-00 campaign with a qualified partner.
- EUREKA STATUS: none.

Nature, not prose, decides the result.
