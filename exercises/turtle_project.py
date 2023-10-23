"""To-Do: describe your scene program."""

__author__ = "730660578"

from turtle import Turtle, colormode, done
from random import randint

"""For my scene, I wanted to design a pretty sunflower with some clouds in the distance. 
I am attempting to go above and beyond in my drawing in a few ways. First of all, I used the "circle"
function from the Turtle documentation page, which we did not use in the tutorial. Secondly, I used 
multiple loops in my code to try and make an interesting pattern. This was essential for making the
flower (or yellow part) of the sunflower. Finally, I wanted to use randomness in my scene and did so by
randomizing the location of the clouds in the background and also by randomizing the dots on the center
of the flower. I also broke my functions down into smaller functions to make the process simpler. Also,
I kept getting a linting error for my import modules saying they needed to be at the top of the file
and putting it above this description was the only way to get rid of it. 
"""

__author__ = "730660578"

colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    # To-do: Declare your Turtle variable(s) here. 
    ertle: Turtle = Turtle()
    ertle.hideturtle()
    ertle.speed(0)
    # To-do: Call the procedures you define and pass your Turtle(s) as an argument.
    draw_background(ertle, -300, -300)
    i: int = 0
    while i < 3:
        draw_cloud(ertle, randint(-300, 0), randint(0, 300))
        i += 1
    i = 0
    while i < 3:
        draw_cloud(ertle, randint(0, 300), randint(0, 300))
        i += 1
    draw_stem(ertle, -25, -300)
    draw_petals(ertle, 0, 0)
    draw_center(ertle, -29, 75) 
    done()


# To-do: define the procedures for other components in your scene here. 
def draw_background(background: Turtle, x: float, y: float) -> None:
    """Combine the grass and the sky."""
    draw_sky(background, x, y)
    draw_grass(background, x, y)


def draw_grass(grass: Turtle, x: float, y: float) -> None:
    """Draw the grass of the picture."""
    grass.setheading(0.0)
    grass.color("dark green")
    grass.penup()
    grass.goto(x, y)
    grass.pendown()
    grass.begin_fill()
    i: int = 0
    while i < 2:
        grass.forward(600)
        grass.left(90)
        grass.forward(200)
        grass.left(90)
        i += 1
    grass.end_fill()
    

def draw_sky(sky: Turtle, x: float, y: float) -> None:
    """Draw the sky."""
    sky.setheading(0.0)
    sky.color("light blue")
    sky.penup()
    sky.goto(x, y)
    sky.pendown()
    sky.begin_fill()
    i: int = 0
    while i < 2:
        sky.forward(600)
        sky.left(90)
        sky.forward(600)
        sky.left(90)
        i += 1
    sky.end_fill()


def draw_cloud(cloud: Turtle, x: float, y: float) -> None:
    """Draws a cloud."""
    i: int = 0
    # Bottom row of cloud. 
    while i < 3:
        cloud.penup()
        cloud.goto(x + 25 * i, y)
        cloud.dot(30, "white")
        i += 1
    i = 0
    x -= 15
    y += 15
    # Middle row of cloud. 
    while i < 4:
        cloud.penup()
        cloud.goto(x + 25 * i, y)
        cloud.dot(30, "white")
        i += 1
    i = 0
    x += 15
    y += 15
    # Top row of cloud. 
    while i < 3:
        cloud.penup()
        cloud.goto(x + 25 * i, y)
        cloud.dot(30, "white")
        i += 1


def draw_stem(stem: Turtle, x: float, y: float) -> None:
    """Draw the stem of the sunflower."""
    stem.setheading(0.0)
    stem.color("green")
    stem.penup()
    stem.goto(x, y)
    stem.pendown()
    i: int = 0
    while i < 2:
        stem.begin_fill()
        stem.forward(50)
        stem.left(90)
        stem.forward(300)
        stem.left(90)
        stem.end_fill()
        i += 1
    draw_leaves(stem, x, -150)
    draw_leaves(stem, x - 150, -200)
  

def draw_leaves(leaves: Turtle, x: float, y: float) -> None:
    """Adds the leaves to the stem."""
    leaves.hideturtle()
    leaves.speed(0)
    leaves.color("green")
    leaves.penup()
    leaves.goto(x, y)
    leaves.pendown()
    leaves.begin_fill()
    leaves.setheading(15)
    leaves.forward(100)
    leaves.right(30)
    leaves.forward(100)
    leaves.right(150)
    leaves.forward(100)
    leaves.right(30)
    leaves.forward(100)
    leaves.end_fill()


def draw_center(center: Turtle, x: float, y: float) -> None:
    """Draw the center of the sunflower."""
    center.color("brown")
    center.penup()
    center.goto(x, y)
    center.pendown()
    center.begin_fill()
    center.circle(75)
    center.end_fill()
    i: int = 0
    while i < 40:
        center_dots(center, randint(-50, 50), randint(-50, 50))
        i += 1
    

def center_dots(dots: Turtle, x: float, y: float) -> None:
    """Creates a dot."""
    dots.penup()
    dots.goto(x, y)
    dots.dot(10, "black")


def draw_petals(petals: Turtle, x: float, y: float) -> None:
    """Draws the petals of the sunflower."""
    petals.penup()
    petals.goto(x, y)
    petals.pendown()
    j: int = 0
    while j < 8:
        one_petal(petals, 67.5 + 45 * j)
        j += 1
    i: int = 0
    while i < 8:
        one_petal(petals, 90 + 45 * i)
        i += 1
    

def one_petal(petal: Turtle, z: float) -> None:
    """Draws one petal."""
    petal.pencolor("black")
    petal.fillcolor("yellow")
    petal.setheading(z)
    petal.begin_fill()
    petal.left(22.5)
    petal.forward(100)
    petal.right(45)
    petal.forward(100)
    petal.right(135)
    petal.forward(100)
    petal.right(45)
    petal.forward(100)
    petal.end_fill()


# To-do: Use the __name__ is "__main__" idiom shown in class. 
if __name__ == "__main__":
    main()