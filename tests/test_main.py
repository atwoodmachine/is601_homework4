'''Test main command line program'''
import pytest
from main import calculate_and_print

@pytest.mark.parametrize("a_input, b_input, operation_input, expected_out",[
    ("5", "3", 'add', "Result: 5 add 3 equals 8"),
    ("10", "2", 'subtract', "Result: 10 subtract 2 equals 8"),
    ("4", "5", 'multiply', "Result: 4 multiply 5 equals 20"),
    ("20", "4", 'divide', "Result: 20 divide 4 equals 5"),
    ("1", "0", 'divide', "An error occurred: Math error: division by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid input: a or 3 is not a valid number"),
    ("5", "b", 'subtract', "Invalid input: 5 or b is not a valid number")
])

def test_main(a_input, b_input, operation_input, expected_out, capsys):
    '''Uses paramtrized data to test command line interface'''
    calculate_and_print(a_input, b_input, operation_input)
    output = capsys.readouterr()
    assert output.out.strip() == expected_out
