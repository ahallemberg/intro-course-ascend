"""
Simple Calculator Module
This module provides basic arithmetic operations.
"""

from utils import validate_numbers, format_result


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of a and b
        
    Raises:
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    result = a + b
    return format_result(result)


def subtract(a, b):
    """
    Subtract second number from first number.
    
    Args:
        a (float): First number
        b (float): Second number to subtract
        
    Returns:
        float: Difference of a and b
        
    Raises:
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    result = a - b
    return format_result(result)

def divide(a, b):
    """
    Divide first number by second number.
    
    Args:
        a (float): Dividend
        b (float): Divisor
        
    Returns:
        float: Quotient of a divided by b
        
    Raises:
        TypeError: If inputs are not numbers
        ValueError: If divisor is zero
    """
    validate_numbers(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return format_result(result)


# TODO: Add multiplication function

# TODO: Add division function


def main():
    """
    Simple interactive calculator for testing.
    """
    print("Simple Calculator")
    print("Available operations: add, subtract")
    print("Type 'quit' to exit")
    
    while True:
        operation = input("\nEnter operation (add/subtract/quit/divide): ").lower().strip()
        
        if operation == 'quit':
            print("Goodbye!")
            break
            
        if operation not in ['add', 'subtract', 'divide']:
            print("Invalid operation. Please use 'add' or 'subtract' or 'divide'")
            continue
            
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if operation == 'add':
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif operation == 'subtract':
                result = subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            elif operation == 'divide':
                result = divide(a,b)
                print(f"Result: {a} / {b} = {result}")
                
        except ValueError:
            print("Please enter valid numbers")
        except TypeError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
