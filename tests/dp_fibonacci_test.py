import pytest
from exercises.dynamic_programming.fibonacci import fibonacci_memo, fibonacci_tab

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (20, 6765),
    (30, 832040)
])
def test_fibonacci_memo(n, expected):
    assert fibonacci_memo(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (20, 6765),
    (30, 832040)
])
def test_fibonacci_tab(n, expected):
    assert fibonacci_tab(n) == expected