"""
Implement BFS and DFS on a Graph

Implement both Breadth-First Search (BFS) and Depth-First Search (DFS) on an 
undirected graph using Python. Demonstrate their differences by applying them 
to the following graph:

    A -- B -- C -- D
    |
    E -- F -- G

Hint:
BFS uses a queue (FIFO) to explore nodes level by level, while DFS uses a stack 
(LIFO) or recursion to explore as deep as possible before backtracking. The order 
in which nodes are visited will differ between the two algorithms.

Task:
1. Implement the BFS function
2. Implement the DFS function
3. Test both algorithms starting from node 'A'
"""


# Graph representation (adjacency list)
graph = {
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C'],
    'E': ['A', 'F'],
    'F': ['E', 'G'],
    'G': ['F']
}


def bfs(graph, start):
    """
    Perform Breadth-First Search on the graph.
    
    Args:
        graph: A dictionary representing the graph as an adjacency list.
        start: The starting node for the search.
        
    Returns:
        A list of nodes in the order they were visited.
    """
    # TODO: Implement BFS
    # Hint: Use a queue (list with pop(0)) to track nodes to visit
    # Keep track of visited nodes to avoid cycles
    pass


def dfs(graph, node, visited=None):
    """
    Perform Depth-First Search on the graph.
    
    Args:
        graph: A dictionary representing the graph as an adjacency list.
        node: The current node being visited.
        visited: A list of already visited nodes (used in recursion).
        
    Returns:
        A list of nodes in the order they were visited.
    """
    # TODO: Implement DFS (recursive approach)
    # Hint: Use recursion to explore as deep as possible before backtracking
    # Keep track of visited nodes to avoid cycles
    pass


# TODO: Test your implementation
# print("BFS starting from A:", bfs(graph, 'A'))
# print("DFS starting from A:", dfs(graph, 'A'))

# Expected outputs:
# BFS: ['A', 'B', 'E', 'C', 'F', 'D', 'G']
# DFS: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
