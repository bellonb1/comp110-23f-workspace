"""The image created is drawing of a house (NFT). Very rare, invest now."""

__author__: str = "730656976"

from turtle import Turtle, colormode, done
from math import sqrt


def draw_window(masterpiece: Turtle, xcoord: float, ycoord: float, length: float) -> None:
    """Creates a window, starting at bottom left corner."""
    masterpiece.color("cyan")
    masterpiece.begin_fill()
    masterpiece.penup()
    masterpiece.setposition(xcoord, ycoord)
    masterpiece.setheading(90)
    masterpiece.pendown()
    for i in range(4):
        masterpiece.forward(length)
        masterpiece.right(90)
    masterpiece.end_fill()

    masterpiece.color(255, 255, 255)
    masterpiece.penup()
    masterpiece.setposition(xcoord + length / 2, ycoord)
    masterpiece.pendown()
    masterpiece.forward(length)
    masterpiece.penup()
    masterpiece.setposition(xcoord, ycoord + length / 2)
    masterpiece.pendown()
    masterpiece.right(90)
    masterpiece.forward(length)


def draw_house(masterpiece: Turtle, xcoord: float, ycoord: float, size: float) -> None:
    """Draws a house-like shape."""
    masterpiece.color("red")
    masterpiece.begin_fill()
    masterpiece.penup()
    masterpiece.setposition(xcoord, ycoord)
    masterpiece.setheading(90)
    masterpiece.pendown()
    for i in range(4):
        masterpiece.forward(size)
        masterpiece.right(90)

    masterpiece.penup()
    masterpiece.setposition(xcoord, ycoord + size)
    masterpiece.pendown()

    masterpiece.right(45)
    masterpiece.forward(size / sqrt(2))
    masterpiece.right(90)
    masterpiece.forward(size / sqrt(2))
    masterpiece.end_fill()
    masterpiece.penup()


def draw_door(masterpiece: Turtle, xcoord: float, ycoord: float, size: float) -> None:
    """Draws a door-like shape."""
    masterpiece.color("brown")
    masterpiece.begin_fill()
    masterpiece.penup()
    masterpiece.setposition(xcoord, ycoord)
    masterpiece.setheading(90)
    masterpiece.pendown()
    for i in range(2):
        masterpiece.forward(size)
        masterpiece.right(90)
        masterpiece.forward(size / 2.25)
        masterpiece.right(90)

    masterpiece.end_fill()
    masterpiece.penup()


def draw_circle(masterpiece: Turtle, xcoord: float, ycoord: float, size: float) -> None:
    """Draws a colored in circle."""
    masterpiece.color("yellow")
    masterpiece.begin_fill()
    masterpiece.penup()
    masterpiece.setposition(xcoord, ycoord)
    masterpiece.setheading(90)
    masterpiece.pendown()
    masterpiece.circle(size)
    masterpiece.end_fill()
    masterpiece.penup()


def main() -> None:
    """Main function, an extremely detailed drawing of a house."""
    masterpiece: Turtle = Turtle()
    masterpiece.speed(9)
    colormode(255)
    draw_circle(masterpiece, 100, 100, 60)
    draw_house(masterpiece, float(-200), float(-200), 250)
    draw_window(masterpiece, float(-150), float(-50), 60)
    draw_door(masterpiece, -100, -200, 80)
    done()


if __name__ == "__main__":
    main()
