# Flux Drive — Conventional Propulsion Demonstrator Path V0.1

## Status

This is an added, practical path. Earlier Flux Drive and Aurora documents remain unchanged.

This path does not claim reactionless propulsion, warp travel, or a new physical effect. It defines the closest buildable real-world propulsion demonstrator that preserves the project's measurement and accountability goals.

## Demonstrator concept

Build a low-power electric/plasma propulsion test article that:

1. consumes measured electrical power;
2. accelerates a declared working mass or produces a declared photon output;
3. measures force and reaction channels;
4. records thermal, vibration, magnetic, and electrical behavior;
5. passes conventional momentum and energy accounting before any advanced interpretation.

The first safe software-and-bench stage uses a low-voltage actuator or air-moving/plasma-free surrogate. Any ionization, vacuum, high voltage, or plasma stage requires qualified engineering review, enclosure, interlocks, and a written hazard analysis.

## Two honest propulsion branches

### Branch A — electric propulsion with working mass

The device accelerates a declared propellant or working fluid. The governing relations are:

[
F=\dot{m}v_e
]

[
I_{sp}=\frac{v_e}{g_0}
]

[
P=\frac{1}{2}\dot{m}v_e^2
]

The force is real because momentum leaves the device in the exhaust or accelerated working mass.

### Branch B — photon thrust

The device emits electromagnetic radiation. For ideal directed radiation:

[
F=\frac{P}{c}
]

This is physically legitimate but extremely small. A 100 W perfectly collimated photon beam produces approximately:

[
F\approx 0.33\,\mu\mathrm{N}
]

The measurement system must therefore have substantially smaller uncertainty than the predicted signal and must account for thermal radiation and cable forces.

## Software sandbox model

The sandbox must include separate models for:

- conventional exhaust momentum;
- photon momentum;
- external electromagnetic coupling;
- thermal drift;
- vibration and cable artifacts;
- zero-thrust sham;
- incomplete reaction-channel data;
- hypothetical unexplained residual.

The hypothetical residual is a diagnostic placeholder only. It must never be presented as a discovered force.

## Test sequence

1. Run the empty-frame baseline.
2. Run the powered-off article.
3. Run a sham electrical load matched for heat and current.
4. Run the conventional actuator with a declared working mass.
5. Reverse orientation and cable routing.
6. Run the photon or advanced article only after safety and calibration gates pass.
7. Compare device, reaction, environmental, and energy channels.
8. Preserve every raw file and failed result.

## Pass/fail rules

### Conventional propulsion pass

- measured force agrees with predicted working-mass or photon momentum within uncertainty;
- energy input and thermal output are recorded;
- controls identify no unmodeled environmental force;
- independent reviewer can reproduce the analysis.

### Reactionless hypothesis status

The reactionless hypothesis remains **unverified** unless a residual exceeds the combined uncertainty after all ordinary momentum channels are measured and independently replicated.

## What this accomplishes

This path can produce a real, measurable propulsion demonstrator using established physics while keeping the more ambitious Flux hypothesis alive as a separate, falsification-first research question.

It gives reviewers something concrete:

- a defined force source;
- equations with units;
- measurable inputs and outputs;
- a safe staged build path;
- explicit stop conditions;
- no inflated claim.

## Current result

On paper, the conventional branch is physically coherent. In the sandbox, it can be simulated and tested against known momentum and energy relations. A physical device has not yet been built or validated. The previous Flux Drive records remain the historical and speculative research layer; this document is the new practical engineering layer.
