from decimal import Decimal
import pytest
from faker import Faker
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for i in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        if(i % 3 == 0):
            b = Decimal(fake.random_number(digits=2))
        else:
            b = Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        op_method = operation_mappings[operation_name]

        if(op_method == divide):
            if b == 0:
                b = Decimal("1")
        
        try:
            if op_method == divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = op_method(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield a, b, operation_name, op_method, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)