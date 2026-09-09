import unittest

from flux_drive_kernel import audit_rows


BASIC_ROWS = [
    {
        "timestamp_s": "0",
        "command": "0",
        "measured_voltage_V": "24",
        "measured_current_A": "0",
        "measured_temperature_C": "22",
        "measured_force_N": "0",
    },
    {
        "timestamp_s": "1",
        "command": "0",
        "measured_voltage_V": "24",
        "measured_current_A": "0",
        "measured_temperature_C": "22",
        "measured_force_N": "1",
    },
]


class HILMeasurementGradeTests(unittest.TestCase):
    def test_measurement_grade_flag_implies_reaction_channel(self):
        report = audit_rows(BASIC_ROWS, require_uncertainty_for_momentum=True)
        self.assertEqual(report.status, "FAIL")
        self.assertIn("reaction_force_N", report.missing_columns)

    def test_uncertainty_inputs_imply_reaction_channel(self):
        report = audit_rows(
            BASIC_ROWS,
            force_impulse_standard_uncertainty_N_s=0.01,
            reaction_impulse_standard_uncertainty_N_s=0.01,
        )
        self.assertEqual(report.status, "FAIL")
        self.assertIn("reaction_force_N", report.missing_columns)

    def test_large_residual_fails_expanded_uncertainty_closure(self):
        rows = [
            {**BASIC_ROWS[0], "reaction_force_N": "0"},
            {**BASIC_ROWS[1], "reaction_force_N": "0"},
        ]
        report = audit_rows(
            rows,
            force_impulse_standard_uncertainty_N_s=0.001,
            reaction_impulse_standard_uncertainty_N_s=0.001,
            coverage_factor=2.0,
            require_uncertainty_for_momentum=True,
        )
        self.assertEqual(report.status, "FAIL")
        self.assertEqual(report.momentum_closure_method, "expanded_uncertainty")
        self.assertEqual(report.momentum_closure_status, "fail")
        self.assertEqual(report.propulsion_verdict, "momentum_not_closed")


if __name__ == "__main__":
    unittest.main()
