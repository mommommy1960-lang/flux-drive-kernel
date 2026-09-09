import tempfile
import unittest
from pathlib import Path

from flux_drive_kernel import audit_csv, audit_rows


class HILTests(unittest.TestCase):
    def test_measured_rows_produce_audit_report(self):
        rows = [
            {"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0.1", "measured_temperature_C": "22", "measured_force_N": "0.0"},
            {"timestamp_s": "0.1", "command": "0.2", "measured_voltage_V": "24", "measured_current_A": "0.5", "measured_temperature_C": "22.1", "measured_force_N": "0.3"},
        ]
        report = audit_rows(rows)
        self.assertEqual(report.status, "PASS")
        self.assertAlmostEqual(report.measured_impulse_N_s, 0.015)
        self.assertAlmostEqual(report.measured_electrical_energy_J, 0.72)
        self.assertAlmostEqual(report.measured_absolute_electrical_energy_J, 0.72)
        self.assertEqual(report.integration_method, "trapezoidal")
        self.assertEqual(report.momentum_closure_status, "not_assessed")

    def test_first_sample_does_not_invent_time_or_impulse(self):
        rows = [
            {"timestamp_s": "10", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0.1", "measured_temperature_C": "22", "measured_force_N": "5.0"},
        ]
        report = audit_rows(rows)
        self.assertEqual(report.status, "PASS")
        self.assertEqual(report.duration_s, 0.0)
        self.assertEqual(report.measured_impulse_N_s, 0.0)
        self.assertEqual(report.measured_electrical_energy_J, 0.0)

    def test_signed_and_absolute_electrical_energy_are_distinguished(self):
        rows = [
            {"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "-0.1", "measured_temperature_C": "22", "measured_force_N": "0"},
            {"timestamp_s": "1", "command": "0", "measured_voltage_V": "24", "measured_current_A": "-0.1", "measured_temperature_C": "22", "measured_force_N": "0"},
        ]
        report = audit_rows(rows)
        self.assertAlmostEqual(report.measured_electrical_energy_J, -2.4)
        self.assertAlmostEqual(report.measured_absolute_electrical_energy_J, 2.4)

    def test_measured_force_is_not_clipped_to_simulation_limit(self):
        rows = [
            {"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0.1", "measured_temperature_C": "22", "measured_force_N": "20"},
            {"timestamp_s": "0.1", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0.1", "measured_temperature_C": "22", "measured_force_N": "20"},
        ]
        report = audit_rows(rows)
        self.assertEqual(report.status, "PASS")
        self.assertEqual(report.peak_abs_force_N, 20.0)
        self.assertAlmostEqual(report.measured_impulse_N_s, 2.0)

    def test_missing_columns_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text("timestamp_s,command\n0,0\n", encoding="utf-8")
            report = audit_csv(path)
        self.assertEqual(report.status, "FAIL")
        self.assertIn("measured_force_N", report.missing_columns)

    def test_nonmonotonic_timestamps_fail(self):
        rows = [
            {"timestamp_s": "1", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "0"},
            {"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "0"},
        ]
        report = audit_rows(rows)
        self.assertEqual(report.status, "FAIL")
        self.assertTrue(report.validation_errors)

    def test_complete_channels_close_momentum(self):
        rows = [
            {"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "0", "reaction_force_N": "0"},
            {"timestamp_s": "0.1", "command": "0.2", "measured_voltage_V": "24", "measured_current_A": "0.5", "measured_temperature_C": "22.1", "measured_force_N": "0.3", "reaction_force_N": "-0.3"},
        ]
        report = audit_rows(rows, require_momentum_channels=True)
        self.assertEqual(report.status, "PASS")
        self.assertEqual(report.momentum_closure_status, "pass")
        self.assertAlmostEqual(report.momentum_residual_N_s, 0.0)
        self.assertEqual(report.momentum_closure_method, "fixed_tolerance_software_check")

    def test_uncertainty_aware_momentum_closure(self):
        rows = [
            {"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "0", "reaction_force_N": "0"},
            {"timestamp_s": "1", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "1", "reaction_force_N": "-0.8"},
        ]
        report = audit_rows(
            rows,
            require_momentum_channels=True,
            force_impulse_standard_uncertainty_N_s=0.1,
            reaction_impulse_standard_uncertainty_N_s=0.1,
            coverage_factor=2.0,
            require_uncertainty_for_momentum=True,
        )
        self.assertEqual(report.status, "PASS")
        self.assertEqual(report.momentum_closure_status, "pass")
        self.assertEqual(report.momentum_closure_method, "expanded_uncertainty")
        self.assertIsNotNone(report.momentum_expanded_uncertainty_N_s)
        self.assertEqual(report.momentum_coverage_factor, 2.0)

    def test_measurement_grade_mode_requires_uncertainty(self):
        rows = [
            {"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "0", "reaction_force_N": "0"},
            {"timestamp_s": "1", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "0", "reaction_force_N": "0"},
        ]
        report = audit_rows(
            rows,
            require_momentum_channels=True,
            require_uncertainty_for_momentum=True,
        )
        self.assertEqual(report.status, "FAIL")
        self.assertEqual(report.propulsion_verdict, "uncertainty_required")

    def test_strict_mode_fails_when_momentum_does_not_close(self):
        rows = [
            {"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "0", "reaction_force_N": "0"},
            {"timestamp_s": "1", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "1", "reaction_force_N": "0"},
        ]
        report = audit_rows(rows, require_momentum_channels=True, momentum_tolerance_N_s=1e-9)
        self.assertEqual(report.status, "FAIL")
        self.assertEqual(report.momentum_closure_status, "fail")
        self.assertEqual(report.propulsion_verdict, "momentum_not_closed")

    def test_strict_mode_rejects_missing_reaction_channel(self):
        rows = [{"timestamp_s": "0", "command": "0", "measured_voltage_V": "24", "measured_current_A": "0", "measured_temperature_C": "22", "measured_force_N": "0"}]
        report = audit_rows(rows, require_momentum_channels=True)
        self.assertEqual(report.status, "FAIL")
        self.assertIn("reaction_force_N", report.missing_columns)

    def test_invalid_momentum_tolerance_is_rejected(self):
        with self.assertRaises(ValueError):
            audit_rows([], momentum_tolerance_N_s=-1.0)

    def test_uncertainty_inputs_must_be_paired(self):
        with self.assertRaises(ValueError):
            audit_rows([], force_impulse_standard_uncertainty_N_s=0.1)


if __name__ == "__main__":
    unittest.main()
