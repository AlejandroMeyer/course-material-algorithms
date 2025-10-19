"""
Coin Change Problem - Dynamic Programming Exercise

Find the minimum number of coins required to make a given amount
using the given denominations.
"""

def coin_change(coins, amount):
    """
    Computes the minimum number of coins required to make a given amount using the given denominations.

    This function uses dynamic programming to solve the coin change problem.

    Args:
        coins (List[int]): A list of coin denominations.
        amount (int): The total amount of money.

    Returns:
        int: The minimum number of coins required to make the given amount, or -1 if it is not possible.

    Example:
        >>> coins = [1, 2, 5]
        >>> amount = 11
        >>> coin_change(coins, amount)
        3
    """
    # TODO: Implement the coin change algorithm
    # Hint: Initialize a dp array with infinity for all values except dp[0] = 0
    # For each coin and each amount, calculate the minimum number of coins needed
    pass
