import unittest

from flux_drive_kernel.system_baseline import (
    Budget,
    G0,
    ThermalBudget,
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

    def test_storage_power_is_part_of_the_ledger(self):
        budget = Budget(
            mass_kg=10,
            input_power_w=80,
            actuator_power_w=60,
            control_power_w=10,
            thermal_power_w=10,
            losses_power_w=5,
            storage_discharge_power_w=5,
        )
        budget.validate()
        self.assertAlmostEqual(budget.source_power_w, 85.0)
        self.assertAlmostEqual(budget.accounted_power_w, 85.0)
        self.assertAlmostEqual(budget.net_storage_power_w, -5.0)

    def test_storage_charging_is_a_power_sink(self):
        budget = Budget(
            mass_kg=10,
            input_power_w=100,
            actuator_power_w=50,
            control_power_w=10,
            thermal_power_w=10,
            losses_power_w=10,
            storage_charge_power_w=20,
        )
        budget.validate()
        self.assertAlmostEqual(budget.net_storage_power_w, 20.0)

    def test_thermal_ledger_closes(self):
        budget = ThermalBudget(
            heat_generated_w=100,
            heat_absorbed_external_w=20,
            heat_rejected_w=90,
            stored_heat_rate_w=30,
        )
        budget.validate()
        self.assertAlmostEqual(budget.thermal_residual_w, 0.0)
        with self.assertRaises(ValueError):
            ThermalBudget(100, 20, 80, 30).validate()

    def test_momentum_residual_is_explicit(self):
        self.assertEqual(momentum_residual(4, -2, -1, -1), 0)


if __name__ == "__main__":
    unittest.main()
