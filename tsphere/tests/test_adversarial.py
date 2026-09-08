import math
import random
import unittest

from tsphere.barrier_transit_protocol import Evidence, REQUIRED_CONTROLS, evaluate_run
from tsphere.tsphere_sim import Mode, TSphere


class AdversarialTSphereTests(unittest.TestCase):
    def test_malformed_commands_fail_closed_without_exceptions(self):
        cases = [
            ("morph", {}),
            ("morph", {"radius_mm": None}),
            ("morph", {"radius_mm": "not-a-number"}),
            ("morph", {"radius_mm": math.nan}),
            ("morph", {"radius_mm": math.inf}),
            ("handoff", {}),
            ("handoff", {"barrier_side": None}),
            ("unknown-command", {"payload": object()}),
        ]
        for name, kwargs in cases:
            sphere = TSphere()
            row = sphere.command(name, **kwargs)
            self.assertTrue(sphere.emergency_stop, (name, row))
            self.assertEqual(sphere.mode, Mode.SAFE, (name, row))

    def test_commands_after_stop_cannot_move_sphere(self):
        sphere = TSphere()
        sphere.command("morph", radius_mm=32)
        sphere.command("stop")
        sphere.emergency_stop = True
        row = sphere.command("roam")
        self.assertEqual(sphere.mode, Mode.SAFE)
        self.assertIn("command_denied", row.note)

    def test_randomized_input_fuzzing_stays_bounded(self):
        rng = random.Random(20260908)
        names = ["roam", "stop", "reset", "morph", "inspect", "handoff", "garbage"]
        for _ in range(1000):
            sphere = TSphere()
            name = rng.choice(names)
            kwargs = {}
            if name == "morph":
                kwargs["radius_mm"] = rng.choice([
                    -1e9, -1, 0, 30, 32, 45, 50, 1e9, "bad", None
                ])
            elif name == "handoff":
                kwargs["barrier_side"] = rng.choice(["A", "B", "C", "", None, 1])
            row = sphere.command(name, **kwargs)
            self.assertGreaterEqual(sphere.radius_mm, sphere.min_radius_mm)
            self.assertLessEqual(sphere.radius_mm, sphere.max_radius_mm)
            self.assertTrue(row.sequence >= 1)

    def test_evidence_gate_rejects_unknown_or_missing_controls(self):
        evidence = Evidence(
            True, True, True, True, True, True, True,
            tuple(sorted(REQUIRED_CONTROLS - {"sealed_barrier"})) + ("magic_control",),
        )
        result = evaluate_run(evidence)
        self.assertEqual(result["status"], "NOT_DEMONSTRATED")
        self.assertIn("sealed_barrier", result["missing_controls"])


if __name__ == "__main__":
    unittest.main()
