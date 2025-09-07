def safe_divide(numerator, denominator):
    try:
        numerator=float(numerator)
        denominator=float(denominator)
    except ValueError:
        return "Not possible"

    try:
        return numerator/denominator
        
    except ZeroDivisionError:
        return "Error message"
