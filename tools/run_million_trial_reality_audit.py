"""Synthetic million-trial falsification stress test for the Flux Drive program.

This tool does NOT simulate or validate exotic propulsion. It quantifies how
ordinary artifact channels can create false positives and how explicit
correction / uncertainty gates reduce that risk.
"""

from __future__ import annotations

import json
import math
import numpy as np

SEED = 20260914
TRIALS = 1_000_000


def run() -> dict:
    rng = np.random.default_rng(SEED)

    # Synthetic artifact amplitudes in micro-newtons. These are deliberately
    # reference values for stress-testing the analysis pipeline, not measurements
    # of a physical Flux Drive device.
    thermal = rng.normal(0.0, 2.5, TRIALS)
    magnetic = rng.normal(0.0, 1.5, TRIALS)
    cable = rng.normal(0.0, 2.0, TRIALS)
    vibration = rng.normal(0.0, 1.0, TRIALS)
    noise = rng.normal(0.0, 0.8, TRIALS)

    raw = thermal + magnetic + cable + vibration + noise

    # Imperfectly estimated artifact channels.
    thermal_est = thermal + rng.normal(0.0, 0.8, TRIALS)
    magnetic_est = magnetic + rng.normal(0.0, 0.6, TRIALS)
    cable_est = cable + rng.normal(0.0, 0.7, TRIALS)
    vibration_est = vibration + rng.normal(0.0, 0.5, TRIALS)

    residual = raw - thermal_est - magnetic_est - cable_est - vibration_est
    residual_sigma = math.sqrt(0.8**2 + 0.6**2 + 0.7**2 + 0.5**2 + 0.8**2)

    false_positive_rates = {}
    for k in (2, 3, 4, 5):
        gate = k * residual_sigma
        false_positive_rates[str(k)] = {
            "naive": float((np.abs(raw) > gate).mean()),
            "corrected": float((np.abs(residual) > gate).mean()),
        }

    detection = {}
    five_sigma_gate = 5.0 * residual_sigma
    for injected_uN in (1, 2, 3, 5, 8, 10, 15):
        detection[str(injected_uN)] = float(
            (np.abs(residual + injected_uN) > five_sigma_gate).mean()
        )

    c = 299_792_458.0
    radiation_reference = {
        str(power_w): {
            "absorb_uN": power_w / c * 1e6,
            "reflect_uN": 2.0 * power_w / c * 1e6,
        }
        for power_w in (10, 100, 1000, 10000)
    }

    inertial_force = {
        str(mass_kg): {
            str(accel): mass_kg * accel for accel in (0.01, 0.1, 1.0)
        }
        for mass_kg in (1, 10, 100, 1000)
    }

    return {
        "seed": SEED,
        "trials": TRIALS,
        "reference_only": True,
        "physical_propulsion_proven": False,
        "post_correction_sigma_uN": residual_sigma,
        "raw_rms_uN": float(np.sqrt(np.mean(raw**2))),
        "residual_rms_uN": float(np.sqrt(np.mean(residual**2))),
        "false_positive_rates": false_positive_rates,
        "five_sigma_injected_signal_detection_probability": detection,
        "radiation_reference_uN": radiation_reference,
        "inertial_force_N": inertial_force,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
