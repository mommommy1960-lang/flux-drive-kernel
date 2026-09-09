# Aurora / Flux Drive Pre-Submission Technical Audit

## Review question

Can the current Aurora and Flux Drive package establish that the proposed
vehicle will fly?

**Answer:** No. It establishes an executable software and measurement-audit
framework, not physical propulsion. The package is suitable for an independent
feasibility review and a controlled bench-test proposal.

## Claims-to-evidence matrix

| Claim | Evidence currently available | Classification | Required next evidence |
|---|---|---|---|
| Aurora command and safety runtime behaves deterministically | Automated unit/invariant tests; replay and schema checks | Demonstrated in software | Green hosted CI result and independent code review |
| Unsafe actuator proposals fail closed | Consent, limit, thermal, emergency-stop, and bridge tests | Demonstrated in software | Hardware-independent safety review |
| The default bench force law is internally coherent | Explicit linear command/current/force model plus regression tests | Demonstrated in software model | Calibration against a real actuator if one is selected |
| Calibration uncertainty supports correlated inputs | First-order covariance-aware propagation | Demonstrated in software | Independent metrology review and real certificate covariance data |
| The Flux Drive produces useful net thrust | No calibrated physical thrust data | Unverified | Measurement-grade force/reaction test, controls, full uncertainty budget |
| Acoustic/EM fields can create a useful external reaction force in the proposed architecture | Conceptual actuator hypothesis only | Hypothesis | Identify, model, and measure the external momentum channel |
| Aurora can operate as a city-sized spacecraft | Requirements-level concept only | Unverified | Complete mass, power, thermal, ECLSS, structure, radiation, GNC, communications, maintenance, and propulsion design |
| Stable black-hole or wormhole transit is available | No validated mechanism or engineering pathway | Unsupported | Relativistic theory and energy-condition analysis by qualified researchers |

## Physics audit

The governing baseline uses `F = dp/dt` and requires every proposed force to be
assigned to a measured momentum channel. Conventional rocket, electric, photon,
and field-interaction propulsion all require momentum accounting across a
properly declared system boundary.

The v0.3 reference model distinguishes the one-way photon momentum baseline
`P/c` from the ideal-reflection limit `2P/c`. The code no longer treats `P/c` as
a universal radiation-pressure expression.

The electrical power ledger also now states explicitly that its `thermal` term
means electrical power consumed by active thermal-management hardware. It must
not be used to re-count heat already represented by actuator/control/loss terms.

The uncertainty implementation includes first-order covariance terms rather
than silently assuming every calibration input is independent.

These corrections improve internal consistency; they do not validate a new
propulsion mechanism.

## Required decisive experiment

The first experiment must be a measurement-grade force test, not a flight test.
It must include traceably calibrated force measurement, an independent reaction
channel, conducted power measurement, acoustic and RF monitoring, vibration and
cable controls, thermal drift correction, environmental magnetic monitoring,
sham actuators, blinded runs, a declared system boundary, and a preregistered
uncertainty threshold.

A single-axis force sensor may be used only for low-energy screening under the
conditions in `MEASUREMENT_GRADE_BUILD_PACKAGE.md`. A claimed anomalous force
must advance to a six-axis force/torque validation stage before it is treated as
propulsion evidence.

A result is positive only if the residual exceeds the complete predeclared
uncertainty budget, survives sham/orientation/cable/environment controls, closes
all declared reaction channels, and survives independent replication.

## Software audit status

The authoritative software status is the current GitHub Actions result, not a
manually copied test-count number in this document. The test suite includes a
deterministic 100-case invariant sweep intended to catch algebra, sign,
calibration, radiation-reference, and accounting regressions. Passing software
tests demonstrate internal software behavior only; they do not demonstrate
physical thrust.

## Submission classification

Submit the work as:

> Aurora: an auditable AI-guided vessel architecture and Flux Drive propulsion
> research program seeking independent feasibility review and experimental
> validation.

Do not submit it as a proven propulsion system, a flight-ready city-ship, or a
black-hole/wormhole transport system.
