# Scientific audit of Zenodo Flux Drive records (2026-09-19)

Status: **correction required; not independent validation; not a demonstrated drive**

Audited records:

- Zenodo 22850488, DOI 10.5281/zenodo.22850488
- Zenodo 22850703, DOI 10.5281/zenodo.22850703

This audit preserves useful work while separating verified calculations from unsupported or incorrect claims. The original records remain part of the evidence trail. Corrected Zenodo versions should cite this audit and label the originals as superseded.

## Result summary

| Item | Audit result |
|---|---|
| Lorentz factor and cruise speed | Correct to displayed precision: for (gamma=365), (eta=sqrt{1-gamma^{-2}}=0.9999962469). |
| “4.3 light-years in 4.3 crew-days” | Correct only for an idealized constant-speed cruise segment, approximately. Earth-frame travel remains about 4.3 years. Acceleration, deceleration, energy, shielding, and trajectory constraints are omitted. |
| “Flat Minkowski Velocity Slicing” | This is ordinary special-relativistic motion, not a new propulsion mechanism and not point-to-point instantaneous travel. |
| Warp-shell energy equation | The displayed throat relation is Morris–Thorne-style wormhole algebra and is not a derivation for the Alcubierre/Fuchs shift metric. The quoted (-4.82	imes10^{40},mathrm{J/m^3}) is therefore not established by the displayed equation. |
| Universal Type-IV boundary claim | Not established. Current repository work found an implementation/convention disagreement; the Hawking–Ellis classification has not completed an independently reproduced, converged, frame-independent proof. |
| Atmospheric “coordinate singularities” | Incorrect. Ordinary relativistic interaction with atmosphere/plasma creates extreme particle, radiation, heating, and momentum-transfer loads; it does not by itself create a metric coordinate singularity or Type-IV stress-energy. |
| 5 T plasma cushion | A concept to analyze, not a resolution. At (gamma=365), an incident proton has about (342,mathrm{GeV}) kinetic energy and a 5 T perpendicular-field gyroradius of roughly (228,mathrm{m}). Neutral dust and radiation remain unresolved. |
| (2.048	imes10^{13},mathrm{J}) SMES | Unsupported as a vehicle subsystem. This is 5.69 GWh. Even the ideal magnetic-field volume is about (2.06	imes10^6,mathrm{m^3}) at 5 T or (1.29	imes10^5,mathrm{m^3}) at 20 T, before structure, shielding, cryogenics, switching, and stress margins. |
| Antihydrogen pellets | Not physically supported. Neutral antihydrogen cannot be electrostatically confined as described, and macroscopic solid antihydrogen pellets are not an available technology. |
| Fuel-flow arithmetic | The conversion (2.41	imes10^{12},mathrm{W}/c^2=2.68	imes10^{-5},mathrm{kg/s}) total annihilated mass and 13.4 mg/s antimatter is arithmetically correct only for ideal 100% conversion. It is not a propulsion closure. |
| Energy closure | At (gamma=365), kinetic energy is (3.27	imes10^{19},mathrm{J/kg}). Running 2.41 TW for 4.3 years supplies (3.27	imes10^{20},mathrm{J}), enough for only about 10 kg of kinetic payload at 100% efficiency, before deceleration and all losses. |
| Radiator/nozzle temperatures | Not supported by the stated geometry. Rejecting (8.44	imes10^{11},mathrm{W}) at 3300 K requires about (1.39	imes10^5,mathrm{m^2}) at emissivity 0.9; the stated 5 m-scale surface is orders of magnitude too small. |
| GaPO4 metrology | Potentially useful instrumentation research, but “zero artifact” and “physically proves” are too strong. Calibration, cross-axis coupling, thermal gradients, wiring forces, EM coupling, drift, and independent replication remain required. |
| VHDL/register map | A design sketch, not hardware validation. The sample decoder omits multiple table registers and does not establish timing closure, fixed-point scaling, fail-safe behavior, CDC handling, or verified synthesis. |
| “Peer-reviewed” / institutional feedback | Unsupported. No verified peer review or technical findings from Stanford, University of Washington, or Paihau–Robinson are recorded. Outreach requests or routing messages must not be rewritten as institutional technical conclusions. |
| “Publication-grade” / “resolved” | Incorrect status language. Zenodo deposit creates a citable public record; it does not confer peer review, correctness, priority over prior physics, or validation. |

## Corrections required in the next Zenodo versions

1. Rename the work as a **concept and falsification plan**, not a peer-reviewed proof or physically closed propulsion system.
2. Replace “near-instantaneous” and “point-to-point shortcut” with “short onboard proper time during idealized relativistic cruise.”
3. State Earth-frame duration, acceleration profile, deceleration, rocket equation, energy budget, radiation, dust, and waste-heat limits.
4. Remove the mixed wormhole/warp equation and the unsupported numerical negative-energy threshold unless derived reproducibly for one frozen metric with conventions and units shown.
5. Replace the universal Type-IV assertion with the current repository status: implementation discrepancy under investigation; classifier/convergence review pending.
6. Remove claims that atmosphere generates coordinate singularities or Type-IV tensors.
7. Label the 5 T field, SMES value, antimatter system, and thermal architecture as unvalidated parameter assumptions, not resolved subsystems.
8. Remove or document every claimed institutional comment with a public, consented source. Outreach alone is not review.
9. Replace “absolute zero pyroelectric artifacts” with the narrower material property and a complete instrument uncertainty budget.
10. Correct the bibliography. The cited “Fuchs et al. (2024), Journal of Mathematical Physics 65(4), 210–225” entry could not be matched to a verified publication and must not remain without a DOI or exact primary source.
11. Do not call a Zenodo upload peer reviewed. Use “public preprint/concept dossier” only after the equations and citations are corrected.
12. Link the corrected records to the GitHub commit, tests, software version, and explicit non-claims.

## Preserved positive result

The useful mathematical core is the special-relativity benchmark:

[
gamma = rac{1}{sqrt{1-eta^2}},qquad
eta = 0.9999962469,
]

which makes a 4.3-year idealized cruise interval correspond to roughly 4.3 days of onboard proper time. This is established textbook physics, not a new drive. The unsolved work is how to accelerate, protect, power, and decelerate a macroscopic vehicle without violating known engineering and physical constraints.

## Project status after audit

- Public record: established.
- Correct special-relativity timing example: established.
- Warp-boundary theorem: not established.
- Positive-energy propulsion source: not established.
- Atmospheric/magnetospheric resolution: not established.
- Macroscopic antimatter architecture: not established.
- CAL-00 residual-force result: not yet physically demonstrated.
- Fame or scientific priority: not established.
