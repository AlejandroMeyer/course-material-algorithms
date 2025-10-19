import pytest
import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'solutions' / 'dynamic_programming'))

from dp_knapsack import knapsack, knapsack_np_ext

@pytest.mark.parametrize("W, wt, val, n, expected", [
    (50, [10, 20, 30], [60, 100, 120], 3, 220),
    (10, [1, 3, 4, 6], [20, 30, 10, 50], 4, 100),
    (7, [1, 3, 4, 5], [1, 4, 5, 7], 4, 9),
    (0, [1, 2, 3], [10, 20, 30], 3, 0),
    (5, [1, 2, 3], [10, 20, 30], 3, 50)
])
def test_knapsack(W, wt, val, n, expected):
    assert knapsack(W, wt, val, n) == expected

@pytest.mark.parametrize("W, wt, val, expected", [
    (50, [10, 20, 30], [60, 100, 120], 220),
    (10, [1, 3, 4, 6], [20, 30, 10, 50], 100),
    (7, [1, 3, 4, 5], [1, 4, 5, 7], 9),
    (0, [1, 2, 3], [10, 20, 30], 0),
    (5, [1, 2, 3], [10, 20, 30], 50)
])
def test_knapsack_np_ext(W, wt, val, expected):
    assert knapsack_np_ext(W, wt, val) == expected  