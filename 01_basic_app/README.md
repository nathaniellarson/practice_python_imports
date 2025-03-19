# Basic Python Application with Proper Imports

This is a simple Python application that demonstrates proper package structure and import mechanisms. The application includes utility functions for basic string manipulation and number operations, along with comprehensive unit tests.

## Application Structure
```
01_basic_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
└── tests/
    ├── __init__.py
    └── tests.py
```

## Running the Application

1. Ensure you're in the `01_basic_app` directory
2. Run the main application:
   ```bash
   python -m app.main
   ```
   This will output:
   - The sum of two numbers (5 + 3 = 8)
   - A capitalized version of "hello world"

3. Run the unit tests:
   ```bash
   python -m unittest tests/tests.py
   ```

## Understanding the Imports

### How Imports Work in This Application

1. **Package Structure**
   - The `app` directory is a Python package (marked by `__init__.py`)
   - The `tests` directory is also a package (marked by `__init__.py`)

2. **Import Mechanisms**
   - In `main.py`, we use absolute imports:
     ```python
     from app.utils import add_numbers, capitalize_string
     ```
   - In `tests.py`, we also use absolute imports:
     ```python
     from app.utils import add_numbers, capitalize_string
     from app.main import process_data
     ```

3. **Why These Imports Work**
   - When running the application with `python -m app.main`, Python adds the parent directory of `app` to the Python path
   - When running tests with `python -m unittest tests/tests.py`, Python adds the current directory to the Python path
   - This allows both the application and tests to use absolute imports from the `app` package

4. **Best Practices Demonstrated**
   - Using absolute imports instead of relative imports
   - Keeping tests in a separate package
   - Using `__init__.py` files to mark directories as packages
   - Running the application as a module with `-m` flag

This structure ensures that imports work consistently whether running the application or tests, and follows Python's recommended practices for package organization. 