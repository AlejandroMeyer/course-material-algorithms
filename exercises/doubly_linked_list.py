# Implementation of a Doubly Linked List in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        """Insert a node with data at a specific position."""
        new_node = Node(data)
        if position == 0:
            self.prepend(data)
            return
        curr = self.head
        index = 0
        while curr and index < position - 1:
            curr = curr.next
            index += 1
        if curr is None:
            self.append(data)  # If position is out of range, append at the end
        else:
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node

    def append(self, data):
        """Add a node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        """Add a node at the beginning of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete a node with a specific value."""
        if self.head is None:
            return
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr == self.head:  # If deleting the head node
                    self.head = curr.next
                curr = None  # Free the memory
                return
            curr = curr.next

    def to_list_forward(self):
        """Return the list elements in forward order."""
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

    def to_list_backward(self):
        """Return the list elements in backward order."""
        elements = []
        curr = self.head
        if curr is None:
            return elements
        while curr.next:
            curr = curr.next
        while curr:
            elements.append(curr.data)
            curr = curr.prev
        return elements

