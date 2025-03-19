# Python Module Path Resolution Example

This example demonstrates how Python resolves imports when running modules from different directories. It shows that Python can find modules in parent directories when running a module as a script.

## Directory Structure
```
03_parent_path_discovery/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── subdir/
│       ├── __init__.py
│       ├── runner.py
│       └── deepdir/
│           ├── __init__.py
│           └── deep_runner.py
└── README.md
```

## Running the Example

1. From the root directory (`03_parent_path_discovery`):
   ```bash
   python -m app.main
   ```
   This will output:
   ```
   [APP] Hello from main! (v1.0.0)
   ```

2. From the subdirectory (`03_parent_path_discovery/app/subdir`):
   ```bash
   python runner.py
   ```
   This will fail with an error like:
   ```
   ModuleNotFoundError: No module named 'app'
   ```
   
   This fails because when running the script directly with `python runner.py`, Python adds only the current directory 
   (`03_parent_path_discovery/app/subdir`) to the Python path. The `app` package is in the parent directory, so Python 
   cannot find it.

   However, running it as a module works:
   ```bash
   python -m subdir.runner
   ```
   This will output:
   ```
   [APP] Hello from subdirectory! (v1.0.0)
   ```

3. From the deep directory (`03_parent_path_discovery/app/subdir/deepdir`):
   ```bash
   python deep_runner.py
   ```
   This will fail with:
   ```
   ModuleNotFoundError: No module named 'app'
   ```

   Running it as a module from the deep directory also fails:
   ```bash
   python -m deepdir.deep_runner
   ```
   This will fail with:
   ```
   ModuleNotFoundError: No module named 'app'
   ```
   
   This fails because Python adds `03_parent_path_discovery/app/subdir` to the path, but we need `03_parent_path_discovery` 
   to find the `app` package.

   To run the deep module successfully, you need to either:

   a. Run from the root directory:
   ```bash
   cd ../../..  # Go back to 03_parent_path_discovery
   python -m app.subdir.deepdir.deep_runner
   ```
   This will output:
   ```
   [APP] Hello from deep directory! (v1.0.0)
   ```

   b. Or use relative imports in deep_runner.py:
   ```python
   from ...utils import format_message, get_version
   ```

## How It Works

1. **Python's Module Search Path with -m Flag**
   - When you run a module with `python -m`, Python adds the parent directory of the specified module to the Python path
   - For example:
     - `python -m app.main` adds `03_parent_path_discovery` to the path
     - `python -m subdir.runner` adds `03_parent_path_discovery/app` to the path
     - `python -m deepdir.deep_runner` adds `03_parent_path_discovery/app/subdir` to the path
   - This is why absolute imports from the root package work in all cases

2. **Import Resolution**
   - In all modules, we use absolute imports:
     ```python
     from app.utils import format_message, get_version
     ```
   - Python looks for `app` in the module search path
   - It finds `app` in the parent directory that was added to the path
   - This allows the imports to work regardless of which directory you run from

3. **Why This Works**
   - Python's module system is designed to work with package hierarchies
   - When running a module as a script with `-m`, Python ensures the module can find its package
   - The parent directory of the specified module is added to the path, not the entire lineage
   - This is why we need to run from the correct directory level

This example demonstrates that Python's module system is flexible enough to handle imports from different directory levels, as long as the package structure is maintained and the correct parent directory is in the Python path. 