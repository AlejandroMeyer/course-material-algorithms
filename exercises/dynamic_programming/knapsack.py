"""
0/1 Knapsack Problem - Dynamic Programming Exercise

Solve the 0/1 knapsack problem using dynamic programming.
Given weights and values of n items, put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.
"""

import numpy as np

def knapsack(W, wt, val, n):
    """
    Computes the maximum value that can be put in a knapsack of a given capacity.

    This function uses dynamic programming to solve the 0/1 knapsack problem.

    Args:
        W (int): The maximum capacity of the knapsack.
        wt (List[int]): A list of weights of the items.
        val (List[int]): A list of values of the items.
        n (int): The number of items.

    Returns:
        int: The maximum value that can be put in the knapsack.

    Example:
        >>> W = 50
        >>> wt = [10, 20, 30]
        >>> val = [60, 100, 120]
        >>> n = len(wt)
        >>> knapsack(W, wt, val, n)
        220
    """
    # TODO: Implement the knapsack algorithm
    # Hint: Create a 2D DP array where dp[i][w] represents the maximum value
    # that can be obtained with first i items and weight limit w
    pass

def knapsack_np(W, wt, val, n):
    """
    Computes the maximum value that can be put in a knapsack of a given capacity.
    This version uses NumPy arrays.

    Args:
        W (int): The maximum capacity of the knapsack.
        wt (List[int]): A list of weights of the items.
        val (List[int]): A list of values of the items.
        n (int): The number of items.

    Returns:
        int: The maximum value that can be put in the knapsack.

    See Also:
        knapsack: The original function knapsack(W, wt, val, n), which solves the same without using numpy.
    """
    # TODO: Implement the knapsack algorithm using NumPy
    # Hint: Use np.zeros() to create the DP array
    pass

def knapsack_np_ext(W, wt, val):
    """
    Computes the maximum value that can be put in a knapsack of a given capacity.
    Extended version that doesn't require n as parameter.

    Args:
        W (int): The maximum capacity of the knapsack.
        wt (List[int]): A list of weights of the items.
        val (List[int]): A list of values of the items.

    Returns:
        int: The maximum value that can be put in the knapsack.

    Raises:
        ValueError: If the lengths of wt and val are not equal.

    Example:
        >>> W = 50
        >>> wt = [10, 20, 30]
        >>> val = [60, 100, 120]
        >>> knapsack_np_ext(W, wt, val)
        220
    """
    # TODO: Implement the extended knapsack algorithm
    # Hint: First validate that len(wt) == len(val)
    # Then calculate n from the length of wt
    pass
