"""The integer lattice. Math §2. [Aakash — Day 0/1, first task]

Everything downstream indexes through this file, which is why it is the first
thing built and the partition test is CI-blocking.

The rule, and it has no exceptions: there is ONE lattice, at the base
resolution c0 = 5 cm. Coarser ring indices are derived from it by integer
division, never recomputed in floating point.

    i_fine(x) = floor(x / c0)
    i_L(x)    = floor(i_fine(x) / k_L),   k_L = c_L / c0 in Z+

Theorem (nested floor, math §2.2): floor(floor(x/c0)/k) == floor(x/(k*c0)).
So the ring-L lattice IS the direct lattice of size k*c0 -- the rings partition
the plane exactly. There is no tolerance to tune and no epsilon.

Computing floor(x/0.20) directly instead is the bug this file exists to
prevent: 0.2 is not representable in binary, the two lattices drift apart, and
near a boundary a point falls in both cells or neither.
"""


def i_fine(x: float, base_cell_m: float) -> int:
    raise NotImplementedError("Aakash — Day 0, hour 3")


def i_ring(x: float, base_cell_m: float, k: int) -> int:
    raise NotImplementedError("Aakash — Day 0, hour 3")


def ring_of(x: float, y: float, schedule, speed_ms: float = 0.0) -> int:
    """Which ring a point falls in, after anisotropic stretch (master v4 §3.2).

    Anisotropy changes ring MEMBERSHIP only. Every cell stays on the same base
    5 cm lattice, so nesting and alignment are untouched -- say this explicitly
    in the report, because it looks like it should break alignment.
    """
    raise NotImplementedError("Aakash — Day 1")


def toroidal_shift(soa, schedule, delta_cells) -> None:
    """Ego-motion shift of the ring buffers, O(perimeter) clear, in place.

    Round-trip must be bit-exact: shift by +d then -d returns the identical
    map. tests/test_lattice.py holds that test and it is CI-blocking.
    """
    raise NotImplementedError("Aakash — Day 1")
