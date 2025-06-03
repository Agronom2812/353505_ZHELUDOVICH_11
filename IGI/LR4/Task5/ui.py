"""
User interface for Task 5
"""

import numpy as np
from .core.matrix_stats import get_stats, calculate_custom_median


class Task5UI:
    def __init__(self, n: int = 5, m: int = 5):
        self.matrix = np.random.randint(-50, 50, size=(n, m))
        self.filtered = None
        self.threshold = None

    def run(self):
        """Main UI loop"""
        while True:
            print("\n=== NUMPY MATRIX OPERATIONS ===")
            print("1. Generate new matrix")
            print("2. Filter by absolute value")
            print("3. Show statistics")
            print("4. Return to main menu")

            choice = input("Select option: ").strip()

            if choice == "1":
                self._generate_matrix()
            elif choice == "2":
                self._filter_matrix()
            elif choice == "3":
                self._show_stats()
            elif choice == "4":
                return
            else:
                print("Invalid input. Enter 1-4")

    def _generate_matrix(self):
        """Generate new random matrix"""
        try:
            n = int(input("Rows (n): "))
            m = int(input("Columns (m): "))
            low = int(input("Min value: "))
            high = int(input("Max value: "))
            self.matrix = np.random.randint(low, high, size=(n, m))
            print("New matrix generated")
        except ValueError:
            print("Please enter valid integers")

    def _filter_matrix(self):
        """Filter matrix by absolute value"""
        try:
            B = float(input("Enter threshold B: "))
            self.threshold = abs(B)
            self.filtered = self.matrix[np.abs(self.matrix) > self.threshold]
            print(f"Found {len(self.filtered)} elements > |{B}|")
        except ValueError:
            print("Please enter a valid number")

    def _show_stats(self):
        """Display statistics with safe handling"""
        if self.filtered is None:
            print("Please filter matrix first (option 2)")
            return

        try:
            stats = get_stats(self.filtered.reshape(-1, 1))  # Ensure 2D array
            custom_median = calculate_custom_median(self.filtered)

            print("\nSTATISTICS:")
            print(f"Elements count: {len(self.filtered)}")
            print(f"Mean: {stats['mean']:.2f}")
            print(f"Median (numpy): {stats['median']:.2f}")
            print(f"Median (custom): {custom_median:.2f}")
            print(f"Variance: {stats['variance']:.2f}")
            print(f"Std deviation: {stats['std_dev']:.2f}")

            if stats['correlation'] is not None:
                print(f"Correlation: {stats['correlation']:.2f}")

        except Exception as e:
            print(f"Error calculating statistics: {str(e)}")
