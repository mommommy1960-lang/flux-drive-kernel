# Flux Drive Corrected Scientific Baseline

Date: 2026-09-20  
Owner: Mya P. Brown  
Status: computational research and measurement planning; no demonstrated drive

## Bottom line

The September 19 document collection does **not** establish instantaneous
point-to-point travel, a flight-capable relativistic vehicle, a reactionless
drive, or a physically closed antimatter propulsion architecture. It contains
one correct special-relativity timing benchmark, useful metrology ideas, and a
substantial falsification-oriented software record. It also contains mixed
metric equations, a false literature attribution, unsupported institutional
feedback, and engineering values presented with more certainty than their
derivations support.

The valid project is therefore the narrower one recorded here: reproduce and
stress-test published spacetime calculations, preserve failures, and prepare a
calibrated small-force experiment. Any stronger claim remains unvalidated.

## Verified mathematical results

### Special-relativity timing benchmark

For a target Lorentz factor of 365,

```text
beta = sqrt(1 - 1/gamma^2) = 0.9999962469436048
v = 299,791,332.862 m/s
```

An idealized 4.3-light-year constant-speed cruise would therefore take about
4.3 years in the endpoint frame and about 4.3 days of onboard proper time.
This excludes acceleration, deceleration, path geometry, shielding, propulsion
efficiency, and the time required to reach cruise speed. It is standard
special relativity, not a new propulsion mechanism or instantaneous travel.

### Morris-Thorne regression failure

For the frozen zero-redshift Morris-Thorne throat with `r0 = 10 m`,
`b(r0) = r0`, and `b'(r0) = 0`,

```text
rho = 0
p_r = -1/(8*pi*r0^2)
p_t = +1/(16*pi*r0^2)
rho + p_r = -3.978873577e-4 m^-2
```

Using `c^4/G` to convert geometric energy density to SI gives approximately
`-4.815e40 J/m^3` for the radial NEC combination. This is a regression result
for that failed wormhole branch. It is not an Alcubierre-shell result, a Fuchs
shell result, or a universal negative-energy threshold.

### Hawking-Ellis classifier

The repository now includes a conservative classifier that:

- accepts a covariant `T_ab` in a local orthonormal frame;
- records relative antisymmetry before any allowed numerical symmetrization;
- certifies Type I only from a complete real eigenspace with Lorentz signature
  `(-,+,+,+)`;
- reports robust complex eigenvalues as Type IV;
- refuses to assign Type II or III from floating-point degeneracy alone; and
- evaluates NEC, WEC, SEC, and DEC only for canonical Type-I variables.

Eight focused classifier tests pass. The complete local suite passes 121 tests
with zero failures. This validates the tested software behavior; it does not
validate a propulsion device or the uncompleted Fuchs reconstruction.

## Correct literature record

The applicable Fuchs reference is:

Jared Fuchs, Christopher Helmerich, Alexey Bobrick, Luke Sellers, Brandon
Melcher, and Gianni Martire, "Constant Velocity Physical Warp Drive
Solution," *Classical and Quantum Gravity* 41 (2024) 095013,
https://doi.org/10.1088/1361-6382/ad26aa; arXiv:2405.02709.

The paper reports a numerical constant-velocity, subluminal construction. A
reproduction still requires exact agreement on the metric, conventions,
Einstein tensor, stress-energy tensor, observer treatment, and convergence.
It does not demonstrate acceleration, steering, an endpoint shortcut, or
instantaneous travel.

Two September checkpoint citations required correction:

- `arXiv:2605.25417` is An T. Le, "Relativistic elastic shells: material
  support and cavity geometry." It is **not** a paper titled "On the boundary
  cost of source-consistent warp shells," and it does not support the claimed
  Fuchs Type-IV-tail conclusion.
- `arXiv:2606.22531` is currently titled "Radiative steering of warp shells."
  It describes subluminal photon-recoil steering and explicitly leaves
  stability/settling questions open. It is not a reactionless or instantaneous
  transport result.

The nonexistent/misattributed boundary-cost citation and all conclusions based
on it are withdrawn from the canonical project record.

## Unresolved numerical result

