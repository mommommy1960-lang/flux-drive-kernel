import unittest

from flux_drive_kernel import BenchConfig, FluxDriveBench


class BenchTests(unittest.TestCase):
    def test_deterministic_step_produces_auditable_state(self):
        bench = FluxDriveBench()
        state = bench.step(0.25, dt_s=0.1)
        self.assertAlmostEqual(state.time_s, 0.1)
        self.assertGreater(state.force_N, 0.0)
        self.assertGreater(state.impulse_N_s, 0.0)
        self.assertGreater(state.electrical_energy_J, 0.0)
        self.assertIsNone(state.safety_trip)

    def test_command_is_limited(self):
        bench = FluxDriveBench(BenchConfig(max_command=0.5))
        state = bench.step(2.0, dt_s=0.1)
        self.assertAlmostEqual(state.command, 0.5)

    def test_simulated_force_is_linear_in_command(self):
        config = BenchConfig(max_current_A=4.0, force_per_amp_N_A=2.0)
        positive = FluxDriveBench(config).step(0.25, dt_s=0.1)
        negative = FluxDriveBench(config).step(-0.25, dt_s=0.1)
        self.assertAlmostEqual(positive.current_A, 1.0)
        self.assertAlmostEqual(positive.force_N, 2.0)
        self.assertAlmostEqual(negative.current_A, 1.0)
        self.assertAlmostEqual(negative.force_N, -2.0)

    def test_zero_command_has_zero_simulated_force_even_with_measured_current(self):
        bench = FluxDriveBench()
        state = bench.step(0.0, dt_s=0.1, measured_current_A=0.2)
        self.assertEqual(state.force_N, 0.0)

    def test_zero_dt_records_initial_sample_without_integrating(self):
        bench = FluxDriveBench()
        state = bench.step(
            0.0,
            dt_s=0.0,
            measured_force_N=20.0,
            measured_current_A=0.2,
            measured_voltage_V=24.0,
        )
        self.assertEqual(state.force_N, 20.0)
        self.assertEqual(state.time_s, 0.0)
        self.assertEqual(state.impulse_N_s, 0.0)
        self.assertEqual(state.electrical_energy_J, 0.0)

    def test_measured_force_is_not_clipped_to_simulation_limit(self):
        bench = FluxDriveBench(BenchConfig(max_force_N=1.0))
        state = bench.step(0.0, dt_s=0.1, measured_force_N=20.0, measured_current_A=0.2)
        self.assertEqual(state.force_N, 20.0)
        self.assertEqual(state.impulse_N_s, 2.0)

    def test_over_current_fails_closed(self):
        bench = FluxDriveBench(BenchConfig(max_current_A=1.0))
        state = bench.step(0.2, dt_s=0.1, measured_current_A=1.01)
        self.assertEqual(state.safety_trip, "over_current")
        self.assertEqual(state.force_N, 0.0)

    def test_over_temperature_fails_closed(self):
        config = BenchConfig(max_temperature_C=30.0)
        bench = FluxDriveBench(config)
        state = bench.step(0.1, dt_s=0.1, measured_temperature_C=30.0)
        self.assertEqual(state.safety_trip, "over_temperature")

    def test_measured_force_is_not_relabelled(self):
        bench = FluxDriveBench()
        state = bench.step(0.0, dt_s=0.1, measured_force_N=2.0, measured_current_A=0.2)
        self.assertAlmostEqual(state.force_N, 2.0)
        self.assertAlmostEqual(state.impulse_N_s, 0.2)

    def test_nonfinite_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            BenchConfig(mass_kg=float("nan"))
        with self.assertRaises(ValueError):
            FluxDriveBench().step(float("nan"), dt_s=0.1)
        with self.assertRaises(ValueError):
            FluxDriveBench().step(0.0, dt_s=float("inf"))

    def test_emergency_stop_is_latching(self):
        bench = FluxDriveBench()
        bench.emergency_stop("operator_stop")
        state = bench.step(1.0, dt_s=0.1)
        self.assertEqual(state.safety_trip, "operator_stop")
        self.assertEqual(state.force_N, 0.0)


if __name__ == "__main__":
    unittest.main()
