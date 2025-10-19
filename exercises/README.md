# Exercises

This folder contains starter code and exercise templates for the algorithms course.

## Structure (current)

- **data_structures/**: Exercises on fundamental data structures
  - `vector.py` - Vector class with operator overloading
  - `doubly_linked_list.py` - Doubly linked list implementation

- **dynamic_programming/**: Exercises on dynamic programming algorithms
  - `fibonacci.py` - Fibonacci sequence using tabulation and memoization
  - `knapsack.py` - 0/1 Knapsack problem
  - `coin_change.py` - Coin change problem

## How to Use

1. Open the exercise file you want to work on
2. Read the docstrings carefully to understand the requirements
3. Implement the functions marked with `# TODO:`
4. Run the corresponding tests in the `/tests` folder to verify your solution
5. Check the `/examples` folder for usage examples

## Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_fibonacci.py

# Run with verbose output
pytest -v tests/
```

## Getting Help

- Read the docstrings and examples in each file
- Check the `/examples` folder for usage patterns
- If you're really stuck, you can check the `/solutions` folder (but try on your own first!)

## Tips

- Start with the simpler exercises (fibonacci, vector) before moving to more complex ones
- Draw diagrams to understand the problem, especially for data structures
- Test your code frequently with the provided test files
- Don't hesitate to add your own test cases
