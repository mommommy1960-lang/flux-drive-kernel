# Flux Drive Factual Evidence Dossier

Status: evidence-gathering and test-design layer  
Updated: 2026-09-08

## Scope

This dossier separates four things that must not be mixed:

1. established physical laws and measurement practice;
2. published claims of anomalous thrust;
3. measured data from the Commons Flux Drive bench;
4. conclusions that survive independent replication.

The project does not treat a force-sensor trace by itself as proof of
reactionless propulsion. A propulsion claim requires an independently calibrated
force measurement, a complete power record, environmental controls, and a
reaction/momentum accounting channel.

## Established measurement facts

- Force transducers are calibrated by applying known compression or tension
  forces and relating the applied force to the transducer output.
- A calibration is only valid for the transducer/readout system and operating
  conditions covered by the calibration.
- Force uncertainty must include the mass standard, local gravitational
  acceleration, air density, readout, drift, hysteresis, creep, and temperature
  effects.
- Ordinary photon radiation pressure is a known comparison floor. For an
  onboard photon emitter, the ideal force-to-power ratio is `1/c`, about
  3.3 nN/W.

Primary references:

- [NIST Calibration of Force Transducers](https://www.nist.gov/programs-projects/calibration-force-transducers)
- [NIST Equipment, Procedures and Uncertainties](https://www.nist.gov/system/files/documents/calibrations/97ncs4b.pdf)
- [NIST Uncertainty in Force Measurements](https://nvlpubs.nist.gov/nistpubs/jres/110/6/j110-6bar.pdf)

## Published anomalous-thrust record

The record is mixed rather than settled:

- NASA Eagleworks reported a closed RF cavity measurement campaign with a
  nonzero thrust signal and included null-thrust tests.
- A later high-accuracy TU Dresden study used a counterbalanced double
  pendulum, battery power, broad frequency coverage, and improved isolation.
  It reported no thrust within the tested range and limited any anomaly below
  the classical photon-radiation force for the supplied power.
- That later study documents ordinary mechanisms capable of imitating thrust,
  including thermal drift, magnetic interactions, cable/feedthrough forces,
  buoyancy, outgassing, and center-of-mass shifts.

References:

- [NASA NTRS: Measurement of Impulsive Thrust from a Closed Radio-Frequency Cavity in Vacuum](https://ntrs.nasa.gov/api/citations/20170000277/downloads/20170000277.pdf)
- [Tajmar, Neunzig and Weikert: High-accuracy thrust measurements of the EMDrive and elimination of false-positive effects](https://link.springer.com/article/10.1007/s12567-021-00385-1)

## What the Flux Drive test must record

Every run should produce synchronized raw channels with units and calibration
metadata:

```text
timestamp_s
command
measured_voltage_V
measured_current_A
measured_temperature_C
measured_force_N
reaction_force_N              # required for momentum closure
vibration_x_m_s2
vibration_y_m_s2
vibration_z_m_s2
magnetic_field_uT
acoustic_pressure_Pa
ambient_pressure_Pa
orientation_deg
run_id
operator_id
calibration_id
```

The current kernel audits the first six channels. The reaction-force and
environmental channels are the next required extension before a propulsion
verdict can be issued.

## Automatic decision gates

1. **Data integrity:** monotonic timestamps, complete rows, finite values,
   units, calibration identifiers, and no missing samples.
2. **Safety:** no over-current, over-temperature, emergency-stop, insulation,
   or telemetry-loss event.
3. **Repeatability:** pre-registered repeated runs agree within a declared
   uncertainty budget.
4. **Null controls:** command-off, dummy-load, reversed orientation,
   perpendicular orientation, and sham-device runs are included.
5. **Artifact rejection:** thermal, magnetic, cable, acoustic, vibration,
   buoyancy, outgassing, and center-of-mass explanations are measured or
   bounded.
6. **Momentum closure:** the measured impulse is reconciled with the reaction
   channel and every known exchanged field or mass flow.
7. **Independent replication:** a second operator reproduces the result from
   frozen code, hardware configuration, and preregistered analysis.

Until gate 6 closes, the result is an observed force signal—not verified
reactionless propulsion.

## Current project status

- Software-in-the-loop: implemented and tested.
- CSV hardware-in-the-loop audit: implemented and tested.
- Measured voltage is included in electrical-energy accounting.
- Safety trips are fail-closed and latched.
- Public factual source register: this dossier.
- Physical hardware data: not yet supplied.
- Momentum closure: not assessed.
- Verified propulsion: not established.
