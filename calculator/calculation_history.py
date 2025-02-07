from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculation_History:
    history: List[Calculation] = []

    @classmethod
    def add_to_history(cls, calculation: Calculation):
        cls.history.append(calculation)
    
    @classmethod
    def get_history(cls):
        return cls.history
    
    @classmethod
    def get_last_calculation(cls):
        if cls.history:
            return cls.history[-1]
        return "None"
    
    @classmethod
    def clear_history(cls):
        cls.history.clear()
