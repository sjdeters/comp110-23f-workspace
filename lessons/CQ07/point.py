"""CQ07 - Intro To Object Oriented Programming!!!"""

from __future__ import annotations

__author__ = "730660578"


class Point:
    """This is my class to represent a point."""
    # Attributes.
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor for assigning initial values for attributes x and y."""
        self.x = x_init
        self.y = y_init
        # Returns self.

    def scale_by(self, factor: int) -> None:
        """Method to mutate a point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method to create a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Helps make points readable."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Creates new point multiplied by factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, constant: int | float) -> Point:
        """Creates a new point added by constant."""
        new_point: Point = Point(self.x + constant, self.y + constant)
        return new_point