# Low-Energy Flux Drive Measurement Bench

This list is for the first physically buildable prototype: an instrumented,
low-energy test fixture. It is not a materials list for a reactionless engine,
black-hole generator, high-power RF system, vacuum system, laser, cryogenic
system, or propulsion vehicle.

## Required before assembly

Every measurement device must have a usable calibration record, range, stated
uncertainty, serial/asset identifier, and sampling specification. An uncalibrated
device can be used for debugging but cannot establish a propulsion result.

### Mechanical fixture

- rigid nonmagnetic base or optical breadboard;
- fixed frame with a defined measurement axis;
- calibrated force transducer/load cell and compatible readout;
- independent reaction-force transducer or reaction fixture;
- adjustable nonbinding mounts;
- reference masses for zero/span and polarity checks;
- low-friction cable-management supports that do not transmit force into the
  measurement axis;
- fasteners, spacers, insulating standoffs, and a removable test-article mount.

### Electrical and thermal instrumentation

- current-limited, isolated low-voltage bench supply;
- independent voltage measurement at the test-article terminals;
- independent current measurement at the same terminals;
- temperature sensors on the test article, mount, cable entry, and nearby frame;
- a separate thermal/current cutoff circuit;
- fuse or resettable over-current protection sized by a qualified person;
- physical latching emergency disconnect;
- dummy electrical load matched to the test article's expected load.

### Environmental instrumentation

- three-axis accelerometer on the fixture;
- three-axis magnetometer away from ferromagnetic hardware;
- acoustic pressure microphone or calibrated acoustic sensor;
- ambient temperature and pressure sensor;
- orientation/tilt reference;
- optional optical displacement or laser distance sensor for independent motion
  confirmation at safe, low-power levels.

### Data acquisition and records

- synchronized multichannel DAQ or synchronized instrument interfaces;
- timestamp source with documented accuracy;
- shielded, strain-relieved signal cables;
- computer capable of writing raw CSV without overwriting;
- immutable run identifier and configuration hash;
- printed or digital calibration certificates;
- test log, operator log, and emergency-stop log.

## Required control articles

The build is incomplete without controls:

1. **Command-off baseline:** all sensors running with zero actuation.
2. **Sham load:** same mass, wiring, thermal load, and mounting, without the
   proposed active mechanism.
3. **Reversed orientation:** active article rotated 180 degrees about the test
   axis.
4. **Perpendicular orientation:** active article rotated 90 degrees to test
   axis coupling.
5. **Cable/feedthrough control:** cable routing and restraints documented and
   repeated.

## Assembly sequence

1. Install the base, fixed frame, transducers, and physical disconnect.
2. Verify that no cable, hose, shield, or fastener bypasses the force channel.
3. Mount the dummy load and complete zero, span, polarity, drift, and repeat
   checks.
4. Add environmental sensors and verify timestamp alignment.
5. Run the command-off baseline and all sham controls.
6. Freeze the wiring diagram, sensor metadata, software commit, and run
   configuration.
7. Operate only at the lowest approved low-energy condition under qualified
   supervision.
8. Export raw data and run:

```bash
python -m flux_drive_kernel \
  --hil-csv data/run001.csv \
  --require-momentum \
  --require-environment
```

## Do not purchase or build yet

Do not escalate to high voltage/current, high-power RF, vacuum, laser,
cryogenic, high-field, explosive, or compact-object concepts based only on a
software PASS. Those require a qualified laboratory, hazard analysis,
independent review, and a separately validated physical design.

## Build-complete definition

The low-energy bench is build-complete when all listed channels are installed,
calibrated, timestamped, independently disconnected from actuation, and able to
produce a strict report with complete channels and a declared uncertainty
budget. That condition makes the physical experiment ready to run; it does not
pre-decide the result.
