# Low-energy measurement bench: buildable controls and measurements

This bench is for measuring ordinary forces and ruling out artifacts. It is
not a wall-phasing machine and it does not energize high-power RF, ultrasound,
high voltage, vacuum, or propulsion hardware.

## Bench architecture

    current-limited 5 V supply
            |
            +-- controller/data logger
            +-- INA219 voltage/current monitor
            +-- low-voltage test article

    test article -> rigid reaction frame -> load cell -> HX711 ADC -> logger
                                 |
                     camera + temperature + IMU + timebase

## Components to source

### Required

- ESP32-S3 or similar low-voltage controller/data logger
- 5 V current-limited USB supply or laboratory supply with a hard current
  limit; no mains wiring on the prototype bench
- 5–10 kg strain-gauge load cell with a calibration certificate
- HX711 24-bit load-cell amplifier board; SparkFun's hookup guide
  documents the load-cell wiring and calibration workflow:
  https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-guide/all
- Adafruit INA219 high-side voltage/current monitor:
  https://www.adafruit.com/product/904
  The documented board is rated up to 26 V and ±3.2 A, with stated precision
  limits.
- Rigid aluminum or plywood reaction frame, fasteners, cable strain relief,
  and a mechanical emergency disconnect
- Calibrated masses or weights for load-cell calibration
- Smartphone or USB camera mounted on a fixed tripod
- DS18B20 or equivalent temperature sensor
- Clear acrylic enclosure and a declared slot/opening for ordinary passage
- Laptop with Python and a USB cable for raw CSV logging

### Optional, still low energy

- Six-axis IMU for vibration and acceleration logging
- Optical interrupter or time-of-flight sensor for timing
- Second camera viewing the opposite side of the enclosure
- Separate microphone and magnetometer for artifact checks

## Controls

Run these in randomized order, with a new run ID for every trial:

1. Empty frame, no test article.
2. Test article present, powered off.
3. Powered article mechanically fixed to the frame.
4. Powered article free but unable to contact the load cell.
5. Powered article with declared ordinary opening.
6. Sham electrical load with the same current and heat profile.
7. Cable-routing and vibration control.
8. Proposed experimental condition, only after the controls are stable.

The first four controls identify frame drift, electrical heating, vibration,
magnetic coupling, cable forces, and sensor offsets before any effect is
considered.

## Calibration and acceptance rules

1. Zero the load cell with the frame empty.
2. Apply at least three known masses spanning the intended measurement range.
3. Fit the calibration line and retain the residuals.
4. Repeat zero and span checks before and after each session.
5. Synchronize every sensor to the same run ID and monotonic timestamp.
6. Report force, voltage, current, power, temperature, vibration, and raw
   sensor data—not only a processed headline number.
7. Do not call a result validated unless the prediction agrees within the
   declared uncertainty, three randomized trials repeat, and an independent
   replication succeeds.

## What this bench can establish

- ordinary actuator force and power;
- mechanical coupling, vibration, thermal drift, and magnetic artifacts;
- movement through a known opening;
- whether the software telemetry and controls are auditable.

## What it cannot establish by itself

- intact-wall matter phasing;
- reactionless propulsion;
- spacecraft propulsion;
- a warp drive or stable traversable black hole.

Any future high-energy stage requires qualified engineering review, a written
hazard analysis, physical interlocks, and explicit human authorization.
