"""
Binary Search Tree (BST) Implementation

Implement a class BinarySearchTree in Python that supports the following operations:
- insert(data): Inserts a node with the specified data.
- search(key): Searches for a node with the given key.
- delete(key): Deletes the node with the given key.
- in_order_traversal(): Returns the in-order traversal of the tree.

Hint:
Remember that in a Binary Search Tree, the left subtree contains values less than 
the node, and the right subtree contains values greater than the node. For the 
delete() operation, consider the three cases: node with no children, node with one 
child, and node with two children.
"""


class Node:
    """A node in the binary search tree."""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """A Binary Search Tree implementation."""
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert a node with the specified data.
        
        Args:
            data: The data to insert into the tree.
        """
        # TODO: Implement this method
        pass
    
    def _insert(self, node, data):
        """
        Helper method to recursively insert data.
        
        Args:
            node: The current node in the recursion.
            data: The data to insert.
        """
        # TODO: Implement this method
        pass

    def search(self, key):
        """
        Search for a node with the given key.
        
        Args:
            key: The key to search for.
            
        Returns:
            True if the key is found, False otherwise.
        """
        # TODO: Implement this method
        pass
    
    def _search(self, node, key):
        """
        Helper method to recursively search for a key.
        
        Args:
            node: The current node in the recursion.
            key: The key to search for.
            
        Returns:
            True if the key is found, False otherwise.
        """
        # TODO: Implement this method
        pass

    def delete(self, key):
        """
        Delete the node with the given key.
        
        Args:
            key: The key of the node to delete.
        """
        # TODO: Implement this method
        pass
    
    def _delete(self, node, key):
        """
        Helper method to recursively delete a node.
        
        Args:
            node: The current node in the recursion.
            key: The key of the node to delete.
            
        Returns:
            The node after deletion.
        """
        # TODO: Implement this method
        pass
    
    def _find_min(self, node):
        """
        Find the minimum value node in a subtree.
        
        Args:
            node: The root of the subtree.
            
        Returns:
            The node with the minimum value.
        """
        # TODO: Implement this method
        pass

    def in_order_traversal(self):
        """
        Return the in-order traversal of the tree.
        
        Returns:
            A list of values in in-order sequence.
        """
        # TODO: Implement this method
        pass

    def _in_order_traversal(self, node, traversal):
        """
        Helper method to perform in-order traversal recursively.
        
        Args:
            node: The current node in the recursion.
            traversal: The list accumulating the traversal.
            
        Returns:
            The traversal list.
        """
        # TODO: Implement this method
        pass
