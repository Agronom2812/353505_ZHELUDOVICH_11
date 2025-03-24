import os
from dotenv import load_dotenv
import square
import circle

load_dotenv()

try:
    r = int(os.getenv('CIRCLE_RADIUS'))
    a = int(os.getenv('SQUARE_SIDE'))
    
    if r <= 0 or a <= 0:
        raise ValueError("Radius and side length must be positive numbers")

r = int(input("Circle radius(r): "))
a = int(input("Square side length(a): "))

circle_area = circle.area(r)
circle_perimeter = circle.perimeter(r)
square_area = square.area(a)
square_perimeter = square.perimeter(a)

print(f"square area: {square_area}")
print(f"square perimeter: {square_perimeter}")
print(f"circle area: {circle_area}")
print(f"circle perimeter: {circle_perimeter}")

except (TypeError, ValueError) as e:
    print(f"Error: {str(e)}")
    exit(1)
