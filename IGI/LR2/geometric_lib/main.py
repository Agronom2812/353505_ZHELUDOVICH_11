import os
from dotenv import load_dotenv
import square
import circle

load_dotenv()

r = int(os.getenv('CIRCLE_RADIUS'))
a = int(os.getenv('SQUARE_SIDE'))

circle_area = circle.area(r)
circle_perimeter = circle.perimeter(r)
square_area = square.area(a)
square_perimeter = square.perimeter(a)

print(f"square area: {square_area}")
print(f"square perimeter: {square_perimeter}")
print(f"circle area: {circle_area}")
print(f"circle perimeter: {circle_perimeter}")