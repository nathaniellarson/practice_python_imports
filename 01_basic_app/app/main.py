"""
Main application module.
"""

from app.utils import add_numbers, capitalize_string

def process_data(numbers: tuple[int, int], text: str) -> tuple[int, str]:
    """
    Process numbers and text using utility functions.
    
    Args:
        numbers: Tuple of two integers
        text: Input string to capitalize
        
    Returns:
        Tuple containing the sum of numbers and capitalized text
    """
    result_sum = add_numbers(*numbers)
    result_text = capitalize_string(text)
    return result_sum, result_text

def main():
    """Main function to demonstrate the application."""
    numbers = (5, 3)
    text = "hello world"
    result_sum, result_text = process_data(numbers, text)
    print(f"Sum: {result_sum}")
    print(f"Capitalized text: {result_text}")

if __name__ == "__main__":
    main() 