import math
import unittest

from flux_drive_kernel.relativistic_mission import (
    C, G0, LIGHT_YEAR_M, MissionInputs, beta_from_gamma,
    find_fastest_passing_profile, gamma_at_distance, simulate_mission,
)


class RelativisticMissionTests(unittest.TestCase):
    def test_alpha_centauri_one_g_peak(self):
        result = simulate_mission(MissionInputs())
        self.assertAlmostEqual(result.metrics["gamma_peak"], 3.21943484244, places=8)
        self.assertAlmostEqual(result.metrics["beta_peak"], 0.95053629023, places=8)

    def test_gamma_365_requires_hundreds_of_light_years_at_one_g(self):
        one_leg_m = C * C * (365.0 - 1.0) / G0
        self.assertGreater(one_leg_m / LIGHT_YEAR_M, 352.0)

    def test_symmetric_trajectory(self):
        total = 4.3 * LIGHT_YEAR_M
        left = gamma_at_distance(0.7 * LIGHT_YEAR_M, total, G0)
        right = gamma_at_distance(total - 0.7 * LIGHT_YEAR_M, total, G0)
        self.assertAlmostEqual(left, right)

    def test_default_scenario_fails_closed_on_energy(self):
        result = simulate_mission(MissionInputs())
        self.assertFalse(result.passed)
        self.assertEqual(result.first_failure, "propulsion_energy")
        self.assertFalse(result.gates["propulsion_energy"])

    def test_invalid_efficiency_is_rejected(self):
        with self.assertRaises(ValueError):
            simulate_mission(MissionInputs(magnetic_deflection_efficiency=1.1))

    def test_dust_larmor_gate_responds_to_charge_to_mass(self):
        low = simulate_mission(MissionInputs(dust_charge_to_mass_C_kg=1.0))
        high = simulate_mission(MissionInputs(dust_charge_to_mass_C_kg=1.0e9))
        self.assertFalse(low.gates["dust_deflection"])
        self.assertTrue(high.gates["dust_deflection"])

    def test_zero_dust_density_remains_finite(self):
        result = simulate_mission(MissionInputs(dust_mass_density_kg_m3=0.0))
        self.assertTrue(all(math.isfinite(v) or math.isnan(v) for v in result.metrics.values()))

    def test_fastest_passing_search_returns_declared_pass(self):
        result = find_fastest_passing_profile(MissionInputs())
        self.assertTrue(result.passed)
        self.assertEqual(result.first_failure, "none")
        self.assertLess(result.metrics["beta_peak"], 0.30)


if __name__ == "__main__":
    unittest.main()
