# scripts/

**Gate 6: every number on a slide comes from a script in here.** If a figure
is not produced by something in this directory, it does not go on a slide.

| Script | Produces |
| --- | --- |
| `memory_table.py` | The memory comparison table — reads `CELL_BYTES` from the frozen struct, so the report cannot drift from the code |
| `sampling_table.py` | `s_az` / `s_rad` tables, single-frame fill rates, blind cone, pothole range limit, pedestrian crossover |

To add: `ablation_table.py` (schedule comparison, thresholds frozen first),
`regret_plot.py`, `timing_table.py`, `ghost_removal_figure.py`.
