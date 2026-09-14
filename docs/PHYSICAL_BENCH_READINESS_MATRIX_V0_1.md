# Physical Bench Readiness Matrix v0.1

**Program:** Commons Flux Drive / Aurora  
**Date:** 2026-09-14  
**Status:** pre-build engineering gate

## Purpose

Translate the existing falsification framework into a concrete readiness checklist for a low-energy, measurement-grade physical bench. This document does not authorize high-energy hardware and does not assume that a propulsion effect exists.

## Readiness dimensions

| Area | Required state before decisive run | Current state | Gate |
|---|---|---|---|
| Force channel | calibrated, serial-tracked, uncertainty documented | specified, not yet physically commissioned | BLOCKED |
| Reaction-force channel | independently calibrated and synchronized | specified, not yet physically commissioned | BLOCKED |
| Electrical measurement | terminal voltage/current independently measured | specified | BLOCKED |
| Thermal channels | article, mount, cable entry, ambient monitored | specified | BLOCKED |
| Vibration / tilt | synchronized 3-axis motion/tilt monitoring | specified | BLOCKED |
| Magnetic environment | synchronized field monitoring | specified | BLOCKED |
| Acoustic / pressure | declared environment monitored | specified | BLOCKED |
| Timestamping | documented common timebase / alignment error | architecture defined | BLOCKED |
| E-stop | physical latching disconnect independent of software | required by governance | BLOCKED |
| Sham article | mechanically/electrically matched control | required, not built | BLOCKED |
| Orientation controls | 0°, 90°, 180° reproducible mounting | required, not commissioned | BLOCKED |
| Analysis freeze | code commit + preregistered exclusions before decisive run | process defined | READY IN SOFTWARE |
| Raw-data preservation | immutable run IDs and non-overwrite storage | software path defined | READY IN SOFTWARE |
| Uncertainty budget | channel-by-channel standard and expanded uncertainty | framework defined, values pending instruments | BLOCKED |
| Independent operator | person/lab not dependent on original analysis | not yet assigned | BLOCKED |

## Build-ready definition

The bench may be called **build-ready** when:

1. every required channel has a selected low-energy instrument class;
2. calibration method and acceptance tolerance are written before assembly;
3. cable routing and mechanical load paths are diagrammed;
4. the physical emergency disconnect is defined;
5. sham and orientation fixtures are included in the mechanical design;
6. the DAQ schema maps one-to-one to the repository HIL fields;
7. the run protocol and analysis plan are frozen enough to prevent post-hoc threshold shopping.

## Experiment-ready definition

The bench may be called **experiment-ready** only after:

- installed instrumentation passes zero/span/polarity/repeatability checks;
- independent reaction sensing is live;
- environmental channels are synchronized;
- sham and orientation controls complete without unexplained coupling;
- data export validates through the repository's strict HIL parser;
- the emergency disconnect is physically tested;
- the decisive-run configuration hash is frozen.

## Promotion rule

No status in this matrix can promote `physical_propulsion_proven` above `false`. That field changes only after a reproducible physical residual survives the full acceptance gate and independent replication.
