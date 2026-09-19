import unittest

from shifted_shell import direct_g01_shifted_metric
from shifted_shell_adm import adm_shifted_metric


class AdmShiftedShellTests(unittest.TestCase):
    def setUp(self):
        self.r = [0.0, 10.0, 20.0, 30.0]
        self.ones = [1.0] * 4

    def test_zero_shift_matches_static_minkowski(self):
        metric = adm_shifted_metric(
            self.r, self.ones, self.ones,
            inner_radius_m=10.0, outer_radius_m=20.0,
            buffer_m=0.5, beta_warp=0.0,
        )
        self.assertEqual(
            metric((0.0, 5.0, 0.0, 0.0)),
            [[-1.0, 0.0, 0.0, 0.0],
             [0.0, 1.0, 0.0, 0.0],
             [0.0, 0.0, 1.0, 0.0],
             [0.0, 0.0, 0.0, 1.0]],
        )

    def test_flat_interior_uses_full_adm_reconstruction(self):
        metric = adm_shifted_metric(
            self.r, self.ones, self.ones,
            inner_radius_m=10.0, outer_radius_m=20.0,
            buffer_m=0.5, beta_warp=0.02,
        )
        value = metric((0.0, 5.0, 0.0, 0.0))
        self.assertAlmostEqual(value[0][0], -1.0 + 0.02**2)
        self.assertAlmostEqual(value[0][1], -0.02)
        self.assertEqual(value[0][2:], [0.0, 0.0])

    def test_direct_g01_and_adm_are_distinct_metric_conventions(self):
        direct = direct_g01_shifted_metric(
            self.r, self.ones, self.ones,
            inner_radius_m=10.0, outer_radius_m=20.0,
            buffer_m=0.5, beta_warp=0.02,
        )
        adm = adm_shifted_metric(
            self.r, self.ones, self.ones,
            inner_radius_m=10.0, outer_radius_m=20.0,
            buffer_m=0.5, beta_warp=0.02,
        )
        point = (0.0, 5.0, 0.0, 0.0)
        self.assertEqual(direct(point)[0][1], adm(point)[0][1])
        self.assertNotEqual(direct(point)[0][0], adm(point)[0][0])

    def test_curved_off_axis_spatial_metric_couples_shift_components(self):
        radial = [1.0, 2.0, 2.0, 1.0]
        metric = adm_shifted_metric(
            self.r, self.ones, radial,
            inner_radius_m=10.0, outer_radius_m=20.0,
            buffer_m=0.5, beta_warp=0.02,
        )
        value = metric((0.0, 5.0, 5.0, 0.0))
        self.assertNotEqual(value[0][2], 0.0)
        self.assertEqual(value[0][3], 0.0)

    def test_rejects_superluminal_parameter(self):
        with self.assertRaises(ValueError):
            adm_shifted_metric(
                self.r, self.ones, self.ones,
                inner_radius_m=10.0, outer_radius_m=20.0,
                buffer_m=0.5, beta_warp=1.0,
            )


if __name__ == "__main__":
    unittest.main()
