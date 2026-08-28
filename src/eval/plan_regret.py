"""Plan regret — coarsening measured in units of decision. Math §8. [Aakash]

This is the research claim. Everything else in the project is engineering.

Plan on the reference map, plan on the compressed map, compare the DECISIONS,
not the reconstructions. If the planner reaches the same waypoint sequence,
the compression was free in the only sense a robot cares about.

It is also the answer to the hardest question you will be asked — "standard
planners want uniform grids, so you give the savings back in resampling" —
alongside the resolution-agnostic query API (§3.7) and the conservative
pyramid (§7.2). Three independent answers, which is why this is worth its days.
"""


def plan(costmap, start, goal):
    raise NotImplementedError("Aakash — Day 4")


def regret(reference_map, compressed_map, queries):
    """Difference in plan cost / decision between the two maps."""
    raise NotImplementedError("Aakash — Day 4")
