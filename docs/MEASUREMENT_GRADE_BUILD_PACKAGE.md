# Flux Drive Measurement-Grade Build Package

## What this package delivers

This is the build and measurement specification for a low-energy, externally
actuated bench demonstrator. It is not a propulsion certification and it does
not authorize high-voltage, high-current, vacuum, laser, cryogenic, RF-power,
or stored-energy construction.

The purpose is to produce data good enough to answer one question:

> Is the measured force larger than the complete calibrated uncertainty budget
> and consistent with an independently measured reaction/momentum balance?

## Bench architecture

Use six isolated functions:

1. **Test article:** mechanically constrained, removable, and incapable of
   uncontrolled motion.
2. **Force channel:** calibrated load cell or force transducer on the defined
   measurement axis.
3. **Reaction channel:** an independent transducer or reaction fixture that
   records the equal-and-opposite interaction with the environment.
4. **Electrical channel:** isolated voltage and current measurement at the
   test-article input terminals.
5. **Environment channel:** temperature, three-axis vibration, magnetic field,
   acoustic pressure, ambient pressure, and orientation.
6. **Safety/data controller:** physical disconnect, latching emergency stop,
   independent thermal/current cutoff, synchronized timestamping, and a
   write-once raw-data record.

No software command may defeat the physical disconnect or the independent
cutoffs.

## Measurement accuracy gates

Before a powered run:

- record the calibration certificate and expiration/status for every channel;
- record sensor range, resolution, sample rate, filter, axis, units, and sign;
- perform zero, span, polarity, hysteresis, and repeatability checks;
- collect a command-off baseline long enough to characterize drift;
- verify timestamp alignment across every instrument;
- freeze the analysis version and configuration hash.

The uncertainty budget must include, at minimum:

- calibration slope and offset;
- raw readout noise and resolution;
- drift, creep, hysteresis, and temperature coefficient;
- timing uncertainty for impulse integration;
- fixture compliance and cable/feedthrough forces;
- vibration, magnetic, acoustic, pressure, and buoyancy coupling;
- repeatability across runs.

The repository's `metrology.py` module performs linear calibration propagation
and root-sum-square momentum-closure uncertainty with an explicit coverage
factor. It assumes independent inputs; correlated calibration terms must not be
silently treated as independent.

## Run sequence

1. Assemble the unpowered fixture and verify the emergency disconnect.
2. Run command-off baseline and sham-device controls.
3. Apply only the lowest approved test condition under qualified supervision.
4. Record synchronized raw data; do not rely on displayed averages.
5. Repeat forward, reversed, and perpendicular orientations.
6. Repeat with the active element replaced by a mass/thermal/electrical sham.
7. Stop on any safety trip, unexplained force, sensor disagreement, telemetry
   loss, insulation fault, or unexplained energy imbalance.
8. Run strict audit mode and retain raw data, report, configuration, and
   calibration records together.

## Acceptance criteria

A run is measurement-valid only when:

- all required channels are present and finite;
- all calibration metadata is present and current;
- no safety or telemetry fault occurred;
- controls and orientations are complete;
- the effect exceeds the predeclared expanded uncertainty;
- the reaction/momentum residual is consistent with zero within its expanded
  uncertainty;
- an independent operator can reproduce the result from frozen materials.

The current software can enforce data presence, numerical validity, safety
trips, impulse accounting, and strict reaction-channel closure. It cannot
certify a physical sensor or calibration certificate that has not been
independently verified.
