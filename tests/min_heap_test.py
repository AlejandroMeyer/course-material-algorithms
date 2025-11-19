"""
Tests for Min-Heap implementation.
"""

import pytest
from exercises.trees_graphs.min_heap import MinHeap


def test_minheap_push_and_pop():
    """Test basic push and pop operations."""
    heap = MinHeap()
    heap.heappush(10)
    heap.heappush(5)
    heap.heappush(15)
    heap.heappush(3)

    assert heap.heappop() == 3
    assert heap.heappop() == 5
    assert heap.heappop() == 10
    assert heap.heappop() == 15


def test_minheap_peek():
    """Test peeking at the minimum element."""
    heap = MinHeap()
    assert heap.peek() is None

    heap.heappush(10)
    assert heap.peek() == 10

    heap.heappush(5)
    assert heap.peek() == 5

    heap.heappush(15)
    assert heap.peek() == 5


def test_minheap_change_priority():
    """Test changing priority of an element."""
    heap = MinHeap()
    heap.heappush(10)
    heap.heappush(5)
    heap.heappush(15)

    # Change 15 to 1 (should become new minimum)
    heap.change_priority(15, 1)
    assert heap.peek() == 1
    assert heap.heappop() == 1

    # Change 10 to 3
    heap.change_priority(10, 3)
    assert heap.heappop() == 3
    assert heap.heappop() == 5


def test_minheap_len():
    """Test heap length."""
    heap = MinHeap()
    assert len(heap) == 0

    heap.heappush(10)
    assert len(heap) == 1

    heap.heappush(5)
    heap.heappush(15)
    assert len(heap) == 3

    heap.heappop()
    assert len(heap) == 2


def test_minheap_empty_pop():
    """Test popping from an empty heap."""
    heap = MinHeap()
    with pytest.raises(IndexError):
        heap.heappop()


def test_minheap_order_property():
    """Test that the heap maintains the min-heap property."""
    heap = MinHeap()
    elements = [20, 15, 30, 10, 25, 5, 40]
    
    for elem in elements:
        heap.heappush(elem)
    
    # Pop all elements and verify they come out in sorted order
    result = []
    while len(heap) > 0:
        result.append(heap.heappop())
    
    assert result == sorted(elements)
