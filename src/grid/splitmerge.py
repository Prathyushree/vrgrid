"""Split and merge with honest uncertainty. Math §4–5. [Aakash — Day 2]

The two rules that are easy to get wrong and impossible to see going wrong:

MERGE is marginalisation over a footprint, so it obeys the law of total
variance -- NOT inverse-variance fusion, which is the rule for repeated
measurements of one quantity. Four children measure four different places.

    mu_p     = sum(w_i mu_i)
    sigma2_p = sum(w_i sigma_i^2)  +  sum(w_i (mu_i - mu_p)^2)
               within-cell            between-cell, the spread you just erased

Drop the second term and merged cells come out most confident exactly where
they straddle a kerb. It compiles fine. It produces a map that looks right.

SPLIT inflates variance and sets the `derived` bit. Children inherit mu_p with
a strictly larger variance; the bit records that the value was not measured.
That bit is what makes merge(split(c)) == c exact (Theorem 2). Without it, a
cell oscillating across a ring boundary as the vehicle changes speed inflates
its variance every frame with no physical cause, and the map drifts toward
uncertainty.
"""


def merge(children, weights=None):
    """Four children -> one parent. See math §4.2 for the exact rule."""
    raise NotImplementedError("Aakash — Day 2")


def split(parent):
    """One parent -> four children, variance inflated, FLAG_DERIVED set. Math §5."""
    raise NotImplementedError("Aakash — Day 2")
