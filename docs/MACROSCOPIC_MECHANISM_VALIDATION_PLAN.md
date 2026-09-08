# Macroscopic mechanism validation plan

## Mechanism that can be validated now

The first mechanism is conventional reaction-mass propulsion. A control
volume around the actuator predicts thrust from the rate of change of working-
fluid momentum and the pressure-area correction:

\[
F=(\dot m v)_e-(\dot m v)_0+A_e(p_e-p_0)
\]

The software implementation is in tsphere/macroscopic_mechanism.py.

This is a valid macroscopic mechanism because it has a defined interaction:
the actuator accelerates a measurable working fluid, and the vehicle receives
the opposite momentum change. It is not a reactionless Flux Drive claim.

## Required physical validation

1. Calibrate a thrust stand with traceable masses or a calibrated load cell.
2. Measure mass flow, exhaust velocity, pressure, electrical power, and
   temperature on synchronized channels.
3. Run powered, unpowered, sham-load, vibration, cable-force, and thermal
   controls.
4. Require at least three repeated trials and one independent replication.
5. Compare measured force with the equation and publish the uncertainty budget.

The software gate returns VALIDATED_FOR_DEFINED_TEST only when the measured
force agrees within the declared uncertainty, repeats at least three times,
and has independent replication. That label is limited to the tested device,
configuration, and operating range.

## Wall-transit boundary

The same standard cannot currently be met for literal intact-wall phasing.
The repository therefore keeps the barrier-transit gate fail-closed:
incomplete or ambiguous evidence returns NOT_DEMONSTRATED. A frequency match,
material resonance, wireless handoff, optical occlusion, or motion through an
existing opening is not macroscopic wall phasing.

To elevate that claim, a future experiment would need a quantitative
interaction model, a sealed continuously observed barrier, full independent
sensor coverage, conservation checks, randomized controls, repeatability, and
independent replication. Until then, the correct result is not validated.
