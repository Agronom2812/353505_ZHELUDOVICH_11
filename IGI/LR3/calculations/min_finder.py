"""
Module for finding minimum number in sequence
"""

from utils.input_utils import get_int_input

def find_min_number() -> int:
    """Find minimum number in sequence"""
    min_num = None
    while True:
        num = get_int_input("Enter number (0 to stop): ")
        if num == 0:
            break
        if min_num is None or num < min_num:
            min_num = num
    return min_num
