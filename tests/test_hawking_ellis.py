import unittest

import numpy as np

from flux_drive_kernel.hawking_ellis import classify, type_I_energy_conditions


class HawkingEllisTests(unittest.TestCase):
    def test_anisotropic_diagonal_source_is_type_i(self):
        result = classify(np.diag([5.0, 1.0, 2.0, 3.0]))
        self.assertEqual(result.kind, "Type I")
        self.assertEqual(
            (result.negative_directions, result.null_directions, result.positive_directions),
            (1, 0, 3),
        )

    def test_fully_degenerate_cosmological_constant_is_type_i(self):
        # T_ab = -Lambda eta_ab makes T^a_b = -Lambda delta^a_b.
        result = classify(np.diag([2.0, -2.0, -2.0, -2.0]))
        self.assertEqual(result.kind, "Type I")

    def test_complex_pair_is_type_iv(self):
        result = classify(
            np.array(
                [
                    [0.0, 1.0, 0.0, 0.0],
                    [1.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0],
                ]
            )
        )
        self.assertEqual(result.kind, "Type IV")

    def test_null_dust_is_not_mislabeled_type_i(self):
        null_covector = np.array([1.0, 1.0, 0.0, 0.0])
        result = classify(np.outer(null_covector, null_covector))
        self.assertEqual(result.kind, "Non-Type-I / degenerate real spectrum")

    def test_frozen_morris_thorne_regression(self):
        radius = 10.0
        rho = 0.0
        radial = -1.0 / (8.0 * np.pi * radius**2)
        tangential = 1.0 / (16.0 * np.pi * radius**2)
        result = classify(np.diag([rho, radial, tangential, tangential]))
        conditions = type_I_energy_conditions(
            rho, np.array([radial, tangential, tangential])
        )
        self.assertEqual(result.kind, "Type I")
        self.assertFalse(conditions["NEC"])
        self.assertFalse(conditions["WEC"])
        self.assertFalse(conditions["SEC"])
        self.assertFalse(conditions["DEC"])

    def test_small_declared_discretization_asymmetry_is_recorded(self):
        tensor = np.diag([5.0e12, 1.0e12, 2.0e12, 3.0e12])
        tensor[0, 1] = 1.0e6
        tensor[1, 0] = 0.0
        result = classify(tensor, symmetry_rtol=1.0e-6)
        self.assertEqual(result.kind, "Type I")
        self.assertGreater(result.relative_antisymmetry, 0.0)

    def test_material_asymmetry_is_rejected(self):
        tensor = np.eye(4)
        tensor[0, 1] = 0.1
        with self.assertRaises(ValueError):
            classify(tensor)

    def test_bad_inputs_and_energy_condition_values_are_rejected(self):
        with self.assertRaises(ValueError):
            classify(np.eye(3))
        with self.assertRaises(ValueError):
            classify(np.full((4, 4), np.nan))
        with self.assertRaises(ValueError):
            type_I_energy_conditions(0.0, np.array([1.0, 2.0]))


if __name__ == "__main__":
    unittest.main()
