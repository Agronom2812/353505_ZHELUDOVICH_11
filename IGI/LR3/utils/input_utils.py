"""
Input utilities module
"""

def get_float_input(prompt: str, min_val: float = None, max_val: float = None) -> float:
    """Get validated float input"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be ≥ {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be ≤ {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

def get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Get validated integer input"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be ≥ {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be ≤ {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")
