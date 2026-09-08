"""Safe, measurement-first Flux Drive actuator-bench kernel."""

from .bench import BenchConfig, BenchState, FluxDriveBench
from .hil import HILReport, audit_csv, audit_rows, report_json
from .relativity import hawking_lifetime_s, rest_energy_joules, schwarzschild_radius_m

__all__ = ["BenchConfig", "BenchState", "FluxDriveBench", "HILReport", "audit_csv", "audit_rows", "report_json", "hawking_lifetime_s", "rest_energy_joules", "schwarzschild_radius_m"]

__version__ = "0.1.0"
