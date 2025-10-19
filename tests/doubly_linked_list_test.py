import pytest
from exercises.data_structures.doubly_linked_list import DoublyLinkedList

@pytest.fixture
def dll():
    return DoublyLinkedList()

def test_append(dll):
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert dll.to_list_forward() == [1, 2, 3]
    assert dll.to_list_backward() == [3, 2, 1]

def test_prepend(dll):
    dll.prepend(3)
    dll.prepend(2)
    dll.prepend(1)
    assert dll.to_list_forward() == [1, 2, 3]
    assert dll.to_list_backward() == [3, 2, 1]

def test_delete_head(dll):
    dll.append(1)
    dll.append(2)
    dll.delete(1)
    assert dll.to_list_forward() == [2]
    assert dll.to_list_backward() == [2]

def test_delete_tail(dll):
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.delete(3)
    assert dll.to_list_forward() == [1, 2]
    assert dll.to_list_backward() == [2, 1]

def test_delete_middle(dll):
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.delete(2)
    assert dll.to_list_forward() == [1, 3]
    assert dll.to_list_backward() == [3, 1]

def test_delete_non_existent(dll):
    dll.append(1)
    dll.append(2)
    dll.delete(4)  # Attempt to delete a non-existent element
    assert dll.to_list_forward() == [1, 2]
    assert dll.to_list_backward() == [2, 1]

@pytest.mark.parametrize("initial_data, data, position, expected_forward, expected_backward", [
    ([], 5, 0, [5], [5]),                        # Insert into empty list
    ([5], 1, 0, [1, 5], [5, 1]),                 # Insert at head when list has elements
    ([1, 5], 2, 1, [1, 2, 5], [5, 2, 1]),        # Insert in the middle
    ([1, 2, 5], 6, 3, [1, 2, 5, 6], [6, 5, 2, 1]), # Insert at the end
    ([1, 2, 5, 6], 3, 2, [1, 2, 3, 5, 6], [6, 5, 3, 2, 1]), # Insert in between
])
def test_insert(dll, initial_data, data, position, expected_forward, expected_backward):
    # Initialisiert die Liste mit initial_data
    for value in initial_data:
        dll.append(value)
    
    # Führt den Insert aus
    dll.insert(data, position)
    
    # Überprüft das Ergebnis in Vorwärts- und Rückwärtsrichtung
    assert dll.to_list_forward() == expected_forward
    assert dll.to_list_backward() == expected_backward