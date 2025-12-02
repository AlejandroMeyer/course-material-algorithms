"""
Dijkstra's Algorithm for Shortest Path

This exercise consists of three parts:

1. Manual Calculation: Calculate the shortest path from node A to all other nodes 
   manually for Graph 1 (defined below). Show your work step by step.

2. Implementation: Implement Dijkstra's algorithm in Python to find the shortest 
   path from a starting node to all other nodes in a weighted graph.

3. Application: Apply your implementation to find the shortest paths from node A 
   in Graph 2 (defined below).

Hint:
Dijkstra's algorithm uses a priority queue (min-heap) to always select the node 
with the smallest tentative distance. Keep track of distances in a dictionary and 
update them as you find shorter paths. The algorithm only works with non-negative 
edge weights.
"""

import heapq


# Graph 1 (simple directed graph for manual calculation)
# A --2--> B --5--> C
# |                 ^
# 1                 |
# v                 2
# D ----------------+
graph1 = {
    'A': [('B', 2), ('D', 1)],
    'B': [('C', 5)],
    'C': [],
    'D': [('C', 2)]
}


# Graph 2 (extended undirected graph)
# More complex graph with 8 nodes (A through H)
graph2 = {
    'A': [('B', 3), ('D', 6)],
    'B': [('A', 3), ('C', 2), ('E', 7)],
    'C': [('B', 2), ('D', 6), ('F', 3), ('G', 5), ('E', 4)],
    'D': [('A', 6), ('C', 6)],
    'E': [('B', 7), ('C', 4), ('G', 2), ('H', 5)],
    'F': [('C', 3), ('G', 6)],
    'G': [('C', 5), ('E', 2), ('F', 6), ('H', 6)],
    'H': [('E', 5), ('G', 6)]
}


def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding shortest paths.
    
    Args:
        graph: Dictionary mapping nodes to list of (neighbor, weight) tuples
        start: Starting node
    
    Returns:
        Dictionary mapping each node to its shortest distance from start
    """
    # TODO: Implement Dijkstra's algorithm
    # 1. Initialize distances dictionary with infinity for all nodes except start
    # 2. Use a priority queue (min-heap) to track (distance, node) pairs
    # 3. While the queue is not empty:
    #    - Pop the node with smallest distance
    #    - For each neighbor, calculate new distance
    #    - If new distance is shorter, update and add to queue
    # 4. Return the distances dictionary
    pass


# Part 1: Manual Calculation for Graph 1
# TODO: Write down your step-by-step manual calculation here as comments:
# Step 1: Initialize distances = {A: 0, B: inf, C: inf, D: inf}, visited = {}
# Step 2: ...
# Step 3: ...
# Final result: {A: 0, B: ?, C: ?, D: ?}


# Part 2 & 3: Test your implementation
if __name__ == "__main__":
    print("=== Part 2: Testing Dijkstra's Algorithm ===\n")
    
    # Test with Graph 1
    print("Graph 1 - Shortest distances from A:")
    # TODO: Uncomment and run
    # result1 = dijkstra(graph1, 'A')
    # print(result1)
    # Expected: {'A': 0, 'B': 2, 'C': 3, 'D': 1}
    
    print("\n=== Part 3: Application to Graph 2 ===\n")
    
    # Apply to Graph 2
    print("Graph 2 - Shortest distances from A:")
    # TODO: Uncomment and run
    # result2 = dijkstra(graph2, 'A')
    # for node in sorted(result2.keys()):
    #     print(f"  {node}: {result2[node]}")
    
    # Expected output:
    # A: 0
    # B: 3
    # C: 5
    # D: 6
    # E: 9
    # F: 8
    # G: 10
    # H: 14
