import math
import unittest

from flux_drive_kernel.shell_metric import (
    C,
    G,
    compactness,
    cumulative_mass_kg,
    diagonal_energy_conditions,
    energy_condition_margins_pa,
    integrate_tov_pressure_pa,
    radial_metric,
    static_einstein_sources_pa,
    tangential_pressure_pa,
    tov_gradient_pa_m,
)
from flux_drive_kernel.shell_smoothing import (
    repeated_moving_average,
    rescale_density_to_mass,
)


class ShellMetricTests(unittest.TestCase):
    def test_tov_newtonian_limit_and_units(self):
        radius, density, mass = 1.0e8, 2.0, 3.0e10
        exact = tov_gradient_pa_m(radius, density, 0.0, mass)
        newtonian = -G * density * mass / radius**2
        self.assertAlmostEqual(exact / newtonian, 1.0, places=12)

    def test_published_baseline_outer_compactness_is_horizon_free(self):
        q = compactness(4.49e27, 20.0)
        self.assertGreater(q, 0.33)
        self.assertLess(q, 0.34)

    def test_mass_pressure_and_metric_pipeline(self):
        dr = 0.05
        radii = [i * dr for i in range(801)]
        volume = 4.0 * math.pi * (20.0**3 - 10.0**3) / 3.0
        density0 = 4.49e27 / volume
        density = [density0 if 10.0 <= r <= 20.0 else 0.0 for r in radii]
        mass = cumulative_mass_kg(radii, density)
        pressure = integrate_tov_pressure_pa(radii, density, mass, cavity_radius_m=10.0)
        e2a, e2b = radial_metric(radii, pressure, mass)
        self.assertTrue(all(p == 0.0 for r, p in zip(radii, pressure) if r < 10.0))
        self.assertGreater(max(pressure), 0.0)
        self.assertTrue(all(math.isfinite(x) and x > 0.0 for x in e2a + e2b))
        expected_outer = 1.0 - 2.0 * G * mass[-1] / (C * C * radii[-1])
        self.assertAlmostEqual(e2a[-1], expected_outer, places=14)
        self.assertAlmostEqual(e2b[-1], 1.0 / expected_outer, places=14)
        pt = tangential_pressure_pa(radii, density, pressure, mass)
        self.assertEqual(len(pt), len(radii))
        self.assertTrue(all(math.isfinite(x) for x in pt))
        eps_g, pr_g, pt_g = static_einstein_sources_pa(radii, e2a, e2b)
        interior = [i for i, radius in enumerate(radii) if 11.0 <= radius <= 19.0]
        rho_error = max(
            abs(eps_g[i] - density[i] * C * C) / (density[i] * C * C)
            for i in interior
        )
        pressure_scale = max(pressure[i] for i in interior)
        pr_error = max(
            abs(pr_g[i] - pressure[i]) / pressure_scale for i in interior
        )
        self.assertLess(rho_error, 5.0e-4)
        self.assertLess(pr_error, 5.0e-3)
        self.assertTrue(all(math.isfinite(pt_g[i]) for i in interior))

    def _smoothed_trial(self, dr, density_span, pressure_span):
        target_mass = 4.49e27
        radii = [i * dr for i in range(round(40.0 / dr) + 1)]
        volume = 4.0 * math.pi * (20.0**3 - 10.0**3) / 3.0
        density0 = target_mass / volume
        raw_density = [density0 if 10.0 <= r <= 20.0 else 0.0 for r in radii]
        raw_mass = cumulative_mass_kg(radii, raw_density)
        raw_pressure = integrate_tov_pressure_pa(
            radii, raw_density, raw_mass, cavity_radius_m=10.0
        )
        density = rescale_density_to_mass(
            radii,
            repeated_moving_average(raw_density, density_span),
            target_mass,
        )
        pressure = repeated_moving_average(raw_pressure, pressure_span)
        mass = cumulative_mass_kg(radii, density)
        radial_metric(radii, pressure, mass)
        tangential = tangential_pressure_pa(radii, density, pressure, mass)
        active = [i for i, value in enumerate(density) if value > max(density) * 1.0e-12]
        margins = {
            name: min(
                energy_condition_margins_pa(
                    density[i] * C * C, pressure[i], tangential[i]
                )[name]
                for i in active
            )
            for name in ("NEC", "WEC", "DEC", "SEC")
        }
        return mass, margins

    def test_declared_trial_has_positive_static_diagonal_margins(self):
        mass, margins = self._smoothed_trial(0.05, 85, 49)
        self.assertAlmostEqual(mass[-1] / 4.49e27, 1.0, places=12)
        self.assertTrue(all(value >= 0.0 for value in margins.values()))

    def test_falsification_gate_rejects_narrow_filter_on_fine_grid(self):
        _, margins = self._smoothed_trial(0.025, 21, 13)
        self.assertLess(margins["DEC"], 0.0)

    def test_horizon_is_rejected(self):
        radii = [0.0, 1.0, 2.0]
        mass = [0.0, C * C / G, C * C / G]
        with self.assertRaises(ValueError):
            radial_metric(radii, [0.0, 0.0, 0.0], mass)

    def test_diagonal_energy_conditions(self):
        self.assertTrue(all(diagonal_energy_conditions(10.0, 1.0, 2.0).values()))
        failed = diagonal_energy_conditions(1.0, -2.0, 0.0)
        self.assertFalse(failed["NEC"])
        self.assertFalse(failed["WEC"])


if __name__ == "__main__":
    unittest.main()
