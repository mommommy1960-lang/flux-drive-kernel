# Physical test next step

The software is ready for real data, but no claim can be made until the bench
is physically assembled and calibrated.

## Immediate sequence

1. Obtain the low-energy components listed in
   LOW_ENERGY_MEASUREMENT_BENCH_BUILD.md.
2. Mount the load cell in a rigid frame and keep all cables mechanically slack
   and strain-relieved away from the force axis.
3. Calibrate zero, span, polarity, drift, and repeatability with known masses.
4. Connect the current-limited supply and INA219 only after a qualified person
   checks polarity and the physical disconnect.
5. Record command-off, sham-load, reversed-orientation, and powered-off runs.
6. Save raw measurements using data/bench/run_template.csv.
7. Audit the file with:

   python -m flux_drive_kernel --hil-csv data/bench/run001.csv --require-momentum --require-environment

8. Stop if the data shows unexplained force, missing channels, overheating,
   telemetry loss, or a non-closing reaction/momentum balance.

## Boundary

This first bench can measure ordinary force and artifacts. It cannot prove
intact-wall phasing. A physical test article must remain low energy and under
qualified human supervision; no high-voltage, high-power RF, acoustic,
vacuum, or propulsion stage is authorized by this document.
