"""
Plotting functions
"""
import matplotlib.pyplot as plt
from .calculations import exact_value, calculate_terms


def plot_comparison(x_values: list, eps: float, save_path: str = None):
    """Plot series vs exact values"""
    fig, ax = plt.subplots(figsize=(10, 6))

    series_results = []
    exact_results = []
    for x in x_values:
        terms = calculate_terms(x, eps)
        series_results.append(terms[-1][1])
        exact_results.append(exact_value(x))

    ax.plot(x_values, series_results, 'bo-', label='Series Expansion')
    ax.plot(x_values, exact_results, 'r--', label='Exact Value')

    ax.set(xlabel='x', ylabel='F(x)',
           title='Series Convergence Analysis')
    ax.grid()
    ax.legend()

    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.close()
