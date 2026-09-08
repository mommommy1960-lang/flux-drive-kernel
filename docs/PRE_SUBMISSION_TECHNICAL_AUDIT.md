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
| Aurora command and safety runtime behaves deterministically | 25 passing local tests; replay and schema checks | Demonstrated in software | Hosted CI result and independent code review |
| Unsafe actuator proposals fail closed | Consent, limit, thermal, emergency-stop, and bridge tests | Demonstrated in software | Hardware-independent safety review |
| The Flux Drive produces useful net thrust | No calibrated physical thrust data | Unverified | Six-axis force measurement, null tests, full uncertainty budget |
| Acoustic/EM fields can create a reaction force | Blue Book actuator concept only | Hypothesis | Identify and measure the external momentum channel |
| Aurora can operate as a city-sized spacecraft | Requirements-level concept only | Unverified | Complete mass, power, thermal, ECLSS, structure, radiation, GNC, and communications design |
| Stable black-hole or wormhole transit is available | No validated mechanism or engineering pathway | Unsupported | Relativistic theory and energy-condition analysis by qualified researchers |

## Physics audit

The governing baseline uses `F = dp/dt` and requires every proposed force to be
assigned to a measured momentum channel. NASA's spacecraft guidance material
describes rocket and ion propulsion through momentum exchange, and NASA's
conservation-of-momentum reference relates force to momentum flux. These are
the correct first checks for the Flux Drive claim.

The relevant comparison sources are:

- NASA, [Gravity and Mechanics / conservation of momentum](https://science.nasa.gov/learn/basics-of-space-flight/chapter3-2/).
- NASA Glenn, [Conservation of Momentum](https://www.grc.nasa.gov/www/k-12/airplane/conmo.html).
- NASA/JPL, [Fundamentals of Electric Propulsion](https://descanso.jpl.nasa.gov/SciTechBook/series1/Goebel__cmprsd_opt.pdf).
- NASA, [Dawn FAQ on ion propulsion](https://science.nasa.gov/mission/dawn/faq/).

These sources establish the comparison baseline; they do not validate Aurora's
proposed mechanism.

## Required decisive experiment

The first experiment must be a measurement-grade force test, not a flight test.
It must include a calibrated six-axis balance, conducted power measurement,
acoustic and RF monitoring, vibration and cable controls, thermal drift
correction, environmental magnetic monitoring, sham actuators, blinded runs,
and a preregistered uncertainty threshold. A result is positive only if the
force residual exceeds the complete uncertainty budget and survives independent
replication.

## Submission classification

Submit the work as:

> Aurora: an auditable AI-guided vessel architecture and Flux Drive propulsion
> research program seeking independent feasibility review and experimental
> validation.

Do not submit it as a proven propulsion system, a flight-ready city-ship, or a
black-hole/wormhole transport system.