The direct-`g01` and full ADM/3+1 implementations currently disagree in the
boundary region. The direct implementation converges toward negative sampled
energy-condition margins in the recorded case, while the ADM implementation
remains positive over the sampled region. These are different metric
conventions until proved otherwise. Neither result may be promoted as the
physical answer.

Required resolution:

1. Freeze one metric, signature, index placement, tetrad, units, and derivative
   convention.
2. Compare metric components and first and second derivatives point by point.
3. Compare Einstein tensors before projecting observer quantities.
4. Quantify antisymmetry and demonstrate its convergence order.
5. Apply the Hawking-Ellis classifier only after the tensor convergence gate.
6. Reproduce the result independently before making a boundary theorem claim.

## Engineering scale corrections

### Relativistic energy

At `gamma = 365`, kinetic energy is about `3.271e19 J/kg`. A 2.41 TW source
operated for 4.3 years produces about `3.270e20 J`, enough to supply the ideal
kinetic energy of only about 10 kg at 100 percent efficiency, before
deceleration, propulsion losses, shielding, structure, and payload support.

### Incident particles and magnetic deflection

At `gamma = 365`, an incident proton carries about 342 GeV of kinetic energy.
Its perpendicular gyroradius in a 5 T magnetic field is about 228 m. A proposed
5 T field therefore remains a parameter-study input, not a demonstrated shield.
Neutral dust, secondary radiation, heat rejection, and field-generating mass
remain open.

### SMES scale

`2.048e13 J` is about 5.69 GWh. The ideal field volume alone is approximately
`2.06e6 m^3` at 5 T or `1.29e5 m^3` at 20 T, before coil structure, stress
containment, cryogenics, switching, protection, and losses. It is not a closed
vehicle subsystem.

### Antihydrogen

Macroscopic solid antihydrogen pellets are not an available technology.
Neutral antihydrogen cannot be confined by the electrostatic quadrupole system
described in the drafts. The proposed fuel vault, injector, and emergency dump
must be treated as speculative fiction/concept art, not an engineering design.

### Waste heat

Radiating `8.44e11 W` at 3300 K with emissivity 0.9 requires about
`1.39e5 m^2` of ideal radiating area. The five-meter-class nozzle geometry in
the drafts does not close the thermal ledger.

### GaPO4 force metrology

Gallium phosphate is a legitimate high-temperature piezoelectric material and
is not pyroelectric by crystal symmetry. That property does not make a complete
balance artifact-free. Cross-axis sensitivity, thermal gradients, cable
forces, electromagnetic coupling, calibration drift, vibration, covariance,
and independent replication remain part of CAL-00.

## Claims withdrawn from the canonical record

- "Fully realized" relativistic drive.
- "Physically closed" propulsion system.
- Universal proof that smooth warp boundaries are Type IV.
- Atmospheric coordinate singularities caused by ordinary relativistic
  particle interaction.
- Resolved 5 T shielding or resolved 5.69 GWh vehicle SMES.
- Buildable solid-antihydrogen pellet architecture.
- Verified institutional findings attributed to Stanford, the University of
  Washington, or Paihau-Robinson without a documented response.
- "Peer-reviewed" status for self-published or Zenodo-deposited drafts.
- "System validated / complete."

Outreach messages, acknowledgments, referrals, and repository deposits are
valuable provenance, but none is scientific validation.

## Current project gates

1. Resolve the direct-`g01` versus ADM metric convention and tensor discrepancy.
2. Demonstrate second-order or better convergence in the boundary region.
3. Apply the classifier to a converged, symmetric stress-energy tensor.
4. Independently reproduce the Fuchs construction and energy-condition scan.
5. Keep acceleration, steering, causal shortcut, and hardware questions
   separate from the constant-velocity metric calculation.
6. Execute CAL-00 with calibrated force and reaction-force channels.
7. Require independent replication before treating any residual as anomalous.

## Scientific status

The project has produced useful research software, a correct proper-time
benchmark, a negative-NEC wormhole regression, a public falsification record,
and a stronger algebraic classifier. It has **not** produced a flight-capable
Flux Drive or reached the point-to-point transport goal.

