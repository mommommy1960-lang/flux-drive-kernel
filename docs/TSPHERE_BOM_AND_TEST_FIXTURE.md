# T-Sphere v0.1: Low-Voltage Prototype BOM

This is a small indoor robotics demonstrator. It is not a propulsion device,
an access device, or a wall-penetration device.

## Core parts

- ESP32-S3 development board with Wi-Fi/BLE
- Two 6 V micro gearmotors with encoders
- Dual low-voltage motor driver with current limiting
- Two micro servos or one geared shell actuator with a cam ring
- 6-8 laser-cut, 3D-printed, or thin polymer shell petals
- Flexible tendon or link rods and mechanical end-stops
- 6 V NiMH pack or current-limited laboratory supply for first tests
- Inline fuse, latching disconnect, and protected power switch
- 6-axis IMU, wheel encoder inputs, and temperature sensor
- Short-range time-of-flight distance sensor
- Optional low-power camera module
- Optional, separately reviewed radar/ultrasonic sensor for barrier sensing
- Soft bumper, acrylic maze panels, foam barrier, and a removable 60 mm slot
- Laptop or phone dashboard for commands and raw CSV telemetry

## First assembly order

1. Build and hand-test the shell mechanism without power.
2. Add end-stops and confirm the shell cannot pinch the wiring.
3. Test each motor from a current-limited supply with the wheels off the table.
4. Add the emergency disconnect and verify it removes motor power directly.
5. Add the controller and sensors; run the software demo before enabling motion.
6. Run the sphere in an open acrylic enclosure at low speed.
7. Add the controlled slot only after 20 open-floor runs pass.
8. Add the barrier-side telemetry receiver and compare logs from both sides.

## Measurement record

Each run must retain: run ID, operator, shell radius target and measured value,
battery voltage, motor current, temperature, IMU data, encoder counts, command
sequence, barrier side, emergency-stop state, and pass/fail reason.

## Stop conditions

Stop immediately for a jam, exposed moving linkage, rising temperature, battery
damage, loss of telemetry, unexpected movement, or any person/animal entering
the test area. The controller must remain in SAFE until a human performs an
explicit reset.

## Phase-effect demonstration

The honest demonstration uses a transparent fixture and a known opening. One
camera records the sphere leaving side A; a second camera records the sphere
entering side B; the telemetry stream records the handoff. If through-wall
sensing is added, its result is labeled sensing—not passage.
