"""SoA allocation against the frozen cell struct. [Shrestha — Day 0, first task]

This blocks Aakash: `scatter()` needs somewhere to write. It is the reason
this is Shrestha's hour-3 item and not a Day-2 item.

One array per field, allocated once at startup. Never array-of-structs, and
never an allocation inside the frame loop — the compile-time memory bound is a
headline claim in the report, and one allocation in the loop makes it false.
"""


def allocate(schedule, device: str = "cpu"):
    """Preallocate ring arrays + refinement pool + transient layer. Returns a
    handle that owns every byte the frame loop will ever touch."""
    raise NotImplementedError("Shrestha — Day 0, hour 3")


def bytes_allocated(handle) -> int:
    """Must match src/eval/metrics.memory_bytes() and the report table."""
    raise NotImplementedError("Shrestha — Day 0, hour 3")
