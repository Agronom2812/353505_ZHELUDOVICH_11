"""
Module for list processing tasks
"""

from typing import List, Tuple
from utils.input_utils import get_float_input

def process_list(numbers: List[float], a: float, b: float) -> Tuple[int, float]:
    """Process list according to task requirements"""
    if a > b:
        a, b = b, a
    
    in_range = sum(1 for num in numbers if a <= num <= b)
    max_index = numbers.index(max(numbers))
    sum_after_max = sum(numbers[max_index+1:])
    
    return in_range, sum_after_max
