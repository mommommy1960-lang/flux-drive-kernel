import math
import unittest

from flux_drive_kernel.positive_energy_shell import ConstantDensityShell


class ConstantDensityShellTests(unittest.TestCase):
    def setUp(self):
        self.shell = ConstantDensityShell(10.0, 20.0, 1.0e12)

    def test_density_matches_mass_over_shell_volume(self):
        expected_volume = 4.0 * math.pi * (20.0**3 - 10.0**3) / 3.0
        self.assertAlmostEqual(self.shell.volume_m3, expected_volume)
        self.assertAlmostEqual(self.shell.density_kg_m3, 1.0e12 / expected_volume)

    def test_density_is_zero_in_cavity_and_exterior(self):
        self.assertEqual(self.shell.density_at_radius_kg_m3(5.0), 0.0)
        self.assertEqual(self.shell.density_at_radius_kg_m3(25.0), 0.0)
        self.assertGreater(self.shell.density_at_radius_kg_m3(15.0), 0.0)

    def test_enclosed_mass_matches_piecewise_equation(self):
        self.assertEqual(self.shell.enclosed_mass_kg(5.0), 0.0)
        self.assertEqual(self.shell.enclosed_mass_kg(10.0), 0.0)
        expected = 1.0e12 * (15.0**3 - 10.0**3) / (20.0**3 - 10.0**3)
        self.assertAlmostEqual(self.shell.enclosed_mass_kg(15.0), expected)
        self.assertEqual(self.shell.enclosed_mass_kg(20.0), 1.0e12)
        self.assertEqual(self.shell.enclosed_mass_kg(100.0), 1.0e12)

    def test_mass_profile_is_monotonic_and_recovers_adm_mass(self):
        masses = [self.shell.enclosed_mass_kg(r) for r in (0, 10, 12, 15, 18, 20, 100)]
        self.assertEqual(masses, sorted(masses))
        self.assertEqual(self.shell.exterior_adm_mass_kg, 1.0e12)

    def test_regular_cavity_and_horizon_check(self):
        self.assertEqual(self.shell.compactness(0.0), 0.0)
        self.assertTrue(all(self.shell.horizon_free_at(r) for r in (0, 10, 15, 20, 100)))

    def test_bad_geometry_and_values_are_rejected(self):
        with self.assertRaises(ValueError):
            ConstantDensityShell(20.0, 10.0, 1.0)
        with self.assertRaises(ValueError):
            ConstantDensityShell(10.0, 20.0, -1.0)
        with self.assertRaises(ValueError):
            self.shell.enclosed_mass_kg(-1.0)


if __name__ == "__main__":
    unittest.main()
