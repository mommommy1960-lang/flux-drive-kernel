# FUNDING & PHYSICAL VALIDATION — START HERE

## The short version

The Commons Flux Drive / Aurora research program has reached a boundary that software cannot honestly cross by itself.

The repository contains an executable falsification and measurement-analysis framework, a million-trial synthetic null-world reality audit, a measurement-grade build package, a low-energy bench plan, frozen CAL-00 measurement requirements, and explicit evidence gates. What it does **not** contain is evidence of reactionless propulsion, warp propulsion, spacetime control, or a flight-capable Aurora.

The next decisive work requires **physical metrology, calibrated instrumentation, bench/laboratory access, and independent replication**.

That is what funding or in-kind support would unlock.

## Why the program stopped here instead of claiming success

A software simulation can test code, analysis logic, controls, failure handling, uncertainty propagation, and false-positive behavior. It cannot establish that an unverified propulsion mechanism produces real force.

The 1,000,000-trial synthetic null-world audit deliberately modeled ordinary thermal, magnetic, cable/feedthrough, vibration/tilt, and measurement-noise artifacts. Its synthetic raw RMS was about 3.757 uN and corrected residual RMS about 1.543 uN. Corrected false-positive rates fell sharply as the gate increased, but the exercise demonstrated exactly why a large-looking force trace cannot be treated as propulsion until ordinary coupling channels are bounded.

Source: [`docs/MILLION_TRIAL_REALITY_AUDIT_2026-09-14.md`](docs/MILLION_TRIAL_REALITY_AUDIT_2026-09-14.md)

Current evidence state remains:

`physical_propulsion_proven=false`

That statement is not a weakness in the program. It is the research-control boundary preventing simulation from being advertised as physical discovery.

## What is already built

The repository currently provides:

- deterministic actuator-bench simulation and safety behavior;
- hardware-in-the-loop CSV replay and validation;
- measured force and reaction-force accounting;
- covariance-aware calibration/uncertainty propagation;
- radiation-momentum sanity references;
- conventional propulsion trade-study equations;
- repeated software invariant testing;
- a million-trial synthetic false-positive stress test;
- a measurement-grade physical build package;
- a low-energy materials/assembly plan;
- blind/sham/orientation control protocols;
- CAL-00 exit criteria;
- a procurement-tier plan designed to prefer borrowing or partner-lab access before purchasing equipment.

Primary technical orientation: [`README.md`](README.md)

## The physical experiment we need next

The immediate milestone is **CAL-00**, a low-energy calibration and baseline-characterization bench. It is not a flight test and is not permission to build hazardous apparatus.

Issue #11 is complete. The pre-instrument-selection measurement requirements are now frozen in [`docs/CAL00_FORCE_RANGE_AND_UNCERTAINTY_REQUIREMENTS_V0_1.md`](docs/CAL00_FORCE_RANGE_AND_UNCERTAINTY_REQUIREMENTS_V0_1.md).

Current design targets for both force and independent reaction-force channels are:

- bipolar calibrated range of at least -100 uN to +100 uN;
- target combined standard uncertainty <=1.0 uN;
- target expanded uncertainty <=2.0 uN, initially using k=2 and revisited from the actual uncertainty model before decisive reporting;
- minimum recorded force sampling of 100 samples/s, with 1,000 samples/s preferred when compatible with noise and synchronization;
- no decisive run above 80% of calibrated usable range;
- known benign reference-force injections before any experimental article is interpreted.

These numbers are **measurement-system design requirements**, not a prediction of the magnitude of any Flux effect.

## What is blocking CAL-00

### 1. Calibrated force and reaction-force instrumentation

We need two defensible force-measurement paths, independently calibrated, capable of satisfying the frozen range and uncertainty requirements and participating in synchronized acquisition.

Tracked in Issue #12.

### 2. Mechanical fixture and load-path engineering

The fixture must prevent cables, fasteners, supports, or other structures from bypassing the declared force channel. It must support sham and 0/90/180-degree orientation controls and a benign reference-injection interface.

Tracked in Issue #13.

### 3. Independent reviewer/operator

A technically qualified independent person must be able to inspect the frozen protocol and, after CAL-00 passes, reproduce a blinded run without being given a target answer.

Tracked in Issue #14.

### 4. Bench/laboratory access and quotes

We need written no-commitment options comparing purchase, borrowing, college/laboratory access, and partner-lab access. The objective is the **lowest-cost path that actually closes the uncertainty budget**, not the fanciest equipment list.

