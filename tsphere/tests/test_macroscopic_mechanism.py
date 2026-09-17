import unittest

from tsphere.macroscopic_mechanism import (
    ThrustInputs,
    thrust_newton,
    validate_thrust_measurement,
)


class MacroscopicMechanismTests(unittest.TestCase):
    def test_control_volume_thrust_equation(self):
        result = thrust_newton(
            ThrustInputs(
                exit_mass_flow_kg_s=0.01,
                exit_velocity_m_s=100.0,
                exit_pressure_pa=110_000.0,
                ambient_pressure_pa=100_000.0,
                exit_area_m2=0.001,
            )
        )
        self.assertAlmostEqual(result, 11.0)

    def test_validation_requires_repetition_and_replication(self):
        result = validate_thrust_measurement(
            predicted_n=11.0,
            measured_n=11.0,
            uncertainty_n=0.01,
            repeated_trials=2,
            independent_replications=0,
        )
        self.assertEqual(result["status"], "NOT_VALIDATED")

    def test_validation_can_pass_only_for_defined_test(self):
        result = validate_thrust_measurement(
            predicted_n=11.0,
            measured_n=11.005,
            uncertainty_n=0.01,
            repeated_trials=3,
            independent_replications=1,
        )
        self.assertEqual(result["status"], "VALIDATED_FOR_DEFINED_TEST")

    def test_large_residual_fails(self):
        result = validate_thrust_measurement(
            predicted_n=11.0,
            measured_n=2.0,
            uncertainty_n=0.01,
            repeated_trials=10,
            independent_replications=2,
        )
        self.assertEqual(result["status"], "NOT_VALIDATED")


if __name__ == "__main__":
    unittest.main()
