"""
UI for Task 4 - Geometric Shapes
"""

from Lab4.Task4.geometry.shapes import SquareWithTriangle
from Lab4.Task4.geometry.color import Color
from Lab4.Task4.geometry.drawing import draw_shape


class Task4UI:
    """User interface for geometric shapes task"""

    def __init__(self):
        self.shape = None

    def run(self):
        """Main UI entry point"""
        while True:
            print("\n=== GEOMETRIC SHAPES ===")
            print("1. Create shape")
            print("2. Show parameters")
            print("3. Draw shape")
            print("4. Back to main menu")

            choice = input("Select option: ").strip()

            if choice == "1":
                self._create_shape()
            elif choice == "2":
                self._show_parameters()
            elif choice == "3":
                self._draw_shape()
            elif choice == "4":
                return
            else:
                print("Invalid input")

    def _create_shape(self):
        """Handle shape creation"""
        try:
            side = float(input("Enter square side length: "))
            if side <= 0:
                raise ValueError("Length must be positive")

            color = input("Color (red/green/blue/yellow/black): ").strip()
            self.shape = SquareWithTriangle(side, Color.from_string(color))
            print("Shape created!")

        except ValueError as e:
            print(f"Error: {str(e)}")

    def _show_parameters(self):
        """Display shape info"""
        if not self.shape:
            print("Create a shape first")
            return
        print("\nShape parameters:")
        print(self.shape.get_parameters())

    def _draw_shape(self):
        """Handle shape visualization"""
        if not self.shape:
            print("Create a shape first")
            return

        label = input("Shape label (press Enter to skip): ").strip()
        filename = input("Output filename [default: figure.png]: ").strip() or "figure.png"

        draw_shape(self.shape, label, filename)
        print(f"Shape saved to {filename}")
