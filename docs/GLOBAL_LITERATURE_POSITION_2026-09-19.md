# Global literature position and novelty boundary

Date checked: 2026-09-19  
Project state: independent numerical reproduction in progress; no propulsion or flight claim

## Bottom line

The present Flux Drive shifted-shell result is **not the first global report** that the Fuchs et al. constant-velocity positive-energy shell develops energy-condition problems outside its apparently compliant bulk region.

The closest known prior result is An T. Le, *On the boundary cost of source-consistent warp shells*, arXiv:2605.25417v1, submitted 25 May 2026. That work reports a frame-independent verification of the Fuchs shell: its interior probes comply, but Hawking–Ellis Type IV violations appear in the smoothing tail beyond the nominal shell. It also scans 600 shell compactness/thickness configurations and reports no construction passing its complete five-criterion standard.

The Flux Drive branch independently found a related pattern on 19 September 2026:

1. sparse x-axis samples appeared positive;
2. six-axis and spherical coverage sharply reduced the weakest NEC margin;
3. neighboring-radius refinement exposed negative sampled NEC, DEC, and SEC margins near r = 12.25 m.

This agreement is scientifically useful as an independent reproduction path, but priority for the general boundary-failure observation belongs to the earlier literature unless a later detailed comparison establishes a distinct new theorem, implementation, bug finding, parameter regime, or independently verified benchmark.

## Closest comparison

| Work | What it establishes | Relative position |
|---|---|---|
| Fuchs et al., CQG 41 (2024) 095013, arXiv:2405.02709 | Published constant-velocity subluminal shell reported to satisfy all energy conditions | Baseline being reproduced and stress-tested |
| Le, arXiv:2602.18023v4 | warpax: frame-independent all-observer energy-condition classification using Hawking–Ellis eigenstructure | Methodologically ahead of the current finite observer sampling |
| Le, arXiv:2605.25417v1 | Finds Fuchs interior compliance but Type IV smoothing-tail violations; scans 600 configurations; none passes full standard | Closest prior result; ahead in coverage and certification |
| Barzegar, Buchert, and Vigneron, arXiv:2602.16495v1 | General classification, structural critique, and new no-go theorems | Broader and more rigorous theoretical framework |
| Le, arXiv:2606.22531v1 | Positive-energy subluminal steering through photon-rocket recoil and Bondi mass loss; not reactionless or FTL | Addresses control/steering more deeply, but remains theoretical |
| Current Flux Drive PR #17 / Issue #20 | Independent implementation, finite-difference Einstein tensor, observer sweeps, and preliminary reproduction of a boundary failure | Useful open reproduction; not first and not yet independently certified |

## What may still be publishable

The present result alone should not be advertised as a novel discovery. A defensible research output may become possible if the project provides one or more of the following:

- a reproducible open benchmark that independently reproduces the published boundary failure;
- a precise comparison between direct-g01 and independent 3+1 implementations;
- convergence/error bounds showing where the failure begins and how it scales;
- a documented discrepancy or defect in an existing implementation;
- a parameter-space result not already covered by the 600-configuration study;
- a source-first alternative that survives frame-independent energy, causality, stability, horizon, and tidal gates;
- a physical CAL-00 residual-force result surviving full conventional momentum accounting and independent replication.

Until then, the correct description is: **open independent replication work that has reproduced the qualitative location and character of a known theoretical obstruction.**

## Fame and validation boundary

A public GitHub repository does not by itself establish scientific priority, peer review, recognition, or fame. Interest, downloads, email replies, and citations do not establish physical validation. Recognition would require a citable release, clear novelty, expert review, reproducibility, and—if physical propulsion is claimed—measurement-grade experimental evidence.

No reviewed source located in this check reports a physical warp-drive vehicle, nearly instantaneous point-to-point transport, or a laboratory implementation of the required spacetime stress-energy. The field remains theoretical.

## Primary sources

- Fuchs et al.: https://arxiv.org/abs/2405.02709
- Bobrick and Martire: https://arxiv.org/abs/2102.06824
- Le, observer-robust verification: https://arxiv.org/abs/2602.18023
- Le, boundary cost: https://arxiv.org/abs/2605.25417
- Barzegar, Buchert, and Vigneron: https://arxiv.org/abs/2602.16495
- Le, steering: https://arxiv.org/abs/2606.22531
- Celmaster and Rubin, Lentz critique: https://arxiv.org/abs/2511.18251

## Next project actions

1. Replace finite observer sampling with Hawking–Ellis eigenvalue classification or cross-check against warpax.
2. Complete the independent 3+1 implementation.
3. Reproduce the r = 12.25 m failure under radial-grid and stencil refinement.
4. Compare the identified region directly with the published smoothing-tail coordinates and conventions.
5. Publish only after stating prior art and isolating an actual new contribution.
