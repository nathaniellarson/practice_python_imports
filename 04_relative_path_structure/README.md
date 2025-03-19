# 04_relative_path_structure

> **Note**: This is a duplicate of the application from `02_intermediate_app`, but using relative imports instead of absolute imports. While this example demonstrates relative imports, they are generally not recommended in Python for several reasons:
> 
> 1. **Fragility**: Relative imports make code more fragile as they depend on the exact package structure. Moving or renaming modules can break imports.
> 
> 2. **Ambiguity**: Relative imports can be ambiguous, especially in larger projects. It's not always clear where the import is coming from.
> 
> 3. **Maintenance**: Absolute imports are easier to maintain and refactor. They make it clear exactly which module is being imported.
> 
> 4. **Testing**: Relative imports can make testing more difficult, especially when running tests from different directories.
> 
> The recommended approach is to use absolute imports (as shown in `02_intermediate_app`) and ensure your package is properly installed or in the Python path.

This example demonstrates a Python application using relative imports with a proper package structure.

## Directory Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── database.py
│   └── services/
│       ├── __init__.py
│       ├── auth.py
│       └── analytics.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_auth.py
    ├── test_analytics.py
    └── test_database.py
```

## Running the Application

To run the application, you must use the `-m` flag to ensure Python treats the directory as a package:

```bash
python -m app.main
```

## Running Tests

When using relative imports, running tests becomes problematic. Here are the different approaches and why they fail:

### Attempt 1: Running from current directory (fails)
```bash
python -m pytest tests/
```
This results in error: `ImportError: attempted relative import beyond top-level package`

### Attempt 2: Running from parent directory (fails)
```bash
cd ..
python -m pytest 04_relative_path_structure/tests/
```
This also results in error: `ImportError: attempted relative import beyond top-level package`

### Attempt 3: Using PYTHONPATH (fails)
```bash
# From the parent directory
PYTHONPATH=$PYTHONPATH:. python -m pytest 04_relative_path_structure/tests/
```
This also results in error: `ImportError: attempted relative import beyond top-level package`

### Why These Approaches Fail

The fundamental issue is that relative imports require a clear package hierarchy, but when running tests, Python's module resolution system doesn't maintain this hierarchy in the way we need. The test files are trying to use relative imports (`from ..app.data import Database`) but Python can't determine the correct parent package.

### Solution: Refactor to Absolute Imports

The only reliable solution is to refactor the test files to use absolute imports, as shown in `02_intermediate_app`. This would involve:

1. Changing imports in test files from:
   ```python
   from ..app.data import Database
   ```
   to:
   ```python
   from app.data import Database
   ```

2. Ensuring the package is properly installed or in the Python path

This is one of the main reasons why relative imports are generally not recommended - they can make testing significantly more difficult and require complex workarounds or refactoring.

## Key Points

1. **Relative Imports**: This example uses relative imports (e.g., `from ..app.data import Database`) to maintain proper package structure.

2. **Package Structure**: The application is organized into logical packages:
   - `config`: Configuration settings
   - `data`: Data models and database operations
   - `services`: Business logic services
   - `tests`: Test suite

3. **Import Behavior**: 
   - When running with `-m`, Python correctly resolves relative imports
   - When running directly, relative imports may fail due to Python's module resolution
   - When running tests, relative imports become problematic due to Python's package hierarchy requirements
