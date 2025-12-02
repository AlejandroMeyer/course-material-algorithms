"""
Min-Heap Implementation with Python's heapq Module

Using Python's heapq module, implement a min-heap that supports the following operations:
- heappush(item): Inserts an item into the heap.
- heappop(): Removes and returns the smallest item from the heap.
- change_priority(item): Change the priority of an item in the heap.

Hint:
The heapq module provides an implementation of the heap queue algorithm (priority queue). 
Note that heapq implements a min-heap by default. To change priority, you'll need to 
remove the old item and insert the new one, then re-heapify.

Task:
Complete the MinHeap class below to demonstrate the functionality of the min-heap.
"""

import heapq


class MinHeap:
    """A min-heap implementation using Python's heapq module."""
    
    def __init__(self):
        """Initialize an empty heap."""
        self.heap = []
    
    def heappush(self, item):
        """
        Insert an item into the heap.
        
        Args:
            item: The item to insert.
        """
        # TODO: Implement this method
        pass
    
    def heappop(self):
        """
        Remove and return the smallest item from the heap.
        
        Returns:
            The smallest item in the heap.
            
        Raises:
            IndexError: If the heap is empty.
        """
        # TODO: Implement this method
        pass
    
    def change_priority(self, old_item, new_item):
        """
        Change the priority of an item in the heap.
        
        Args:
            old_item: The item to remove.
            new_item: The new item to insert.
        """
        # TODO: Implement this method
        pass
    
    def peek(self):
        """
        Return the smallest item without removing it.
        
        Returns:
            The smallest item in the heap, or None if empty.
        """
        # TODO: Implement this method
        pass
    
    def __len__(self):
        """Return the number of items in the heap."""
        return len(self.heap)
    
    def __repr__(self):
        """Return a string representation of the heap."""
        return f"MinHeap({self.heap})"


# TODO: Add demonstration code here showing:
# 1. Creating a heap
# 2. Inserting elements
# 3. Removing the smallest element
# 4. Changing priority of an element
# 5. Displaying the heap state after each operation
