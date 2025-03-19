"""
Module in subdirectory that imports from parent app.
"""

from app.utils import format_message, get_version

def run():
    """Run function from subdirectory."""
    message = format_message("Hello from subdirectory!")
    version = get_version()
    print(f"{message} (v{version})")

if __name__ == "__main__":
    run() 