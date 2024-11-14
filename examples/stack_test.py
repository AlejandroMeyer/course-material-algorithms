import pytest
from stack import Stack

# from your_module import Stack  # Uncomment this line and replace 'your_module' with the actual module name

# Fixture to create a new Stack instance for each test
@pytest.fixture
def stack():
    return Stack()

def test_push(stack):
    stack.push(10)
    assert stack.stack[-1] == 10  # Check if the last pushed item is correct

def test_pop(stack):
    stack.push(10)
    stack.push(20)
    assert stack.pop() == 20  # Check if the last item (LIFO) is popped
    assert stack.pop() == 10  # Check if the previous item is popped

def test_is_empty_on_new_stack(stack):
    assert stack.is_empty() is True  # New stack should be empty

def test_is_empty_after_push(stack):
    stack.push(1)
    assert stack.is_empty() is False  # Stack is not empty after pushing an item

def test_is_empty_after_pop(stack):
    stack.push(1)
    stack.pop()
    assert stack.is_empty() is True  # Stack should be empty after popping all elements

def test_pop_from_empty_stack(stack):
    assert stack.pop() is None  # Pop from an empty stack should return None