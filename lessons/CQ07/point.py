"""CQ07 - Intro To Object Oriented Programming!!!"""

from __future__ import annotations

__author__ = "730660578"


class Point:
    """This is my class to represent a point."""
    # Attributes.
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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