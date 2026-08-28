"""Reference map — the ground truth every metric is measured against. [Aakash]

Master v4 §3.8, math §9. Built once per sequence and cached on disk: aggregate
all scans of a sequence with GT poses at 5 cm, static points only, then treat
that as truth.

Build this EARLY. Without it you are tuning the ring schedule by eye and have
no answer when a judge asks whether coarsening lost the kerb.
"""


def build(sequence: str, out_path: str) -> None:
    raise NotImplementedError("Aakash — Day 1")


def load(path: str):
    raise NotImplementedError("Aakash — Day 1")
