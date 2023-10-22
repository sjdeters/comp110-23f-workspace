"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-150,-100)
leo.pendown()

leo.color(97,224,238)

leo.speed(50)
leo.hideturtle()

side_length: int = 300

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color("black")
bob.penup()
bob.goto(-150,-100)
bob.pendown()
bob.speed(100)
k: int = 0
while (k < 100):
    bob.forward(side_length)
    bob.left(120)
    side_length *= 0.97
    k += 1
done()