"""MAGNUSPHERE coupled relativistic environment-protection feasibility model.

This module is a transparent screening calculation, not a spacecraft design.
It couples a symmetric constant-proper-acceleration trajectory to swept
interstellar gas/dust, pre-ionization, magnetic deflection, residual shielding,
secondary radiation, heat rejection, and ideal kinetic-energy requirements.

Every efficiency and environmental value is an explicit input.  A passing run
means only that the declared algebraic gates did not fail; it is not evidence
that the hardware exists or that omitted physics is harmless.
"""

from dataclasses import dataclass
import math
from typing import Dict, List


C = 299_792_458.0
G0 = 9.80665
LIGHT_YEAR_M = 9.460_730_472_580_8e15
SIGMA = 5.670_374_419e-8
PROTON_MASS_KG = 1.672_621_923_69e-27
ELEMENTARY_CHARGE_C = 1.602_176_634e-19


def _finite_positive(name: str, value: float, *, allow_zero: bool = False) -> None:
    if not math.isfinite(value) or value < 0.0 or (not allow_zero and value == 0.0):
        relation = "non-negative" if allow_zero else "positive"
        raise ValueError(f"{name} must be finite and {relation}")


def _fraction(name: str, value: float) -> None:
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be a finite fraction in [0, 1]")


@dataclass(frozen=True)
class MissionInputs:
    distance_ly: float = 4.3
    proper_acceleration_m_s2: float = G0
    maximum_crew_acceleration_m_s2: float = G0
    spacecraft_mass_kg: float = 1_000_000.0
    frontal_area_m2: float = 100.0
    crew_and_shelter_mass_kg: float = 100_000.0
    radiator_area_m2: float = 10_000.0
    radiator_temperature_K: float = 1_200.0
    radiator_emissivity: float = 0.9
    background_temperature_K: float = 3.0
    gas_number_density_m3: float = 100_000.0
    dust_mass_density_kg_m3: float = 1.0e-23
    natural_ionized_fraction: float = 0.1
    gas_preionization_efficiency: float = 0.99
    dust_preionization_efficiency: float = 0.90
    magnetic_deflection_efficiency: float = 0.99
    magnetic_field_T: float = 5.0
    magnetic_standoff_m: float = 1_000.0
    dust_charge_to_mass_C_kg: float = 1.0e5
    gas_ionization_energy_J_kg: float = 1.31e9
    dust_ionization_energy_J_kg: float = 1.0e9
    preionizer_available_power_W: float = 1.0e12
    impact_energy_to_heat_fraction: float = 0.25
    secondary_radiation_fraction: float = 0.10
    shelter_radiation_transmission: float = 1.0e-6
    crew_dose_limit_Gy: float = 1.0
    shield_mass_kg: float = 1_000_000.0
    shield_effective_removal_energy_J_kg: float = 1.0e8
    maximum_shield_loss_fraction: float = 0.25
    propulsion_efficiency: float = 0.5
    regenerative_braking_fraction: float = 0.0
    available_mission_energy_J: float = 1.0e22
    maximum_earth_time_years: float = 100.0
    steps: int = 2_000

    def validate(self) -> None:
        positive = (
            "distance_ly", "proper_acceleration_m_s2",
            "maximum_crew_acceleration_m_s2", "spacecraft_mass_kg",
            "frontal_area_m2", "crew_and_shelter_mass_kg",
            "radiator_area_m2", "radiator_temperature_K", "radiator_emissivity",
            "gas_number_density_m3", "magnetic_field_T", "magnetic_standoff_m",
            "dust_charge_to_mass_C_kg", "gas_ionization_energy_J_kg",
            "dust_ionization_energy_J_kg", "preionizer_available_power_W",
            "crew_dose_limit_Gy", "shield_mass_kg",
            "shield_effective_removal_energy_J_kg", "propulsion_efficiency",
            "available_mission_energy_J",
            "maximum_earth_time_years",
        )
        for name in positive:
            _finite_positive(name, float(getattr(self, name)))
        for name in ("background_temperature_K", "dust_mass_density_kg_m3"):
            _finite_positive(name, float(getattr(self, name)), allow_zero=True)
        for name in (
            "natural_ionized_fraction", "gas_preionization_efficiency",
            "dust_preionization_efficiency", "magnetic_deflection_efficiency",
            "impact_energy_to_heat_fraction", "secondary_radiation_fraction",
            "shelter_radiation_transmission", "maximum_shield_loss_fraction",
            "regenerative_braking_fraction",
        ):
            _fraction(name, float(getattr(self, name)))
        if self.radiator_temperature_K <= self.background_temperature_K:
            raise ValueError("radiator temperature must exceed background temperature")
        if not isinstance(self.steps, int) or self.steps < 10:
            raise ValueError("steps must be an integer >= 10")


@dataclass(frozen=True)
class MissionResult:
    passed: bool
    first_failure: str
    gates: Dict[str, bool]
    metrics: Dict[str, float]
    limitations: List[str]


