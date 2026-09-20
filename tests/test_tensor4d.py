import math
import unittest

from flux_drive_kernel.tensor4d import (
    christoffel,
    einstein_tensor,
    inverse4,
    max_abs,
)


def minkowski(_point):
    return [
        [-1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def isotropic_schwarzschild(point):
    _, x, y, z = point
    radius = math.sqrt(x * x + y * y + z * z)
    ratio = 1.0 / radius
    lapse2 = ((1.0 - ratio) / (1.0 + ratio)) ** 2
    spatial = (1.0 + ratio) ** 4
    return [
        [-lapse2, 0.0, 0.0, 0.0],
        [0.0, spatial, 0.0, 0.0],
        [0.0, 0.0, spatial, 0.0],
        [0.0, 0.0, 0.0, spatial],
    ]


class Tensor4DTests(unittest.TestCase):
    def test_inverse(self):
        inverse = inverse4(
            [[-2, 0, 0, 0], [0, 3, 0, 0], [0, 0, 4, 0], [0, 0, 0, 5]]
        )
        self.assertEqual(inverse[0][0], -0.5)
        self.assertAlmostEqual(inverse[3][3], 0.2)

    def test_minkowski_is_exactly_flat(self):
        point = (0.0, 2.0, 3.0, 4.0)
        steps = (0.01, 0.01, 0.01, 0.01)
        self.assertEqual(max_abs(christoffel(minkowski, point, steps)), 0.0)
        self.assertEqual(max_abs(einstein_tensor(minkowski, point, steps)), 0.0)

    def test_isotropic_schwarzschild_vacuum_is_second_order_convergent(self):
        point = (0.0, 20.0, 3.0, 4.0)
        errors = []
        for step in (0.08, 0.04, 0.02):
            tensor = einstein_tensor(
                isotropic_schwarzschild,
                point,
                (step, step, step, step),
            )
            errors.append(max_abs(tensor))
        self.assertGreater(errors[0] / errors[1], 3.5)
        self.assertLess(errors[0] / errors[1], 4.5)
        self.assertGreater(errors[1] / errors[2], 3.5)
        self.assertLess(errors[1] / errors[2], 4.5)
        self.assertLess(errors[2], 1.0e-7)

    def test_singular_metric_rejected(self):
        with self.assertRaises(ValueError):
            inverse4([[0.0] * 4 for _ in range(4)])


if __name__ == "__main__":
    unittest.main()
