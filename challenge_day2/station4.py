def is_fibonacci(n: int) -> bool:
    """Checks if a given number is a Fibonacci number."""
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

# Sample input
sample_input = [17, 72, 16]
sample_output = [is_fibonacci(n) for n in sample_input]
print(sample_output)  # This should print [False, False, False]

# Actual input
input_values = [3203, 5276, 8647]
output_values = [is_fibonacci(n) for n in input_values]
print(output_values)
