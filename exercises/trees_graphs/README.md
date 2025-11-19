# Trees, Heaps, and Graphs - Exercises

This folder contains programming exercises for the Trees, Heaps, and Graphs chapter.

## Exercises

### 1. Binary Search Tree (BST) Implementation
**File:** `binary_search_tree.py`

Implement a Binary Search Tree with the following operations:
- `insert(data)`: Insert a node
- `search(key)`: Search for a node
- `delete(key)`: Delete a node
- `in_order_traversal()`: Return in-order traversal

**Points:** 10

### 2. Min-Heap with Python's heapq Module
**File:** `min_heap.py`

Implement a min-heap using Python's `heapq` module with:
- `heappush(item)`: Insert an item
- `heappop()`: Remove and return the smallest item
- `change_priority(item)`: Change the priority of an item

**Points:** 10

### 3. BFS and DFS on a Graph
**File:** `bfs_dfs.py`

Implement both Breadth-First Search (BFS) and Depth-First Search (DFS) on an undirected graph. Demonstrate their differences by applying them to the provided graph.

**Points:** 15

### 4. Dijkstra's Algorithm
**File:** `dijkstra.py`

This exercise consists of three parts:
1. **Manual Calculation (5 points):** Calculate shortest paths manually for Graph 1
2. **Implementation (10 points):** Implement Dijkstra's algorithm
3. **Application (5 points):** Apply to Graph 2

**Total Points:** 20

## Running the Exercises

To work on an exercise:
1. Open the corresponding file in `exercises/trees_graphs/`
2. Read the docstring and hints
3. Implement the required functions (look for `TODO` comments)
4. Test your implementation

## Testing

Run the tests for your exercises:

```bash
# Test a specific exercise
pytest tests/bst_test.py
pytest tests/min_heap_test.py
pytest tests/bfs_dfs_test.py
pytest tests/dijkstra_test.py

# Run all tests
pytest tests/
```

## Getting Help

- Check the hints in each exercise file
- Review the lecture materials on Trees, Heaps, and Graphs
- Refer to the solution files in `solutions/trees_graphs/` if you get stuck
- Make sure to understand the solution before moving on

## Tips

1. **Binary Search Tree:** Remember the BST property - left subtree contains smaller values, right subtree contains larger values
2. **Min-Heap:** The `heapq` module implements a min-heap by default
3. **BFS vs DFS:** BFS uses a queue (FIFO), DFS uses a stack or recursion (LIFO)
4. **Dijkstra's Algorithm:** Use a priority queue to always process the node with the smallest distance
