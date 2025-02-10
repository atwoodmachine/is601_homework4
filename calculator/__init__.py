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
    def calculator():
        print("Calculator initialized")

        while(True):
            user_input = input("Enter an operation (add, subtract, multiply or divide) and two operands, or 'exit' to quit\n")

            if user_input.lower() == "exit":
                print("Exiting calculator")
                break
            
            try:
                operation, a, b = user_input.split()
                a, b = float(a), float(b)
            except ValueError:
                print("Invalid input. Valid input format is: <operation> <operand1> <operand2>\n")
                continue

            if operation not in ("add", "subtract", "multiply", "divide"):
                print(f"Unrecognized operation '{operation}'. Please enter one of: add, subtract, multiply, divide\n")
                continue

            try:
                print(Calculator.calculate_operation(a, b, eval(operation)))
            except ValueError as e:
                print(e)

