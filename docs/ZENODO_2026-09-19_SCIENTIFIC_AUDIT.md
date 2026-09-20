# Scientific Audit of September 19 Zenodo Flux Records

Audited records:

- Zenodo 22850488, DOI 10.5281/zenodo.22850488
- Zenodo 22850703, DOI 10.5281/zenodo.22850703

Status: correction required; not independent validation; not a demonstrated
drive.

## Findings

| Item | Audit result |
|---|---|
| Lorentz benchmark | For gamma 365, beta is 0.9999962469. This is correct special relativity. |
| Travel time | About 4.3 onboard days for an idealized 4.3-year constant-speed segment; acceleration and deceleration are excluded. |
| Propulsion claim | Ordinary time dilation does not supply thrust, energy, shielding, steering, or an endpoint shortcut. |
| Negative-energy value | The `-4.82e40 J/m^3` result belongs to the frozen Morris-Thorne throat regression, not the displayed Alcubierre/Fuchs model. |
| Universal Type-IV claim | Not established. The direct-`g01` and ADM implementations disagree in the boundary region. |
| Atmospheric singularity | Incorrect. Relativistic atmosphere/plasma interaction creates particle, radiation, heat, and momentum loads, not a coordinate singularity by itself. |
| 5 T shield | At gamma 365, an incident proton carries about 342 GeV and has an approximately 228 m perpendicular gyroradius in 5 T. Dust and secondary radiation remain unresolved. |
| SMES | `2.048e13 J` is 5.69 GWh. Ideal field volume is about `2.06e6 m^3` at 5 T or `1.29e5 m^3` at 20 T, before engineering margins. |
| Antihydrogen | Macroscopic solid antihydrogen pellets are unavailable; neutral antihydrogen cannot be electrostatically confined as described. |
| Energy | At gamma 365, kinetic energy is about `3.27e19 J/kg`. A 2.41 TW source operating for 4.3 years supplies only about 10 kg of ideal kinetic payload before deceleration and losses. |
| Waste heat | Rejecting `8.44e11 W` at 3300 K and emissivity 0.9 requires about `1.39e5 m^2` of ideal radiating area. |
| GaPO4 | A legitimate high-temperature piezoelectric candidate, but not an artifact-free balance by itself. |
| VHDL | A register-map sketch, not verified hardware, timing closure, or fail-safe certification. |
| Institutional feedback | Outreach is not peer review. No verified Stanford, University of Washington, or Paihau-Robinson technical findings are recorded. |
| Zenodo status | A DOI makes the work citable; it does not establish correctness, novelty, peer review, or validation. |

## Bibliography correction

The applicable source is Jared Fuchs et al., "Constant Velocity Physical Warp
Drive Solution," *Classical and Quantum Gravity* 41 (2024) 095013,
DOI `10.1088/1361-6382/ad26aa`, arXiv:2405.02709. The dossier's *Journal of
Mathematical Physics* citation is incorrect.

`arXiv:2605.25417` is An T. Le, "Relativistic elastic shells: material support
and cavity geometry." It is not a boundary-cost paper and does not support the
claimed Fuchs Type-IV-tail conclusion.

`arXiv:2606.22531` is An T. Le, "Radiative steering of warp shells." It treats
subluminal photon-recoil steering and does not establish reactionless or
instantaneous travel.

## Required record correction

1. Publish corrected Zenodo versions that cite the original records and this
   audit.
2. Describe the work as a concept and falsification program, not a peer-reviewed
   proof or physically closed propulsion system.
3. Remove the mixed wormhole/warp equation and unsupported universal Type-IV
   claim.
4. Label the 5 T field, SMES, antimatter, thermal, and flight architecture as
   unvalidated parameter studies.
5. Replace institutional "feedback" with a verified correspondence-status log.
6. Link the corrected records to the exact GitHub commit and test result.

## Preserved result and current boundary

The useful result is the special-relativity proper-time benchmark and the
falsification-oriented measurement/software framework. No physical Flux Drive,
reactionless propulsion, faster-than-light travel, or instantaneous
point-to-point transport has been demonstrated.
