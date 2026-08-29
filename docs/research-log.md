# Research Log

Append-only. Newest entries at the bottom. One entry per finding, with who and when.

Format:

```
## YYYY-MM-DD — <name>
**Module:** <research module>
**Finding:**
**Source:**
**So what:** what this changes in the build, if anything.
```

---

## 2026-08-29 — Pratyushi
**Module:** R3 (Traversability, Evaluation & Novelty Claim)
**Finding:** Formulated and frozen the formal evaluation metric specifications and algorithmic pseudocode for Plan Regret $R(S)$, Discrete Fréchet Distance $d_F$, Coarsening-Justification Ratio $\rho = IL/\text{spread}$, and Dynamic Removal rates ($DR, SP, F$). Handed over `docs/eval-metric-specs.md` to Aakash to unblock `src/eval/plan_regret.py` and `src/eval/metrics.py`. Established the core invariant: both optimal reference path $\pi^*$ and candidate schedule path $\pi_S$ must be evaluated strictly on the 5 cm reference map $M^*$ so that unobserved obstacles / blurred kerbs result in infinite regret rather than false safety.
**Source:** `docs/sih-math.md` §8, §9, §10; `docs/eval-metric-specs.md`
**So what:** Unblocks Aakash (D1) to implement the evaluation harness and A* path regret scorer. Establishes the exact testable invariant that $R(S) \ge 0$ for all schedules and $R(S) \approx 0$ at our 8.94 MB operating point.
