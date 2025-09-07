def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Invalid input. Please enter numbers only."

    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
