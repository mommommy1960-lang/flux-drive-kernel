"""Deterministic toy model. This code does not model or enable propulsion."""
from __future__ import annotations
import math
from dataclasses import dataclass
from enum import Enum

class KernelState(str, Enum):
    NEUTRAL = "neutral"
    SIMULATING = "simulating"
    FROZEN = "frozen"

@dataclass(frozen=True)
class Parameters:
    amplitude: float
    width: float
    duration: float
    uncertainty: float = 0.10

@dataclass(frozen=True)
class Result:
    field_index: float
    toy_energy: float
    uncertainty_low: float
    uncertainty_high: float
    claim_level: str = "simulation-only; no propulsion evidence"

class FluxKernel:
    MAX_AMPLITUDE = 1.0
    MAX_WIDTH = 100.0
    MAX_DURATION = 10_000.0

    def __init__(self) -> None:
        self.state = KernelState.NEUTRAL

    def freeze(self) -> None:
        self.state = KernelState.FROZEN

    def neutralize(self) -> None:
        self.state = KernelState.NEUTRAL

    def simulate(self, p: Parameters) -> Result:
        values = (p.amplitude, p.width, p.duration, p.uncertainty)
        if not all(math.isfinite(v) for v in values):
            self.state = KernelState.NEUTRAL
            raise ValueError("all parameters must be finite")
        if not (0 <= p.amplitude <= self.MAX_AMPLITUDE):
            raise ValueError("amplitude outside simulation bound")
        if not (0 < p.width <= self.MAX_WIDTH):
            raise ValueError("width outside simulation bound")
        if not (0 <= p.duration <= self.MAX_DURATION):
            raise ValueError("duration outside simulation bound")
        if not (0 <= p.uncertainty <= 1):
            raise ValueError("uncertainty outside probability bound")
        if self.state is KernelState.FROZEN:
            raise PermissionError("independent freeze is active")
        self.state = KernelState.SIMULATING
        try:
            field = p.amplitude * math.exp(-1.0 / p.width)
            energy = field * field * p.width * p.duration
            spread = energy * p.uncertainty
            return Result(field, energy, max(0.0, energy-spread), energy+spread)
        finally:
            self.state = KernelState.NEUTRAL
