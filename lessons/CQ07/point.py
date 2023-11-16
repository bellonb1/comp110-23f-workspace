"""Introduction to creating classes."""
from __future__ import annotations


class Point:
    """Class Point which contains an x and y variable for a 2d plane."""
    x: float
    y: float

    def __str__(self) -> str:
        """Prints out points in a readable way."""
        return "x: " + str(self.x) + "; " + "y: " + str(self.y)

    def __mul__(self, factor: int | float) -> Point:
        """Scale function with __mul__ functionality."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __add__(self, factor: int | float) -> Point:
        """Add function with __sum__ functionality."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
    
    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Point constructor."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Mutates Point object, multiplying x and y by input."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns Point object multiplied by factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    