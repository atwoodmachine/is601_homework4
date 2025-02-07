'''Tests operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    '''Verify addition correctness'''
    test = Calculation(Decimal('4'), Decimal('5'), add)
    assert test.calculate() == Decimal('9'), "Addition failed"

def test_operation_subtract():
    '''Verify subtraction correctness'''
    test = Calculation(Decimal('18'), Decimal('5'), subtract)
    assert test.calculate() == Decimal('13'), "Subtraction failed"

def test_operation_multiply():
    '''Verify multiplication correctness'''
    test = Calculation(Decimal('3'), Decimal('7'), multiply)
    assert test.calculate() == Decimal('21'), "Multiplication failed"

def test_operation_divide():
    '''Verify division correctness'''
    test = Calculation(Decimal('90'), Decimal('10'), divide)
    assert test.calculate() == Decimal('9'), "Division failed"

def test_operation_divide_by_zero():
    '''Verify division by zero raises error'''
    with pytest.raises(ValueError, match="Math error: division by zero"):
        test = Calculation(Decimal('11'), Decimal('0'), divide)
        test.calculate()
