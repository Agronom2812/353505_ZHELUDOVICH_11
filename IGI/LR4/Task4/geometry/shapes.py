from abc import ABC, abstractmethod
from math import sqrt
from Lab4.Task4.geometry.color import Color


class ShapePropertiesMixin:
    """Mixin providing common shape properties and validation"""

    @staticmethod
    def validate_side(side: float):
        """Validate that side is positive"""
        if side <= 0:
            raise ValueError("Side must be positive")
        return side


class GeometricShape(ABC):
    """Abstract base class for all geometric shapes"""

    @property
    @abstractmethod
    def name(self) -> str:
        """Shape display name"""
        pass

    @abstractmethod
    def area(self) -> float:
        """Calculate shape area"""
        pass

    @abstractmethod
    def get_parameters(self) -> str:
        """Get formatted shape description"""
        pass


class SquareWithTriangle(GeometricShape, ShapePropertiesMixin):
    """Square with equilateral triangle on top"""

    def __init__(self, side: float, color: Color):
        """
        Args:
            side: Length of square side (must be > 0)
            color: Color object
        """
        super().__init__
        self._side = self.validate_side(side)
        self._color = color

    @property
    def name(self) -> str:
        return "Square+Triangle"

    def area(self) -> float:
        """Total area = square + triangle"""
        return self._side ** 2 + (sqrt(3) / 4) * self._side ** 2

    def get_parameters(self) -> str:
        return f"{self.name} (side={self._side}, color={self._color.value}, area={self.area():.2f})"

    @property
    def side(self) -> float:
        """Getter for side length"""
        return self._side

    @side.setter
    def side(self, value: float):
        """Setter for side length with validation"""
        self._side = self.validate_side(value)

    @property
    def color(self) -> Color:
        """Getter for color"""
        return self._color

    @color.setter
    def color(self, value: Color):
        """Setter for color"""
        if not isinstance(value, Color):
            raise TypeError("Color must be an instance of the Color class")
        self._color = value
