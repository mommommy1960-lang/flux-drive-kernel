import unittest

from tsphere.hypothesis_registry import MechanismHypothesis, evaluate_evidence


def complete_hypothesis() -> MechanismHypothesis:
    return MechanismHypothesis(
        name="Candidate barrier interaction",
        interaction="A declared field interaction with the sphere and barrier",
        governing_equations="A complete field equation with boundary conditions",
        boundary_conditions="Sealed barrier and specified initial state",
        predicted_observables="Force, energy, mass, timing, and sensor signatures",
        required_controls=("powered_off", "sham", "sealed_barrier"),
        falsifiers="No transit, barrier damage, or conservation mismatch",
    )


class HypothesisRegistryTests(unittest.TestCase):
    def test_incomplete_packet_is_blocked(self):
        hypothesis = MechanismHypothesis("incomplete", "", "", "", "", (), "")
        result = hypothesis.review_status()
        self.assertEqual(result["status"], "BLOCKED")
        self.assertFalse(result["validated"])

    def test_complete_packet_is_reviewable_not_validated(self):
        result = complete_hypothesis().review_status()
        self.assertEqual(result["status"], "READY_FOR_REVIEW")
        self.assertFalse(result["validated"])

    def test_evidence_gate_requires_replication_and_controls(self):
        result = evaluate_evidence(
            complete_hypothesis(),
            repeated_trials=3,
            independent_replications=1,
            all_controls_passed=False,
            measurements_within_uncertainty=True,
        )
        self.assertEqual(result["status"], "NOT_VALIDATED")

    def test_defined_validation_requires_all_gates(self):
        result = evaluate_evidence(
            complete_hypothesis(),
            repeated_trials=3,
            independent_replications=1,
            all_controls_passed=True,
            measurements_within_uncertainty=True,
        )
        self.assertEqual(result["status"], "VALIDATED_FOR_DEFINED_TEST")
        self.assertTrue(result["validated"])


if __name__ == "__main__":
    unittest.main()
