def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling division by zero and non-numeric inputs.
    
    Args:
        numerator: The numerator as a string
        denominator: The denominator as a string
    
    Returns:
        The division result as float or error message as string
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."