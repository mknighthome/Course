def add_nums(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract_nums(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply_nums(a, b):
    """Return the product of two numbers."""
    return a * b


def divide_nums(a, b):
    """Return the quotient of two numbers. Raise ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def calculate(a, b, operation):
    """Perform a basic arithmetic operation."""
    operation = operation.strip().lower()
    if operation in {"add", "+"}:
        return add_nums(a, b)
    if operation in {"subtract", "sub", "-"}:
        return subtract_nums(a, b)
    if operation in {"multiply", "mul", "*"}:
        return multiply_nums(a, b)
    if operation in {"divide", "div", "/"}:
        return divide_nums(a, b)
    raise ValueError(f"Unsupported operation: {operation}")


__all__ = [
    "add_nums",
    "subtract_nums",
    "multiply_nums",
    "divide_nums",
    "calculate",
]