# pylint: disable=invalid-name
'''Test set up for use with faker generated data'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide

def test_calculation_operation(a, b, operation, expected):
    '''Tests calculation result'''
    calc = Calculation(a, b, operation)
    assert calc.calculate() == expected, f"Failed operation {operation.__name__} with {a} and {b}"

def test_divide_by_zero():
    '''Tests divide by zero throws error'''
    calc = Calculation(Decimal("10"), Decimal("0"), divide)
    with pytest.raises(ValueError, match="Math error: division by zero"):
        calc.calculate()
