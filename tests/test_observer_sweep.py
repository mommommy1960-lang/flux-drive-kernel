import unittest

from flux_drive_kernel.observer_sweep import (
    fibonacci_directions,
    observer_energy_condition_margins,
)

MINKOWSKI = [
    [-1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
]


class ObserverSweepTests(unittest.TestCase):
    def test_direction_count_and_unit_norm(self):
        directions = fibonacci_directions(100)
        self.assertEqual(len(directions), 100)
        for direction in directions:
            self.assertAlmostEqual(
                sum(value * value for value in direction),
                1.0,
                places=12,
            )

    def test_vacuum_saturates_all_conditions(self):
        zero = [[0.0] * 4 for _ in range(4)]
        result = observer_energy_condition_margins(MINKOWSKI, zero)
        self.assertEqual(result["null_samples"], 100)
        self.assertEqual(result["timelike_samples"], 1000)
        self.assertTrue(
            all(value == 0.0 for value in result["minima"].values())
        )

    def test_positive_dust_passes(self):
        dust = [
            [10.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ]
        result = observer_energy_condition_margins(MINKOWSKI, dust)
        self.assertTrue(
            all(value >= 0.0 for value in result["minima"].values())
        )

    def test_negative_energy_fails(self):
        bad = [
            [-1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ]
        result = observer_energy_condition_margins(MINKOWSKI, bad)
        self.assertLess(result["minima"]["WEC"], 0.0)
        self.assertLess(result["minima"]["NEC"], 0.0)

    def test_large_pressure_fails_dec(self):
        bad = [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 3.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ]
        result = observer_energy_condition_margins(MINKOWSKI, bad)
        self.assertLess(result["minima"]["DEC"], 0.0)

    def test_dec_margin_has_energy_density_units(self):
        dust = [
            [10.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ]
        result = observer_energy_condition_margins(
            MINKOWSKI,
            dust,
            direction_count=4,
            speed_count=2,
            maximum_speed=0.5,
        )
        self.assertLessEqual(result["minima"]["DEC"], 10.0)
        self.assertGreaterEqual(result["minima"]["DEC"], 0.0)


if __name__ == "__main__":
    unittest.main()
