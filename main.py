from calculator import Calculator

def main():
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

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
            print(Calculator.calculate_operation(a, b, operation_mappings[operation]))
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()