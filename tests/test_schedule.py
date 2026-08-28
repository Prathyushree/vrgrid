"""Ring schedule validation. Master v4 §3.1."""

import pytest
from vrgrid.grid.schedule import Ring, Schedule, ScheduleError, load, validate


def _schedule(cells_m):
    return Schedule(
        name="test",
        base_cell_m=0.05,
        rings=[
            Ring(ring=i, half_width_m=10 * (i + 1), cell_m=c, cells=1000, s_az_cm=0.0)
            for i, c in enumerate(cells_m)
        ],
        total_cells=1000 * len(cells_m),
        vertical_extent_m=(-2.0, 6.0),
        hysteresis_eps=0.1,
    )


def test_default_schedule_loads_and_validates():
    s = load("5/10/20/40")
    assert [r.cell_m for r in s.rings] == [0.05, 0.10, 0.20, 0.40]
    assert s.total_cells == 745_000
    assert [s.k(i) for i in range(4)] == [1, 2, 4, 8]


def test_ablation_schedule_loads_and_validates():
    s = load("5/10/50")
    assert s.total_cells == 520_000
    assert [s.k(i) for i in range(3)] == [1, 2, 10]


def test_fifty_is_legal_next_to_ten():
    """50/10 = 5 is an integer. The requirement is integer ratios, not powers
    of two — 50 cm was only ever broken next to 20 cm."""
    validate(_schedule([0.05, 0.10, 0.50]))


def test_fifty_is_rejected_next_to_twenty():
    """50/20 = 2.5. Non-integer ratios make the lattices drift apart in
    floating point and produce gaps and double-counts at ring boundaries."""
    with pytest.raises(ScheduleError, match="non-integer ratio"):
        validate(_schedule([0.05, 0.10, 0.20, 0.50]))


def test_cell_must_be_integer_multiple_of_base_lattice():
    with pytest.raises(ScheduleError, match="not an integer multiple"):
        validate(_schedule([0.05, 0.075]))


def test_half_widths_must_increase():
    s = _schedule([0.05, 0.10])
    s.rings[1].half_width_m = 5.0
    with pytest.raises(ScheduleError, match="strictly increase"):
        validate(s)


def test_warns_when_cell_size_diverges_from_sensor_spacing():
    """Flaw E4: 5 cm cells out to 100 m passes the integer test and is still
    nonsense. s_az at 100 m is 34.9 cm."""
    s = _schedule([0.05])
    s.rings[0].half_width_m = 100
    s.rings[0].s_az_cm = 34.9
    with pytest.warns(UserWarning, match="diverges"):
        validate(s)
