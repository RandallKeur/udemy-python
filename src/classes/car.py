"""Class to represent the car manager in the turtle crossing game"""
from random import randint, choice
from turtle import Turtle

from src.constants.values import CAR_COLORS, TURTLE_CROSSING_SCREEN, TURTLE_CROSSING_OFFSETS, CAR_STARTING_DISTANCE, \
    PLAYER_FINISH_LINE


class Car(Turtle):
    """Class to represent the car manager in the turtle crossing game"""

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(CAR_COLORS))
        self.go_to_random_location()

    def go_to_random_location(self):
        """Method to move the car to a random starting location"""
        x_value = TURTLE_CROSSING_SCREEN["x"]["max"] - CAR_STARTING_DISTANCE
        y_value = randint(TURTLE_CROSSING_SCREEN["y"]["min"]
                          + TURTLE_CROSSING_OFFSETS["player"],
                          PLAYER_FINISH_LINE)
        self.goto(x=x_value, y=y_value)

