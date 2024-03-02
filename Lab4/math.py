import math
# 1. Write a Python program to convert degree to radian.

def deg_to_rad(deg):
    rad = deg * (math.pi / 180)
    return rad


# 2. Write a Python program to calculate the area of a trapezoid.
def area_of_trapezoid(height, base1, base2):
    return (base1 + base2) / 2 * height


# 3. Write a Python program to calculate the area of regular polygon.
def area_of_polygon(n, side_length):
    return (n * side_length ** 2) / (4 * math.tan(math.pi / n))

# 4. Write a Python program to calculate the area of a parallelogram. 
def area_of_parallelogram(base, height):
    return base * height