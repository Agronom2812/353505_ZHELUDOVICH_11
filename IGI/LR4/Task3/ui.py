"""
UI for Series Analysis Task (Task 3)
"""

import numpy as np
from Lab4.Task3.series.analyzer import SeriesAnalyzer
from Lab4.Task3.series.visualization import plot_comparison


class Task3UI:
    """Handles user interaction for series analysis (Task 3)"""

    def __init__(self):
        self.analyzer = SeriesAnalyzer()
        self.default_x = np.linspace(1.5, 5.0, 10)
        self.default_eps = 1e-6

    def run(self):
        """Main entry point for task"""
        while True:
            self._show_menu()
            choice = input("Enter choice (1-4): ").strip()

            if choice == '1':
                self._analyze_single_point()
            elif choice == '2':
                self._plot_default()
            elif choice == '3':
                self._plot_custom()
            elif choice == '4':
                return
            else:
                print("Invalid input. Enter 1-4")

    @staticmethod
    def _show_menu():
        """Display task menu"""
        print("\n=== SERIES ANALYSIS (TASK 3) ===")
        print("1. Analyze single point")
        print("2. Plot default comparison")
        print("3. Custom plot")
        print("4. Back to main menu")

    def _analyze_single_point(self):
        """Analyze specific x value"""
        try:
            x = float(input("Enter x (>1): "))
            eps = float(input(f"Epsilon [default: {self.default_eps}]: ") or self.default_eps)

            if x <= 1:
                raise ValueError("x must be > 1")

            stats = self.analyzer.analyze(x, eps)
            print("\nRESULTS:")
            for k, v in stats.items():
                print(f"{k:>10}: {v:.6f}")

        except ValueError as e:
            print(f"Error: {e}")

    def _plot_default(self):
        """Generate default plot"""
        try:
            output = input("Output file [default: plot.png]: ") or "plot.png"
            plot_comparison(self.default_x, self.default_eps, output)
            print(f"Plot saved to {output}")
        except Exception as e:
            print(f"Plotting failed: {e}")

    def _plot_custom(self):
        """Generate custom plot"""
        try:
            start = float(input("Start x (>1): "))
            end = float(input("End x: "))
            points = int(input("Points: "))
            eps = float(input(f"Epsilon [default: {self.default_eps}]: ") or self.default_eps)

            if start <= 1 or end <= start:
                raise ValueError("Invalid range")

            x_values = np.linspace(start, end, points)
            output = input("Output file: ") or "custom_plot.png"

            plot_comparison(x_values, eps, output)
            print(f"Plot saved to {output}")

        except ValueError as e:
            print(f"Error: {e}")
