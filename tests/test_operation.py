from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    test = Calculation(Decimal('4'), Decimal('5'), add)
    assert test.calculate() == Decimal('9'), "Addition failed"

def test_operation_subtract():
    test = Calculation(Decimal('18'), Decimal('5'), subtract)
    assert test.calculate() == Decimal('13')

def test_operation_multiply():
    test = Calculation(Decimal('3'), Decimal('7'), multiply)
    assert test.calculate() == Decimal('21')

def test_operation_divide():
    test = Calculation(Decimal('90'), Decimal('10'), divide)
    assert test.calculate() == Decimal('9')

def test_operation_divide_by_zero():
    with pytest.raises(ValueError, match="Math error: division by zero"):
        test = Calculation(Decimal('11'), Decimal('0'), divide)
        test.calculate()