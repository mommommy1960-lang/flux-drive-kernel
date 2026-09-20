import unittest

from tsphere.tunneling_scaling import (
    ELECTRON_MASS_KG,
    log10_transmission,
    mass_scaling_ratio,
)


class TunnelingScalingTests(unittest.TestCase):
    def test_probability_gets_smaller_for_larger_mass(self):
        electron = log10_transmission(ELECTRON_MASS_KG, 1.0, 0.01)
        one_gram = log10_transmission(1e-3, 1.0, 0.01)
        self.assertLess(one_gram, electron)

    def test_wider_barrier_makes_exponent_more_negative(self):
        narrow = log10_transmission(ELECTRON_MASS_KG, 1.0, 1e-9)
        wide = log10_transmission(ELECTRON_MASS_KG, 1.0, 2e-9)
        self.assertLess(wide, narrow)

    def test_mass_scaling_is_square_root_in_wkb_exponent(self):
        self.assertAlmostEqual(mass_scaling_ratio(4.0, 1.0), 2.0)


if __name__ == "__main__":
    unittest.main()
