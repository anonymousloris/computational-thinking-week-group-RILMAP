def evaluate_expression(expression: str) -> float:
    """
    Evaluates a given arithmetic expression using predefined values for a, c, d, and e.
    
    :param expression: A string representing an arithmetic expression (e.g., "e+c+d").
    :return: The result of the evaluated expression as a float.
    """
    # Predefined values for the variables
    a = 3
    c = 4
    d = 4
    e = 3.5
    
    # Use Python's eval() function to evaluate the expression with the given variables
    return eval(expression)

def solution_station_7(expression: str) -> float:
    """
    Solves the expression given for station 7.
    
    :param expression: The arithmetic expression to evaluate.
    :return: The evaluated result as a float.
    """
    return evaluate_expression(expression)


if __name__ == "__main__":
    # Example usage and basic testing
    example_input = "c*e"
    result = solution_station_7(example_input)
    print(f"The result of the expression '{example_input}' is {result}")
