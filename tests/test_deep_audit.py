import math
import random
import unittest

from flux_drive_kernel import BenchConfig, FluxDriveBench
from flux_drive_kernel.metrology import calibrate_linear, momentum_closure
from flux_drive_kernel.reference import radiation_momentum_force_N
from flux_drive_kernel.system_baseline import Budget, momentum_residual


class DeepAuditTests(unittest.TestCase):
    def test_hundred_cycle_invariant_sweep(self):
        """Exercise 100 deterministic randomized cases across core invariants.

        This is not physical validation. It is a software-level adversarial
        sweep intended to catch algebra/sign/boundary regressions before bench
        data are interpreted.
        """
        rng = random.Random(20260908)

        for cycle in range(100):
            with self.subTest(cycle=cycle):
                max_current = rng.uniform(0.1, 10.0)
                force_per_amp = rng.uniform(0.01, 5.0)
                command = rng.uniform(-1.0, 1.0)
                dt = rng.uniform(1e-4, 0.25)
                config = BenchConfig(
                    max_current_A=max_current,
                    force_per_amp_N_A=force_per_amp,
                    max_force_N=max(100.0, max_current * force_per_amp * 2.0),
                )
                state = FluxDriveBench(config).step(command, dt_s=dt)
                expected_current = abs(command) * max_current
                expected_force = command * max_current * force_per_amp
                self.assertAlmostEqual(state.current_A, expected_current, places=12)
                self.assertAlmostEqual(state.force_N, expected_force, places=12)
                self.assertGreaterEqual(state.electrical_energy_J, 0.0)
                self.assertTrue(math.isfinite(state.impulse_N_s))

                # Independent momentum channels should close exactly in the
                # synthetic control case.
                impulse = rng.uniform(-1.0, 1.0)
                closure = momentum_closure(
                    impulse,
                    -impulse,
                    force_standard_uncertainty_N_s=0.001,
                    reaction_standard_uncertainty_N_s=0.001,
                )
                self.assertAlmostEqual(closure.value, 0.0, places=15)

                # Calibration algebra remains finite and internally coherent.
                raw = rng.uniform(-100.0, 100.0)
                slope = rng.uniform(0.01, 10.0)
                offset = rng.uniform(-5.0, 5.0)
                calibrated = calibrate_linear(
                    raw,
                    slope=slope,
                    offset=offset,
                    raw_standard_uncertainty=0.01,
                    slope_standard_uncertainty=0.001,
                    offset_standard_uncertainty=0.001,
                )
                self.assertAlmostEqual(calibrated.value, slope * raw + offset, places=12)
                self.assertGreaterEqual(calibrated.standard_uncertainty, 0.0)

                # Power accounting must close only when categories sum to input.
                actuator = rng.uniform(0.0, 50.0)
                control = rng.uniform(0.0, 20.0)
                thermal_management = rng.uniform(0.0, 10.0)
                losses = rng.uniform(0.0, 10.0)
                exported = rng.uniform(0.0, 20.0)
                total = actuator + control + thermal_management + losses + exported
                budget = Budget(
                    mass_kg=rng.uniform(0.1, 1000.0),
                    input_power_w=total,
                    actuator_power_w=actuator,
                    control_power_w=control,
                    thermal_power_w=thermal_management,
                    losses_power_w=losses,
                    exported_power_w=exported,
                )
                budget.validate()
                self.assertAlmostEqual(budget.power_residual_w, 0.0, places=10)

                # Radiation reference never exceeds ideal 2P/c for the admitted
                # momentum-transfer-factor range.
                power = rng.uniform(0.0, 10000.0)
                factor = rng.uniform(0.0, 2.0)
                force = radiation_momentum_force_N(power, momentum_transfer_factor=factor)
                self.assertGreaterEqual(force, 0.0)
                self.assertLessEqual(force, 2.0 * power / 299_792_458.0 + 1e-24)

                self.assertAlmostEqual(momentum_residual(impulse, -impulse, 0.0, 0.0), 0.0)


if __name__ == "__main__":
    unittest.main()
