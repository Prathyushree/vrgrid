#!/usr/bin/env python3
"""Regenerate the sensor sampling tables and derived limits. Math §1.

This is the most defensible original analysis in the project and it is one
equation and one plot. Gate 6: the slide numbers come from here.

    python scripts/sampling_table.py
"""

import math

import yaml

H = 1.73                       # sensor height, m
D_THETA = math.radians(0.2)    # azimuthal step
D_PHI = math.radians(26.9 / 63)  # vertical beam spacing
PHI_MIN = math.radians(24.8)   # lowest beam depression


def s_az(r: float) -> float:
    """Azimuthal spacing — linear in range. Eq (1)."""
    return r * D_THETA


def s_rad(r: float) -> float:
    """Radial ground spacing — QUADRATIC in range. Eq (3). The axis everybody
    forgets, and the reason a uniform far-field grid is empty."""
    return r * r * D_PHI / H


def p_fill(r: float, c: float) -> float:
    """Single-frame probability that a ground cell of size c at range r gets a
    return. Eq (4)."""
    return min(1.0, c / s_rad(r)) * min(1.0, c / s_az(r))


def r_max(width_m: float) -> float:
    """Max range at which a negative obstacle of given width is sampled at all.
    Eq (6)."""
    return math.sqrt(width_m * H / D_PHI)


def main() -> None:
    print("Sampling spacing\n")
    print(f"{'r (m)':>7} {'s_az (cm)':>11} {'s_rad (m)':>11}")
    for r in (10, 25, 50, 80, 100):
        print(f"{r:>7} {s_az(r)*100:>11.1f} {s_rad(r):>11.2f}")
    print("\nAt 50 m consecutive laser rings land 10.8 m apart on the road.")

    print("\n\nSingle-frame cell fill rate\n")
    print(f"{'ring':>5} {'r (m)':>7} {'c (cm)':>8} {'c/s_rad':>9} {'c/s_az':>8} {'P_fill':>8}")
    for ring, r, c in ((0, 10, 0.05), (1, 25, 0.10), (2, 50, 0.20), (3, 100, 0.40)):
        print(f"{ring:>5} {r:>7} {c*100:>8.0f} {c/s_rad(r):>9.3f} "
              f"{min(1, c/s_az(r)):>8.2f} {p_fill(r, c)*100:>7.1f}%")
    print(f"{'unif':>5} {50:>7} {5:>8} {0.05/s_rad(50):>9.3f} "
          f"{min(1, 0.05/s_az(50)):>8.2f} {p_fill(50, 0.05)*100:>7.2f}%")
    print(f"\nThe uniform 5 cm baseline is {100-p_fill(50, 0.05)*100:.2f}% empty at 50 m.")
    print(f"Coarsening improves the Ring 2 fill rate {p_fill(50,0.20)/p_fill(50,0.05):.0f}x.")
    print("Rings 2-3 are filled by ego-motion, not by the sensor: ring-sweep filling.")

    print("\n\nDerived limits\n")
    r_blind = H / math.tan(PHI_MIN)
    ring0_area = 20 * 20
    print(f"blind cone radius        {r_blind:.2f} m")
    print(f"blind disc area          {math.pi*r_blind**2:.1f} m^2 "
          f"({math.pi*r_blind**2/ring0_area*100:.1f}% of Ring 0) — unknown, never free")
    for w in (0.30, 0.50, 1.00):
        print(f"pothole {w*100:>3.0f} cm detectable within {r_max(w):>5.1f} m")

    v, dt = 1.4, 0.1
    print(f"\npedestrian at {v} m/s moves {v*dt*100:.0f} cm/frame — exceeds Ring 0 (5 cm)")
    print("and Ring 1 (10 cm) but not Ring 2 (20 cm); crossover at ~25 m. Beyond")
    print("that, pedestrian motion is a semantic prior, not a measurement.")

    with open("configs/thresholds.yaml") as f:
        cfg = yaml.safe_load(f)
    assert abs(cfg["sensor"]["blind_cone_m"] - r_blind) < 0.02, "config drifted from math §1.4"


if __name__ == "__main__":
    main()
