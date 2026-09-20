# Coupled Trajectory–Dust–Radiation–Thermal Screen v0.1

**Status:** public computational research artifact; not a flight design or
physical validation.

## Purpose

This model connects the corrected 4.3-light-year trajectory to the engineering
constraints that a standalone magnetosphere cannot solve: propulsion energy,
neutral gas and dust, pre-ionization power, magnetic bending distance,
residual-impact shielding, secondary radiation, and heat rejection.

The model is deliberately fail-closed. A green gate means only that a declared
algebraic threshold was not exceeded. It does not prove that an engine, shield,
pre-ionizer, magnet, radiator, or human-rated craft can be built.

## Corrected trajectory

For constant proper acceleration `a`, the symmetric accelerate-halfway and
decelerate-halfway profile uses

`gamma(x) = 1 + a min(x, D-x) / c^2`.

For `D = 4.3 ly` and `a = 1 g`, the peak values are approximately
`gamma = 3.2194` and `beta = 0.95054`. The endpoint-frame duration is about
5.93 years and the onboard proper time about 3.56 years.

The earlier `gamma = 365` baseline is rejected for this route: at 1 g it needs
about 353 light-years to accelerate and about 705 light-years to accelerate and
stop. Fitting it inside 4.3 light-years requires roughly 164 g.

## Coupled gates

1. **Acceleration:** declared proper acceleration must remain below the crew
   limit.
2. **Energy:** ideal relativistic kinetic energy, acceleration and braking,
   divided by declared efficiency, must remain inside the declared energy
   budget.
3. **Pre-ionizer:** neutral gas and dust ionization energy per unit proper time
   must remain below available forward-system power.
4. **Magnetic deflection:** relativistic Larmor radius
   `r_L = gamma beta c / ((q/m) B)` must be smaller than stand-off distance.
5. **Heat rejection:** residual deposited heat must not exceed
   `epsilon sigma A (T^4 - T_bg^4)`.
6. **Shield survival:** energy-equivalent removed shield mass must remain below
   the declared replaceable mass fraction.
7. **Radiation:** transmitted secondary energy per shelter mass must remain
   below the declared screening dose.
8. **Duration:** the endpoint-frame trip time must remain below the declared
   maximum mission duration.

## Default result and meaning

Run:

```bash
python tools/run_relativistic_mission_screen.py
python -m unittest tests.test_relativistic_mission -v
```

The deliberately ambitious default represents a million-kilogram craft with a
1 g Alpha Centauri profile. Its first expected failure is the declared
propulsion-energy budget. Other results depend on explicit assumed efficiencies
and must be treated as sensitivity-study inputs, not measured performance.

The runner also performs a bounded search over acceleration and reports the
fastest profile that passes every declared gate without changing the vehicle or
environment assumptions. This is a transparent requirements trade, not proof
that the assumed components are achievable.

With the v0.1 defaults and a total declared mission-energy ceiling of
`1.0e22 J`, the fastest algebraically passing profile peaks near `0.231 c` and
takes about 36.7 endpoint-frame years. Its apparent pass remains conditional on
the declared dust charge-to-mass ratio, efficiencies, scalar radiation model,
and mean environment. Those values have not been experimentally validated for
this architecture.

## Required next validation stages

- replace mean dust density with a size-frequency distribution and Monte Carlo
  rare-grain encounters;
- use SRIM/Geant4-class particle transport for radiation and secondary showers;
- use hydrodynamic impact/ablation models for the sacrificial shield;
- model laser coupling, plume expansion, recombination and incomplete
  ionization before claiming pre-ionizer performance;
- solve charged-grain trajectories in a three-dimensional field map;
- couple radiator geometry and view factors to a transient thermal network;
- independently reproduce every equation and unit;
- retain CAL-00 as the separate physical force-measurement gate.

## Scientific non-claims

This artifact does not demonstrate reactionless propulsion, a warp drive,
faster-than-light travel, a working magnetosphere, adequate shielding, a power
source, or a flight-capable vehicle. It identifies which declared requirement
fails first and makes the assumptions inspectable.
