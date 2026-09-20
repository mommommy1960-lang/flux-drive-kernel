import unittest

from flux_drive_kernel.shifted_shell import (
    direct_g01_shifted_metric,
    eulerian_sources_from_einstein,
)
from flux_drive_kernel.tensor4d import einstein_tensor, max_abs


class ShiftedShellTests(unittest.TestCase):
    def setUp(self):
        self.radii = [0.0, 10.0, 20.0, 30.0]
        self.ones = [1.0, 1.0, 1.0, 1.0]

    def test_zero_beta_matches_static_metric(self):
        metric = direct_g01_shifted_metric(
            self.radii,
            self.ones,
            self.ones,
            inner_radius_m=10.0,
            outer_radius_m=20.0,
            buffer_m=0.5,
            beta_warp=0.0,
        )
        self.assertEqual(
            metric((0.0, 15.0, 0.0, 0.0)),
            [
                [-1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ],
        )

    def test_constant_interior_shift_is_flat(self):
        metric = direct_g01_shifted_metric(
            self.radii,
            self.ones,
            self.ones,
            inner_radius_m=10.0,
            outer_radius_m=20.0,
            buffer_m=0.5,
            beta_warp=0.02,
        )
        tensor = einstein_tensor(
            metric,
            (0.0, 5.0, 0.0, 0.0),
            (0.05, 0.05, 0.05, 0.05),
        )
        self.assertLess(max_abs(tensor), 1.0e-12)

    def test_transition_has_symmetric_nonzero_curvature(self):
        metric = direct_g01_shifted_metric(
            self.radii,
            self.ones,
            self.ones,
            inner_radius_m=10.0,
            outer_radius_m=20.0,
            buffer_m=0.5,
            beta_warp=0.02,
        )
        tensor = einstein_tensor(
            metric,
            (0.0, 15.0, 0.0, 0.0),
            (0.05, 0.05, 0.05, 0.05),
        )
        self.assertGreater(max_abs(tensor), 0.0)
        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(tensor[i][j], tensor[j][i], places=12)

    def test_zero_tensor_projects_to_zero_sources(self):
        metric = [
            [-1.0, -0.02, 0.0, 0.0],
            [-0.02, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
        zero = [[0.0] * 4 for _ in range(4)]
        energy, momentum, stress = eulerian_sources_from_einstein(
            metric,
            zero,
        )
        self.assertEqual(energy, 0.0)
        self.assertEqual(momentum, [0.0, 0.0, 0.0])
        self.assertEqual(
            stress,
            [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
        )


if __name__ == "__main__":
    unittest.main()
