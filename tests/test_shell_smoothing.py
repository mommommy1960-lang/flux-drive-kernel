import math
import unittest

from flux_drive_kernel.shell_smoothing import (
    PUBLISHED_SMOOTHING_PASSES,
    moving_average,
    pressure_span_for_density_span,
    repeated_moving_average,
    rescale_density_to_mass,
    spherical_shell_mass_kg,
)


class ShellSmoothingTests(unittest.TestCase):
    def test_centered_moving_average_and_short_endpoint_windows(self):
        self.assertEqual(moving_average([0, 0, 3, 0, 0], 3), [0, 1, 1, 1, 0])

    def test_four_published_passes_soften_a_step_without_negative_density(self):
        profile = [0.0] * 20 + [10.0] * 20 + [0.0] * 20
        smoothed = repeated_moving_average(profile, 7)
        self.assertEqual(PUBLISHED_SMOOTHING_PASSES, 4)
        self.assertTrue(all(value >= 0.0 for value in smoothed))
        self.assertLess(max(abs(b - a) for a, b in zip(smoothed, smoothed[1:])), 10.0)
        self.assertGreater(smoothed[19], 0.0)
        self.assertGreater(smoothed[40], 0.0)

    def test_constant_profile_is_invariant(self):
        smoothed = repeated_moving_average([4.0] * 41, 9)
        self.assertTrue(all(abs(value - 4.0) < 1.0e-12 for value in smoothed))

    def test_published_span_ratio_is_represented_but_absolute_span_is_explicit(self):
        pressure_span = pressure_span_for_density_span(43)
        self.assertEqual(pressure_span, 25)
        self.assertAlmostEqual(43 / pressure_span, 1.72)

    def test_spherical_mass_and_explicit_normalization(self):
        radii = [float(r) for r in range(31)]
        density = [1.0 if 10 <= r <= 20 else 0.0 for r in radii]
        target = spherical_shell_mass_kg(radii, density)
        raw_smoothed = repeated_moving_average(density, 5)
        normalized = rescale_density_to_mass(radii, raw_smoothed, target)
        self.assertAlmostEqual(
            spherical_shell_mass_kg(radii, normalized),
            target,
            delta=target * 1.0e-12,
        )
        self.assertTrue(all(value >= 0.0 and math.isfinite(value) for value in normalized))

    def test_invalid_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            moving_average([1.0, 2.0], 2)
        with self.assertRaises(ValueError):
            repeated_moving_average([1.0, 2.0, 3.0], 3, passes=0)
        with self.assertRaises(ValueError):
            pressure_span_for_density_span(10)
        with self.assertRaises(ValueError):
            spherical_shell_mass_kg([0.0, 1.0], [1.0, -1.0])


if __name__ == "__main__":
    unittest.main()
