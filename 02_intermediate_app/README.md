# Intermediate Python Application with Submodules

This is a more complex Python application that demonstrates advanced package structure, submodules, and proper import mechanisms. The application simulates a system with user authentication, analytics tracking, and database operations.

## Application Structure
```
02_intermediate_app/
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

## Features
- Configuration management with dataclasses
- Database connection handling
- User authentication service
- Analytics event tracking
- Comprehensive unit tests with pytest
- Proper package structure with submodules

## Running the Application

1. Ensure you're in the `02_intermediate_app` directory
2. Run the main application:
   ```bash
   python -m app.main
   ```
   This will:
   - Connect to the database
   - Authenticate a test user
   - Track a login event
   - Display user events

3. Run the unit tests:
   ```bash
   pytest tests/
   ```

## Understanding the Imports

### Package Structure
- The application is organized into three main submodules:
  - `config`: Configuration management
  - `data`: Data models and database operations
  - `services`: Business logic services

### Import Mechanisms

1. **Absolute Imports**
   ```python
   from app.data import Database
   from app.services import AuthService
   ```
   Used in `main.py` to import from the root package.

2. **Relative Imports**
   ```python
   from ..config import config
   from ..data import User
   ```
   Used within submodules to import from parent or sibling modules.

3. **Package-Level Imports**
   ```python
   from .models import User, AnalyticsEvent
   from .database import Database
   ```
   Used in `__init__.py` files to expose module contents.

### Why These Imports Work

1. **Package Recognition**
   - Each directory containing `__init__.py` is recognized as a Python package
   - The root `app` directory is the main package
   - Subdirectories (`config`, `data`, `services`) are subpackages

2. **Import Resolution**
   - When running `python -m app.main`, Python adds the parent directory to the Python path
   - This allows absolute imports from the root package
   - Relative imports work because Python knows the package hierarchy

3. **Test Imports**
   - Tests use absolute imports from the `app` package
   - The test directory is a separate package
   - pytest adds the current directory to the Python path

### Best Practices Demonstrated

1. **Package Organization**
   - Clear separation of concerns
   - Logical grouping of related functionality
   - Proper use of `__init__.py` files

2. **Import Style**
   - Use absolute imports for clarity
   - Use relative imports within packages
   - Explicit imports in `__init__.py` files

3. **Testing**
   - Separate test package
   - Use of pytest fixtures
   - Comprehensive test coverage

This structure provides a solid foundation for a larger application while maintaining clean code organization and proper Python packaging practices. 