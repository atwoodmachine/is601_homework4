import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a,b])
        operation = operation_mappings.get(operation_name)
        if operation:
            print(f"Result: {a} {operation_name} {b} equals {operation(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid input: {a} or {b} is not a valid number")
    except ZeroDivisionError:
        print(f"Math error: division by zero")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <operand1> <operand2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == "__main__":
    main()