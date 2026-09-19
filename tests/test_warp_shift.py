import unittest

from flux_drive_kernel.warp_shift import (
    compact_shift_shape,
    radial_causal_margin,
    shifted_g01,
)


class WarpShiftTests(unittest.TestCase):
    def test_shape_is_bounded_monotonic_and_centered(self):
        radii = [10.0 + i * 0.1 for i in range(101)]
        shape = [compact_shift_shape(r, 10.0, 20.0, 0.5) for r in radii]
        self.assertTrue(all(0.0 <= value <= 1.0 for value in shape))
        self.assertTrue(all(right <= left for left, right in zip(shape, shape[1:])))
        self.assertAlmostEqual(
            compact_shift_shape(15.0, 10.0, 20.0, 0.5),
            0.5,
        )

    def test_published_shift_value_is_applied(self):
        self.assertAlmostEqual(shifted_g01(0.0, 1.0), -0.02)
        self.assertEqual(shifted_g01(0.0, 0.0), 0.0)

    def test_radial_causal_margin(self):
        self.assertGreater(radial_causal_margin(0.5, 2.0, 0.02), 0.0)
        self.assertLess(radial_causal_margin(0.5, 2.0, 0.6), 0.0)

    def test_invalid_buffer_and_superluminal_input_are_rejected(self):
        with self.assertRaises(ValueError):
            compact_shift_shape(15.0, 10.0, 20.0, 5.0)
        with self.assertRaises(ValueError):
            shifted_g01(0.0, 1.0, 1.0)


if __name__ == "__main__":
    unittest.main()
