# Aurora/Flux: an auditable systems architecture and falsification protocol for an unverified advanced-propulsion concept

**Author:** Mya P. Brown, independent researcher, Seattle, Washington, United States  
**Corresponding author:** mommommy1960@gmail.com  
**Manuscript status:** pre-submission draft for formal peer review  
**Evidence status:** software and measurement-protocol contribution; no demonstrated propulsion

## Abstract

Advanced-propulsion proposals are vulnerable to a recurring category error: internally consistent simulation output, instrument response, or incomplete force measurements are treated as evidence of net propulsion. This paper presents Aurora/Flux, an open, auditable software and measurement architecture designed to prevent that promotion error. The implementation separates deterministic simulation, prototype instrumentation, and verified propulsion as distinct states. It records force, impulse, electrical energy, temperature, safety events, configuration, and provenance; provides a hardware-in-the-loop data interface; and fails closed when an independent reaction-force channel is absent from a strict momentum-closure test. The accompanying experimental protocol requires traceable calibration, synchronized raw channels, sham articles, orientation reversals, environmental monitoring, a complete uncertainty budget, preregistered decision thresholds, and independent reproduction. Aurora, a proposed long-duration city-ship architecture, is treated only as a requirements decomposition and systems-integration problem. Flux Drive is treated only as a propulsion hypothesis whose first admissible test is a low-energy force-balance experiment. No net thrust, reactionless propulsion, spacetime engineering, flight readiness, or human-rated capability is claimed. The contribution is a reproducible method for deciding whether a candidate effect should advance, be revised, or be stopped.

**Keywords:** propulsion measurement; momentum closure; uncertainty; falsification; reproducible software; spacecraft systems engineering

## 1. Introduction

A propulsion claim is credible only when the system boundary is explicit and the measured momentum transfer is consistent with the forces exchanged across that boundary. Conventional thrust follows momentum conservation: a vehicle accelerates expelled mass or exchanges momentum with an external field or medium. A force-like signal on a sensor is not, by itself, proof of vehicle-level thrust. Thermal drift, vibration rectification, cable forces, acoustic coupling, magnetic interaction, buoyancy, filtering, timing offsets, and calibration errors can all create or distort apparent signals.

Aurora/Flux was built to make those distinctions executable. The project has two related but separate scopes:

1. **Flux Drive** is an unverified actuator and propulsion research program. Its current artifact is a safe software kernel and a measurement protocol.
2. **Aurora** is a conceptual long-duration vessel and city-ship architecture. Its current artifact is a requirements-level decomposition, not a flight design.

The research question is deliberately narrow: can an auditable software and measurement workflow determine whether a candidate force survives ordinary explanations and closes momentum within declared uncertainty? The present paper does not answer whether a novel drive works, because no calibrated physical dataset establishing useful net thrust exists.

## 2. Evidence states and promotion gates

The architecture defines three non-interchangeable evidence states.

- **Simulation:** deterministic models and synthetic sensor channels. Results demonstrate software behavior only.
- **Prototype instrumentation:** measurements from physical devices with declared calibration and environmental context. Results may characterize a test article but do not automatically establish propulsion.
- **Verified propulsion:** a future state requiring a statistically and metrologically valid residual, closed momentum and energy accounting, controls, preregistered rules, and independent replication.

Promotion is denied if provenance is incomplete, required channels are missing, a safety event occurred, the uncertainty budget is incomplete, controls were not executed, or the reaction channel does not close. This implements a falsification-first rule: the system seeks the least extraordinary adequate explanation before advancing a claim.

## 3. Methods

### 3.1 Software architecture

The reference kernel is implemented in Python with standard-library tests. It provides:

- deterministic actuator-bench and controller models;
- command limiting, over-current and over-temperature trips, and emergency-stop behavior;
- telemetry for voltage, current, temperature, force, impulse, and electrical energy;
- CSV ingestion for hardware-in-the-loop measured channels;
- automatic input validation and machine-readable reports;
- a strict reaction-force momentum-closure mode;
- linear calibration and uncertainty propagation, including correlated inputs where declared;
- frozen configuration and reproducible replay; and
- automated tests on pushes and pull requests.

