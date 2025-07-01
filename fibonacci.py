def fibonacci(n):
    """
    Calculates the nth term of the Fibonacci sequence using an iterative approach.

    Args:
        n: The position in the Fibonacci sequence (integer, 0-indexed).

    Returns:
        The nth Fibonacci number, or None if the input is invalid.
    """
    if not isinstance(n, int) or n < 0:
        print("Error: Input must be a non-negative integer.")
        return None
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example of how to use the function:
# To calculate the 10th Fibonacci number (remembering it's 0-indexed, so it's the 11th term)
# print(fibonacci(10))
