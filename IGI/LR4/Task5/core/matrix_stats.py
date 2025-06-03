"""
Statistical calculations for matrices
Fixed version with safe correlation calculation
"""

import numpy as np
from typing import Union

def calculate_custom_median(arr: np.ndarray) -> Union[float, np.floating]:
    """
    Manual median calculation
    Args:
        arr: Input numpy array
    Returns:
        Median value
    """
    if len(arr) == 0:
        return float('nan')

    sorted_arr = np.sort(arr)
    n = len(sorted_arr)
    return sorted_arr[n//2] if n % 2 == 1 else (sorted_arr[n//2-1] + sorted_arr[n//2])/2

def get_stats(matrix: np.ndarray) -> dict:
    """
    Calculate basic statistics with safe correlation
    Args:
        matrix: Input array (1D or 2D)
    Returns:
        Dictionary with statistics
    """
    stats = {
        'mean': np.mean(matrix),
        'median': np.median(matrix),
        'variance': np.var(matrix),
        'std_dev': np.std(matrix),
        'correlation': None
    }

    # Safe correlation calculation
    if matrix.ndim == 2 and matrix.shape[0] > 1 and matrix.shape[1] > 1:
        corr = np.corrcoef(matrix)
        stats['correlation'] = corr[0, 1] if corr.size > 1 else None

    return stats
