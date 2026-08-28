# src/grid — Aakash

The contribution lives here. Read the cited math section before editing.

- **Lattice, math §2.** One lattice at 5 cm. `i_L = i_fine // k_L`, integer
  division. Never `floor(x/0.20)` — float lattices drift and produce gaps at
  ring boundaries. The partition test is CI-blocking.
- **Fusion, math §3.** Kalman, range-dependent measurement model. Accumulate
  as int32 in 1 cm units. No float atomics, ever (§3.4).
- **Merge, math §4.** Law of total variance, both terms. Not inverse-variance.
- **Split, math §5.** Inflate variance, set `FLAG_DERIVED`. The bit is what
  makes `merge(split(c)) == c` exact.
- **Ring migration, master v4 §3.2.** Hysteresis ε = 0.1: split at `R_L`,
  merge only at `R_L(1+ε)`. Anisotropy changes ring *membership* only — cells
  stay on the base lattice.
- **Pool, master v4 §3.4.** 512 × 16 × 12 B, preallocated. No allocation in
  the frame loop.

The cell struct in `include/vrgrid/cell.py` is frozen at 12 bytes. Adding a
field means recomputing every memory figure in the report — whole-team call.

Theorem tests are proofs, not tuning targets. If one fails, the code is wrong.
