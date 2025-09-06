# Getting Started with the Calculator

## Overview

This simple calculator demonstrates basic Python programming concepts and serves as a practical example for learning Git workflows.

## File Structure

### `src/calculator.py`
The main calculator module containing:
- `add(a, b)` - Addition function
- `subtract(a, b)` - Subtraction function
- `main()` - Interactive calculator interface

### `src/utils.py`
Utility functions that support the calculator:
- `validate_numbers()` - Input validation
- `format_result()` - Result formatting
- `is_safe_division()` - Division safety check
- `get_operation_symbol()` - Symbol mapping

## Running the Calculator

```bash
cd src
python calculator.py
```

## Extending the Calculator

When adding new functions, follow these patterns:

### 1. Function Structure
```python
def operation_name(a, b):
    """
    Clear docstring explaining the function.
    
    Args:
        a (float): First parameter description
        b (float): Second parameter description
        
    Returns:
        float: Return value description
        
    Raises:
        TypeError: When this exception occurs
    """
    validate_numbers(a, b)
    # Your calculation logic here
    result = a # operation b
    return format_result(result)
```

### 2. Adding to Main Function
Update the `main()` function to include your new operation in:
- Available operations list
- Input validation
- Operation execution

### 3. Testing Your Changes
Always test your functions with:
- Normal inputs
- Edge cases (zero, negative numbers)
- Invalid inputs (strings, None)

## Best Practices

1. **Always validate inputs** using `validate_numbers()`
2. **Format results** using `format_result()`
3. **Write clear docstrings** for all functions
4. **Handle errors gracefully** with try/except blocks
5. **Use meaningful variable names**

## Common Issues

### Division by Zero
```python
if not is_safe_division(b):
    raise ValueError("Cannot divide by zero")
```

### Type Errors
The `validate_numbers()` function handles this automatically.

### Large Numbers
Python handles large integers automatically, but consider adding warnings for very large results.
