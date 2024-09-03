def fibonacci(n: int) -> int:
  
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def solution_station_1(input_number: int) -> int:
    
    return fibonacci(input_number)


if __name__ == "__main__":
    example_input = 9
    result = solution_station_1(example_input)
    print(f"The Fibonacci number at position {example_input} is {result}")
