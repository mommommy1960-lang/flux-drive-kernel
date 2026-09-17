import unittest

from tsphere.mechanism_screen import (
    acoustic_pressure_force,
    classify_candidate,
    photon_pressure_force,
    required_force_for_acceleration,
)


class MechanismScreenTests(unittest.TestCase):
    def test_newtonian_force_requirement(self):
        self.assertAlmostEqual(required_force_for_acceleration(0.1, 0.01), 0.001)

    def test_photon_pressure_is_power_limited(self):
        self.assertGreater(photon_pressure_force(10.0, 0.01), 0.0)
        self.assertAlmostEqual(photon_pressure_force(10.0, 0.01, 0.0), 10.0 / 299792458.0)

    def test_acoustic_force_scale_is_pressure_times_area(self):
        self.assertAlmostEqual(acoustic_pressure_force(2.0, 0.01), 0.02)

    def test_measurement_gate_rejects_unresolved_effect(self):
        result = classify_candidate(
            predicted_force_n=0.001,
            measured_force_n=0.001,
            control_residual_n=0.0009,
            uncertainty_n=0.0002,
        )
        self.assertEqual(result, "NOT_RESOLVED")

    def test_measurement_gate_can_report_model_consistency(self):
        result = classify_candidate(
            predicted_force_n=0.001,
            measured_force_n=0.0012,
            control_residual_n=0.0,
            uncertainty_n=0.00005,
        )
        self.assertEqual(result, "CONSISTENT_WITH_MODEL")


if __name__ == "__main__":
    unittest.main()
