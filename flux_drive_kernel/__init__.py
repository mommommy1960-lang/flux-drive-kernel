"""Safe, measurement-first Flux Drive and Aurora reference kernel."""

from .bench import BenchConfig, BenchState, FluxDriveBench
from .hil import HILReport, audit_csv, audit_rows, report_json
from .relativity import hawking_lifetime_s, rest_energy_joules, schwarzschild_radius_m
from .metrology import CalibratedMeasurement, calibrate_linear, is_consistent_with_zero, momentum_closure
from .reference import (
    ReferenceObservation,
    force_to_power_N_W,
    load_reference_csv,
    photon_pressure_force_N,
    radiation_momentum_force_N,
)
from .system_baseline import Budget, ThermalBudget
from .conventional_propulsion import (
    G0_M_S2,
    acceleration_from_thrust_m_s2,
    exhaust_velocity_m_s,
    ideal_electric_thrust_from_power_N,
    ideal_rocket_delta_v_m_s,
    mass_flow_for_thrust_kg_s,
    mass_ratio_for_delta_v,
    propellant_fraction_for_delta_v,
    specific_impulse_s,
    thrust_from_mass_flow_N,
)

__all__ = [
    "BenchConfig",
    "BenchState",
    "FluxDriveBench",
    "HILReport",
    "audit_csv",
    "audit_rows",
    "report_json",
    "hawking_lifetime_s",
    "rest_energy_joules",
    "schwarzschild_radius_m",
    "CalibratedMeasurement",
    "calibrate_linear",
    "is_consistent_with_zero",
    "momentum_closure",
    "ReferenceObservation",
    "force_to_power_N_W",
    "load_reference_csv",
    "photon_pressure_force_N",
    "radiation_momentum_force_N",
    "Budget",
    "ThermalBudget",
    "G0_M_S2",
    "acceleration_from_thrust_m_s2",
    "exhaust_velocity_m_s",
    "ideal_electric_thrust_from_power_N",
    "ideal_rocket_delta_v_m_s",
    "mass_flow_for_thrust_kg_s",
    "mass_ratio_for_delta_v",
    "propellant_fraction_for_delta_v",
    "specific_impulse_s",
    "thrust_from_mass_flow_N",
]

__version__ = "0.3.0"
