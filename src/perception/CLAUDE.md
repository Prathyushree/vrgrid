# src/perception — JP

- **Frames.** Vehicle frame is x forward, y left, z up. Every transform you
  write goes in `docs/frames.md` in the same commit — origin, axes,
  handedness, units. Frame confusion is the most common silent bug here: the
  map looks plausible and slowly rotates. Run the static-wall test on Day 0.
- **Wire things in, do not rebuild them.** Patchwork++ for ground, KISS-ICP
  for odometry, pretrained FRNet 19-class for semantics. Zero training.
- **Motion labels are ground truth**, read from the raw `.label` files
  (`moving-*`, IDs 250-259). Disclose it; it isolates the mapping
  contribution from segmentation error, which is what a careful evaluator wants.
- **Dataset:** SemanticKITTI sequences 00, 07, 08 only (~40 GB). Cache format
  is yours to choose, but it must be deterministic — the same sequence must
  produce byte-identical inputs twice.
- **Units.** Ranges and gradients are float metres, heights are int16 in 1 cm.
  Suffix every variable `_m` or `_cm`. Never mix silently.
- **Checkpoint and dataset paths live in `configs/`**, never inline.
