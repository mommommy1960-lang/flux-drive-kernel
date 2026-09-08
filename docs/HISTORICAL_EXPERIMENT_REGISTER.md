# Historical Experiment Register

The machine-readable file `data/literature_reference_experiments.csv` records
published summary values from earlier closed-cavity propulsion tests. These are
reference observations, not newly calibrated measurements. The source papers do
not provide a common raw-data/calibration package that can be re-certified by
this repository.

## Imported observations

- NASA Eagleworks reported approximately `1.2 mN/kW` across 40–80 W in a vacuum
  campaign. The register represents those summary values as 48, 72, and 96 µN.
- The later TU Dresden work describes orientation-dependent micro-Newton-scale
  signals, cable/magnetic interactions, thermal drift, and tests that removed
  the anomalous result. Its final conclusion limited anomalous thrust below the
  classical photon-pressure force for the tested power.

The cyber bench can compare these observations, calculate force-to-power
ratios, and use them to define replication targets. It cannot call a published
summary “calibrated raw data” without the original instrument files,
calibration certificates, uncertainty budget, and chain of custody.

Primary sources:

- [NASA Eagleworks closed RF cavity report](https://ntrs.nasa.gov/api/citations/20170000277/downloads/20170000277.pdf)
- [Tajmar, Neunzig and Weikert high-accuracy study](https://link.springer.com/article/10.1007/s12567-021-00385-1)
- [NIST force-transducer calibration service](https://www.nist.gov/programs-projects/calibration-force-transducers)
