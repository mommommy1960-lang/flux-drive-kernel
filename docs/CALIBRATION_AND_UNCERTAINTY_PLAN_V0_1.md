# Calibration and Uncertainty Plan v0.1

**Scope:** low-energy Flux measurement bench only.

## Objective

Ensure every claimed residual is traceable to calibrated measurements and a declared uncertainty model before any interpretation is attempted.

## Channel classes

### Force and reaction force

For each channel preserve:

- instrument make/model and serial or asset identifier;
- nominal range and resolution;
- calibration date/source;
- zero drift and repeatability;
- span/polarity verification method;
- sampling rate and antialias filtering;
- mounting geometry;
- standard uncertainty contribution.

The force and reaction-force channels must be independently calibrated. A shared calibration error must be represented as covariance rather than silently treated as independent noise.

### Voltage and current

Measure at the test-article terminals, not merely at the supply display. Record instrument uncertainty, input impedance/shunt characteristics, synchronization error, and any filtering.

### Temperature

At minimum monitor the active article, mount, cable entry/feedthrough region, and ambient environment. Record sensor placement because thermal gradients can generate mechanical drift even when average temperature appears stable.

### Environmental channels

Document measurement uncertainty and sampling for vibration/acceleration, magnetic field, acoustic pressure, ambient pressure, and orientation/tilt.

## Uncertainty model

For each derived result preserve:

1. raw channel uncertainties;
2. calibration uncertainty;
3. repeatability / short-term noise;
4. drift across the run window;
5. timestamp alignment uncertainty;
6. geometry / lever-arm uncertainty where applicable;
7. covariance between channels;
8. numerical integration uncertainty;
9. declared coverage factor for expanded uncertainty.

## Momentum-closure quantity

For a run window compute measured test-article impulse and independently measured reaction impulse with their covariance-aware uncertainties. Report the residual impulse and its expanded uncertainty. A residual inside the expanded uncertainty is closure, not propulsion.

## Calibration sequence

Before each decisive run block:

1. warm instruments to their documented stable state;
2. capture a zero baseline;
3. perform positive and negative span/polarity checks using a traceable reference method appropriate to the instrument;
4. repeat the zero check;
5. record drift and hysteresis;
6. verify time synchronization using a common event visible to all relevant channels;
7. freeze calibration metadata with the run configuration hash.

After the run block, repeat zero/span checks to detect calibration drift.

## Acceptance criteria

A decisive run is invalid if:

- required calibration metadata are missing;
- a channel saturates;
- a zero/span check fails its predeclared tolerance;
- timestamp alignment is outside its predeclared tolerance;
- the reaction channel is unavailable for a momentum claim;
- exclusions are invented after seeing the result without being separately labeled exploratory.

## Reporting rule

Always report effect estimate **and** uncertainty. Never report only a significance label, pass/fail word, or plotted excursion without the underlying units and uncertainty budget.
