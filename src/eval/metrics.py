"""Information-loss metrics. Math §9. [Aakash]

Report per-ring, never as a single scalar — the whole claim is that error is
allowed to grow with range, so an aggregate number hides the result.

Far-ring accuracy must be reported as a function of frames-since-first-
observation, not as a scalar. P_fill < 2% beyond 25 m means the far field is
filled by ego-motion sweeping the ring pattern across the ground, not by any
single frame ("ring-sweep filling", math §1.3). Single-frame far-field numbers
are meaningless.
"""


def height_rmse_per_ring(grid, reference):
    raise NotImplementedError("Aakash — Day 2")


def occupancy_iou_per_ring(grid, reference):
    raise NotImplementedError("Aakash — Day 2")


def fill_rate(grid, reference):
    """Fraction of cells with at least one observation, per ring, vs frame count."""
    raise NotImplementedError("Aakash — Day 2")


def memory_bytes(grid):
    raise NotImplementedError("Aakash — Day 2")
