# Tests

This folder contains test files for all exercises.

## Running Tests

### Run all tests
```bash
pytest tests/
```

### Run a specific test file
```bash
pytest tests/test_fibonacci.py
```

### Run with verbose output
```bash
pytest -v tests/
```

### Run with coverage report
```bash
pytest --cov=exercises --cov=solutions tests/
```

## Test Files

- `test_fibonacci.py` - Tests for Fibonacci implementations
- `test_knapsack.py` - Tests for Knapsack problem
- `test_vector.py` - Tests for Vector class
- `test_doubly_linked_list.py` - Tests for Doubly Linked List
- `test_doubly_linked_list_music.py` - Extended tests with music playlist example

## Writing Your Own Tests

Feel free to add your own test cases to better understand the problems and edge cases!

Example:
```python
def test_my_custom_case():
    # Your test here
    assert fibonacci_tab(15) == 610
```
