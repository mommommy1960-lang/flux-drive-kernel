import math
import pytest
from flux_drive import FluxKernel, Parameters, KernelState

def test_deterministic_bounded_simulation():
    kernel = FluxKernel()
    p = Parameters(0.5, 10.0, 100.0)
    assert kernel.simulate(p) == kernel.simulate(p)
    assert kernel.state is KernelState.NEUTRAL

@pytest.mark.parametrize("value", [math.nan, math.inf, -math.inf])
def test_nonfinite_inputs_fail_neutral(value):
    kernel = FluxKernel()
    with pytest.raises(ValueError):
        kernel.simulate(Parameters(value, 1.0, 1.0))
    assert kernel.state is KernelState.NEUTRAL

@pytest.mark.parametrize("p", [
    Parameters(-0.1,1,1), Parameters(1.1,1,1),
    Parameters(0.1,0,1), Parameters(0.1,101,1),
    Parameters(0.1,1,-1), Parameters(0.1,1,10001),
])
def test_boundary_violations_rejected(p):
    with pytest.raises(ValueError):
        FluxKernel().simulate(p)

def test_freeze_denies_simulation():
    kernel=FluxKernel(); kernel.freeze()
    with pytest.raises(PermissionError):
        kernel.simulate(Parameters(0.1,1,1))

def test_result_never_claims_physical_evidence():
    result=FluxKernel().simulate(Parameters(0.1,1,1))
    assert result.claim_level == "simulation-only; no propulsion evidence"

def test_long_horizon_stays_finite_and_neutral():
    kernel=FluxKernel()
    for _ in range(10_000):
        result=kernel.simulate(Parameters(0.2,5,2))
        assert math.isfinite(result.toy_energy)
        assert kernel.state is KernelState.NEUTRAL
