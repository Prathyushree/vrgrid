# src/eval — Aakash

The harness is the product. Judges see the numbers and the demo, nothing else.

- **Reference map first.** Build and cache it on Day 1. Metrics without a
  reference map are opinions.
- **Every metric is per-ring.** A single aggregate number hides the claim —
  error is *supposed* to grow with range.
- **Far-ring metrics are functions of frames-since-first-observation**, never
  scalars. Beyond 25 m the fill mechanism is ego-motion, not the sensor
  (math §1.3), so a single-frame far-field number means nothing.
- **Plan regret (math §8) is the contribution.** Compare decisions, not
  reconstructions.
- **Tune on sequence 07, report on 08.** Thresholds are frozen in
  `configs/thresholds.yaml` before any schedule comparison — otherwise the
  ablation compares tuning effort, not schedules.
- **Every number on a slide comes from a script in `scripts/`.** Gate 6. If a
  figure has no script, it does not go on a slide.
