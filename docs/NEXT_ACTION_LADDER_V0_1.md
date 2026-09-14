# Flux / Aurora Next-Action Ladder v0.1

**Purpose:** turn the instruction “do the next thing, then determine the next thing” into a governed engineering loop rather than an endless simulation loop.

## Recursive rule

At the end of every completed task, ask:

1. What evidence changed?
2. What is the highest-value unresolved blocker?
3. Can it be resolved in software/documentation now?
4. If yes, resolve it and verify the result.
5. If no, record the exact physical, financial, partner, or safety dependency instead of pretending progress occurred.
6. Update the public/current-status record if the change is material.

## Current ladder

### Stage 1 — software falsification framework

- million-trial synthetic audit: COMPLETE
- CI on audit/manual PR: PASS
- audit/manual promoted to `main`: COMPLETE

### Stage 2 — physical-bench documentation

- readiness matrix: DRAFTED
- calibration / uncertainty plan: DRAFTED
- blind-control protocol: DRAFTED
- procurement tiers: DRAFTED
- CAL-00 exit criteria: DRAFTED

### Stage 3 — design freeze inputs

Next unresolved blockers:

1. choose target force range and required expanded uncertainty;
2. select or identify access to calibrated force and reaction-force instrumentation;
3. select synchronized DAQ approach;
4. define mechanical fixture geometry and cable load-path drawing;
5. define benign reference-injection method for CAL-00;
6. identify independent reviewer/operator;
7. obtain quotes / access offers before purchase.

### Stage 4 — CAL-00 build and commissioning

Physical work required. Software cannot honestly complete this stage without actual hardware, calibration records, and raw measurements.

### Stage 5 — blind CAL-00 validation

Physical work required. Pass/fail must be driven by preregistered criteria.

### Stage 6 — first low-energy experimental article run

Blocked until CAL-00 passes. Any residual remains a measured residual until controls and uncertainty justify a higher evidence state.

### Stage 7 — replication and scaling

Blocked until a repeatable candidate anomaly survives Stage 6. Require independent operator replication and a predictive scaling law before discussing useful vehicle integration.

### Stage 8 — Aurora integration decision

Aurora continues conventional subsystem development regardless of Flux outcome. Experimental Flux integration remains optional and gated.

## Stop condition for autonomous software work

Autonomous software/documentation work stops when the next valid evidence requires:

- a physical measurement;
- money or procurement authorization;
- access to a partner lab;
- a qualified safety review;
- a human legal/contract decision;
- or independent replication.

At that point the correct result is a crisp blocker and an executable request, not fabricated completion.
