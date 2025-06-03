"""
Statistical analysis of series
"""
import statistics
from typing import Dict
from .calculations import calculate_terms


class SeriesAnalyzer:
    def __init__(self):
        self.terms = []

    def analyze(self, x: float, eps: float) -> Dict[str, float]:
        """Calculate statistics for series terms"""
        self.terms = calculate_terms(x, eps)
        term_values = [term for _, _, term in self.terms]

        return {
            'mean': statistics.mean(term_values),
            'median': statistics.median(term_values),
            'mode': statistics.mode(term_values),
            'variance': statistics.variance(term_values),
            'stdev': statistics.stdev(term_values),
            'iterations': len(self.terms)
        }
