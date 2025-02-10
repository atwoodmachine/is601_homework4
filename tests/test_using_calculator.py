import sys
from io import StringIO
import pytest
from calculator import Calculator

def calculator_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    output = StringIO()
    sys.stdout = output

    Calculator.calculator()

    sys.stdout = sys.__stdout__
    return output.getvalue()

def test_wrong_operation(monkeypatch):
    inputs = ["ad 1 2", "exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "Unrecognized operation" in output

def test_non_number(monkeypatch):
    inputs = ["add 1 v", "exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "Invalid input" in output

def test_exit(monkeypatch):
    inputs = ["exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "Exiting calculator" in output

def test_valid_operation(monkeypatch):
    inputs = ["add 1 2", "exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "3.0" in output

def test_divide_by_zero(monkeypatch):
    inputs = ["divide 1 0", "exit"]
    output = calculator_input(monkeypatch, inputs)
    assert "Math error: division by zero" in output