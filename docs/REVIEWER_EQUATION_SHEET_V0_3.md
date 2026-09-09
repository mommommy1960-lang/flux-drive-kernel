# Aurora / Flux Drive Reviewer Equation Sheet v0.3

## Purpose

This sheet gives a reviewer one place to audit the present mathematical
bookkeeping. It is not a derivation of a new propulsion law. Every equation
below is either conventional mechanics/metrology or a software reference model.
The proposed Flux Drive mechanism remains unverified until a physical experiment
identifies and measures a real external momentum channel.

## 1. Inertial force requirement

For vehicle mass `m` and acceleration `a` in a declared inertial frame:

`F_net = m a`

Units:

- `m`: kg
- `a`: m/s^2
- `F_net`: N = kg m/s^2

Falsification/consistency gate: a claimed acceleration without the corresponding
net force/momentum exchange is not established by this equation.

## 2. Near-Earth vertical actuator force

Using positive upward acceleration:

`F_actuator = m (g + a_vertical)`

with `g = 9.80665 m/s^2` as the conventional standard-gravity reference.

For hover, `a_vertical = 0`, so `F_actuator = mg`.

This is a sizing identity, not evidence that the present Flux Drive can supply
that force.

## 3. Momentum boundary

For a declared experimental system boundary:

`Delta p_vehicle + Delta p_exhaust + Delta p_radiation + Delta p_environment = 0`

The environment term must be decomposed experimentally when relevant, including
fixture/support reaction, cable/feedthrough force, acoustic coupling, magnetic
interaction, electrostatics, atmosphere/buoyancy/convection, vibration/tilt,
and any other measured external channel.

Falsification gate: if a measured force disappears or follows one of those
channels under controls, it is not evidence of a new propulsion mechanism.

## 4. Impulse

`J = integral F(t) dt = Delta p`

For discretely sampled data, the integration rule and timing uncertainty must be
specified and frozen before the decisive run.

Units: N s = kg m/s.

## 5. Electrical energy

At the test-article terminals:

`E_electrical = integral V(t) I(t) dt`

The present software uses current magnitude for positive consumed electrical
energy in its simplified bench model. A real AC/RF experiment requires the
appropriate instantaneous or complex-power treatment, including phase and
harmonics where relevant.

## 6. Electrical input-power ledger

For the current design-accounting interval:

`P_input = P_actuator + P_control + P_thermal_management + P_losses + P_export`

`P_thermal_management` means electrical load consumed by active cooling/heating
hardware. It is not a second entry for heat already represented by the other
terms.

The residual is:

`R_P = P_input - sum(P_accounted)`

A nonzero residual beyond the declared tolerance means the ledger is incomplete.

## 7. Software actuator reference law

The default bench model is intentionally ordinary and linear:

`|I| = |u| I_max`

`F_model = sign(u) |I| K_F`

where:

- `u` is the dimensionless command in `[-u_max, u_max]`;
- `I_max` is maximum current magnitude in A;
- `K_F` is a reference force constant in N/A.

Therefore, below force saturation:

`F_model = u I_max K_F`

This is a controller/HIL plant model only. `K_F` must not be interpreted as a
measured Flux Drive property unless it is independently calibrated on hardware.

## 8. Radiation momentum reference

For radiation power `P` and an effective normal momentum-transfer factor `eta`:

`F_radiation = eta P / c`

where `c = 299792458 m/s` and, for the simple normal-incidence reference cases:

- `eta = 1`: emitted radiation or complete absorption;
- `eta = 2`: ideal specular reflection;
- intermediate `eta`: effective partial momentum transfer.

Geometry, spectrum, cavity fields, leakage, and scattering require a real
model; `eta` is not a free parameter that may be chosen to fit a desired force.

## 9. Linear calibration

For a calibrated channel:

`y = s x + b`

where `x` is the raw value, `s` the calibration slope, and `b` the offset.

Using first-order uncertainty propagation with possible correlations:

`u_y^2 = s^2 u_x^2 + x^2 u_s^2 + u_b^2`

`          + 2 s x cov(x,s) + 2 s cov(x,b) + 2 x cov(s,b)`

The covariance terms may be set to zero only when independence is justified.

## 10. Momentum-closure uncertainty

For measured force impulse `J_f` and reaction impulse `J_r`:

`R_J = J_f + J_r`

and:

`u_R^2 = u_f^2 + u_r^2 + 2 cov(J_f, J_r)`

Expanded uncertainty is reported as:

`U = k u_R`

with the chosen coverage factor `k` stated. A conventional `k=2` interval is
approximately 95% only under suitable distribution and degrees-of-freedom
conditions; the report must state the basis for any probability interpretation.

## 11. Physical acceptance gate

A candidate force is not promoted to propulsion evidence unless all of the
following hold:

1. the signal exceeds the predeclared expanded uncertainty;
2. sham/device-off controls do not reproduce it;
3. reversed and perpendicular orientations behave according to a preregistered
   prediction rather than an artifact pattern;
4. cable/feedthrough, magnetic, thermal, acoustic, vibration, pressure,
   convection, and buoyancy pathways are bounded below the effect size;
5. reaction/momentum accounting closes across the declared boundary;
6. the analysis version and exclusion rules were frozen before the decisive run;
7. an independent operator reproduces the result.

Only after these gates pass should mechanism inference and propulsion sizing
begin.

## 12. Aurora architecture boundary

Aurora currently has two separate engineering levels:

- **Lab vessel:** executable software, instrumentation, safety, and bench-test
  architecture.
- **City-ship:** requirements-level concept requiring independent closure of
  mass, structure, power, thermal rejection, ECLSS, radiation, GNC,
  communications, maintenance, conventional propulsion, and any experimental
  propulsion layer.

The Flux Drive must never be the city-ship's only safety-critical mobility
assumption until it is independently demonstrated. Conventional maneuvering,
attitude control, docking, abort, and station-keeping capability remain separate
requirements.

## Reference standards / comparison sources

- NIST Technical Note 1297, uncertainty propagation and expanded uncertainty.
- NASA/JPL conventional spacecraft propulsion references for momentum exchange.
- Published high-precision propellantless-thrust balance work as prior art for
  thermal, magnetic, cable, orientation, and null-control testing.

These references constrain the measurement method; they do not validate the
Flux Drive hypothesis.
