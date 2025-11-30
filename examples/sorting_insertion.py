"""
Coding Session: Insertion Sort
====================================

This module contains the starter code for the coding session.

Workflow (for students during the session):
1. Implement insertion_sort()
2. Add comparison counter
3. Analyze best-case vs worst-case
4. Debug off-by-one errors
"""

import time
from typing import List, Tuple


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array using the Insertion Sort algorithm.
    
    Args:
        arr: List of numbers to sort
        
    Returns:
        The sorted list (modified in-place)
        
    TODO: Implement the Insertion Sort algorithm
    
    Hints:
    - Start at index 1 (the first element is trivially sorted)
    - For each element: Find the correct position in the sorted part
    - Shift larger elements to the right
    """
    # TODO: Implement the algorithm here
    # Step 1: Outer loop - iterate through all elements starting at index 1
    # Step 2: Store the current element as 'key'
    # Step 3: Inner loop - shift larger elements to the right
    # Step 4: Insert 'key' at the correct position
    
    pass  # Replace this with your implementation


def insertion_sort_with_count(arr: List[int]) -> Tuple[List[int], int]:
    """
    Insertion Sort with comparison counting.
    
    Args:
        arr: List of numbers to sort
        
    Returns:
        Tuple of (sorted list, number of comparisons)
        
    TODO: Extend your implementation with a comparison counter
    """
    comparisons = 0
    
    # TODO: Copy your implementation from above
    # and add comparisons += 1 at every comparison point
    
    pass  # Replace this


def analyze_performance():
    """
    Analyzes the performance of Insertion Sort for different inputs.
    
    Run this function to compare best-case vs worst-case.
    """
    import random
    
    # Generate test data
    n = 1000
    
    # Best Case: Already sorted array
    sorted_array = list(range(n))
    
    # Worst Case: Reverse sorted array
    reversed_array = list(range(n, 0, -1))
    
    # Average Case: Random array
    random_array = random.sample(range(n), n)
    
    print("=" * 60)
    print("Performance Analysis: Insertion Sort")
    print("=" * 60)
    print(f"Array size: n = {n}")
    print()
    
    # Best Case
    arr_copy = sorted_array.copy()
    _, best_comparisons = insertion_sort_with_count(arr_copy)
    print(f"Best Case (sorted):       {best_comparisons:>10} comparisons")
    print(f"  Expected: O(n) = {n}")
    print()
    
    # Worst Case
    arr_copy = reversed_array.copy()
    _, worst_comparisons = insertion_sort_with_count(arr_copy)
    print(f"Worst Case (reversed):    {worst_comparisons:>10} comparisons")
    print(f"  Expected: O(n²) = n*(n-1)/2 = {n*(n-1)//2}")
    print()
    
    # Average Case
    arr_copy = random_array.copy()
    _, avg_comparisons = insertion_sort_with_count(arr_copy)
    print(f"Average Case (random):    {avg_comparisons:>10} comparisons")
    print(f"  Expected: O(n²/4) ≈ {n*n//4}")
    print()
    
    # Ratio
    print("-" * 60)
    print(f"Worst / Best = {worst_comparisons / best_comparisons:.1f}x slower")
    print(f"Avg / Best   = {avg_comparisons / best_comparisons:.1f}x slower")


def compare_with_builtin():
    """
    Compares Insertion Sort with Python's built-in sorted().
    """
    import random
    
    sizes = [100, 500, 1000, 2000]
    
    print("=" * 60)
    print("Comparison: Insertion Sort vs. Python's sorted()")
    print("=" * 60)
    print(f"{'n':>8} | {'Insertion Sort':>15} | {'sorted()':>15} | {'Speedup':>10}")
    print("-" * 60)
    
    for n in sizes:
        arr = random.sample(range(n * 10), n)
        
        # Measure Insertion Sort
        arr_copy = arr.copy()
        start = time.perf_counter()
        insertion_sort(arr_copy)
        insertion_time = time.perf_counter() - start
        
        # Measure built-in sorted()
        arr_copy = arr.copy()
        start = time.perf_counter()
        sorted(arr_copy)
        sorted_time = time.perf_counter() - start
        
        speedup = insertion_time / sorted_time if sorted_time > 0 else float('inf')
        
        print(f"{n:>8} | {insertion_time*1000:>12.3f} ms | {sorted_time*1000:>12.3f} ms | {speedup:>8.1f}x")
    
    print()
    print("Note: Python's sorted() uses Timsort (hybrid of Merge + Insertion Sort)")


# ============================================================================
# BUGGY VERSION - For Debugging Exercise
# ============================================================================

def insertion_sort_buggy(arr: List[int]) -> List[int]:
    """
    WARNING: This version contains an off-by-one error!
    
    Find the bug and fix it.
    
    Hint: Test with various arrays:
    - [5, 2, 4, 6, 1, 3]
    - [3, 2, 1]
    - [1, 2, 3]
    - [1]
    - []
    """
    # BUG 1: Wrong start condition in outer loop
    for i in range(0, len(arr)):  # Should start at 1!
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def insertion_sort_buggy_v2(arr: List[int]) -> List[int]:
    """
    WARNING: This version contains a different off-by-one error!
    
    Find the bug and fix it.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # BUG 2: Wrong condition - missing >= 0
        while j > 0 and arr[j] > key:  # Should be j >= 0!
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def insertion_sort_buggy_v3(arr: List[int]) -> List[int]:
    """
    WARNING: This version contains yet another bug!
    
    Find the bug and fix it.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            # BUG 3: j is not decremented -> infinite loop!
            # j -= 1  # This line is missing!
        arr[j + 1] = key
    return arr


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n🎓 Insertion Sort - Live Coding Session\n")
    
    # Test 1: Simple test
    test_array = [5, 2, 4, 6, 1, 3]
    print(f"Original: {test_array}")
    
    result = insertion_sort(test_array.copy())
    if result:
        print(f"Sorted: {result}")
    else:
        print("❌ insertion_sort() not implemented yet!")
    
    print()
    
    # Test 2: Performance analysis
    print("Run analyze_performance() to see best/worst-case.")
    print("Run compare_with_builtin() to compare with sorted().")
