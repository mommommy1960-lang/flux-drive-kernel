# Flux Drive Measurement-Grade Build Package

## What this package delivers

This is the build and measurement specification for a low-energy, externally
actuated bench demonstrator. It is not a propulsion certification and it does
not authorize high-voltage, high-current, vacuum, laser, cryogenic, RF-power,
or stored-energy construction.

The purpose is to produce data good enough to answer one question:

> Is the measured force larger than the complete calibrated uncertainty budget
> and consistent with an independently measured reaction/momentum balance?

## Declared experimental boundary

Before any powered run, the operator must define the system boundary in writing.
At minimum the momentum ledger must state whether each of the following lies
inside or outside that boundary and how it is measured or bounded:

- test article and moving internal masses;
- force fixture, balance, supports, table, and building/Earth reaction path;
- electrical cables, feedthroughs, connectors, coolant lines, and data lines;
- expelled gas, outgassing, leaks, fans, pumps, or other mass flow;
- acoustic coupling to air and structure;
- electromagnetic radiation and conducted RF;
- magnetic interaction with the laboratory and Earth's field;
- electrostatic interaction and ground paths;
- ambient atmosphere, buoyancy, pressure, and convection;
- vibration, seismic motion, tilt, and center-of-mass shifts.

An unexplained residual is not classified as propulsion merely because a known
channel was not instrumented.

## Bench architecture

Use six isolated functions:

1. **Test article:** mechanically constrained, removable, and incapable of
   uncontrolled motion.
2. **Force channel:** calibrated force measurement on the declared axis or axes.
3. **Reaction channel:** an independent transducer or reaction fixture that
   records the interaction with the environment.
4. **Electrical channel:** isolated voltage and current measurement at the
   test-article input terminals.
5. **Environment channel:** temperature, three-axis vibration, magnetic field,
   acoustic pressure, ambient pressure, and orientation.
6. **Safety/data controller:** physical disconnect, latching emergency stop,
   independent thermal/current cutoff, synchronized timestamping, and a
   write-once raw-data record.

No software command may defeat the physical disconnect or independent cutoffs.

## Force-instrument stages

The earlier documents used both a single-axis force transducer and a six-axis
force/torque system. They are now assigned to different stages rather than
presented as competing requirements.

### Stage A — screening

A traceably calibrated single-axis force transducer may be used only for a
low-energy screening experiment when:

- the hypothesized force direction is declared in advance;
- cross-axis forces and torques are mechanically bounded or independently
  monitored;
- the fixture cannot convert a large off-axis load into an apparent on-axis
  signal within the claimed effect size; and
- no propulsion claim is made from Stage A alone.

### Stage B — validation

A six-axis force/torque balance is required before a claimed anomalous force is
promoted to propulsion evidence. Stage B must resolve axial force, transverse
forces, and torques sufficiently to test whether fixture coupling, cable force,
center-of-mass motion, or tilt can reproduce the signal.

## Measurement accuracy gates

Before a powered run:

- record the calibration certificate and expiration/status for every channel;
- record sensor range, resolution, sample rate, filter, axis, units, and sign;
- perform zero, span, polarity, hysteresis, and repeatability checks;
- collect a command-off baseline long enough to characterize drift;
- verify timestamp alignment across every instrument;
- freeze the analysis version and configuration hash;
- preregister the acceptance threshold and planned exclusions.

The uncertainty budget must include, at minimum:

- calibration slope and offset;
- raw readout noise and resolution;
- drift, creep, hysteresis, and temperature coefficient;
- timing uncertainty for impulse integration;
- fixture compliance and cable/feedthrough forces;
- vibration, magnetic, acoustic, pressure, convection, and buoyancy coupling;
- repeatability across runs;
- covariance terms when calibration or environmental inputs are correlated.

The repository's `metrology.py` module now performs first-order covariance-aware
linear calibration propagation and covariance-aware momentum-closure
uncertainty with an explicit coverage factor. Zero covariance is appropriate
only when independence is justified.

A coverage factor must be reported with the expanded uncertainty. `k = 2` is a
common convention and is approximately a 95% interval only under suitable
statistical conditions; the report must not silently equate every `k = 2`
interval with an exact 95% confidence interval.

## Run sequence

1. Assemble the unpowered fixture and verify the emergency disconnect.
2. Run command-off baseline and sham-device controls.
3. Apply only the lowest approved test condition under qualified supervision.
4. Record synchronized raw data; do not rely on displayed averages.
5. Repeat forward, reversed, and perpendicular orientations.
6. Repeat with the active element replaced by a mass/thermal/electrical sham.
7. Repeat cable-routing and feedthrough controls without changing the test article.
8. Stop on any safety trip, unexplained force, sensor disagreement, telemetry
   loss, insulation fault, or unexplained energy imbalance.
9. Run strict audit mode and retain raw data, report, configuration, calibration
   records, analysis commit, and preregistration together.

## Acceptance criteria

A run is measurement-valid only when:

- all required channels are present and finite;
- all calibration metadata is present and current;
- no safety or telemetry fault occurred;
- controls and orientations are complete;
- the effect exceeds the predeclared expanded uncertainty;
- the reaction/momentum residual is consistent with zero within its expanded
  uncertainty after all declared external channels are accounted for;
- changing cable routing, orientation, or sham conditions does not reproduce the
  claimed signal; and
- an independent operator can reproduce the result from frozen materials.

A measurement-valid anomaly is still not a new propulsion law. It becomes a
candidate effect requiring mechanism analysis and independent replication.

The current software can enforce data presence, numerical validity, safety
trips, impulse accounting, calibration propagation, and strict reaction-channel
closure. It cannot certify a physical sensor, calibration certificate, fixture,
or environmental bound that has not been independently verified.
