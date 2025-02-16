from calculator.calculation import Calculation
from calculator.calculation_history import Calculation_History
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def calculate_operation(a: Decimal, b:Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calc = Calculation(a, b, operation)
        Calculation_History.add_to_history(calc)
        return calc.calculate()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.calculate_operation(a, b, add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.calculate_operation(a, b, subtract)
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.calculate_operation(a, b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.calculate_operation(a, b, divide)