Tracked in Issue #15.

## What money or in-kind support would pay for

Funding is useful when it closes a documented evidence gap. Priority order:

1. access to calibrated force/reaction-force metrology that meets CAL-00 requirements;
2. calibration services and traceability documentation;
3. synchronized data acquisition and required environmental sensors;
4. low-energy mechanical fixture fabrication and reference-force injection capability;
5. qualified independent experimental review/operator time;
6. laboratory/bench access;
7. only after those gates are satisfied, the controlled experimental run itself.

Equipment should not be purchased merely because funds become available. Every purchase must map to a frozen measurement requirement or safety/control requirement.

## In-kind support is valuable too

A university, metrology laboratory, manufacturer, research group, or qualified individual could materially advance the program without transferring cash by providing:

- temporary access to suitable calibrated force instrumentation;
- calibration services;
- synchronized DAQ access;
- low-energy bench space;
- fixture fabrication/machining;
- experimental-design/metrology review;
- an independent blinded operator;
- written quotations or feasibility assessments.

## What funding does NOT buy

Funding does not purchase a predetermined scientific conclusion.

It does not authorize us to call a simulation a measurement, a residual a propulsion effect, or a prototype a flight-capable vehicle. It does not authorize hazardous high-voltage, high-current, RF, vacuum, laser, cryogenic, high-field, explosive, or compact-object experiments outside qualified facilities and independent safety review.

A null result is an acceptable research result and must remain in the record.

## Evidence ladder

The program uses the following promotion sequence:

**simulation -> instrumented prototype -> measured residual -> candidate anomaly -> independently verified propulsion**

A result advances only when the gate for the next state is satisfied. Failure returns the result to artifact investigation rather than being hidden or rebranded.

See [`docs/AURORA_FLUX_VALIDATION_MANUAL_V0_4.md`](docs/AURORA_FLUX_VALIDATION_MANUAL_V0_4.md).

## External metrology basis

The CAL-00 uncertainty framework follows standard metrology concepts rather than inventing special rules for this project. NIST Technical Note 1297 defines expanded uncertainty as U = k u_c and describes reporting the coverage factor; NIST convention commonly uses k=2, while the actual coverage interpretation depends on the uncertainty model. NIST also maintains SI-traceable force-transducer calibration services and has published work on micro-newton force realization.

References:

- NIST TN 1297, Expanded Uncertainty: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-6-expanded-uncertainty
- NIST TN 1297, Reporting Uncertainty: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty
- NIST, Calibration of Force Transducers: https://www.nist.gov/programs-projects/calibration-force-transducers
- Pratt et al., Force Calibration Via Electrostatics: https://www.nist.gov/publications/force-calibration-electrostatics

## Due-diligence route

A potential funder, laboratory, reviewer, or collaborator can start here and then inspect:

1. [`README.md`](README.md) — current technical capabilities and evidence boundary;
2. [`docs/MILLION_TRIAL_REALITY_AUDIT_2026-09-14.md`](docs/MILLION_TRIAL_REALITY_AUDIT_2026-09-14.md) — synthetic false-positive stress test;
3. [`docs/CAL00_FORCE_RANGE_AND_UNCERTAINTY_REQUIREMENTS_V0_1.md`](docs/CAL00_FORCE_RANGE_AND_UNCERTAINTY_REQUIREMENTS_V0_1.md) — frozen first-bench measurement requirements;
4. [`docs/CALIBRATION_AND_UNCERTAINTY_PLAN_V0_1.md`](docs/CALIBRATION_AND_UNCERTAINTY_PLAN_V0_1.md) — calibration and uncertainty accounting;
5. [`docs/LOW_ENERGY_BENCH_MATERIALS_LIST.md`](docs/LOW_ENERGY_BENCH_MATERIALS_LIST.md) — physical bench requirements;
6. Issues #12-#15 — live physical blockers.

## The funding proposition

The proposition is deliberately narrow:

**Help us move from a well-documented software/metrology research program to a properly calibrated physical falsification experiment.**

The immediate objective is not to promise a working Flux Drive. It is to obtain a physical answer that deserves to be believed either way.

If the result is ordinary physics, the program records ordinary physics. If a reproducible residual survives calibration, controls, uncertainty, momentum accounting, and independent replication, only then does the evidence state change.

That is what the money is for: **buying the experiment the right to answer the question, not buying the answer.**
