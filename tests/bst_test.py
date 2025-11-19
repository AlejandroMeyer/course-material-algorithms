"""
Tests for Binary Search Tree implementation.
"""

import pytest
from exercises.trees_graphs.binary_search_tree import BinarySearchTree


def test_bst_insert_and_traversal():
    """Test BST insertion and in-order traversal."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(3)
    bst.insert(7)
    bst.insert(15)
    bst.insert(25)

    # Check in-order traversal (should be sorted)
    assert bst.in_order_traversal() == [3, 5, 7, 10, 15, 20, 25]


def test_bst_search():
    """Test BST search functionality."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(3)
    bst.insert(7)

    # Search for existing elements
    assert bst.search(10) == True
    assert bst.search(5) == True
    assert bst.search(20) == True
    assert bst.search(3) == True
    assert bst.search(7) == True

    # Search for non-existing elements
    assert bst.search(15) == False
    assert bst.search(1) == False
    assert bst.search(100) == False


def test_bst_delete_leaf():
    """Test deleting a leaf node (no children)."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(3)

    bst.delete(3)
    assert bst.in_order_traversal() == [5, 10, 20]
    assert bst.search(3) == False


def test_bst_delete_one_child():
    """Test deleting a node with one child."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(3)

    bst.delete(5)
    assert bst.in_order_traversal() == [3, 10, 20]
    assert bst.search(5) == False


def test_bst_delete_two_children():
    """Test deleting a node with two children."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(3)
    bst.insert(7)
    bst.insert(15)
    bst.insert(25)

    bst.delete(20)
    result = bst.in_order_traversal()
    assert result == [3, 5, 7, 10, 15, 25]
    assert bst.search(20) == False


def test_bst_delete_root():
    """Test deleting the root node."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)

    bst.delete(10)
    result = bst.in_order_traversal()
    assert 10 not in result
    assert len(result) == 2
    assert 5 in result and 20 in result


def test_bst_empty_tree():
    """Test operations on an empty tree."""
    bst = BinarySearchTree()
    assert bst.in_order_traversal() == []
    assert bst.search(10) == False


def test_bst_single_element():
    """Test BST with a single element."""
    bst = BinarySearchTree()
    bst.insert(42)
    assert bst.in_order_traversal() == [42]
    assert bst.search(42) == True
    
    bst.delete(42)
    assert bst.in_order_traversal() == []
