"""Determinism. CI-blocking. [Shrestha]

Fixed-point int32 accumulation in 1 cm units is the whole reason this passes.
Float atomic adds are non-associative: the map differs run to run, and bugs
move when you look at them. Math §3.4.
"""

import pytest

pytestmark = pytest.mark.skip(reason="awaiting scatter()/fuse() — Day 1")


@pytest.mark.determinism
def test_same_input_twice_gives_identical_map_hash():
    """Run the same 50 frames of sequence 08 twice. Byte-identical SoA arrays."""
    raise NotImplementedError


@pytest.mark.determinism
def test_point_order_does_not_change_the_map():
    """Shuffle the points within a scan. Fixed-point accumulation is
    associative, so the result must be identical — this is the test that
    actually catches a float atomic sneaking in."""
    raise NotImplementedError


def test_no_allocation_inside_the_frame_loop():
    """Preallocated bound is a headline claim. Track peak RSS across 100 frames
    and assert it does not grow after the first."""
    raise NotImplementedError
