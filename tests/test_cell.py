"""The frozen cell struct. If this file goes red, the report's memory table is
wrong — every ratio in it is computed from CELL_BYTES."""

import numpy as np
from vrgrid.cell import (
    CELL_BYTES,
    CELL_DTYPE,
    FLAG_BLIND,
    FLAG_DERIVED,
    FLAG_DYNAMIC,
    FLAG_REFINED,
    TRAV_CLASS,
    TRAV_CLEARANCE,
    TRAV_CONFIDENCE,
    TRAV_ROUGHNESS,
    TRAV_SLOPE,
    TRAV_STEP,
    alloc_soa,
    soa_bytes,
)


def test_cell_is_twelve_bytes():
    """Master v4 §3.3. Adding a field means recomputing every memory figure."""
    assert CELL_DTYPE.itemsize == CELL_BYTES == 12


def test_no_hidden_padding():
    """The int16s sit at offsets 0 and 2, so the struct is naturally aligned and
    needs no filler byte. If numpy inserts padding, the layout drifted."""
    assert sum(CELL_DTYPE.fields[n][0].itemsize for n in CELL_DTYPE.names) == 12


def test_heights_are_int16_centimetres():
    """int16 at 1 cm covers +-327 m. Quantisation noise sigma = q/sqrt(12) =
    2.9 mm, under a third of sensor noise at the closest range."""
    assert CELL_DTYPE["ground_height"] == np.int16
    assert CELL_DTYPE["ceiling_height"] == np.int16


def test_traversability_bits_are_six_distinct_flags():
    """Math §7.1. A bitfield, not a scalar: a planner facing a clearance
    failure behaves differently from one facing a slope."""
    bits = [
        TRAV_CLEARANCE,
        TRAV_SLOPE,
        TRAV_STEP,
        TRAV_ROUGHNESS,
        TRAV_CLASS,
        TRAV_CONFIDENCE,
    ]
    assert len(set(bits)) == 6
    assert all(b < 256 for b in bits)
    assert sum(bits) == 0b111111


def test_flag_bits_distinct():
    bits = [FLAG_DERIVED, FLAG_REFINED, FLAG_BLIND, FLAG_DYNAMIC]
    assert len(set(bits)) == 4


def test_soa_allocation_is_one_array_per_field():
    soa = alloc_soa(1000)
    assert set(soa) == set(CELL_DTYPE.names)
    assert all(a.shape == (1000,) for a in soa.values())
    assert sum(a.nbytes for a in soa.values()) == soa_bytes(1000) == 12_000


def test_memory_headline_numbers():
    """The three figures the pitch leads with. If the cell grows, these move."""
    assert soa_bytes(745_000) / 1e6 == 8.94                    # ours, 4-ring
    assert round(soa_bytes(520_000) / 1e6, 2) == 6.24          # ablation, 3-ring
    uniform_5cm_cells = 4000 * 4000                            # 200x200 m at 5 cm
    assert round(uniform_5cm_cells / 745_000, 1) == 21.5       # cell-count ratio
