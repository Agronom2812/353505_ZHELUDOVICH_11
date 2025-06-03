"""
Decorators module
"""

def input_validator(func):
    """Validate function inputs"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"Input error: {e}")
        except Exception as e:
            print(f"Calculation error: {e}")
    return wrapper
