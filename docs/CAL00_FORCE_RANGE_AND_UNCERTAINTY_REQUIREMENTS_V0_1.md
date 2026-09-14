# CAL-00 Force Range and Uncertainty Requirements v0.1

**Status:** pre-instrument-selection engineering requirement  
**Scope:** low-energy CAL-00 measurement bench  
**Evidence state:** design requirement, not a physical measurement and not evidence of propulsion

## Purpose

Issue #11 requires the first CAL-00 force range, standard-uncertainty target, expanded-uncertainty target, sampling requirement, and saturation margin to be frozen before selecting instruments. The purpose is to make instrument selection evidence-driven rather than choosing a device first and inventing a requirement around it.

## Inputs from the existing program

The million-trial synthetic null-world audit used reference artifact standard deviations of 2.5 uN thermal, 1.5 uN magnetic, 2.0 uN cable/feedthrough, 1.0 uN vibration/tilt, and 0.8 uN residual measurement noise. The resulting synthetic raw RMS was about 3.757 uN and the corrected residual RMS about 1.543 uN. These values are simulation/reference values only; they are not measurements of a Flux device.

The same audit showed that under that synthetic residual model a 5-sigma gate detected an injected 8 uN signal only about 57.37% of the time, 10 uN about 93.06%, and 15 uN essentially 100%. This does not predict a propulsion effect. It supplies a defensible scale for designing a bench capable of distinguishing benign micro-newton reference injections from an artifact floor similar to the one deliberately modeled in the audit.

## CAL-00 measurement requirement

### Primary force channels

For both the test-article force channel and the independent reaction-force channel:

- **required bipolar measurement range:** at least **-100 uN to +100 uN** (-1.0e-4 N to +1.0e-4 N);
- **preferred usable engineering range:** **-200 uN to +200 uN** if this can be obtained without materially worsening uncertainty or cost;
- **target combined standard uncertainty, u_c:** **<= 1.0 uN** (1.0e-6 N) for a run-window force estimate after calibration and declared corrections;
- **target expanded uncertainty, U:** **<= 2.0 uN** (2.0e-6 N), initially using **coverage factor k = 2**;
- **resolution/display increment:** must be materially finer than the uncertainty target; target **<= 0.2 uN** equivalent force per reported increment. Resolution alone does not establish accuracy;
- **saturation rule:** no decisive run may exceed 80% of the calibrated usable range. A saturated channel invalidates that run for a momentum claim.

The k=2 convention is a reporting/design target, not a guarantee of exactly 95% coverage. The final coverage factor must be revisited from the actual uncertainty model and effective degrees of freedom before a decisive result is reported.

## Why +/-100 uN

This range is intentionally not based on an assumed Flux effect. No propulsion magnitude is being predicted.

It is selected because it provides roughly an order of magnitude of headroom above the 8-15 uN benign injected-force region used in the existing synthetic detection study, while remaining centered on the micro-newton metrology problem that CAL-00 is intended to characterize. The 80% saturation rule leaves a normal decisive-run envelope of approximately +/-80 uN.

If actual baseline characterization shows environmental or fixture artifacts that approach this envelope, CAL-00 must stop and the range requirement must be revised before a decisive run. The range must never be silently expanded after seeing a desired-looking result.

## Benign reference-injection ladder

Before any active experimental article is interpreted, the bench should demonstrate recoverability of known, non-propulsive reference forces across both polarities. Initial target ladder:

- 2 uN (uncertainty-edge characterization; not required to be a high-confidence detection);
- 5 uN;
- 10 uN;
- 20 uN;
- 50 uN;
- repeat 10 uN after the high point to test hysteresis/drift;
- corresponding negative-polarity points where the reference method permits.

The exact traceable injection method must be chosen with the metrology partner/instrument path. CAL-00 does not authorize hazardous actuation.

## Sampling and synchronization

Instrument selection shall support:

- **minimum recorded force sampling:** 100 samples/s per force channel;
- **preferred:** 1,000 samples/s where noise performance and synchronized acquisition remain acceptable;
- simultaneous or deterministically synchronized force and reaction-force acquisition;
- raw unfiltered data retention;
- documented analog/digital filtering and antialias behavior;
- timestamp alignment characterized rather than assumed;
- analysis may downsample only by a frozen, documented method.

The 100 Hz floor is a characterization requirement, not a statement that a physical Flux signal is expected at any frequency. It provides enough temporal information to inspect vibration, switching, settling, cable transients, and reference-injection edges before selecting any lower analysis bandwidth.

## Acceptance tests before an experimental article

The candidate instrumentation path must demonstrate:

1. traceable or otherwise defensibly documented calibration over the relevant range;
2. zero, positive-span, negative-span/polarity, and repeat checks;
3. no saturation through the reference ladder;
4. combined standard uncertainty at or below 1.0 uN for the declared measurand, or an explicit failure to meet CAL-00;
5. expanded uncertainty reported with the coverage factor;
6. force and reaction-force channels independently calibrated;
7. covariance/common-mode calibration terms preserved where applicable;
8. known 5, 10, 20, and 50 uN reference injections recovered within the predeclared uncertainty/tolerance model;
9. baseline drift and hysteresis quantified;
10. synchronized force/reaction acquisition sufficient for uncertainty-aware impulse closure.

## Decision rule

Meeting these specifications makes an instrument path eligible for CAL-00. It does **not** validate Flux propulsion.

If no affordable instrument or partner-lab path can achieve the <=1 uN combined standard-uncertainty target over the required range, Issue #12 must report that fact. The program may then revise the experiment around demonstrated metrology capability, but it may not weaken the uncertainty requirement merely to obtain a desired result.

## External metrology basis

The uncertainty terminology follows NIST TN 1297: combined standard uncertainty is built from individual uncertainty components and covariance where appropriate; expanded uncertainty is U = k u_c; NIST convention commonly uses k=2 while requiring the coverage factor to be reported. NIST also documents SI-traceable force-transducer calibration and published work on micro-newton force realization.

External references:

- NIST Technical Note 1297, Expanded Uncertainty: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-6-expanded-uncertainty
- NIST Technical Note 1297, Reporting Uncertainty: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty
- NIST, Calibration of Force Transducers: https://www.nist.gov/programs-projects/calibration-force-transducers
- Pratt et al., Force Calibration Via Electrostatics (NIST, 2006): https://www.nist.gov/publications/force-calibration-electrostatics

## Issue #11 disposition

This document satisfies the design-definition portion of Issue #11:

- range is stated in SI units;
- combined and expanded uncertainty targets are stated;
- coverage factor is stated and qualified;
- sampling and saturation requirements are stated;
- rationale is tied to benign reference injection and the existing synthetic artifact floor;
- no propulsion-effect magnitude is assumed.

Next dependency: Issue #12, identify purchase/borrow/partner-lab instrumentation paths capable of meeting these requirements at the lowest defensible total cost.
