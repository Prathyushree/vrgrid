"""GPU kernels. [Shrestha]

Fixed-point int32 atomics in 1 cm units. Float atomic adds are non-associative
and make the map differ run to run, which is why `make test-determinism` is
CI-blocking. See math §3.4.

Structure-of-arrays throughout, for coalesced access.

Do NOT go near OptiX / ray-tracing cores for visibility cleanup: not supported
on Jetson, reachable only through Vulkan VK_KHR_ray_query, and not publicly
confirmed to be hardware-accelerated there. The cleanup is already O(1) per
cell by range-image comparison. One line in future work, nothing more.
"""


def scatter_kernel(points, labels, soa, schedule):
    raise NotImplementedError("Shrestha — Day 1")


def fuse_kernel(soa, accumulators):
    raise NotImplementedError("Shrestha — Day 1")


def pyramid_kernel(soa):
    """Build the conservative pyramid: per-block H_max, H_min, C_min, n_min and
    the AND-mask of traversability bitfields. Math §7.2. ~1.24 MB."""
    raise NotImplementedError("Shrestha — Day 4")
