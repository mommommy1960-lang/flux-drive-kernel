import unittest

from flux_drive_kernel.metrology import (
    calibrate_linear,
    is_consistent_with_zero,
    momentum_closure,
)


class MetrologyTests(unittest.TestCase):
    def test_linear_calibration_propagates_uncertainty(self):
        measurement = calibrate_linear(
            2.0, slope=3.0, offset=1.0,
            raw_standard_uncertainty=0.1,
            slope_standard_uncertainty=0.2,
            offset_standard_uncertainty=0.05,
        )
        self.assertAlmostEqual(measurement.value, 7.0)
        self.assertGreater(measurement.expanded_uncertainty, 0.0)

    def test_positive_covariance_increases_linear_uncertainty(self):
        independent = calibrate_linear(
            2.0, slope=3.0,
            raw_standard_uncertainty=0.1,
            slope_standard_uncertainty=0.2,
        )
        correlated = calibrate_linear(
            2.0, slope=3.0,
            raw_standard_uncertainty=0.1,
            slope_standard_uncertainty=0.2,
            covariance_raw_slope=0.01,
        )
        self.assertGreater(correlated.standard_uncertainty, independent.standard_uncertainty)

    def test_impossible_covariance_is_rejected(self):
        with self.assertRaises(ValueError):
            calibrate_linear(
                1.0,
                slope=2.0,
                raw_standard_uncertainty=0.1,
                slope_standard_uncertainty=0.1,
                covariance_raw_slope=0.02,
            )

    def test_closed_momentum_is_consistent_with_zero(self):
        measurement = momentum_closure(
            0.03, -0.03,
            force_standard_uncertainty_N_s=0.001,
            reaction_standard_uncertainty_N_s=0.001,
        )
        self.assertTrue(is_consistent_with_zero(measurement))

    def test_momentum_covariance_is_supported(self):
        independent = momentum_closure(
            0.03, -0.03,
            force_standard_uncertainty_N_s=0.001,
            reaction_standard_uncertainty_N_s=0.001,
        )
        anticorrelated = momentum_closure(
            0.03, -0.03,
            force_standard_uncertainty_N_s=0.001,
            reaction_standard_uncertainty_N_s=0.001,
            force_reaction_covariance_N2_s2=-5e-7,
        )
        self.assertLess(anticorrelated.standard_uncertainty, independent.standard_uncertainty)

    def test_nonclosed_momentum_fails_zero_interval(self):
        measurement = momentum_closure(
            0.03, -0.01,
            force_standard_uncertainty_N_s=0.001,
            reaction_standard_uncertainty_N_s=0.001,
        )
        self.assertFalse(is_consistent_with_zero(measurement))

    def test_invalid_uncertainty_is_rejected(self):
        with self.assertRaises(ValueError):
            calibrate_linear(1.0, slope=1.0, raw_standard_uncertainty=-1.0)


if __name__ == "__main__":
    unittest.main()
