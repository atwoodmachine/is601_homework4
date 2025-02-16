'''Tests operations using parameterized values'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("num1, num2, operation, expected_out", [
    #Addition tests
    (Decimal('3'), Decimal('1.2'), add, Decimal('4.2')),
    (Decimal('-2'), Decimal('8'), add, Decimal('6')),
    (Decimal('2'), Decimal('-8'), add, Decimal('-6')),
    (Decimal('-4'), Decimal('-9'), add, Decimal('-13')),
    (Decimal('-3.2'), Decimal('-9.1'), add, Decimal('-12.3')),
    #Subtraction tests
    (Decimal('3'), Decimal('1.2'), subtract, Decimal('1.8')),
    (Decimal('-2'), Decimal('8'), subtract, Decimal('-10')),
    (Decimal('2'), Decimal('-8'), subtract, Decimal('10')),
    (Decimal('-4'), Decimal('-9'), subtract, Decimal('5')),
    (Decimal('-3.2'), Decimal('-9.1'), subtract, Decimal('5.9')),
    #Multiplication tests
    (Decimal('3'), Decimal('1.2'), multiply, Decimal('3.6')),
    (Decimal('-2'), Decimal('8'), multiply, Decimal('-16')),
    (Decimal('2'), Decimal('-8'), multiply, Decimal('-16')),
    (Decimal('-4'), Decimal('-9'), multiply, Decimal('36')),
    (Decimal('-3.2'), Decimal('-9.1'), multiply, Decimal('29.12')),
    #Division tests
    (Decimal('3'), Decimal('1.2'), divide, Decimal('2.5')),
    (Decimal('-8'), Decimal('2'), divide, Decimal('-4')),
    (Decimal('24'), Decimal('-8'), divide, Decimal('-3')),
    (Decimal('-18'), Decimal('-9'), divide, Decimal('2')),
    (Decimal('-3.2'), Decimal('-0.1'), divide, Decimal('32')),
])
def test_calculator(num1, num2, operation, expected_out):
    '''Use parameterized tests for operations'''
    calc = Calculation(num1, num2, operation)
    received = calc.calculate()
    assert received == expected_out, f"Failed '{operation.__name__}' with '{num1}' and '{num2}', received '{received}', expected '{expected}'"
