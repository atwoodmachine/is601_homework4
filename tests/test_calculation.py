from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operation(a, b, operation, expected):
    calc = Calculation(a, b, operation)
    assert calc.calculate() == expected, f"Failed operation {operation.__name__} with {a} and {b}"

def test_divide_by_zero():
    calc = Calculation(Decimal("10"), Decimal("0"), divide)
    with pytest.raises(ValueError, match="Math error: division by zero"):
        calc.calculate()
