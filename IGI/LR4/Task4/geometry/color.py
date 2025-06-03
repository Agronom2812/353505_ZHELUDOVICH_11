from enum import Enum

class Color(Enum):
    """Available colors for figures"""
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    BLACK = "black"

    @classmethod
    def from_string(cls, color_str: str):
        try:
            return cls(color_str.lower())
        except ValueError:
            raise ValueError(f"Invalid color. Available: {list(c.value for c in cls)}")
