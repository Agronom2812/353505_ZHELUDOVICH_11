from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from Lab4.Task4.geometry.shapes import SquareWithTriangle


def draw_shape(shape: SquareWithTriangle, label: str = "", filename: str = None):
    """Visualize shape with optional saving"""
    fig, ax = plt.subplots()

    # Draw square
    square = Rectangle((0, 0), shape.side, shape.side,
                       fc=shape.color.value, ec='black')
    ax.add_patch(square)

    # Draw triangle
    triangle_height = (sqrt(3) / 2) * shape.side
    triangle = Polygon([
        [0, shape.side],
        [shape.side, shape.side],
        [shape.side / 2, shape.side + triangle_height]
    ], fc=shape.color.value)
    ax.add_patch(triangle)

    # Add label
    if label:
        ax.text(shape.side / 2, -0.5, label, ha='center')

    # Configure plot
    ax.set_xlim(-1, shape.side + 1)
    ax.set_ylim(-1, shape.side + triangle_height + 1)
    ax.set_aspect('equal')
    ax.grid(True)

    if filename:
        plt.savefig(filename)
    plt.show()
