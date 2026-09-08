import tempfile
import unittest
from pathlib import Path

from flux_drive_kernel.reference import (
    force_to_power_N_W,
    load_reference_csv,
    photon_pressure_force_N,
)


class ReferenceTests(unittest.TestCase):
    def test_photon_pressure_baseline(self):
        self.assertAlmostEqual(photon_pressure_force_N(1.0), 3.33564095e-9, places=16)

    def test_force_to_power_ratio(self):
        self.assertAlmostEqual(force_to_power_N_W(48e-6, 40.0), 1.2e-6)

    def test_reference_csv_is_machine_readable(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "references.csv"
            path.write_text(
                "experiment_id,input_power_W,reported_force_N,source_url,result_class,calibration_status\n"
                "demo,40,0.000048,https://example.com,positive,published_summary_only\n",
                encoding="utf-8",
            )
            observations = load_reference_csv(path)
        self.assertEqual(len(observations), 1)
        self.assertAlmostEqual(observations[0].reported_force_N, 48e-6)


if __name__ == "__main__":
    unittest.main()
