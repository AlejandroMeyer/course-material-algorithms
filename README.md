# Algorithms and Data Structures: Examples and Exercises with Python

Welcome to the **Algorithms and Data Structures** repository! This collection includes Python scripts, Jupyter Notebooks, and practical exercises to support learning foundational programming concepts and techniques, including algorithms, data structures, and testing.

## 📚 Contents

- **Examples**: Hands-on Python examples that cover core concepts in algorithms and data structures.
- **Notebooks**: Interactive Jupyter Notebooks to explore and run code directly.
- **Exercises**: Practical tasks and challenges to reinforce understanding.

## 🧩 Structure of the Repository

- **examples/** - Contains standalone Python scripts with examples on:
  - Basic data types and functions
  - Variable scope and modules
  - Algorithms like GCD, sorting, and search methods

- **notebooks/** - Jupyter Notebooks covering:
  - Interactive explanations and code samples
  - Visualizations for sorting, searching, and graph algorithms
  - Testing demonstrations using `unittest`, `pytest`, and `hypothesis`

- **exercises/** - Tasks and problem sets for practice:
  - Basic to advanced exercises with hints
  - Guided problems to apply concepts
  - Solutions included in a separate `solutions/` folder for reference

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

3. **Run Jupyter Notebooks**:
   Launch Jupyter Notebook to explore the notebooks interactively:
   ```bash
   jupyter notebook
   ```
> 💡 **Hint**: You can initialize Jupyter Notebooks directly in **VS Code**. Google Colab also uses the Jupyter Notebook environment, so the interface will feel familiar.

## 📝 Usage

- **Python Scripts**: Run any example directly from the `examples/` directory.
  ```bash
  python examples/gcd_example.py
  ```
- **Notebook Exploration**: Navigate through the Notebooks for interactive code exploration and explanations.
- **Exercises**: Solve problems in the `exercises/` folder. Solutions are available in the `solutions/` folder for reference after attempting the exercises.

## 🧪 Testing

This repository includes examples of testing with different frameworks:
- **unittest** - Built-in framework for basic unit testing.
- **pytest** - For parameterized tests and flexible testing.
- **hypothesis** - Property-based testing to explore edge cases.

Example:
```bash
pytest tests/test_gcd.py
```

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
