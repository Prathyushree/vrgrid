"""SemanticKITTI loader. [JP — Day 0, first task]

Sequences 00, 07, 08 only — about 40 GB, not the full 200 GB. Start the
download before anything else on Day 0; it is the one item on the critical
path that neither cleverness nor effort can accelerate.

Motion labels come straight out of the raw `.label` files (`moving-*`,
IDs 250-259). Nothing is retrained. Disclose it plainly in the report: motion
labels are ground truth, so the mapping contribution is evaluated independently
of segmentation quality. That is a feature — it isolates the contribution from
segmentation error.
"""

MOVING_LABEL_IDS = range(250, 260)  # verify against the raw files — Hriday, hour 4


def scans(sequence: str):
    """Yield (points, labels, pose) per frame."""
    raise NotImplementedError("JP — Day 0/1")


def poses(sequence: str):
    raise NotImplementedError("JP — Day 0/1")
