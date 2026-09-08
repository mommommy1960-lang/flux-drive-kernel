# Flux Drive: Real-World Test Plan, Phase 0

## Purpose

Phase 0 establishes whether a controllable bench channel produces a repeatable
measured force signal with closed energy and safety accounting. It does not test
warp travel or reactionless propulsion.

## Test sequence

1. **Software-in-the-loop:** run the deterministic model and verify command
   limits, telemetry, energy accounting, and latching trips.
2. **Hardware-in-the-loop:** feed timestamped voltage, current, temperature,
   and independently calibrated force measurements into the kernel without
   enabling external actuation.
3. **Instrumented bench:** use a qualified lab, independent emergency stop,
   shielded low-energy actuator hardware, calibrated load cell, isolated power
   measurement, and thermal monitoring.
4. **Momentum/energy audit:** compare measured impulse against the declared
   interaction channel. Any apparent force must be tested against vibration,
   cable forces, magnetic coupling, thermal drift, acoustic coupling, and air
   currents.
5. **Independent replication:** freeze the code and test configuration before
   another operator repeats the measurement.

## Pass criteria

- no safety trip bypasses are possible through the software interface;
- force and current channels are timestamped and independently calibrated;
- repeated runs agree within a predeclared tolerance;
- all known environmental coupling checks are recorded;
- no propulsion claim is made unless momentum and energy accounting closes.

## Stop conditions

Stop immediately on over-current, over-temperature, emergency-stop input,
unexpected force with zero command, sensor disagreement, insulation fault,
loss of telemetry, or unexplained energy imbalance. Do not increase voltage,
current, vacuum, laser power, magnetic field, or stored energy to chase a
surprising result.

