"""
Tests for Dijkstra's algorithm implementation.
"""

import pytest
from exercises.trees_graphs.dijkstra import dijkstra, graph1, graph2


def test_dijkstra_graph1():
    """Test Dijkstra's algorithm on Graph 1."""
    result = dijkstra(graph1, 'A')
    
    # Expected shortest distances
    assert result['A'] == 0
    assert result['B'] == 2
    assert result['C'] == 3
    assert result['D'] == 1


def test_dijkstra_graph2():
    """Test Dijkstra's algorithm on Graph 2."""
    result = dijkstra(graph2, 'A')
    
    # Expected shortest distances
    expected = {
        'A': 0,
        'B': 3,
        'C': 5,
        'D': 6,
        'E': 9,
        'F': 8,
        'G': 10,
        'H': 14
    }
    
    for node, distance in expected.items():
        assert result[node] == distance, f"Distance to {node} should be {distance}, got {result[node]}"


def test_dijkstra_single_node():
    """Test Dijkstra on a graph with a single node."""
    single = {'A': []}
    result = dijkstra(single, 'A')
    assert result['A'] == 0


def test_dijkstra_unreachable_nodes():
    """Test Dijkstra with unreachable nodes."""
    disconnected = {
        'A': [('B', 1)],
        'B': [],
        'C': []
    }
    result = dijkstra(disconnected, 'A')
    
    assert result['A'] == 0
    assert result['B'] == 1
    assert result['C'] == float('inf')  # Unreachable


def test_dijkstra_different_start_node():
    """Test Dijkstra starting from different nodes."""
    # Start from D in graph1
    result = dijkstra(graph1, 'D')
    
    assert result['D'] == 0
    assert result['C'] == 2
    assert result['A'] == float('inf')  # A is not reachable from D in directed graph
    assert result['B'] == float('inf')  # B is not reachable from D in directed graph


def test_dijkstra_symmetric_paths():
    """Test Dijkstra on a symmetric graph."""
    symmetric = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2)],
        'C': [('A', 4), ('B', 2)]
    }
    result = dijkstra(symmetric, 'A')
    
    assert result['A'] == 0
    assert result['B'] == 1
    assert result['C'] == 3  # Shorter path A->B->C (1+2=3) than A->C (4)


def test_dijkstra_multiple_paths():
    """Test Dijkstra finds the shortest among multiple paths."""
    multi_path = {
        'A': [('B', 5), ('C', 2)],
        'B': [('D', 1)],
        'C': [('B', 1), ('D', 5)],
        'D': []
    }
    result = dijkstra(multi_path, 'A')
    
    assert result['A'] == 0
    assert result['B'] == 3  # A->C->B is shorter (2+1=3) than A->B (5)
    assert result['C'] == 2
    assert result['D'] == 4  # A->C->B->D (2+1+1=4) is shorter than A->C->D (2+5=7)
