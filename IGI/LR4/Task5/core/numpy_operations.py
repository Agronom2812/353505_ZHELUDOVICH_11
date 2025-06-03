"""
Core NumPy array operations
"""
import numpy as np

class NumpyMatrix:
    def __init__(self, rows: int = 5, cols: int = 5, low: int = -50, high: int = 50):
        """
        Initialize random integer matrix
        Args:
            rows: Number of rows
            cols: Number of columns
            low: Minimum random value
            high: Maximum random value
        """
        self.matrix = np.random.randint(low, high, size=(rows, cols))
        self.filtered = None
        self.threshold = None

    def filter_absolute(self, threshold: float) -> np.ndarray:
        """
        Filter elements > |threshold|
        Returns:
            Filtered 1D array
        """
        self.threshold = abs(threshold)
        self.filtered = self.matrix[np.abs(self.matrix) > self.threshold]
        return self.filtered