def gamma_at_distance(distance_from_start_m: float, total_distance_m: float,
                      proper_acceleration_m_s2: float) -> float:
    """Lorentz factor for accelerate-halfway/decelerate-halfway flight."""
    leg_distance = min(distance_from_start_m, total_distance_m - distance_from_start_m)
    return 1.0 + proper_acceleration_m_s2 * max(0.0, leg_distance) / (C * C)


def beta_from_gamma(gamma: float) -> float:
    return math.sqrt(max(0.0, 1.0 - 1.0 / (gamma * gamma)))


def larmor_radius_m(gamma: float, beta: float, magnetic_field_T: float,
                    charge_to_mass_C_kg: float) -> float:
    return gamma * beta * C / (charge_to_mass_C_kg * magnetic_field_T)


def simulate_mission(inputs: MissionInputs) -> MissionResult:
    inputs.validate()
    distance_m = inputs.distance_ly * LIGHT_YEAR_M
    dx = distance_m / inputs.steps
    midpoint_m = 0.5 * distance_m
    gamma_peak = 1.0 + inputs.proper_acceleration_m_s2 * midpoint_m / (C * C)
    beta_peak = beta_from_gamma(gamma_peak)
    rapidity_peak = math.acosh(gamma_peak)
    proper_time_s = 2.0 * C / inputs.proper_acceleration_m_s2 * rapidity_peak
    earth_time_s = 2.0 * C / inputs.proper_acceleration_m_s2 * math.sinh(rapidity_peak)

    radiator_capacity_W = (
        inputs.radiator_emissivity * SIGMA * inputs.radiator_area_m2
        * (inputs.radiator_temperature_K ** 4 - inputs.background_temperature_K ** 4)
    )
    gas_deflected_fraction = min(
        1.0,
        (inputs.natural_ionized_fraction
         + (1.0 - inputs.natural_ionized_fraction)
         * inputs.gas_preionization_efficiency)
        * inputs.magnetic_deflection_efficiency,
    )
    dust_deflected_fraction = min(
        1.0,
        inputs.dust_preionization_efficiency * inputs.magnetic_deflection_efficiency,
    )

    total_residual_impact_J = 0.0
    total_secondary_radiation_J = 0.0
    shield_loss_kg = 0.0
    peak_heat_W = 0.0
    peak_preionizer_W = 0.0
    first_heat_failure_ly = math.nan
    first_ionizer_failure_ly = math.nan

    for index in range(inputs.steps):
        x = (index + 0.5) * dx
        gamma = gamma_at_distance(x, distance_m, inputs.proper_acceleration_m_s2)
        beta = beta_from_gamma(gamma)
        if beta == 0.0:
            continue
        proper_dt_s = dx / (gamma * beta * C)
        swept_gas_kg = inputs.gas_number_density_m3 * PROTON_MASS_KG * inputs.frontal_area_m2 * dx
        swept_dust_kg = inputs.dust_mass_density_kg_m3 * inputs.frontal_area_m2 * dx
        gas_impact_J = (gamma - 1.0) * swept_gas_kg * C * C
        dust_impact_J = (gamma - 1.0) * swept_dust_kg * C * C
        residual_J = (
            gas_impact_J * (1.0 - gas_deflected_fraction)
            + dust_impact_J * (1.0 - dust_deflected_fraction)
        )
        ionizer_J = (
            swept_gas_kg * (1.0 - inputs.natural_ionized_fraction)
            * inputs.gas_preionization_efficiency * inputs.gas_ionization_energy_J_kg
            + swept_dust_kg * inputs.dust_preionization_efficiency
            * inputs.dust_ionization_energy_J_kg
        )
        ionizer_W = ionizer_J / proper_dt_s
        heat_W = residual_J * inputs.impact_energy_to_heat_fraction / proper_dt_s
        peak_preionizer_W = max(peak_preionizer_W, ionizer_W)
        peak_heat_W = max(peak_heat_W, heat_W)
        if ionizer_W > inputs.preionizer_available_power_W and math.isnan(first_ionizer_failure_ly):
            first_ionizer_failure_ly = x / LIGHT_YEAR_M
        if heat_W > radiator_capacity_W and math.isnan(first_heat_failure_ly):
            first_heat_failure_ly = x / LIGHT_YEAR_M
        total_residual_impact_J += residual_J
        total_secondary_radiation_J += residual_J * inputs.secondary_radiation_fraction
        shield_loss_kg += residual_J / inputs.shield_effective_removal_energy_J_kg

    crew_dose_Gy = (
        total_secondary_radiation_J * inputs.shelter_radiation_transmission
        / inputs.crew_and_shelter_mass_kg
    )
    proton_qm = ELEMENTARY_CHARGE_C / PROTON_MASS_KG
    proton_larmor_m = larmor_radius_m(gamma_peak, beta_peak, inputs.magnetic_field_T, proton_qm)
    dust_larmor_m = larmor_radius_m(
        gamma_peak, beta_peak, inputs.magnetic_field_T,
        inputs.dust_charge_to_mass_C_kg,
    )
    kinetic_peak_J = (gamma_peak - 1.0) * inputs.spacecraft_mass_kg * C * C
    propulsion_energy_J = kinetic_peak_J / inputs.propulsion_efficiency
    braking_energy_J = kinetic_peak_J * (
        1.0 - inputs.regenerative_braking_fraction
    ) / inputs.propulsion_efficiency
    total_mission_energy_J = propulsion_energy_J + braking_energy_J

    gates = {
        "crew_acceleration": inputs.proper_acceleration_m_s2 <= inputs.maximum_crew_acceleration_m_s2,
        "propulsion_energy": total_mission_energy_J <= inputs.available_mission_energy_J,
        "preionizer_power": peak_preionizer_W <= inputs.preionizer_available_power_W,
        "proton_deflection": proton_larmor_m <= inputs.magnetic_standoff_m,
        "dust_deflection": dust_larmor_m <= inputs.magnetic_standoff_m,
        "heat_rejection": peak_heat_W <= radiator_capacity_W,
        "shield_survival": shield_loss_kg <= inputs.shield_mass_kg * inputs.maximum_shield_loss_fraction,
        "crew_radiation": crew_dose_Gy <= inputs.crew_dose_limit_Gy,
        "mission_duration": earth_time_s <= inputs.maximum_earth_time_years * 365.25 * 86400.0,
    }
    order = (
        "crew_acceleration", "propulsion_energy", "preionizer_power",
        "proton_deflection", "dust_deflection", "heat_rejection",
        "shield_survival", "crew_radiation", "mission_duration",
    )
    first_failure = next((name for name in order if not gates[name]), "none")
    metrics = {
        "proper_acceleration_m_s2": inputs.proper_acceleration_m_s2,
        "proper_acceleration_g": inputs.proper_acceleration_m_s2 / G0,
        "gamma_peak": gamma_peak,
        "beta_peak": beta_peak,
        "proper_time_s": proper_time_s,
        "earth_time_s": earth_time_s,
        "earth_time_years": earth_time_s / (365.25 * 86400.0),
        "proper_time_years": proper_time_s / (365.25 * 86400.0),
        "kinetic_energy_peak_J": kinetic_peak_J,
        "total_mission_energy_J": total_mission_energy_J,
        "radiator_capacity_W": radiator_capacity_W,
        "peak_deposited_heat_W": peak_heat_W,
        "peak_preionizer_power_W": peak_preionizer_W,
        "total_residual_impact_energy_J": total_residual_impact_J,
        "shield_loss_kg": shield_loss_kg,
        "crew_dose_Gy": crew_dose_Gy,
        "proton_larmor_radius_m": proton_larmor_m,
        "dust_larmor_radius_m": dust_larmor_m,
        "first_heat_failure_ly": first_heat_failure_ly,
        "first_ionizer_failure_ly": first_ionizer_failure_ly,
    }
    limitations = [
        "One-dimensional mean-density screen; no stochastic rare-grain distribution.",
        "Deflection efficiencies are declared inputs, not demonstrated hardware performance.",
        "Shield removal energy is an effective parameter, not hydrodynamic impact simulation.",
        "Radiation uses a scalar energy-to-dose screen and omits particle transport/biology.",
        "Propulsion energy is an ideal lower-bound budget and does not select an engine.",
        "A software pass is not physical validation or evidence of a flight-capable system.",
    ]
    return MissionResult(all(gates.values()), first_failure, gates, metrics, limitations)


