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
        self.assertAlmostEqual(report.measured_impulse_N_s, 0.03)
        self.assertAlmostEqual(report.measured_electrical_energy_J, 1.2)
        self.assertEqual(report.momentum_closure_status, "not_assessed")

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


if __name__ == "__main__":
    unittest.main()
