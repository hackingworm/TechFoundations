def inc(x: int) -> int:
    """Increments and returns the given integer."""
    if not isinstance(x, int):
        raise TypeError("Given number is not an integer.")
    return x + 1


def dec(x: int) -> int:
    """Decrements and returns the given integer."""
    if not isinstance(x, int):
        raise TypeError("Given number is not an integer.")
    return x - 1


def add(x: int, y: int) -> int:
    """Adds and returns two given integers with increment and decrement functions."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Given input is not an integer.")
    if x < 0 or y < 0:
        raise ValueError("One or more inputs are less than 0.")

    # Implement your code here.
