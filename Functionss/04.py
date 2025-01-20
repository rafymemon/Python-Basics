import math

radius = input("Enter The Radius : ")
radius_in_int = int(radius)


def circle_state(radius_in_int):
    area = math.pi * radius_in_int**2
    circumference = 2 * math.pi * radius_in_int
    return area, circumference


a, c = circle_state(radius_in_int)
print("Area :", a, "Circumference :", c)