The default simulated relationship between command, current, and force is a reference plant, not a physical claim. Its purpose is to test control logic, units, sign conventions, accounting, and failure behavior before measurements are interpreted.

Strict audit mode requires both a primary force channel and an independent reaction channel. If the reaction channel is absent, the result is `not_assessed` or a failed strict audit; it cannot be reported as momentum closure. The software integrates each signed force channel over time to obtain the primary and reaction impulses, then defines the closure residual as their signed sum.

Acceptance requires the residual to be consistent with zero within the predeclared expanded uncertainty of both channels. A nonzero primary impulse accompanied by an equal-and-opposite reaction is ordinary momentum exchange, not reactionless propulsion.

### 3.2 Measurement protocol

The minimum physical test is a low-energy, mechanically constrained bench experiment with six isolated functions: test article, primary force transducer, independent reaction transducer or fixture, isolated electrical measurement, environmental monitoring, and an independently interruptible safety/data controller.

Before powered testing, each channel must have recorded range, resolution, sampling rate, filtering, units, sign convention, calibration status, and time alignment. Zero, span, polarity, hysteresis, repeatability, and command-off drift checks are required. The analysis version and configuration hash are frozen before the first unblinded powered run.

The run matrix includes:

1. command-off baselines;
2. sham-device controls;
3. lowest approved active condition;
4. forward, reversed, and perpendicular orientations;
5. cable and feedthrough perturbation controls;
6. thermal, vibration, acoustic, magnetic, pressure, and buoyancy monitoring; and
7. blinded repetition when a candidate residual is present.

The uncertainty budget includes calibration slope and offset, resolution, noise, drift, creep, hysteresis, temperature coefficient, integration timing, fixture compliance, cable forces, environmental coupling, and between-run repeatability. Correlated calibration terms must be represented as covariance terms rather than silently combined as independent errors. The treatment follows the general NIST principle that a measurement result is incomplete without a quantitative statement of its uncertainty.

A result advances only when it exceeds the complete preregistered uncertainty threshold, survives all controls, closes declared momentum and energy channels, and is reproduced by an independent operator. A single-axis sensor can screen a low-energy setup; any candidate anomalous force must advance to multi-axis force/torque validation.

### 3.3 Aurora city-ship boundary

Aurora is not presented as a build-ready spacecraft. It is a systems-engineering frame that makes the missing work visible. A credible long-duration inhabited vehicle requires quantitative budgets and verified interfaces for at least structure, mass properties, power generation and distribution, thermal rejection, environmental control and life support, radiation protection, guidance-navigation-control, communications, propulsion, maintenance, fault containment, logistics, human factors, and governance.

The propulsion hypothesis cannot substitute for those subsystems. Conversely, a coherent city-ship requirements model cannot validate the propulsion hypothesis. The architecture therefore keeps vessel requirements, simulated command/telemetry schemas, and propulsion evidence as separate objects connected by explicit interfaces.

This separation follows established systems-engineering practice: requirements, verification methods, interfaces, risks, and configuration states must be traceable across the life cycle. Aurora presently remains at the concept and requirements stage.

### 3.4 Falsification rules

The Flux hypothesis is stopped or revised under any of the following conditions:

- the apparent force follows temperature, vibration, acoustic pressure, magnetic field, cable configuration, or sensor orientation;
- the signal appears in a sham article;
- the sign or magnitude fails to transform as preregistered under orientation reversal;
- the reaction channel accounts for the measured impulse;
- the effect falls below the complete expanded uncertainty;
- the result depends on post-hoc filtering, time windows, exclusions, or uncorrected multiple testing;
- raw data, calibration records, configuration, or code revision cannot reproduce the report; or
- an independent apparatus does not replicate the residual.

An unexplained residual that survives one apparatus is not a discovery claim. It is a trigger for stronger controls, independent calibration, and replication.

## 4. Results

The public repository contains source code, schemas, example data, audit documents, and automated tests. The non-hardware submission check is:

```text
python tools/run_submission_demo.py
```

This command validates schemas, executes the local software tests, and reports the software-only evidence boundary. It does not activate RF, acoustic, high-voltage, high-current, vacuum, laser, cryogenic, stored-energy, or propulsion hardware.

