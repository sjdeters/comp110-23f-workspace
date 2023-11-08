"""Checking correctness of point.py."""

# Import the class.
from lessons.CQ07.point import Point


my_point: Point = Point(1.0, 2.0)

point: str = (f"({my_point.x}, {my_point.y})")
print(point)

my_point.scale_by(3)
point = (f"({my_point.x}, {my_point.y})")
print(point)

my_second_point: Point = my_point.scale(3)
point = (f"({my_second_point.x}, {my_second_point.y})")
print(point)