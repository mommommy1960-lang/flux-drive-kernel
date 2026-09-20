# T-Sphere Phase-Effect Demonstrator: Real-World Build Plan v0.1

## Design decision

The earlier files contain a **Synchronizer Sphere**, resonator timing,
metamaterial interfaces, acoustic/EM telemetry, and a simulated bubble-wall
testbed. They do not contain a validated wall-phasing mechanism. We therefore
reuse the proven software and measurement discipline while defining a new,
conventional robotics prototype.

The first article is a **morphing inspection sphere**. Its “phase effect” is
tested as a transparent, instrumented sequence:

1. Unit A operates on barrier side A.
2. It contracts to pass through a known slot, seam, vent, or pipe opening.
3. A barrier-side sensor records its position and telemetry.
4. Unit A emerges on side B and expands again.
5. A second unit may perform a wireless handoff to make the transition look
   continuous in the operator display.

No intact wall is drilled, cut, or penetrated by the device. A later research
track can test through-wall sensing, but that is not physical passage.

## Reusable material from the existing work

- **Aurora Blue Book:** IMU, temperature, Hall, microphone, current/voltage,
  compute, watchdog, rail-cut, telemetry, and interlock architecture.
- **Flux Drive measurement package:** synchronized timestamps, calibration
  records, raw-data retention, sham/control runs, orientation reversals, and
  uncertainty accounting.
- **Quantum Flux Drive manual:** the synchronizer-sphere concept, resonator
  timing, metamaterial as a research material, and a simulated bubble-wall
  hardware-in-the-loop idea.
- **Maya Node:** consent tokens, audit trail, human approval, and fail-closed
  command handling.

## Physical architecture

### Mobility core

- Two low-voltage geared micro-motors with independent encoders.
- A central battery holder and protected motor driver.
- A removable internal chassis so the outer shell can change shape without
  exposing moving parts.

### Morphing shell

- Six to eight overlapping lightweight shell petals.
- A tendon, cam, or miniature linear-actuator ring that changes the sphere
  diameter from approximately 90 mm to 60 mm.
- Mechanical end-stops; the controller never relies on software alone to stop
  a pinch or over-travel condition.
- Soft outer bumper and a visible service disconnect.

### Sensing and control

- IMU and wheel encoders for pose and slip detection.
- Temperature and battery-voltage monitoring.
- Short-range time-of-flight sensor for the maze and slot.
- Optional camera and approved radar/ultrasonic module for non-destructive
  barrier sensing.
- ESP32-class controller for the low-voltage prototype, with a separate
  laptop/phone dashboard for logs and commands.

### Telemetry

Every command and sample records: sequence, timestamp, mode, shell radius,
battery voltage, temperature, emergency-stop state, barrier side, sensor
status, and operator authorization. Raw logs are retained; displayed values do
not replace raw measurements.

## Test fixture

Build a clear acrylic maze with interchangeable panels:

- 90 mm open corridor;
- 60 mm controlled slot;
- fabric curtain and foam barrier;
- opaque panel with a separately instrumented sensor on the far side;
- removable wall panel with a clearly labeled pre-existing passage.

The fixture must be openable so every run can be visually audited. Do not use
concealed doors, unmarked openings, or edits that could make a result appear
to be matter phasing.

## Pass/fail tests

1. **Morph repeatability:** 100 open/close cycles with no jam or shell damage.
2. **Maze traversal:** 20 successful runs through the controlled slot.
3. **Telemetry integrity:** every command has a monotonic sequence and a
   matching raw-data record.
4. **Fail-closed behavior:** invalid radius, over-temperature, low battery,
   lost telemetry, or emergency-stop command prevents motion.
5. **Barrier handoff:** the operator display identifies side A/side B without
   claiming the shell crossed an intact barrier.
6. **Sensing track:** if a radar/ultrasonic module is added, compare its output
   against known targets and report false positives and false negatives.

## What would count as a genuine breakthrough

A claim of intact-wall passage would require independent observers, a sealed
and continuously monitored test volume, synchronized optical/radio/acoustic/
magnetic tracking, mass and energy accounting, and repeatable results with
controls that rule out openings, relays, reflections, and hidden transport.
The present project is not allowed to label the conventional demonstrator as
that result.
