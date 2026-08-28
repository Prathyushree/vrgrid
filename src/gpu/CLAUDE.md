# src/gpu — Shrestha

- **Fixed-point, never float atomics.** int32 accumulators in 1 cm units.
  Float atomic adds are non-associative: the map changes run to run and bugs
  move when you look at them. `make test-determinism` is CI-blocking (math §3.4).
- **Structure-of-arrays.** One array per field, for coalesced access. Never
  array-of-structs.
- **No allocation in the frame loop.** Grid arrays, refinement pool (512 × 16
  × 12 B = 98 KB), transient layer and tracked-object list are all preallocated
  at startup. One allocation in the loop makes the memory claim false.
- **Timing is p50 and p99, not mean**, and percentiles are nearest-rank —
  numpy's default interpolation invents a latency no frame ever took and
  rounds the tail down. A 10 Hz claim is about the tail.
- **Rings are annuli, not squares.** Four full squares would cost 910,000
  cells against a 745,000-cell headline. `allocators.annulus_index()` bands
  each ring into four rectangles; it returns -1 for the hole, and a -1 read as
  an index dumps the far field into cell 0.
- **Scatter has two paths, and they must stay bit-identical.** `scatter_sorted`
  (default, scratch sized by points) and `scatter_atomic` (dense accumulator,
  the literal reading of master v4 §3.5). `tests/test_kernels.py` asserts they
  agree field-for-field; if they diverge, the optimisation is the bug.
- **`annulus_index()` returns -1 for the hole.** Scatter drops those. A -1 used
  as an index piles the far field into cell 0 and still looks plausible.
- **No OptiX / RT cores.** Unsupported on Jetson; visibility cleanup is already
  O(1) per cell by range-image comparison. Future-work line only.

Day 0–1 your work blocks both other devs, so the allocator and timing harness
are non-negotiable and come first. From Day 2 it reverses and you are
optimising what they built — which is also why you are the right person to
pull onto split/merge if Aakash is behind at the Day 2 gate.