def find_fastest_passing_profile(inputs: MissionInputs, iterations: int = 60) -> MissionResult:
    """Return the highest-acceleration profile that passes all declared gates.

    The search changes only proper acceleration between a small positive value
    and the declared crew limit. It is a requirements trade, not an optimizer
    over vehicle design or a proof that the assumed hardware can be built.
    """
    inputs.validate()
    floor = inputs.maximum_crew_acceleration_m_s2 * 1.0e-9
    ceiling = inputs.maximum_crew_acceleration_m_s2
    samples = [floor * (ceiling / floor) ** (i / 299.0) for i in range(300)]
    sampled = [simulate_mission(MissionInputs(**{
        **inputs.__dict__, "proper_acceleration_m_s2": acceleration,
    })) for acceleration in samples]
    passing = [(i, result) for i, result in enumerate(sampled) if result.passed]
    if not passing:
        return sampled[0]
    index, best = passing[-1]
    if index == len(samples) - 1:
        return best
    low = samples[index]
    high = samples[index + 1]
    for _ in range(iterations):
        middle = 0.5 * (low + high)
        candidate = simulate_mission(MissionInputs(**{
            **inputs.__dict__, "proper_acceleration_m_s2": middle,
        }))
        if candidate.passed:
            low = middle
            best = candidate
        else:
            high = middle
    return best