On 11 September 2026, the submission command exited successfully. Twenty-five software tests passed and three Aurora schemas were validated. The reported state was `hardware_io=disabled` and `physical_propulsion_proven=false`. A deterministic evidence bundler preserved the command output, runtime, source-file hashes, and source-manifest hash. No random sampling was used in this software verification run.

GitHub-hosted execution did not produce a computational result. The job stopped before checkout or test execution because GitHub reported an account-level billing authorization lock. This is classified as an infrastructure failure and is not combined with the local result.

The observed result therefore supports only the claim that the tested local software package satisfied its declared software checks. It supplies no evidence of physical force, net thrust, or vehicle performance.

## 5. Discussion

The result demonstrates the practical value of explicit evidence states. The same run that verifies deterministic safety and audit behavior also emits a machine-readable denial of physical propulsion proof. This prevents a passing software suite from being promoted into a physical claim.

The strict reaction-channel rule is intentionally asymmetric: incomplete evidence cannot pass. A candidate primary-force signal without a synchronized independent reaction measurement remains unassessed rather than anomalous. Similarly, a residual that appears only after post-hoc filtering or incomplete environmental controls cannot advance.

For Aurora, the method prevents systems-level completeness from being inferred from a propulsion concept. Even a future validated actuator would leave mass, power, thermal, life-support, radiation, control, maintenance, and governance requirements unresolved. The city-ship architecture remains useful as a traceability framework while remaining unverified as a vehicle.

## 6. Limitations

The current project has no measurement-grade physical thrust dataset, no independently calibrated actuator result, no demonstrated external momentum channel for the proposed acoustic/electromagnetic concepts, and no independent replication. It has not established reactionless propulsion, faster-than-light travel, spacetime-curvature control, useful vehicle thrust, flight safety, or human-rated life support. Software correctness cannot certify an instrument or physical claim.

The current contribution is therefore methodological: an auditable boundary between idea, simulation, measurement, and verified engineering.

## 7. Conclusion

Aurora/Flux converts extraordinary-propulsion review from a narrative exercise into a set of executable gates. The architecture preserves negative results, rejects incomplete momentum accounting, and prevents a city-ship concept from being presented as demonstrated hardware. The appropriate next scientific decision is not whether Aurora will fly. It is whether an independent reviewer considers the low-energy, measurement-grade protocol sufficient to test a bounded actuator hypothesis. The admissible outcomes are: proceed to controlled experiment, revise the model or measurement design, or stop because the claim is not physically supported.

## Data and code availability

Source, tests, schemas, example data, and audit materials are available at <https://github.com/mommommy1960-lang/flux-drive-kernel>. The submission manuscript and supporting materials are frozen on branch `aurora-flux-formal-review` at revision `e6dd7434ce125b99e4bd962741c486411aacf9b0`. No archived repository DOI has been assigned.

## References

1. National Aeronautics and Space Administration. *NASA Systems Engineering Handbook*, NASA/SP-2016-6105 Rev. 2, 2016. <https://www.nasa.gov/reference/systems-engineering-handbook/>
2. B. N. Taylor and C. E. Kuyatt. *Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results*, NIST Technical Note 1297, 1994 edition. <https://www.nist.gov/pml/nist-technical-note-1297>
3. National Aeronautics and Space Administration, Glenn Research Center. *Beginner's Guide to Propulsion*. <https://www.grc.nasa.gov/www/k-12/airplane/bgp.html>
4. Joint Committee for Guides in Metrology. *Evaluation of measurement data—Guide to the expression of uncertainty in measurement*, JCGM 100:2008. <https://www.bipm.org/en/committees/jc/jcgm/publications>

## Statements and Declarations

**Funding:** The author declares that no funds, grants, or other support were received during the preparation of this manuscript.

**Competing interests:** The author has no relevant financial or non-financial interests to disclose.

**Author contributions:** Mya P. Brown performed the conceptualization, methodology, software development, validation, investigation, project administration, and writing. The author read and approved the final manuscript.

**Ethics and safety:** No human participants, animals, or operational propulsion hardware were used for this software manuscript. The repository prohibits direct connection to hazardous hardware without qualified engineering supervision, independent safety review, and a physical emergency disconnect.

**Use of artificial intelligence:** AI tools assisted with drafting and software development. Mya P. Brown reviewed the manuscript and accepts responsibility for its content and claims.
