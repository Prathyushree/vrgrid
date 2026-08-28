"""Timing harness. [Shrestha — Day 0, with the allocator]

Per-stage wall time, reported the way the dashboard shows it: load, transform,
range image, scatter, fuse, split/merge, cleanup. Median and p95, never mean —
a 10 Hz claim is about the tail.

Also owns the allocating dense-3D baseline stub, which exists to produce the
286x and 21.5x memory comparison honestly rather than by arithmetic alone.
"""

import time
from contextlib import contextmanager


@contextmanager
def stage(name: str, sink=None):
    t0 = time.perf_counter()
    try:
        yield
    finally:
        dt_ms = (time.perf_counter() - t0) * 1e3
        if sink is not None:
            sink.setdefault(name, []).append(dt_ms)


def summarise(sink) -> dict:
    """Median and p95 per stage."""
    raise NotImplementedError("Shrestha — Day 0, hour 3")
