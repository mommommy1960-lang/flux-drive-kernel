# Ingest and audit report

## Audit date

2026-09-08

## Inputs found

### data/bench/run_template.csv

This file contains column headers only and zero data rows. The strict HIL audit
returned FAIL with all required measurement and environment columns missing
from the materialized input.

### data/literature_reference_experiments.csv

This file contains five literature-summary rows with experiment identifiers,
input power, reported or summarized force, source URLs, result class, and
calibration-status notes. It is not a synchronized bench dataset and cannot be
ingested as a physical T-Sphere run.

The strict HIL audit returned FAIL because it lacks timestamped voltage,
current, temperature, force, reaction-force, vibration, magnetic, acoustic,
pressure, and orientation channels.

## Result

No physical T-Sphere measurements were ingested. No propulsion or wall-transit
verdict can be issued from these files.

This is the correct fail-closed outcome: published summaries may inform a
literature benchmark, but they cannot substitute for raw, synchronized,
calibrated measurements from the project apparatus.

## Required next input

Provide a populated run file based on data/bench/run_template.csv, including
raw synchronized rows and calibration metadata. The repository auditor can
then evaluate data completeness, safety trips, impulse, electrical energy,
reaction/momentum closure, and environmental channels.
