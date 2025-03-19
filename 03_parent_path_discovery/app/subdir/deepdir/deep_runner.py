"""
Module in deep directory that imports from root app.
"""

from app.utils import format_message, get_version

def run():
    """Run function from deep directory."""
    message = format_message("Hello from deep directory!")
    version = get_version()
    print(f"{message} (v{version})")

if __name__ == "__main__":
    run() 