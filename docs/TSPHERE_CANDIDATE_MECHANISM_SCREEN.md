# T-Sphere Candidate Mechanism Screen v0.1

## Purpose

This screen converts the “make the T-Sphere phase” request into equations that
can be measured with ordinary laboratory instruments. It does not assume that
any candidate is correct.

## Candidate A — quantum tunneling

Use the WKB screening exponent already implemented in
`tsphere/tunneling_scaling.py`:

\[
\log_{10}T \approx -\frac{2a}{\ln 10}\frac{\sqrt{2m\Delta E}}{\hbar}.
\]

This is useful as a scale test for microscopic particles. It does not provide
a macroscopic robot design because the coherent many-body state, barrier model,
and environmental isolation required for a sphere are not supplied.

## Candidate B — electromagnetic or optical momentum

For an ordinary radiation-pressure upper bound:

\[
F_\text{rad} = \frac{(1+R)P}{c}.
\]

The software computes this baseline. It is a real force, but it pushes on the
target; it does not make the target transparent or create reactionless motion.

## Candidate C — acoustic pressure

For a first pressure-force scale:

\[
F_\text{acoustic} \approx p_\text{rms}A.
\]

This can move light objects or create fixture forces. It cannot be labeled
barrier transit without proving that the measured effect is not ordinary
pressure, vibration, heating, cable coupling, or acoustic leakage.

## Candidate D — spacetime shortcut

A warp or wormhole proposal must specify a metric and its stress-energy source,
then show that the source can be created, confined, controlled, and kept stable.
The existing T-Sphere materials do not provide those terms or a laboratory
source. This remains a theoretical branch, not a hardware instruction.

## Measurement decision rule

For a proposed force experiment, the software reports:

- `NOT_RESOLVED` when the signal does not exceed controls and uncertainty;
- `MODEL_INVALID` when the claimed model predicts no positive effect;
- `INCONSISTENT_WITH_MODEL` when a signal exists but does not match the model;
- `CONSISTENT_WITH_MODEL` only when the signal clears controls and uncertainty
  and agrees with the declared prediction.

“Consistent with model” is not the same as “new physics.” Independent
replication and artifact elimination are still required.

## Immediate result

The available devices are sufficient for Candidates B and C at low energy and
for the measurement side of Candidate D. They cannot create the missing
macroscopic tunneling or spacetime-shortcut mechanism. The next hardware build
should therefore measure ordinary force and artifact channels first, while the
theoretical branch remains explicitly separate.
