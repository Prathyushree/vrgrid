"""Coordinate transforms. [JP — Day 0, hour 0-2 with the whole team]

EVERY transform in this file must also be written down in `docs/frames.md`,
with origin, axes, handedness and units. Frame confusion is the most common
silent bug in this project: the map looks entirely plausible and slowly
rotates. It costs three days if found on Day 4 and minutes if found now.

Vehicle frame: x forward, y left, z up.

Do the static-wall test before anything else — drive a sequence past a flat
wall and check the wall stays flat and stationary in the map. It catches
sensor-to-vehicle and vehicle-to-world errors in one shot.
"""

import numpy as np


def sensor_to_vehicle() -> np.ndarray:
    raise NotImplementedError("JP — Day 0")


def vehicle_to_world(pose) -> np.ndarray:
    raise NotImplementedError("JP — Day 0")


def transform_points(points: np.ndarray, T: np.ndarray) -> np.ndarray:
    raise NotImplementedError("JP — Day 0")
