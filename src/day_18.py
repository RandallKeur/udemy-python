""" Day 18 of Coding Challenges for Turtle graphics"""
# pylint: disable=no-name-in-module
from math import floor, sqrt
from random import randint
from turtle import colormode, Turtle, Screen

from src.constants.values import DEFAULT_TURTLE_DISTANCE


def go_to_start(turtle: Turtle) -> None:
    """ Go to the starting position for the painting"""
    turtle.penup()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)


def configure_turtle() -> Turtle:
    """ Configure the turtle for painting"""
    turtle = Turtle()
    turtle.speed("fastest")
    turtle.hideturtle()
    colormode(255)
    go_to_start(turtle)
    return turtle


def next_row(turtle: Turtle, dots_per_row: int) -> None:
    """ Go to the next row for the turtle to paint"""
    turtle.setheading(90)
    turtle.forward(DEFAULT_TURTLE_DISTANCE)
    turtle.setheading(180)
    turtle.forward(DEFAULT_TURTLE_DISTANCE * dots_per_row)
    turtle.setheading(0)


def paint_random_color_dot(turtle: Turtle) -> None:
    """ Paint random colored dot"""
    random_color = tuple((randint(0, 255), randint(0, 255), randint(0, 255)))
    turtle.color(random_color)
    turtle.dot(20, random_color)


def paint_dots(number_of_dots: int) -> None:
    """ Paint a picture with the turtle screen"""
    turtle = configure_turtle()
    dots_per_row = floor(sqrt(number_of_dots))

    for dot_count in range(1, number_of_dots + 1):
        paint_random_color_dot(turtle)
        turtle.forward(DEFAULT_TURTLE_DISTANCE)

        if dot_count % dots_per_row == 0:
            next_row(turtle, dots_per_row)

    turtle.hideturtle()
    screen = Screen()
    screen.exitonclick()
