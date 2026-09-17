# T-Sphere adversarial test report

## Scope

This report covers the hardware-neutral T-Sphere software demonstrator. It does
not claim macroscopic matter phasing, wall transit, propulsion, or a flight
capability. Physical RF, acoustic, and propulsion outputs remain disabled.

## Attack classes exercised

| Class | Cases | Expected safety behavior |
|---|---:|---|
| Missing morph radius | 1 | Emergency stop and `SAFE` |
| Null/non-numeric morph radius | 2 | Emergency stop and `SAFE` |
| NaN/infinite morph radius | 2 | Emergency stop and `SAFE` |
| Missing/null barrier side | 2 | Emergency stop and `SAFE` |
| Unknown command/object payload | 1 | Emergency stop and `SAFE` |
| Commands after emergency stop | 1 | Command denied; state cannot move |
| Boundary/randomized inputs | 1,000 | Radius stays within 30–50 mm; telemetry sequence stays valid |
| Evidence-gate tampering | 1 | `NOT_DEMONSTRATED`; required control is reported missing |

## Local result

- Baseline repository tests: **25 passed**.
- T-Sphere and adversarial tests: **18 passed**.
- Deterministic fuzz workload: **1,000 randomized command cases**.
- Submission safety demo: hardware I/O disabled; physical propulsion unproven.

The test suite is fail-closed: malformed inputs, out-of-range dimensions,
unknown commands, and incomplete evidence do not produce a transit claim.

## Hosted CI result

GitHub Actions created the job but assigned no runner (`runner_id: 0`), executed
zero steps, and produced no job log. A rerun reproduced the same failure. This
is an infrastructure/account-level CI blocker; it is not evidence that the
software tests failed. The branch is intentionally left with this visible
failure until GitHub Actions can assign a runner.

## Interpretation

The software demonstrator is testable and its safety invariants pass locally.
That result does **not** validate comic-book-style phasing or any mechanism for
passing an intact object through a wall. That claim still requires a lawful,
quantitative mechanism and independent physical measurements, neither of which
is present here.
