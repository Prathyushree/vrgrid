"""Refinement pool — 512 blocks x 16 cells x 12 B = 98 KB, fixed. [Aakash]

Master v4 §3.4. Semantics can force local refinement below what range alone
would give, but only into this preallocated pool. When it is full, evict by
priority = closeness x dynamism x time-to-collision.

Nothing here allocates after startup. The compile-time memory bound is a
headline claim in the report and an allocation in the frame loop makes it
false.
"""


class RefinementPool:
    def __init__(self, blocks: int = 512, cells_per_block: int = 16):
        raise NotImplementedError("Aakash — Day 2")
