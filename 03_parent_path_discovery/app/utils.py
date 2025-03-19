"""
Utility functions.
"""

def format_message(message: str) -> str:
    """Format a message with a prefix."""
    return f"[APP] {message}"

def get_version() -> str:
    """Get the application version."""
    return "1.0.0" 