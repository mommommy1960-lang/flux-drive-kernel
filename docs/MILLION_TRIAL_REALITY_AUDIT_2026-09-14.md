# Flux Drive Million-Trial Reality Audit — 2026-09-14

## Scope

This report stress-tests the **analysis pipeline**, not a propulsion mechanism.
It uses 1,000,000 synthetic null-world trials containing ordinary artifact
channels (thermal, magnetic, cable, vibration, and measurement noise) and asks
how often those artifacts would be mistaken for thrust.

The result does **not** establish reactionless propulsion, warp propulsion,
spacetime control, or flight capability. It is a falsification tool.

## Reproducibility

Run:

```bash
python tools/run_million_trial_reality_audit.py
```

Seed: `20260914`  
Trials: `1,000,000`

## Synthetic artifact model

Reference-only standard deviations, in micro-newtons:

- thermal: 2.5
- magnetic: 1.5
- cable/feedthrough: 2.0
- vibration/tilt: 1.0
- residual measurement noise: 0.8

Artifact-channel estimates are deliberately imperfect so the stress test does
not grant the analysis unrealistically perfect subtraction.

## Main result

The raw null-world signal had an RMS amplitude of approximately **3.757 uN**.
After explicit artifact-channel correction, the residual RMS fell to
approximately **1.543 uN**.

Using the corrected residual uncertainty as the gate scale, the observed false
positive rates were:

| Gate | Naive raw-channel false positive | Corrected-channel false positive |
|---|---:|---:|
| 2 sigma | 41.1106% | 4.5320% |
| 3 sigma | 21.8202% | 0.2723% |
| 4 sigma | 10.0519% | 0.0064% |
| 5 sigma | 4.0024% | 0.0001% |

This is the central engineering lesson: **a large-looking force trace is not a
propulsion result when the experiment has not first bounded ordinary coupling
channels.** In this synthetic null model, naive thresholding remains badly
misleading even at apparently stringent thresholds because the raw signal still
contains structured artifacts.

## Detection tradeoff at a five-sigma gate

With the same synthetic residual noise model, the probability of detecting a
fixed injected signal at the five-sigma gate was approximately:

- 1 uN: 0.0008%
- 2 uN: 0.0105%
- 3 uN: 0.1089%
- 5 uN: 3.9078%
- 8 uN: 57.3665%
- 10 uN: 93.0603%
- 15 uN: 99.9999%

This demonstrates why a rigorous experiment must report **sensitivity and
uncertainty**, not merely whether a trace crossed zero.

## Radiation-momentum sanity check

Using `F = eta P / c`:

| Directed power | Absorption/emission reference | Ideal reflection reference |
|---|---:|---:|
| 10 W | 0.0334 uN | 0.0667 uN |
| 100 W | 0.3336 uN | 0.6671 uN |
| 1 kW | 3.3356 uN | 6.6713 uN |
| 10 kW | 33.3564 uN | 66.7128 uN |

Therefore radiation leakage or directed electromagnetic momentum cannot be
ignored merely because the measured force is in the micro-newton range.

## Vehicle force-scaling sanity check

From `F = m a`:

- 1 kg at 0.1 m/s^2 requires 0.1 N.
- 10 kg at 0.1 m/s^2 requires 1 N.
- 100 kg at 0.1 m/s^2 requires 10 N.
- 1000 kg at 0.1 m/s^2 requires 100 N.

A micro-newton-scale bench anomaly, even if eventually verified, would therefore
still be many orders of magnitude away from meaningful vehicle translation
unless a physically demonstrated scaling law closes that gap.

## Engineering consequence for Aurora

Aurora should continue to separate:

1. **lab validation** — low-energy, instrumented, falsification-first tests;
2. **conventional mobility** — ordinary propulsion for translation, attitude,
   docking, station keeping, collision avoidance, and abort;
3. **experimental Flux layer** — isolated behind evidence gates and never used
   as the only safety-critical mobility assumption.

## Required next physical milestone

Do not increase simulated thrust coefficients to make the model "work." The
next meaningful milestone is a calibrated, low-energy physical bench run that:

- records force and reaction force simultaneously;
- records voltage/current at the measured terminals;
- records temperature and declared environmental channels;
- includes sham/device-off, orientation-reversal, and perpendicular controls;
- freezes the analysis and exclusion rules before the decisive run;
- reports uncertainty-aware momentum closure;
- is independently repeated.

Until those conditions are met, `physical_propulsion_proven=false` remains the
correct state.
