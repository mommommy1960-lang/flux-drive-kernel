import unittest

from tsphere.barrier_transit_protocol import Evidence, REQUIRED_CONTROLS, evaluate_run


class BarrierTransitProtocolTests(unittest.TestCase):
    def test_incomplete_claim_is_not_demonstrated(self):
        evidence = Evidence(
            object_continuity=True,
            optical_coverage=True,
            no_barrier_damage=True,
            no_unobserved_path=True,
            conservation_within_uncertainty=True,
            randomized_repeatability=False,
            independent_replication=False,
            controls_completed=tuple(sorted(REQUIRED_CONTROLS)),
        )
        self.assertEqual(evaluate_run(evidence)["status"], "NOT_DEMONSTRATED")

    def test_missing_control_is_reported(self):
        evidence = Evidence(
            True, True, True, True, True, True, True,
            ("empty", "powered_off"),
        )
        result = evaluate_run(evidence)
        self.assertIn("sealed_barrier", result["missing_controls"])
        self.assertEqual(result["status"], "NOT_DEMONSTRATED")

    def test_only_complete_independent_result_can_pass(self):
        evidence = Evidence(
            True, True, True, True, True, True, True,
            tuple(sorted(REQUIRED_CONTROLS)),
        )
        self.assertEqual(evaluate_run(evidence)["status"], "DEMONSTRATED")


if __name__ == "__main__":
    unittest.main()
