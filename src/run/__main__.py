"""Pipeline entry point — `python -m vrgrid.run --seq 08 --schedule 5/10/20/40`.

Thin wiring only: parse arguments, load config, call into the owned modules.
No logic lives here, so it belongs to nobody and everybody. Keep it that way.
"""

import argparse

from vrgrid.grid import schedule as schedule_mod


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="vrgrid.run")
    p.add_argument("--seq", default="08", help="SemanticKITTI sequence")
    p.add_argument("--schedule", default="5/10/20/40", help="ring schedule name")
    p.add_argument("--thresholds", default="configs/thresholds.yaml")
    p.add_argument("--frames", type=int, default=None, help="stop after N frames")
    p.add_argument("--out", default=None, help="write map + metrics here")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    sched = schedule_mod.load(args.schedule)
    print(f"schedule {sched.name}: {len(sched.rings)} rings, "
          f"{sched.total_cells:,} cells, {sched.total_cells * 12 / 1e6:.2f} MB")
    raise NotImplementedError("pipeline wiring — Day 1, once scatter() lands")


if __name__ == "__main__":
    raise SystemExit(main())
