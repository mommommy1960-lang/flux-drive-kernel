# CAL-00 Reference-Data Replay and Low-Energy Bench Plan

## Purpose

Use published propulsion-test methods and openly documented measurement values to test the Flux Drive analysis pipeline before any physical claim is made.

This package distinguishes:

1. **reference data**: measurements from established propulsion or test-facility work;
2. **synthetic fixtures**: generated data used only to test software behavior;
3. **Flux observations**: data that would come from a future physical test article.

No reference or synthetic dataset is evidence that Flux Drive produces thrust.

## Reference cases

### Case R1 — conventional electric propulsion

Use a documented electric-propulsion thrust-stand case as a positive control. The 2025 Robinson Research Institute facility paper reports a pendulum stand designed for forces up to 200 mN, with approximately 1 mN precision and ±2.3 mN full-scale accuracy during initial testing. This is a facility-characterization reference, not a Flux result.

Expected software behavior:
- a known conventional thrust signal is detected;
- force/impulse and electrical channels remain dimensionally consistent;
- uncertainty is reported rather than hidden;
- the reaction/environment accounting remains explicit.

### Case R2 — null/control propulsion

Use a zero-thrust or sham dataset with the same timing, thermal profile, and electrical load as the proposed condition.

Expected software behavior:
- no propulsion claim;
- any apparent force below the declared uncertainty remains unresolved;
- drift, vibration, cable force, and thermal correlations are reported.

### Case R3 — anomalous-claim artifact replay

Use a clearly labeled synthetic replay of artifact signatures discussed in the disputed EM Drive literature: thermal gradients, cable/electromagnetic coupling, and suspension geometry effects.

Expected software behavior:
- apparent force may appear in the raw channel;
- controls and reversal tests identify the artifact;
- the result fails the verified-propulsion gate.

## Minimum replay schema

Every row must contain:

- `run_id`
- `timestamp_s`
- `condition`
- `command`
- `measured_voltage_V`
- `measured_current_A`
- `measured_temperature_C`
- `measured_force_N`
- `reaction_force_N` when available
- `vibration_rms`
- `magnetic_field`
- `cable_configuration`
- `calibration_id`
- `source_class`: `reference`, `synthetic_fixture`, or `flux_observation`

## Analysis sequence

1. Validate units, timestamps, missing channels, and run identity.
2. Reconstruct force and reaction impulse using the same integration rule.
3. Calculate electrical energy and absolute throughput separately.
4. Apply calibration and uncertainty propagation.
5. Compare forward, reverse, sham, powered-off, and cable-routing conditions.
6. Test thermal, vibration, magnetic, and suspension-correlated covariates.
7. Check momentum closure:
   [
   J_mathrm{device}+J_mathrm{reaction}+J_mathrm{environment}=0
   ]
   within the declared combined uncertainty.
8. Preserve raw data, processing configuration, and failed gates.
9. Assign one status only: `simulation`, `reference_replay`, `artifact_detected`, `inconclusive`, or `verified_conventional_propulsion`.

## CAL-00 low-energy bench

The existing low-energy bench document defines a safe first stage:

- current-limited 5 V supply;
- ESP32-S3 or equivalent logger;
- 5–10 kg calibrated load cell and HX711 ADC;
- INA219 voltage/current monitor;
- rigid reaction frame;
- camera, temperature sensor, optional IMU, and common timebase;
- raw CSV logging;
- randomized empty-frame, powered-off, fixed, sham-load, cable-routing, and proposed-condition controls.

The bench can establish ordinary actuator force, power, thermal drift, vibration, magnetic coupling, cable forces, and telemetry integrity. It cannot establish reactionless propulsion by itself.

## Acceptance gate

A Flux observation cannot advance to physical-propulsion evidence unless:

- calibration residuals are retained;
- three randomized trials repeat within the declared uncertainty;
- forward/reverse and sham controls behave as expected;
- environmental channels are recorded;
- momentum closure survives the uncertainty budget;
- an independent reviewer can reproduce the analysis;
- no ordinary artifact explains the signal.

## Dataset policy

Do not copy third-party data into the repository unless its license permits redistribution. Store source citation, DOI/URL, extracted variables, and transformation code. If redistribution is not permitted, use a small synthetic fixture that reproduces the published measurement structure and label it synthetic.

## Current conclusion

The reference replay can make the software pipeline testable and can demonstrate that the controls catch known false positives. It cannot establish that the Flux Drive flies. That requires new, calibrated, independently reviewed physical measurements.
