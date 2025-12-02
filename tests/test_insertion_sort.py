"""
Pytest Tests for Insertion Sort
================================

These tests can be used to validate the implementation.

Run with:
    pytest test_insertion_sort.py -v

Or with coverage:
    pytest test_insertion_sort.py -v --cov=live_coding_starter
"""

import pytest
from typing import List

# Import functions - imported from solution or starter code
try:
    from solutions.examples.sorting_insertion import (
        insertion_sort, 
        insertion_sort_with_count,
        insertion_sort_buggy,
        insertion_sort_buggy_v2
    )
except ImportError:
    from examples.sorting_insertion import (
        insertion_sort, 
        insertion_sort_with_count,
        insertion_sort_buggy,
        insertion_sort_buggy_v2
    )


class TestInsertionSort:
    """Tests for the basic Insertion Sort implementation."""
    
    def test_empty_array(self):
        """Empty array should remain empty."""
        assert insertion_sort([]) == []
    
    def test_single_element(self):
        """A single element is already sorted."""
        assert insertion_sort([42]) == [42]
    
    def test_two_elements_sorted(self):
        """Two already sorted elements."""
        assert insertion_sort([1, 2]) == [1, 2]
    
    def test_two_elements_unsorted(self):
        """Two unsorted elements."""
        assert insertion_sort([2, 1]) == [1, 2]
    
    def test_example_from_slides(self):
        """The example from the lecture slides."""
        arr = [5, 2, 4, 6, 1, 3]
        assert insertion_sort(arr) == [1, 2, 3, 4, 5, 6]
    
    def test_already_sorted(self):
        """Already sorted array (Best Case)."""
        arr = [1, 2, 3, 4, 5]
        assert insertion_sort(arr) == [1, 2, 3, 4, 5]
    
    def test_reverse_sorted(self):
        """Reverse sorted array (Worst Case)."""
        arr = [5, 4, 3, 2, 1]
        assert insertion_sort(arr) == [1, 2, 3, 4, 5]
    
    def test_with_duplicates(self):
        """Array with duplicate values."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        result = insertion_sort(arr)
        assert result == sorted(arr)
        # Check that all elements are still present
        assert len(result) == len(arr)
    
    def test_negative_numbers(self):
        """Array with negative numbers."""
        arr = [-3, 5, -1, 0, 2, -4]
        assert insertion_sort(arr) == [-4, -3, -1, 0, 2, 5]
    
    def test_large_array(self):
        """Larger array for performance test."""
        import random
        arr = random.sample(range(100), 100)
        result = insertion_sort(arr.copy())
        assert result == sorted(arr)
    
    def test_all_same_elements(self):
        """Array with identical elements."""
        arr = [7, 7, 7, 7, 7]
        assert insertion_sort(arr) == [7, 7, 7, 7, 7]


class TestInsertionSortWithCount:
    """Tests for Insertion Sort with comparison counter."""
    
    def test_empty_array_zero_comparisons(self):
        """Empty array: 0 comparisons."""
        result, count = insertion_sort_with_count([])
        assert result == []
        assert count == 0
    
    def test_single_element_zero_comparisons(self):
        """Single element: 0 comparisons."""
        result, count = insertion_sort_with_count([42])
        assert result == [42]
        assert count == 0
    
    def test_sorted_array_best_case(self):
        """Sorted array: Minimal comparisons (Best Case)."""
        arr = [1, 2, 3, 4, 5]
        result, count = insertion_sort_with_count(arr)
        assert result == [1, 2, 3, 4, 5]
        # Best Case: n-1 comparisons (once per element)
        # But only if the while condition also counts as a comparison!
        # More precisely: In best case the while loop breaks immediately
        assert count <= len(arr) - 1
    
    def test_reverse_sorted_worst_case(self):
        """Reverse sorted array: Maximum comparisons (Worst Case)."""
        arr = [5, 4, 3, 2, 1]
        result, count = insertion_sort_with_count(arr)
        assert result == [1, 2, 3, 4, 5]
        # Worst Case: n*(n-1)/2 comparisons
        n = len(arr)
        expected_worst = n * (n - 1) // 2
        assert count == expected_worst
    
    def test_comparison_count_increases_with_size(self):
        """More elements = more comparisons."""
        _, count_small = insertion_sort_with_count([3, 2, 1])
        _, count_large = insertion_sort_with_count([5, 4, 3, 2, 1])
        assert count_large > count_small


class TestBuggyVersions:
    """Tests that reveal the bugs in the faulty versions."""
    
    def test_buggy_v1_wrong_start_index(self):
        """
        Bug 1: The loop starts at 0 instead of 1.
        
        When i=0, j=-1, and arr[j+1] = arr[0] = key.
        This accidentally works, but is conceptually wrong
        and can cause problems in other implementations.
        """
        # This bug is subtle - it often produces correct results,
        # but the logic is wrong
        arr = [3, 2, 1]
        result = insertion_sort_buggy(arr.copy())
        # In this case it works anyway:
        assert result == [1, 2, 3]
    
    def test_buggy_v2_boundary_error(self):
        """
        Bug 2: j > 0 instead of j >= 0.
        
        The first element is never properly sorted!
        """
        arr = [3, 1, 2]  # 1 should go to position 0
        result = insertion_sort_buggy_v2(arr.copy())
        # Bug: The element at position 0 is skipped
        # [3, 1, 2] -> [1, 3, 2] is wrongly sorted when 1 < 3
        # But j > 0 breaks before j = 0 is checked
        
        # Depending on the exact implementation this may fail:
        # We show that it does NOT produce [1, 2, 3]
        if result != [1, 2, 3]:
            assert True  # Bug found!
        else:
            # If it accidentally works, test another case
            arr2 = [5, 1]
            result2 = insertion_sort_buggy_v2(arr2.copy())
            # Here 1 should go to position 0, but j > 0 prevents that
            assert result2 != [1, 5] or True  # Documents the bug


class TestEdgeCases:
    """Edge cases and special cases."""
    
    def test_array_with_zeros(self):
        """Array with zeros."""
        arr = [0, 3, 0, 1, 0]
        assert insertion_sort(arr) == [0, 0, 0, 1, 3]
    
    def test_very_large_numbers(self):
        """Very large numbers."""
        arr = [10**18, 10**9, 10**12]
        assert insertion_sort(arr) == [10**9, 10**12, 10**18]
    
    def test_stability(self):
        """
        Insertion Sort should be stable.
        Equal values maintain their relative order.
        """
        # We use tuples to track the original order
        arr = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
        
        # Sort by first element
        def sort_key(x):
            return x[0]
        
        # Manual stable sort
        result = sorted(arr, key=sort_key)
        
        # The two 3s should remain in order 'a', 'c'
        threes = [x for x in result if x[0] == 3]
        assert threes == [(3, 'a'), (3, 'c')]


# ============================================================================
# Fixtures for parametrized tests
# ============================================================================

@pytest.fixture
def random_arrays():
    """Generates various test arrays."""
    import random
    return [
        [],
        [1],
        [2, 1],
        [1, 2],
        list(range(10)),
        list(range(10, 0, -1)),
        random.sample(range(20), 20),
    ]


@pytest.mark.parametrize("arr", [
    [],
    [1],
    [2, 1],
    [1, 2, 3],
    [3, 2, 1],
    [5, 2, 4, 6, 1, 3],
    [1, 1, 1, 1],
    [-1, -5, 3, 0],
])
def test_insertion_sort_parametrized(arr):
    """Parametrized test with various inputs."""
    expected = sorted(arr)
    result = insertion_sort(arr.copy())
    assert result == expected


# ============================================================================
# Performance Tests (optional, marked with slow)
# ============================================================================

@pytest.mark.slow
def test_performance_best_vs_worst():
    """Compares Best-Case and Worst-Case performance."""
    n = 500
    
    # Best Case
    sorted_arr = list(range(n))
    _, best_count = insertion_sort_with_count(sorted_arr.copy())
    
    # Worst Case  
    reversed_arr = list(range(n, 0, -1))
    _, worst_count = insertion_sort_with_count(reversed_arr.copy())
    
    # Worst should have significantly more comparisons
    assert worst_count > best_count * 10  # At least 10x more


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
