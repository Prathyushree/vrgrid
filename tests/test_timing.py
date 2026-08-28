"""Timing harness. [Shrestha]

The harness must not be a source of the jitter it measures, and it must report
the tail rather than the mean.
"""

import numpy as np
import pytest
from vrgrid.gpu.timing import SENSOR_HZ, Timer


def _fill(timer, stage, samples):
    for s in samples:
        timer.record(stage, s)
    return timer


def test_reports_p50_and_p99_not_the_mean():
    """95 frames at 10 ms and 5 at 500 ms. The mean says 34.5 ms and looks
    survivable; the p99 says 500 ms, which is five dropped frames of
    obstacles."""
    samples = [10.0] * 95 + [500.0] * 5
    s = _fill(Timer(), "total", samples).summary()["total"]
    assert s["p50_ms"] == pytest.approx(10.0)
    assert s["p99_ms"] == 500.0
    assert s["max_ms"] == 500.0
    assert np.mean(samples) < 35.0  # what a mean would have hidden


def test_percentiles_are_observed_samples_not_interpolated():
    """numpy's default linear interpolation returns a p99 of 14.9 ms for 99
    frames at 10 ms and one at 500 ms -- a latency no frame ever took, and a
    33x under-statement of the spike. Nearest-rank never invents a value."""
    samples = [10.0] * 99 + [500.0]
    s = _fill(Timer(), "total", samples).summary()["total"]
    assert s["p99_ms"] in samples
    assert s["p99_ms"] != pytest.approx(np.percentile(samples, 99))  # the default
    assert s["max_ms"] == 500.0  # the single spike still surfaces here


def test_headroom_is_fps_over_sensor_rate():
    """40 FPS against a 10 Hz sensor is 4x headroom, not 3x."""
    t = _fill(Timer(), "total", [25.0] * 100)
    h = t.headroom()
    assert h["fps_p50"] == pytest.approx(40.0)
    assert h["headroom_p50"] == pytest.approx(4.0)
    assert SENSOR_HZ == 10.0


def test_a_pipeline_that_misses_the_rate_only_at_p99_is_reported_as_missing():
    t = _fill(Timer(), "total", [20.0] * 98 + [150.0, 160.0])
    assert t.headroom()["meets_sensor_rate"] is False


def test_recording_does_not_allocate():
    """A harness that appends to a list every frame allocates in the frame
    loop -- the exact invariant it is meant to police."""
    import tracemalloc

    t = Timer()
    t.record("scatter", 1.0)  # warm up
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()[0]
    for i in range(10_000):
        t.record("scatter", float(i % 7))
    after = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    assert after - before < 4096, f"recording allocated {after - before} bytes"


def test_buffer_is_circular_and_bounded():
    t = Timer(capacity=64)
    _fill(t, "scatter", [1.0] * 500)
    assert t.summary()["scatter"]["n"] == 500       # count is exact
    assert t._samples("scatter").size == 64         # memory is not


def test_context_manager_records_the_stage():
    t = Timer()
    with t.stage("fuse"):
        pass
    assert t.summary()["fuse"]["n"] == 1


def test_unused_stages_are_omitted():
    t = Timer()
    t.record("scatter", 1.0)
    assert set(t.summary()) == {"scatter"}


def test_snapshot_is_detached_from_the_live_buffer():
    """The dashboard renders from a snapshot at its own rate, so it can never
    throttle the pipeline -- and must not hold a reference into live memory."""
    t = _fill(Timer(), "total", [10.0] * 10)
    snap = t.snapshot()
    _fill(t, "total", [999.0] * 10)
    assert snap["stages"]["total"]["max_ms"] == 10.0


def test_reset_clears_counts_without_reallocating():
    t = Timer()
    buf_id = id(t._buf)
    _fill(t, "scatter", [1.0] * 10)
    t.reset()
    assert t.summary() == {}
    assert id(t._buf) == buf_id


def test_unknown_stage_is_a_loud_error():
    """Silently accepting a typo would leave a stage missing from the table
    with nothing to say it is missing."""
    with pytest.raises(KeyError):
        Timer().record("scater", 1.0)
