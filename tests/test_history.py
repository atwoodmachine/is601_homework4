'''Test calculation history'''

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculation_history import Calculation_History
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def setup_test():
    '''Clear history and set up with 4 calculations'''
    Calculation_History.clear_history()
    Calculation_History.add_to_history(Calculation(Decimal('10'), Decimal('3'), add))
    Calculation_History.add_to_history(Calculation(Decimal('4'), Decimal('2'), subtract))
    Calculation_History.add_to_history(Calculation(Decimal('5'), Decimal('5'), multiply))
    Calculation_History.add_to_history(Calculation(Decimal('32'), Decimal('4'), divide))

def test_get_history(setup_test):
    '''Test get history, should return 4 from setup'''
    hist = Calculation_History.get_history()
    assert len(hist) == 4, "Failed to get history"

def test_add_to_history(setup_test):
    '''Test adding new calculation to history'''
    calc = Calculation(Decimal('8'), Decimal('4'), multiply)
    Calculation_History.add_to_history(calc)
    assert Calculation_History.get_last_calculation() == calc, "Failed to add to history"

def test_get_last_calc(setup_test):
    '''Test retrieving latest calculation added'''
    calc = Calculation(Decimal('9'), Decimal('3'), divide)
    Calculation_History.add_to_history(calc)
    assert Calculation_History.get_last_calculation() == calc, "Failed get last calculation"

def test_get_last_on_empty(setup_test):
    '''Test return latest when history is empty'''
    Calculation_History.clear_history()
    assert(Calculation_History.get_last_calculation()) is None, "Failed get last calculation on empty history"

def test_clear_history(setup_test):
    '''Test to ensure clear history returns empty list'''
    Calculation_History.clear_history()
    assert len(Calculation_History.get_history()) == 0, "Failed to clear history"
