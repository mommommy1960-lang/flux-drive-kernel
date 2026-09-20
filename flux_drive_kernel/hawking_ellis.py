"""Conservative numerical Hawking--Ellis stress-energy classification.

The input is a covariant stress-energy tensor in a local orthonormal frame
with metric ``eta = diag(-1, +1, +1, +1)``.  The implementation certifies
only the cases that are stable under numerical linear algebra:

* Type I: the mixed tensor has a complete real eigenbasis whose invariant
  eigenspaces carry Lorentz signature (-,+,+,+).
* Type IV: at least one robust complex-conjugate eigenvalue pair is present.
* Otherwise: a real but null/defective/degenerate case that requires an exact
  or high-precision canonical reduction before a Type-II/III label is used.

This module does not infer physical realizability from algebraic type alone.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


@dataclass(frozen=True)
class Classification:
    """Numerical classification result and diagnostic quantities."""

    kind: str
    eigenvalues: np.ndarray
    negative_directions: int
    null_directions: int
    positive_directions: int
    eigen_residual: float
    relative_antisymmetry: float
    note: str


def _as_symmetric_tensor(
    tensor: np.ndarray,
    *,
    symmetry_rtol: float,
    symmetry_atol: float,
) -> tuple[np.ndarray, float]:
    value = np.asarray(tensor, dtype=float)
    if value.shape != (4, 4):
        raise ValueError("T_cov must be a finite 4x4 array")
    if not np.all(np.isfinite(value)):
        raise ValueError("T_cov must be a finite 4x4 array")
    if symmetry_rtol < 0.0 or symmetry_atol < 0.0:
        raise ValueError("symmetry tolerances must be nonnegative")

    scale = max(1.0, float(np.linalg.norm(value, ord=2)))
    antisymmetric = value - value.T
    relative = float(np.linalg.norm(antisymmetric, ord=2) / scale)
    allowed = symmetry_atol + symmetry_rtol * scale
    if float(np.linalg.norm(antisymmetric, ord=2)) > allowed:
        raise ValueError(
            "T_cov is not symmetric within the declared numerical tolerance"
        )

    # A stress-energy tensor is symmetric.  Averaging only after the explicit
    # tolerance check removes convergent finite-difference roundoff without
    # concealing a material implementation error.
    return 0.5 * (value + value.T), relative


def mixed_tensor(T_cov: np.ndarray) -> np.ndarray:
    """Return ``T^a_b = eta^(ac) T_cb`` after a strict symmetry check."""

    tensor, _ = _as_symmetric_tensor(
        T_cov, symmetry_rtol=1.0e-12, symmetry_atol=1.0e-12
    )
    return ETA @ tensor


def _cluster_real_eigenvalues(values: np.ndarray, tolerance: float) -> list[list[int]]:
    groups: list[list[int]] = []
    for index, value in enumerate(values):
        for group in groups:
            if abs(value - values[group[0]]) <= tolerance:
                group.append(index)
                break
        else:
            groups.append([index])
    return groups


def _nullspace(matrix: np.ndarray, tolerance: float) -> np.ndarray:
    _, singular_values, vh = np.linalg.svd(matrix)
    rank = int(np.count_nonzero(singular_values > tolerance))
    return vh[rank:].conj().T


def classify(
    T_cov: np.ndarray,
    tol: float = 1.0e-9,
    *,
    symmetry_rtol: float = 1.0e-9,
    symmetry_atol: float = 1.0e-12,
) -> Classification:
    """Classify a local orthonormal-frame stress-energy tensor.

    ``symmetry_rtol`` must be chosen from an independently demonstrated
    discretization/convergence error when finite-difference tensors are used.
    The returned ``relative_antisymmetry`` keeps that numerical repair visible.
    """

    if tol <= 0.0 or not np.isfinite(tol):
        raise ValueError("tol must be finite and positive")

    tensor, relative_antisymmetry = _as_symmetric_tensor(
        T_cov,
        symmetry_rtol=symmetry_rtol,
        symmetry_atol=symmetry_atol,
    )
    mixed = ETA @ tensor
    values, vectors = np.linalg.eig(mixed)
    scale = max(1.0, float(np.linalg.norm(mixed, ord=2)))
    spectral_tolerance = tol * scale

    residuals = []
    for index in range(4):
        vector = vectors[:, index]
        residuals.append(
            float(
                np.linalg.norm(mixed @ vector - values[index] * vector)
                / scale
            )
        )
    max_residual = max(residuals)

    if np.any(np.abs(np.imag(values)) > spectral_tolerance):
        return Classification(
            kind="Type IV",
            eigenvalues=values,
            negative_directions=0,
            null_directions=0,
            positive_directions=0,
            eigen_residual=max_residual,
            relative_antisymmetry=relative_antisymmetry,
            note="Robust complex eigenvalue pair detected.",
        )

    real_values = np.real(values)
    groups = _cluster_real_eigenvalues(real_values, spectral_tolerance)
    bases: list[np.ndarray] = []
    for group in groups:
        eigenvalue = float(np.mean(real_values[group]))
        basis = _nullspace(
            mixed - eigenvalue * np.eye(4),
            tolerance=max(spectral_tolerance, tol),
        )
        bases.append(np.real_if_close(basis).astype(float))

    eigenbasis_dimension = sum(basis.shape[1] for basis in bases)
    if eigenbasis_dimension == 4:
        eigenbasis = np.column_stack(bases)
        gram = 0.5 * (
            eigenbasis.T @ ETA @ eigenbasis
            + (eigenbasis.T @ ETA @ eigenbasis).T
        )
        gram_values = np.linalg.eigvalsh(gram)
        gram_scale = max(1.0, float(np.max(np.abs(gram_values))))
        gram_tolerance = tol * gram_scale
        negative = int(np.count_nonzero(gram_values < -gram_tolerance))
        positive = int(np.count_nonzero(gram_values > gram_tolerance))
        null = 4 - negative - positive
        if (negative, null, positive) == (1, 0, 3):
            return Classification(
                kind="Type I",
                eigenvalues=real_values,
                negative_directions=negative,
                null_directions=null,
                positive_directions=positive,
                eigen_residual=max_residual,
                relative_antisymmetry=relative_antisymmetry,
                note=(
                    "Complete real eigenbasis with Lorentz signature "
                    "(-,+,+,+)."
                ),
            )
    else:
        negative = null = positive = 0

    return Classification(
        kind="Non-Type-I / degenerate real spectrum",
        eigenvalues=real_values,
        negative_directions=negative,
        null_directions=null,
        positive_directions=positive,
        eigen_residual=max_residual,
        relative_antisymmetry=relative_antisymmetry,
        note=(
            "Real spectrum is null, defective, or not numerically certified; "
            "use an exact or high-precision canonical reduction before a "
            "Type-II/III label."
        ),
    )


def type_I_energy_conditions(
    rho: float, pressures: np.ndarray, tol: float = 0.0
) -> dict[str, bool]:
    """Return NEC, WEC, SEC, and DEC for canonical Type-I components."""

    p = np.asarray(pressures, dtype=float)
    if p.shape != (3,) or not np.all(np.isfinite(p)) or not np.isfinite(rho):
        raise ValueError("rho and pressures must be finite; pressures has length 3")
    if tol < 0.0 or not np.isfinite(tol):
        raise ValueError("tol must be finite and nonnegative")

    nec_terms = rho + p
    return {
        "NEC": bool(np.all(nec_terms >= -tol)),
        "WEC": bool(rho >= -tol and np.all(nec_terms >= -tol)),
        "SEC": bool(
            np.all(nec_terms >= -tol) and rho + float(np.sum(p)) >= -tol
        ),
        "DEC": bool(rho >= -tol and np.all(rho >= np.abs(p) - tol)),
    }
