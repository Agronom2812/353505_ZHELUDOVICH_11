"""
Module for sequence initialization methods
"""

from typing import List, Union, Iterator
import random


def input_sequence() -> List[float]:
    """
    Initialize sequence via user input
    """
    n = int(input("Enter sequence length: "))
    return [float(input(f"Enter element {i + 1}: ")) for i in range(n)]


def generate_random_sequence(size: int = 10, min_val: float = 0, max_val: float = 100) -> Iterator[float]:
    """
    Generate random sequence (generator function)

    Args:
        size: Sequence length
        min_val: Minimum value
        max_val: Maximum value

    Yields:
        Random float numbers one by one
    """
    for _ in range(size):
        yield random.uniform(min_val, max_val)


def generate_arithmetic_sequence(start: float = 0, step: float = 1, size: int = 10) -> Iterator[float]:
    """
    Generate arithmetic sequence

    Args:
        start: First element
        step: Increment step
        size: Sequence length

    Yields:
        Elements of arithmetic progression
    """
    current = start
    for _ in range(size):
        yield current
        current += step


def initialize_sequence(method: str = 'input', **kwargs) -> Union[List[float], Iterator[float]]:
    """
    Initialize sequence using specified method

    Args:
        method: 'input', 'random' or 'arithmetic'
        **kwargs: Parameters for generator

    Returns:
        Sequence as list or generator
    """
    if method == 'input':
        return input_sequence()
    elif method == 'random':
        return generate_random_sequence(**kwargs)
    elif method == 'arithmetic':
        return generate_arithmetic_sequence(**kwargs)
    else:
        raise ValueError("Unknown initialization method")

