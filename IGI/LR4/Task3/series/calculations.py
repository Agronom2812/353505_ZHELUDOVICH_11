"""
Series calculation functions
"""
import math
from typing import Tuple, List

def calculate_terms(x: float, eps: float, max_iter: int = 500) -> List[Tuple[int, float, float]]:
    """Generate series terms until convergence"""
    terms = []
    result = 0.0
    for n in range(max_iter):
        term = 2 / ((2*n + 1) * x**(2*n + 1))
        result += term
        terms.append((n+1, result, term))
        if abs(term) < eps:
            break
    return terms

def exact_value(x: float) -> float:
    """Calculate exact value using math.log"""
    return math.log((x + 1) / (x - 1))
