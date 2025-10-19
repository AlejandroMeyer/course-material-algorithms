"""
Fibonacci - Dynamic Programming Exercise

Implement the Fibonacci sequence using two different approaches:
1. Tabulation (Bottom-Up)
2. Memoization (Top-Down)
"""

def fibonacci_tab(n):
    """
    Calculate the nth Fibonacci number using tabulation (bottom-up approach).
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> fibonacci_tab(5)
        5
        >>> fibonacci_tab(10)
        55
    """
    # TODO: Implement tabulation approach
    # Hint: Create a dp array and fill it iteratively
    pass

def fibonacci_memo(n, memo=None):
    """
    Calculate the nth Fibonacci number using memoization (top-down approach).
    
    Args:
        n (int): The position in the Fibonacci sequence
        memo (dict): Dictionary to store computed values
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> fibonacci_memo(5)
        5
        >>> fibonacci_memo(10)
        55
    """
    # TODO: Implement memoization approach
    # Hint: Use a dictionary to store previously computed values
    pass
