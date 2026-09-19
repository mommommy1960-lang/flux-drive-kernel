import math
import unittest

from flux_drive_kernel.spacetime_consistency import (
    C_M_S,
    alcubierre_top_hat_shape,
    assess_morris_thorne_throat,
    required_average_speed_m_s,
)


class WormholeConsistencyTests(unittest.TestCase):
    def test_flare_out_implies_radial_nec_violation_at_standard_throat(self):
        result = assess_morris_thorne_throat(10.0, 10.0, 0.5, 0.0)
        self.assertTrue(result.geometric_throat_conditions_pass)
        self.assertTrue(result.radial_nec_is_violated)

    def test_nonmatching_shape_radius_fails_throat(self):
        result = assess_morris_thorne_throat(10.0, 9.0, 0.5, 0.0)
        self.assertFalse(result.radius_matches)
        self.assertFalse(result.geometric_throat_conditions_pass)

    def test_no_flare_out_does_not_pass(self):
        result = assess_morris_thorne_throat(10.0, 10.0, 1.0, 0.0)
        self.assertFalse(result.flares_out)
        self.assertAlmostEqual(result.radial_nec_j_m3, 0.0)


class WarpProfileTests(unittest.TestCase):
    def test_top_hat_is_near_one_at_center_and_half_at_boundary(self):
        self.assertGreater(alcubierre_top_hat_shape(0.0, 10.0, 2.0), 0.999)
        self.assertAlmostEqual(alcubierre_top_hat_shape(10.0, 10.0, 2.0), 0.5, places=7)

    def test_profile_decays_outside_bubble(self):
        self.assertLess(alcubierre_top_hat_shape(20.0, 10.0, 2.0), 1e-12)

    def test_required_speed_check_exposes_superluminal_request(self):
        speed = required_average_speed_m_s(4.0e16, 1.0)
        self.assertGreater(speed, C_M_S)
        self.assertTrue(math.isfinite(speed))


class InputValidationTests(unittest.TestCase):
    def test_bad_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            assess_morris_thorne_throat(0.0, 0.0, 0.0, 0.0)
        with self.assertRaises(ValueError):
            alcubierre_top_hat_shape(-1.0, 10.0, 1.0)
        with self.assertRaises(ValueError):
            required_average_speed_m_s(1.0, 0.0)


if __name__ == "__main__":
    unittest.main()
