import unittest

from tsphere.tsphere_sim import Mode, TSphere


class TSphereTests(unittest.TestCase):
    def test_morph_and_handoff_are_logged(self):
        sphere = TSphere()
        sphere.command("roam")
        sphere.command("morph", radius_mm=32)
        sphere.command("handoff", barrier_side="B")
        self.assertEqual(sphere.radius_mm, 32)
        self.assertEqual(sphere.barrier_side, "B")
        self.assertEqual(sphere.mode, Mode.HANDOFF)
        self.assertEqual([row.sequence for row in sphere.telemetry], [1, 2, 3])

    def test_invalid_morph_fails_closed(self):
        sphere = TSphere()
        row = sphere.command("morph", radius_mm=10)
        self.assertTrue(sphere.emergency_stop)
        self.assertEqual(sphere.mode, Mode.SAFE)
        self.assertIn("radius_limit", row.note)

    def test_stop_is_safe_and_reset_is_explicit(self):
        sphere = TSphere()
        sphere.command("roam")
        sphere.command("stop")
        self.assertEqual(sphere.mode, Mode.SAFE)
        sphere.command("reset")
        self.assertFalse(sphere.emergency_stop)


if __name__ == "__main__":
    unittest.main()
