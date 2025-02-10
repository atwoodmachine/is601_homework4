"""Test calculator with command line user input"""
import sys
from io import StringIO
from calculator import Calculator

def calculator_input(monkeypatch, inputs):
    '''Set up monkeypatch to simulate user input from command line'''
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    output = StringIO()
    sys.stdout = output

    Calculator.calculator()

    sys.stdout = sys.__stdout__
    return output.getvalue()

def test_wrong_operation(monkeypatch):
    '''Test unrecognized operation'''
    inputs = ["ad 1 2", "exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "Unrecognized operation" in output

def test_non_number(monkeypatch):
    '''Test wrong value in operand'''
    inputs = ["add 1 v", "exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "Invalid input" in output

def test_exit(monkeypatch):
    '''Test exiting'''
    inputs = ["exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "Exiting calculator" in output

def test_valid_operation(monkeypatch):
    '''Test valid input'''
    inputs = ["add 1 2", "exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "3.0" in output

def test_divide_by_zero(monkeypatch):
    '''Test division by zero'''
    inputs = ["divide 1 0", "exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "Math error: division by zero" in output
