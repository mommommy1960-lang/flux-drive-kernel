import math
import unittest

from flux_drive_kernel.spacetime_consistency import (
    C_M_S,
    alcubierre_top_hat_shape,
    assess_morris_thorne_throat,
    required_average_speed_m_s,
    scan_zero_tidal_metric,
    zero_tidal_shape_m,
    zero_tidal_stress_energy,
    zero_tidal_lateral_acceleration_m_s2,
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


class FrozenMetricTensorTests(unittest.TestCase):
    def test_lateral_tidal_acceleration_is_zero_at_rest_and_scales(self):
        self.assertEqual(zero_tidal_lateral_acceleration_m_s2(10.0, 0.0), 0.0)
        low = zero_tidal_lateral_acceleration_m_s2(10.0, 1000.0)
        wide = zero_tidal_lateral_acceleration_m_s2(20.0, 1000.0)
        self.assertAlmostEqual(low / wide, 4.0)

    def test_shape_function_matches_throat_and_decays(self):
        self.assertEqual(zero_tidal_shape_m(10.0, 10.0), 10.0)
        self.assertEqual(zero_tidal_shape_m(20.0, 10.0), 5.0)

    def test_complete_diagonal_has_expected_symmetry_and_signs(self):
        source = zero_tidal_stress_energy(10.0, 10.0)
        diagonal = source.tensor_diagonal_j_m3()
        self.assertEqual(len(diagonal), 4)
        self.assertAlmostEqual(diagonal[2], diagonal[3])
        self.assertLess(source.energy_density_j_m3, 0.0)
        self.assertLess(source.radial_pressure_j_m3, 0.0)
        self.assertGreater(source.tangential_pressure_j_m3, 0.0)
        self.assertLess(source.radial_nec_j_m3, 0.0)
        self.assertAlmostEqual(
            source.tangential_nec_j_m3,
            0.0,
            delta=abs(source.energy_density_j_m3) * 1e-14,
        )

    def test_throat_energy_scale_falls_as_inverse_radius_squared(self):
        small = zero_tidal_stress_energy(10.0, 10.0)
        large = zero_tidal_stress_energy(20.0, 20.0)
        self.assertAlmostEqual(
            abs(small.energy_density_j_m3) / abs(large.energy_density_j_m3),
            4.0,
        )

    def test_radial_decay_is_inverse_fourth_power(self):
        near = zero_tidal_stress_energy(10.0, 10.0)
        far = zero_tidal_stress_energy(20.0, 10.0)
        self.assertAlmostEqual(
            abs(near.energy_density_j_m3) / abs(far.energy_density_j_m3),
            16.0,
        )

    def test_scan_preserves_nec_failure_and_does_not_claim_stability(self):
        points = scan_zero_tidal_metric(10.0, (1.0, 1.5, 2.0, 5.0))
        self.assertEqual(len(points), 4)
        self.assertTrue(all(point.horizon_free_at_point for point in points))
        self.assertTrue(all(point.stress_energy.radial_nec_j_m3 < 0.0 for point in points))
        self.assertTrue(all(not point.stability_assessed for point in points))


if __name__ == "__main__":
    unittest.main()
