# Blind Control Run Protocol v0.1

**Purpose:** prevent expectation, run labeling, and post-hoc analysis choices from converting ordinary artifacts into a preferred result.

## Core rule

The operator who records the decisive run sequence should not need to know which run labels correspond to active, sham, reversed, or perpendicular conditions during first-pass analysis whenever the physical setup permits blinding.

## Run families

A decisive block should contain a randomized mixture of:

- command-off baselines;
- sham article runs;
- active-article runs;
- 180-degree reversal runs;
- 90-degree perpendicular runs;
- repeat baselines after thermal settling.

The exact sequence is generated and sealed before the block. The analysis code receives neutral run identifiers rather than descriptive labels.

## Pre-registration

Before acquiring the decisive block, freeze:

1. software commit SHA;
2. run-duration and settling rules;
3. primary force/impulse metric;
4. reaction-force closure metric;
5. environmental exclusion thresholds;
6. uncertainty model and coverage factor;
7. primary significance / promotion gate;
8. treatment of missing or saturated channels;
9. orientation prediction, if the hypothesis makes one.

Any later change is exploratory and cannot retroactively convert the original run into a confirmatory result.

## Analysis sequence

1. ingest raw data without condition labels;
2. validate required channels and timestamps;
3. calculate calibrated force, reaction force, impulse, energy, and environmental summaries;
4. apply only frozen exclusions;
5. produce the run-level report;
6. lock the report hash;
7. reveal condition labels;
8. compare active/sham/orientation families;
9. perform secondary exploratory analyses only after the primary result is preserved.

## Failure logic

A candidate effect is downgraded if it:

- appears comparably in sham or command-off runs;
- follows thermal drift rather than preregistered orientation behavior;
- disappears when cable routing or mechanical restraints are controlled;
- lacks reaction/momentum accounting;
- depends on deleting inconvenient runs after unblinding;
- cannot be reproduced in a new independently randomized block.

## Independent repetition

If a residual survives the first block, a second operator should receive the protocol, frozen software version, calibration requirements, and acceptance criteria without being given a target numerical result to reproduce.

## Claim boundary

Passing the blind-control protocol may justify the phrase **candidate anomaly** if all other acceptance criteria are also satisfied. It does not by itself establish a propulsion mechanism.
