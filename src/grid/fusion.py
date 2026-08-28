"""Per-cell height and occupancy fusion. Math §3, §10. [Aakash — Day 1]

Kalman update with a range-dependent measurement model: a return at 50 m is
not evidence of the same strength as a return at 5 m.

Accumulation is fixed-point int32 in 1 cm units. Float atomic adds are
non-associative, so two runs over identical input produce different maps and
bugs move when you look at them. `make test-determinism` is CI-blocking for
exactly this reason. See math §3.4.

Class fusion is Boyer-Moore streaming majority in one byte (4-bit candidate,
4-bit counter): match -> increment, mismatch -> decrement, zero -> adopt.
Never average softmax vectors across frames.
"""


def scatter(soa, points, labels, pose, schedule) -> None:
    raise NotImplementedError("Aakash — Day 1")


def fuse(soa, accumulators, thresholds) -> None:
    raise NotImplementedError("Aakash — Day 1")


def visibility_cleanup(soa, range_image, thresholds) -> None:
    """O(1) per cell by range-image comparison, no ray casting. Math §10.4.

    Hard guard: never clear a cell that has a return in the current scan.
    Without it this eats fences, poles and sign posts within a few frames.
    """
    raise NotImplementedError("Aakash — Day 3")
