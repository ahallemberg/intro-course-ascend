"""
Utility functions for the calculator module.
"""


def validate_numbers(*args):
    """
    Validate that all arguments are numbers.
    
    Args:
        *args: Variable number of arguments to validate
        
    Raises:
        TypeError: If any argument is not a number
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Expected number, got {type(arg).__name__}: {arg}")


def format_result(result):
    """
    Format calculation result for display.
    
    Args:
        result (float): The calculation result
        
    Returns:
        float or int: Formatted result (int if whole number, float otherwise)
    """
    # Return as integer if it's a whole number
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result


def is_safe_division(divisor):
    """
    Check if division is safe (divisor is not zero).
    
    Args:
        divisor (float): The number to divide by
        
    Returns:
        bool: True if safe to divide, False otherwise
    """
    return divisor != 0


# TODO: Add function to check for very large numbers
# Students might implement this as an enhancement

def get_operation_symbol(operation):
    """
    Get the mathematical symbol for an operation.
    
    Args:
        operation (str): Operation name
        
    Returns:
        str: Mathematical symbol
    """
    symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    return symbols.get(operation.lower(), '?')
