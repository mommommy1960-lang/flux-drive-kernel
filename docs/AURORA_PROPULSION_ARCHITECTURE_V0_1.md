# Aurora Propulsion Architecture v0.1

## Status

Requirements architecture only. This document deliberately separates proven
spaceflight functions from the experimental Flux Drive program. It does not
claim that a city-sized spacecraft can presently be built, launched, or powered.

## Design rule

Aurora must never depend on an unverified propulsion mechanism for a
safety-critical function.

The vessel architecture therefore has four propulsion/mobility layers:

1. assembly and emplacement;
2. conventional translation and mission propulsion;
3. attitude control, docking, station-keeping, and abort mobility;
4. experimental Flux Drive research, isolated behind evidence and safety gates.

## 1. Assembly and emplacement

A city-sized Aurora should not be baselined as a vehicle that launches intact
from Earth's surface. Before any detailed trade study, the more credible
requirements path is modular launch and in-space assembly.

Candidate assembly regions for later trade study include:

- low Earth orbit with debris/drag/traffic constraints;
- higher Earth orbit with radiation and logistics constraints;
- cislunar space;
- Earth-Moon Lagrange-region logistics nodes;
- lunar-orbit or lunar-surface-supported industrial architecture in a much
  longer-term scenario.

"Space dock" is used here as a systems-engineering placeholder for a modular
assembly, inspection, checkout, refueling/resupply, and safe-haven facility. It
is not assumed to exist today at Aurora scale.

Orbital debris is a serious engineering and governance hazard, but Earth orbit
is not literally out of physical room. The design problem is collision risk,
traffic coordination, protected orbital regimes, debris generation, shielding,
and maneuver capacity, not lack of geometric volume.

## 2. Conventional mission propulsion

Aurora requires a conventional propulsion baseline even if Flux Drive research
continues. Technology selection is intentionally left open until a mass,
mission, power, thermal, and propellant trade exists.

Required conventional functions include:

- departure and trajectory correction;
- rendezvous and docking;
- collision avoidance;
- station keeping;
- safe-mode translation;
- abort / retreat capability;
- controlled disposal or parking if the vessel becomes non-mission-capable.

Candidate technology families for future qualified trade studies include:

- chemical propulsion for high-thrust impulsive maneuvers where appropriate;
- electric propulsion for high-efficiency low-thrust operations;
- solar-electric or nuclear-electric power/propulsion architectures where
  mission scale and regulation justify study;
- solar sails, beamed momentum, or other externally coupled concepts for
  specialized functions.

No candidate is selected by this document.

## 3. Attitude, docking, and local control

Attitude control and docking must be independent of the experimental Flux Drive.
The architecture requires:

- redundant attitude sensors;
- independently safable attitude actuators;
- docking-relative navigation;
- collision-avoidance authority;
- momentum unloading;
- safe-mode pointing for power, thermal, and communications survival;
- crew/manual intervention appropriate to flight phase.

A propulsion experiment may not disable or share a single point of failure with
these functions.

## 4. Flux Drive experimental layer

Until physical validation exists, Flux Drive is an experiment carried by the
architecture, not the architecture's guaranteed engine.

Promotion gates are:

- **G0 — software:** deterministic model, safety logic, data schema, audit trail;
- **G1 — bench anomaly:** calibrated signal above the complete uncertainty
  budget and surviving preregistered controls;
- **G2 — independent replication:** another qualified team reproduces the
  effect from frozen materials;
- **G3 — mechanism:** a physically coherent momentum/field interaction model
  predicts the observed result and survives new tests;
- **G4 — engineering prototype:** repeatable thrust, efficiency, thermal,
  lifetime, EMC, structural, and control behavior demonstrated on hardware;
- **G5 — flight experiment:** qualified small-scale space test with conventional
  recovery/abort capability;
- **G6 — mission propulsion:** only after repeated flight evidence and
  independent safety certification.

Warp/spacetime terminology remains speculative until a relativistic mechanism
and corresponding evidence exist. An unexplained bench force is not by itself a
warp drive.

## Aurora autonomy / AI boundary

Aurora may eventually contain highly autonomous mission-management and fault-
management software. The engineering requirement is not "sentience"; it is
capability, continuity, authority, and safety behavior that can be tested.

Required governance invariants:

- human trust does not automatically confer authority;
- capability does not confer sovereignty;
- continuity does not confer immunity from oversight;
- care or mission-preservation objectives do not justify coercion;
- consequential actions remain attributable, bounded, auditable, and
  independently interruptible;
- the crew retains appropriate insight and intervention capability;
- autonomous fault management must fail toward a survivable state rather than
  protect its own continued operation at any cost.

The word "sentient" may be used in fiction/philosophy discussions, but engineering
acceptance criteria must be stated in observable behaviors and interfaces.

## City-ship closure prerequisites

Before a city-ship propulsion sizing study can be credible, Aurora needs at
minimum:

- itemized dry/wet mass ledger with uncertainty;
- structural architecture and load cases;
- pressure-volume and habitat geometry;
- population and mission-duration assumptions;
- ECLSS closure and reserve model;
- agriculture/food strategy if applicable;
- electrical generation/storage/distribution budgets;
- heat-rejection architecture;
- radiation dose and storm-shelter model;
- maintenance, spares, repair, and manufacturing assumptions;
- communications and navigation architecture;
- conventional propulsion and propellant/reaction-mass trade;
- assembly/logistics sequence;
- independent safety and human-rating pathway.

Only after those are bounded should a city-ship acceleration, range, transit
time, or launch/assembly cost be advertised.

## Near-term practical target

The near-term buildable Aurora is not the city-ship. It is the **Aurora Lab
Vessel / digital-twin stack**: auditable flight-like software, sensor/actuator
interfaces, fault management, human authorization, deterministic replay,
hardware-in-the-loop testing, and a small supervised propulsion-measurement
program.

That creates a credible technology ladder from software to instrumentation to
small hardware without requiring the city-ship to exist first.
