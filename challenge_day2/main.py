from tests import tests
from station1 import solution_station_1
from station2 import solution_station_2
from station3 import solution_station_3
from station4 import solution_station_4
from station5 import solution_station_5
from station6 import solution_station_6
from station7 import solution_station_7

# List three observations of all inputs (not sample inputs) observed at the same time

#Station 6


# Example values based on the format station7
observation1 = ('10:09:23', 9, 'c*e', 15, 20, 'sample text', 25, 'another text')
observation2 = ('10:09:33', 26, 'e+a+c', 35, 40, 'text example', 30, 'more text')
observation3 = ('10:09:43', 50, 'a*c+d', 45, 50, 'final text', 35, 'last text')

def combined_algorithm(observations: tuple) -> int:
    output1 = solution_station_1(observations[1])
    output2 = solution_station_2(observations[2])
    output3 = solution_station_3(observations[3])
    output4 = solution_station_4(observations[4])
    output5 = solution_station_5(observations[5])
    output6 = solution_station_6(observations[6])
    output7 = solution_station_7(observations[7])
    assert isinstance(output1, int)
    assert isinstance(output2, str)
    assert isinstance(output3, bool)
    assert isinstance(output4, bool)
    assert isinstance(output5, int)
    assert isinstance(output6, float)
    assert isinstance(output7, float)
    return output1 * int.from_bytes(output2[0].encode("unicode_escape"), byteorder='big') * (3 if output3 else 2) * (5 if output4 else 4) * output5 * output6 * output7

# Run the combined algorithm for each observation and print the results
FINAL_OUTPUT1 = combined_algorithm(observation1)
FINAL_OUTPUT2 = combined_algorithm(observation2)
FINAL_OUTPUT3 = combined_algorithm(observation3)

print("Final Output 1:", FINAL_OUTPUT1)
print("Final Output 2:", FINAL_OUTPUT2)
print("Final Output 3:", FINAL_OUTPUT3)

# Optional: Run tests (assuming tests is implemented)
tests.Test_Exercise(combined_algorithm)
