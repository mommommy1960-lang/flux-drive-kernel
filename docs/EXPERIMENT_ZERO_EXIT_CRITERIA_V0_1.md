# Experiment Zero Exit Criteria v0.1

**Experiment:** CAL-00 / Experiment Zero  
**Objective:** prove the bench can detect injected known signals, reject ordinary artifacts, preserve raw data, and correctly refuse unsupported propulsion claims.

## Experiment Zero is not a propulsion test

CAL-00 exists to validate the measurement system itself. A bench that cannot reliably recognize known injected signals and reject sham artifacts is not ready to test an unknown mechanism.

## Required demonstrations

### 1. Null stability

Run repeated command-off baselines across the intended run duration. Quantify drift, RMS noise, autocorrelation, and environmental correlations.

### 2. Known mechanical injection

Apply a benign, independently quantified reference perturbation within the force channel's calibrated range. The analysis must recover the injected magnitude and sign within the preregistered uncertainty.

### 3. Sign reversal

Repeat the reference perturbation with reversed sign/polarity where physically appropriate. The analysis must reverse correspondingly rather than producing a one-sided offset.

### 4. Reaction closure

Known mechanical injections must appear consistently in the force and reaction-force accounting within expanded uncertainty.

### 5. Sham rejection

Run matched sham configurations. The system must not promote ordinary thermal, cable, vibration, acoustic, or magnetic artifacts into a candidate anomaly.

### 6. Blind-label recovery

Analyze a randomized block before condition labels are revealed. The primary classification and measurements are frozen before unblinding.

### 7. Data integrity

Every run must preserve raw channels, calibration metadata, software commit, configuration hash, operator/time metadata, and any exclusion reason.

## Pass definition

Experiment Zero passes only if:

- required channels are present and synchronized;
- known injections are recovered within the preregistered uncertainty;
- sign/orientation behavior matches the injected reference;
- momentum/reaction accounting closes within expanded uncertainty;
- sham/control runs remain below the candidate-anomaly promotion gate;
- rerunning the analysis from raw data reproduces the preserved report;
- no manual editing of raw measurements is required.

## Fail definition

Any failure is preserved as evidence and returns the program to calibration, fixture, environmental-control, or software-debugging work. The threshold is not relaxed after seeing the result.

## Exit from CAL-00

Only after CAL-00 passes may the program schedule a low-energy experimental article run under the frozen blind-control and uncertainty protocols.

Even after CAL-00 passes, `physical_propulsion_proven=false` remains mandatory. CAL-00 validates the measurement process, not the Flux hypothesis.
