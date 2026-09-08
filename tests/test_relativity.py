import unittest

from flux_drive_kernel.relativity import (
    hawking_lifetime_s,
    rest_energy_joules,
    schwarzschild_radius_m,
)


class RelativityScaleTests(unittest.TestCase):
    def test_one_solar_mass_radius_is_about_three_kilometres(self):
        self.assertAlmostEqual(schwarzschild_radius_m(1.98847e30) / 1000.0, 2.953, places=2)

    def test_mass_energy_is_mc_squared(self):
        self.assertAlmostEqual(rest_energy_joules(1.0), 8.987551787e16, delta=1e8)

    def test_hawking_lifetime_scales_as_mass_cubed(self):
        self.assertAlmostEqual(hawking_lifetime_s(2.0) / hawking_lifetime_s(1.0), 8.0)

    def test_nonpositive_mass_is_rejected(self):
        with self.assertRaises(ValueError):
            schwarzschild_radius_m(0.0)


if __name__ == "__main__":
    unittest.main()
