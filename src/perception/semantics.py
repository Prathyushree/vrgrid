"""Semantic segmentation. [JP]

Pretrained FRNet, 19 classes, off the shelf, Apache 2.0. ZERO training.
Wire it in; do not reimplement it and do not fine-tune it. The checkpoint path
lives in the config, never inline.

Semantics feed refinement (a cell can be forced finer than range alone would
give) and one bit of the traversability bitfield. Geometry decides, semantics
filters: a road with a 40 cm pothole is class `road` and is not drivable; a
packed grass verge is class `vegetation` and often is.
"""


def segment(range_image):
    raise NotImplementedError("JP — Day 2")
