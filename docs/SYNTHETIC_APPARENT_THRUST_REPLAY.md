# Synthetic Flux Drive Replay — Apparent Thrust Demonstration

## Purpose

This is a deliberately synthetic educational replay. It demonstrates how a force channel can look like propulsion while the complete momentum balance shows an ordinary artifact or a null result.

It does **not** prove Flux Drive propulsion.

## Common setup

Assume:

- test article mass: (m=1.0\,\mathrm{kg})
- run duration: (t=10\,\mathrm{s})
- apparent device-channel force: (F_d=10\,\mu\mathrm{N})
- device-channel impulse:

[
J_d = F_d t = 10\,\mu\mathrm{N}\times10\,\mathrm{s}
    = 100\,\mu\mathrm{N\,s}
]

If the force were real and external momentum were not otherwise exchanged, the predicted velocity change would be:

[
\Delta v = \frac{J_d}{m}
        = 100\,\mu\mathrm{m/s}
]

That calculation only propagates an assumed measured force. It does not establish the force's cause.

## Case A — conventional propulsion reference

Synthetic channels:

- device force: (+10\,\mu\mathrm{N})
- reaction/exhaust momentum channel: (-10\,\mu\mathrm{N})
- environmental channel: (0\,\mu\mathrm{N})

[
J_\mathrm{total}=100-100+0=0\,\mu\mathrm{N\,s}
]

Interpretation: the software correctly detects ordinary propulsion with momentum carried away by the reaction channel. This is a positive control for the analysis pipeline, not reactionless propulsion.

## Case B — thermal or cable artifact

Synthetic channels:

- device force channel: (+10\,\mu\mathrm{N})
- reaction/exhaust channel: (0\,\mu\mathrm{N})
- environmental/cable/thermal channel: (-10\,\mu\mathrm{N})

[
J_\mathrm{total}=100+0-100=0\,\mu\mathrm{N\,s}
]

Interpretation: the device sensor reports apparent thrust, but the complete accounting attributes the momentum to the environment. The result fails the reactionless-propulsion claim.

## Case C — incomplete measurement

Synthetic channels:

- device force channel: (+10\,\mu\mathrm{N})
- reaction channel: not measured
- environmental channel: not measured

The software may report:

[
J_d=100\,\mu\mathrm{N\,s}
]

But the total momentum is unknown:

[
J_\mathrm{total}=100+J_\mathrm{unknown}
]

Interpretation: this is **inconclusive**, not propulsion.

## Why synthetic data cannot prove Flux Drive

Synthetic data can verify that the code:

- integrates force into impulse;
- propagates uncertainty;
- distinguishes missing from zero channels;
- detects balanced reaction momentum;
- flags environmental covariates;
- refuses to upgrade an incomplete result to propulsion.

Synthetic data cannot supply:

- an unmodeled physical force;
- independent calibration;
- a real reaction boundary;
- a real energy and momentum exchange;
- laboratory replication.

## Required status rule

The replay must assign only one of:

- `verified_conventional_propulsion` — force and reaction channel close as expected;
- `artifact_detected` — apparent signal tracks an environmental or instrumental channel;
- `inconclusive` — required reaction or environmental channel is missing;
- `Flux_observation_pending` — no physical Flux dataset exists yet.

It must never assign `verified_flux_propulsion` to synthetic or borrowed data.

## Result

The closest honest demonstration is:

> We can make the Flux software see an apparent (10\,\mu\mathrm{N}) signal, calculate the corresponding impulse and predicted motion, and then show that the same signal is equally compatible with thermal drift, cable force, or ordinary reaction momentum unless the full calibrated boundary is measured.

That is precisely why CAL-00 exists.
