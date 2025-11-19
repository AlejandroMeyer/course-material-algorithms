"""
Tests for BFS and DFS implementations.
"""

import pytest
from exercises.trees_graphs.bfs_dfs import bfs, dfs


# Test graph (same as in the exercise)
graph = {
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C'],
    'E': ['A', 'F'],
    'F': ['E', 'G'],
    'G': ['F']
}


def test_bfs_starting_from_a():
    """Test BFS starting from node A."""
    result = bfs(graph, 'A')
    
    # Should visit all nodes
    assert len(result) == 7
    assert set(result) == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    
    # A should be first
    assert result[0] == 'A'
    
    # B and E should come before their descendants
    assert result.index('B') < result.index('C')
    assert result.index('E') < result.index('F')


def test_dfs_starting_from_a():
    """Test DFS starting from node A."""
    result = dfs(graph, 'A')
    
    # Should visit all nodes
    assert len(result) == 7
    assert set(result) == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    
    # A should be first
    assert result[0] == 'A'


def test_bfs_single_node():
    """Test BFS on a graph with a single node."""
    single_graph = {'A': []}
    result = bfs(single_graph, 'A')
    assert result == ['A']


def test_dfs_single_node():
    """Test DFS on a graph with a single node."""
    single_graph = {'A': []}
    result = dfs(single_graph, 'A')
    assert result == ['A']


def test_bfs_disconnected_component():
    """Test BFS on a graph with disconnected components."""
    disconnected = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = bfs(disconnected, 'A')
    # Should only visit A and B
    assert set(result) == {'A', 'B'}


def test_dfs_disconnected_component():
    """Test DFS on a graph with disconnected components."""
    disconnected = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = dfs(disconnected, 'A')
    # Should only visit A and B
    assert set(result) == {'A', 'B'}


def test_bfs_vs_dfs_order():
    """Test that BFS and DFS produce different orderings."""
    bfs_result = bfs(graph, 'A')
    dfs_result = dfs(graph, 'A')
    
    # Both should visit all nodes
    assert set(bfs_result) == set(dfs_result)
    
    # But the order should typically be different
    # (This might not always be true depending on implementation details,
    # but for this specific graph it should be)
    assert bfs_result != dfs_result
