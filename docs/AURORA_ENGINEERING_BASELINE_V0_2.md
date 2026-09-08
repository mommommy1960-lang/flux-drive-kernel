# Aurora Engineering Baseline v0.2

## Purpose and status

This document turns the Aurora concept into an auditable preliminary design
baseline. It closes documentation gaps with explicit assumptions, equations,
interfaces, and pass/fail criteria. A design reference value is not a measured
fact, and no entry in this document certifies flight or propulsion.

Aurora has two nested scopes:

1. **Aurora Lab Vessel:** a small, enclosed, sensor-and-actuator experiment
   platform described by the current Blue Book.
2. **Aurora City-Ship:** the larger human habitat concept. It remains a
   requirements-level architecture until its mass, power, life-support,
   structure, radiation, thermal, and propulsion designs are independently
   closed.

## Gap-closure matrix

| Area | Baseline added here | Acceptance evidence still required | Status |
|---|---|---|---|
| Propulsion | Momentum, force, power, and lift equations | Calibrated thrust measurement with reaction-channel accounting | UNPROVEN |
| Mass | Separate lab and city-ship mass ledgers | Itemized CAD/BOM mass and center-of-gravity survey | PARTIAL |
| Structure | Load cases and factors of safety to be filled by CAD analysis | FEA, coupon tests, and qualification article | OPEN |
| Power | Bus, peak, continuous, and reserve accounting | Battery/BMS characterization and thermal validation | PARTIAL |
| Thermal | Heat-generation and radiator sizing equations | Thermal-vacuum or equivalent controlled test | OPEN |
| Life support | Required closed-loop functions and reserves | Human-rated ECLSS design and test | OPEN |
| Radiation | Shielding dose-budget method | Particle transport model and exposure test/analysis | OPEN |
| GNC | State, estimator, controller, and abort interfaces | Hardware-in-loop and flight-like sensor validation | PARTIAL |
| Communications | Local, near-field, and deep-space interfaces separated | Link budget and qualified radios/antennas | OPEN |
| Safety | Consent, interlock, rail-cut, and human reset behavior | Independent safety review and fault-injection results | PARTIAL |

## Governing bookkeeping

For a vehicle of mass `m`, the required net force for acceleration `a` is:

`F_net = m * a`

For vertical lift near Earth, the actuator must provide at least:

`F_lift >= m * (g + a_vertical)`

where `g = 9.80665 m/s^2`. For an isolated system, the momentum balance must
close:

`Delta_p_vehicle + Delta_p_exhaust + Delta_p_radiation + Delta_p_environment = 0`

If no exhaust, radiation, field interaction, or environmental momentum channel
is measured, a claimed net thrust is not established. Power accounting must
also close:

`P_input = P_actuation + P_control + P_thermal + P_losses + P_export`

The software may calculate these quantities, but only calibrated instruments
and controlled experiments can establish them physically.

## Aurora Lab Vessel reference configuration

The Blue Book's 500 W bench supply is retained as the maximum prototype input
reference. The lab vessel is not a flight article and must remain enclosed and
interlocked.

Required measured channels:

- six-axis force/torque measurement with calibration certificate;
- input voltage, current, phase, and harmonic content;
- acoustic pressure and frequency spectrum;
- RF conducted power before and after attenuation;
- temperature at every power and actuator rail;
- vibration and seismic reference channels;
- environmental electromagnetic and acoustic background;
- synchronized timestamps and hash-chained raw data.

The first physical question is not whether the lab vessel flies. It is whether
the actuator produces a repeatable force residual that survives blind controls,
dummy loads, cable-motion controls, thermal drift correction, and independent
replication.

## City-Ship preliminary architecture

The city-ship design must be decomposed into separately closed modules:

- pressure vessels and structural trusses;
- habitation, agriculture, water, waste, and atmosphere loops;
- power generation, storage, distribution, and fault isolation;
- heat collection, transport, and rejection;
- radiation shielding and storm shelter;
- propulsion and propellant/reaction-mass system;
- avionics, navigation, guidance, control, and communications;
- maintenance, spares, docking, rescue, and emergency shelter;
- Aurora mission software with human command authority and independent safety
  supervision.

No city-ship mass, population, range, or acceleration claim may be published
until each module has an itemized mass and power budget with uncertainty.

## Propulsion decision gate

The Flux Drive is not promoted from experiment to propulsion until all gates
below pass:

1. The proposed force-producing mechanism is stated in a governing model with
   defined boundary conditions.
2. The model passes dimensional, energy, and momentum-conservation review or
   identifies a measurable interaction channel outside the vehicle.
3. A calibrated force balance measures a repeatable signal above the complete
   uncertainty budget.
4. Null tests and sham-actuator tests do not reproduce the signal.
5. Thermal, acoustic, electromagnetic, cable, vibration, and magnetic artifacts
   are independently bounded.
6. The result replicates under blinded operation and by an independent team.
7. Only after those gates pass may a flight propulsion sizing study begin.

Until then, the Flux Drive interface remains simulation-only and all physical
RF, acoustic, power, and propulsion hardware remains behind qualified review,
interlocks, and explicit human approval.

## Definition of done for v0.2 software

- Every command and telemetry message validates against its JSON schema.
- Every replay produces the same state and telemetry hash.
- Unsafe commands fail closed.
- Mass, power, thermal, and force ledgers reject missing or non-finite values.
- A test report distinguishes modeled values, measured values, and claims.
- No software result is labeled flight proof without physical evidence.

## Bottom line

This baseline makes the design package internally computable and testable. It
does not fill unknown physics with invented numbers. The next decisive result
must come from a measurement-grade force experiment; until that exists, Aurora
is a credible software and laboratory architecture, not a demonstrated flying
city-ship.
