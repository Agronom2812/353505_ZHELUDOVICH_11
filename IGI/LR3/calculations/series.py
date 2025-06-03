"""
Module for series expansion calculation
"""

import math
from typing import Tuple, List
from utils.decorators import input_validator

@input_validator
def calculate_series(x: float, eps: float, max_iter: int = 500) -> Tuple[float, int, List[Tuple[int, float, float]]]:
    """Calculate series expansion with history"""
    result = 0.0
    history = []
    
    for n in range(max_iter):
        term = 2 / ((2*n + 1) * x**(2*n + 1))
        result += term
        history.append((n+1, result, term))
        if abs(term) < eps:
            break
            
    return result, len(history), history

def exact_value(x: float) -> float:
    """Calculate exact value using math"""
    return math.log((x + 1) / (x - 1))
