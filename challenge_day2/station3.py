# station3.py

def solution_station_3(input1, input2, input3):
    """
    This function takes three inputs and checks if each input is even.
    Returns True if the number is even, False if the number is odd.
    """
    output1 = input1 % 2 == 0
    output2 = input2 % 2 == 0
    output3 = input3 % 2 == 0
    
    return output1, output2, output3

# Testing the function with the provided inputs
if __name__ == "__main__":
    # Given input values for testing
    input_values = (32035, 52762, 86476)
    output = solution_station_3(*input_values)
    print("Output:", output)
