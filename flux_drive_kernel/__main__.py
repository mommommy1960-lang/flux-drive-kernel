"""Command-line entry point for the safe actuator-bench simulation."""

from __future__ import annotations

import argparse
import json

from .bench import FluxDriveBench
from .hil import audit_csv, report_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=1.0)
    parser.add_argument("--dt", type=float, default=0.01)
    parser.add_argument("--command", type=float, default=0.25)
    parser.add_argument("--hil-csv", help="audit a measured-channel CSV instead of running simulation")
    args = parser.parse_args()
    if args.hil_csv:
        print(report_json(audit_csv(args.hil_csv)))
        return 0
    if args.seconds <= 0 or args.dt <= 0:
        parser.error("--seconds and --dt must be positive")

    bench = FluxDriveBench()
    steps = max(1, int(args.seconds / args.dt))
    for _ in range(steps):
        bench.step(args.command, args.dt)
        if bench.stopped:
            break
    print(json.dumps(bench.state.as_dict(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
