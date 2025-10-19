# Algorithms and Data Structures: Examples and Exercises with Python

Welcome to the **Algorithms and Data Structures** repository! This collection includes Python scripts, Jupyter Notebooks, and practical exercises to support learning foundational programming concepts and techniques, including algorithms, data structures, and testing.

## 📚 Contents

- **Examples**: Hands-on Python examples that cover core concepts in algorithms and data structures.
- **Notebooks**: Interactive Jupyter Notebooks to explore and run code directly.
- **Exercises**: Starter code and templates for practicing algorithms and data structures.
- **Solutions**: Complete solutions to all exercises (for reference after attempting exercises).
- **Tests**: Unit tests to verify your implementations.

## 🚀 Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   - Python 3.9+
   - Required libraries (for testing and notebooks):
     ```bash
     pip install -r requirements.txt
     ```
   - Example `requirements.txt` includes:
     ```bash
     jupyter
     pytest
     hypothesis
     pandas
     ```

> 💡 **Hint**: **Colab** comes with many libraries pre-installed, including popular ones like `numpy`, `pandas`, and `matplotlib`. This allows you to start coding without additional setup.

## 📝 Usage

### Working on Exercises

1. **Start with an exercise**:
   ```bash
   # Open an exercise file
   code exercises/dynamic_programming/fibonacci.py
   ```

2. **Read the requirements** in the docstrings and implement the TODOs

3. **Run tests to verify your solution**:
   ```bash
   # Run tests for your implementation
   pytest tests/dp_fibonacci_test.py -v
   ```

4. **Compare with solutions** (only after attempting!):
   ```bash
   # Check the solution
   code solutions/dynamic_programming/dp_fibonacci.py
   ```

### Running Examples

- **Python Scripts**: Run any example directly from the `examples/` directory.
  ```bash
  python examples/stack_usage.py
  python examples/dynamic_fibonacci.py
  ```

### Exploring Notebooks

- **Notebook Exploration**: Navigate through the Notebooks for interactive code exploration and explanations.
  ```bash
  jupyter notebook notebooks/
  ```
  
> 💡 **Hint**: You can initialize Jupyter Notebooks directly in **VS Code**. Google Colab also uses the Jupyter Notebook environment, so the interface will feel familiar.

## 🧪 Testing

This repository includes examples of testing with different frameworks:
- **unittest** - Built-in framework for basic unit testing.
- **pytest** - For parameterized tests and flexible testing.
- **hypothesis** - Property-based testing to explore edge cases.

Example:
```bash
pytest tests/test_gcd.py
```

## 🧩 Structure of the Repository

```
algorithms-course-material/
├── examples/          # Standalone Python examples
│   ├── stack.py
│   ├── dynamic_fibonacci.py
│   └── ...
├── exercises/         # Starter code for exercises
│   ├── dynamic_programming/
│   │   ├── fibonacci.py
│   │   ├── knapsack.py
│   │   └── coin_change.py
│   └── data_structures/
│       ├── vector.py
│       └── doubly_linked_list.py
├── solutions/         # Complete solutions (check after attempting!)
│   ├── dynamic_programming/
│   └── data_structures/
├── tests/             # Unit tests for exercises
│   ├── dp_fibonacci_test.py
│   ├── dp_knapsack_test.py
│   └── ...
└── notebooks/         # Interactive Jupyter Notebooks
    ├── 0_python101.ipynb
    ├── 1_python101.ipynb
    └── ...
```

### Directory Details

- **examples/** - Contains standalone Python scripts with examples on:
  - Basic data types and functions
  - Variable scope and modules
  - Algorithms like GCD, sorting, and search methods
  - Stack implementations and usage

- **exercises/** - Starter code for practice:
  - Function signatures with TODO comments
  - Comprehensive docstrings with examples
  - Clear requirements for each exercise
  - Organized by topic (dynamic_programming, data_structures)

- **solutions/** - Complete implementations:
  - ⚠️ Only look after attempting exercises yourself!
  - Reference implementations for comparison
  - Alternative approaches and optimizations

- **tests/** - Unit tests for verification:
  - Pytest-based test suites
  - Test your implementations before checking solutions
  - Examples of parameterized testing

- **notebooks/** - Jupyter Notebooks covering:
  - Interactive explanations and code samples
  - Visualizations for sorting, searching, and graph algorithms
  - Testing demonstrations using `unittest`, `pytest`, and `hypothesis`

## 📖 Further Reading and Resources

You will find mor literature in our slides, exercises and notebooks.

- **Python Documentation**:
  - [Python Data Types](https://docs.python.org/3/library/stdtypes.html)
  - [unittest Documentation](https://docs.python.org/3/library/unittest.html)
- **Books**:
  - *Think Python: How to Think Like a Computer Scientist*
  - *Python Data Science Handbook* by Jake VanderPlas

## 🤝 Contributing

Feel free to submit issues or contribute by creating pull requests! Contributions to add more examples, exercises, or improve the documentation are welcome.
