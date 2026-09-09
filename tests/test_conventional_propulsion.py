import math
import unittest

from flux_drive_kernel.conventional_propulsion import (
    G0_M_S2,
    acceleration_from_thrust_m_s2,
    exhaust_velocity_m_s,
    ideal_electric_thrust_from_power_N,
    ideal_rocket_delta_v_m_s,
    mass_flow_for_thrust_kg_s,
    mass_ratio_for_delta_v,
    propellant_fraction_for_delta_v,
    specific_impulse_s,
    thrust_from_mass_flow_N,
)


class ConventionalPropulsionTests(unittest.TestCase):
    def test_specific_impulse_and_exhaust_velocity_are_inverse(self):
        ve = exhaust_velocity_m_s(300.0)
        self.assertAlmostEqual(ve, 300.0 * G0_M_S2)
        self.assertAlmostEqual(specific_impulse_s(ve), 300.0)

    def test_rocket_equation_mass_ratio_two(self):
        expected = exhaust_velocity_m_s(300.0) * math.log(2.0)
        self.assertAlmostEqual(ideal_rocket_delta_v_m_s(2.0, 1.0, 300.0), expected)
        self.assertAlmostEqual(mass_ratio_for_delta_v(expected, 300.0), 2.0)
        self.assertAlmostEqual(propellant_fraction_for_delta_v(expected, 300.0), 0.5)

    def test_mass_flow_and_thrust_are_inverse(self):
        thrust = thrust_from_mass_flow_N(0.01, 400.0)
        self.assertAlmostEqual(mass_flow_for_thrust_kg_s(thrust, 400.0), 0.01)

    def test_electric_propulsion_power_relation(self):
        ve = exhaust_velocity_m_s(2000.0)
        expected = 2.0 * 0.7 * 1000.0 / ve
        self.assertAlmostEqual(
            ideal_electric_thrust_from_power_N(
                1000.0,
                2000.0,
                jet_power_efficiency=0.7,
            ),
            expected,
        )

    def test_acceleration_from_thrust(self):
        self.assertAlmostEqual(acceleration_from_thrust_m_s2(10.0, 1000.0), 0.01)

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            ideal_rocket_delta_v_m_s(1.0, 2.0, 300.0)
        with self.assertRaises(ValueError):
            mass_ratio_for_delta_v(-1.0, 300.0)
        with self.assertRaises(ValueError):
            ideal_electric_thrust_from_power_N(100.0, 1000.0, jet_power_efficiency=1.1)


if __name__ == "__main__":
    unittest.main()
