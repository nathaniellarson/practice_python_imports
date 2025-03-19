"""
Main application module.
"""

from app.utils import format_message, get_version

def main():
    """Main function."""
    message = format_message("Hello from main!")
    version = get_version()
    print(f"{message} (v{version})")

if __name__ == "__main__":
    main() 