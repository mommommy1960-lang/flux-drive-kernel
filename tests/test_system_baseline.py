import unittest

from flux_drive_kernel.system_baseline import (
    Budget,
    G0,
    momentum_residual,
    required_vertical_lift,
)


class SystemBaselineTests(unittest.TestCase):
    def test_vertical_lift_equation(self):
        self.assertAlmostEqual(required_vertical_lift(10.0), 10.0 * G0)

    def test_power_ledger_must_close(self):
        budget = Budget(10, 100, 60, 10, 20, 10)
        budget.validate()
        self.assertAlmostEqual(budget.accounted_power_w, 100.0)
        self.assertAlmostEqual(budget.power_residual_w, 0.0)
        with self.assertRaises(ValueError):
            Budget(10, 100, 60, 10, 20, 9).validate()

    def test_momentum_residual_is_explicit(self):
        self.assertEqual(momentum_residual(4, -2, -1, -1), 0)


if __name__ == "__main__":
    unittest.main()
