"""Split/merge theorems. Math §4–5. [Aakash]

These are proofs, not tuning targets. If one fails, the implementation is
wrong — do not weaken the test to make it pass.
"""

import pytest

pytestmark = pytest.mark.skip(reason="awaiting src/grid/splitmerge.py — Aakash, Day 2")


@pytest.mark.theorem
def test_merge_uses_law_of_total_variance():
    """sigma2_p = sum(w_i sigma_i^2) + sum(w_i (mu_i - mu_p)^2).

    Constructed case: four children with identical tiny variance but means
    straddling a 12 cm kerb. Inverse-variance fusion returns a *smaller*
    variance than any child — confidently wrong exactly at the kerb. The
    correct rule returns a variance dominated by the between-cell spread.
    """
    raise NotImplementedError


@pytest.mark.theorem
def test_split_strictly_inflates_variance():
    """Children inherit mu_p with strictly larger variance, and FLAG_DERIVED set."""
    raise NotImplementedError


@pytest.mark.theorem
def test_round_trip_idempotence():
    """merge(split(c)) == c exactly, in mean AND variance, when no measurement
    intervenes. Math §5, Theorem 2.

    This is what the `derived` bit buys. Without it a cell oscillating across a
    ring boundary as the vehicle changes speed inflates variance every frame
    with no physical cause, and the map drifts toward uncertainty.
    """
    raise NotImplementedError


def test_hysteresis_prevents_boundary_thrash():
    """Split at R_L, merge only at R_L(1+eps). A cell parked on the boundary
    must not split and merge on consecutive frames."""
    raise NotImplementedError
