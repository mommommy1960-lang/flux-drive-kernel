import math
import unittest

from flux_drive_kernel.shell_cartesian import static_cartesian_metric
from flux_drive_kernel.shell_metric import (
    C,
    G,
    cumulative_mass_kg,
    integrate_tov_pressure_pa,
    radial_metric,
    static_einstein_sources_pa,
)
from flux_drive_kernel.tensor4d import einstein_tensor, max_abs


class ShellCartesianTests(unittest.TestCase):
    def test_flat_profiles_return_minkowski(self):
        metric = static_cartesian_metric(
            [0.0, 10.0, 20.0],
            [1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
        )
        tensor = einstein_tensor(
            metric,
            (0.0, 5.0, 2.0, 1.0),
            (0.05, 0.05, 0.05, 0.05),
        )
        self.assertEqual(max_abs(tensor), 0.0)

    def test_cartesian_engine_matches_spherical_sources(self):
        dr = 0.025
        radii = [i * dr for i in range(1601)]
        volume = 4.0 * math.pi * (20.0**3 - 10.0**3) / 3.0
        density0 = 4.49e27 / volume
        density = [
            density0 if 10.0 <= radius <= 20.0 else 0.0
            for radius in radii
        ]
        mass = cumulative_mass_kg(radii, density)
        pressure = integrate_tov_pressure_pa(
            radii,
            density,
            mass,
            cavity_radius_m=10.0,
        )
        e2a, e2b = radial_metric(radii, pressure, mass)
        eps_s, pr_s, pt_s = static_einstein_sources_pa(radii, e2a, e2b)
        metric = static_cartesian_metric(radii, e2a, e2b)
        radius = 15.0
        index = round(radius / dr)
        tensor = einstein_tensor(
            metric,
            (0.0, radius, 0.0, 0.0),
            (0.05, 0.05, 0.05, 0.05),
        )
        scale = C**4 / (8.0 * math.pi * G)
        eps_c = scale * tensor[0][0] / e2a[index]
        pr_c = scale * tensor[1][1] / e2b[index]
        pt_c = scale * tensor[2][2]
        self.assertLess(abs(eps_c - eps_s[index]) / abs(eps_s[index]), 0.02)
        self.assertLess(abs(pr_c - pr_s[index]) / abs(pr_s[index]), 0.02)
        self.assertLess(
            abs(pt_c - pt_s[index])
            / max(abs(pt_s[index]), abs(pr_s[index])),
            0.05,
        )
        curvature_scale = 1.0 / 25.0**2
        residuals = []
        for step in (0.2, 0.1, 0.05):
            exterior = einstein_tensor(
                metric,
                (0.0, 25.0, 0.0, 0.0),
                (step, step, step, step),
            )
            residuals.append(max_abs(exterior) / curvature_scale)
        self.assertGreater(residuals[0] / residuals[1], 3.5)
        self.assertGreater(residuals[1] / residuals[2], 3.5)
        self.assertLess(residuals[2], 2.0e-5)


if __name__ == "__main__":
    unittest.main()
