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
    parser.add_argument("--require-momentum", action="store_true", help="require reaction_force_N and test momentum closure")
    parser.add_argument("--require-environment", action="store_true", help="require environmental channels")
    parser.add_argument("--momentum-tolerance", type=float, default=1e-6, help="legacy/software-check closure tolerance in N*s")
    parser.add_argument("--force-impulse-std-uncertainty", type=float, default=None, help="standard uncertainty of measured force impulse in N*s")
    parser.add_argument("--reaction-impulse-std-uncertainty", type=float, default=None, help="standard uncertainty of reaction impulse in N*s")
    parser.add_argument("--force-reaction-covariance", type=float, default=0.0, help="covariance of force/reaction impulse estimates in (N*s)^2")
    parser.add_argument("--coverage-factor", type=float, default=2.0, help="expanded-uncertainty coverage factor")
    parser.add_argument(
        "--measurement-grade-momentum",
        action="store_true",
        help="fail unless momentum closure is assessed with supplied calibrated uncertainties",
    )
    args = parser.parse_args()

    if args.hil_csv:
        report = audit_csv(
            args.hil_csv,
            require_momentum_channels=args.require_momentum,
            require_environment_channels=args.require_environment,
            momentum_tolerance_N_s=args.momentum_tolerance,
            force_impulse_standard_uncertainty_N_s=args.force_impulse_std_uncertainty,
            reaction_impulse_standard_uncertainty_N_s=args.reaction_impulse_std_uncertainty,
            force_reaction_covariance_N2_s2=args.force_reaction_covariance,
            coverage_factor=args.coverage_factor,
            require_uncertainty_for_momentum=args.measurement_grade_momentum,
        )
        print(report_json(report))
        return 0 if report.status == "PASS" else 1

    if args.seconds <= 0 or args.dt <= 0:
        parser.error("--seconds and --dt must be positive")

    bench = FluxDriveBench()
    steps = max(1, int(args.seconds / args.dt))
    for _ in range(steps):
        bench.step(args.command, args.dt)
        if bench.stopped:
            break
    print(json.dumps(bench.state.as_dict(), indent=2, sort_keys=True))
    return 0 if not bench.stopped else 1


if __name__ == "__main__":
    raise SystemExit(main())
