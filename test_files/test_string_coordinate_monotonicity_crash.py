import numpy as np

from cfchecker.cfchecks import CFChecker


def test_string_valued_coordinate_does_not_crash():
    """Regression test: string arrays must not crash monotonicity checks."""
    checker = CFChecker(silent=True)

    result = checker.isStrictlyMonotonic(np.array(['label_a', 'label_b', 'label_c']))

    assert result == 0
