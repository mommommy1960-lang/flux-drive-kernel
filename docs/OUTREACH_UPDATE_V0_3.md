# Non-Confidential External Review Update — v0.3

Use this text only after the v0.3 audit branch is published to the repository's
main branch.

## Short update

The public Aurora / Flux Drive package has completed a new technical audit and
correction pass. The claim boundary is unchanged: no reactionless propulsion,
warp drive, or flight-capable city-ship has been demonstrated.

The public update:

- corrects the software actuator reference law and makes the modeled sign/
  scaling explicit;
- prevents measured force channels from being clipped by simulation limits;
- makes HIL impulse/energy integration explicit and preserves signed electrical
  energy information;
- adds covariance-aware calibration and uncertainty propagation;
- adds an expanded-uncertainty momentum-closure path for measurement-grade data;
- clarifies radiation-momentum reference cases;
- separates single-axis screening from six-axis validation instrumentation;
- defines the experimental momentum/environment boundary more completely;
- strengthens electrical storage and thermal bookkeeping;
- adds a conventional normal-space propulsion reference layer for Aurora,
  independent of the experimental Flux Drive; and
- documents an in-space modular assembly architecture rather than assuming a
  city-sized spacecraft launches intact from Earth.

Please use the latest public main branch for any review. We continue to seek
skeptical technical criticism, falsification criteria, metrology guidance, and
an appropriate supervised physical measurement pathway. Protected unpublished
mechanism or implementation details remain outside this public update.
