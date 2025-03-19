"""
Utility functions for the application.
"""

def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b

def capitalize_string(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text: Input string
        
    Returns:
        String with first letter of each word capitalized
    """
    return ' '.join(word.capitalize() for word in text.split()) 