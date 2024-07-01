"""Class to represent food in the snake game"""
from random import randint
from turtle import Turtle

from src.constants.values import SNAKE_FOOD


class Food(Turtle):
    """Class to represent food in the snake game"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("chartreuse")
        self.speed("fastest")
        self.move_to_new_location()

    def move_to_new_location(self):
        """Randomly move the food to a new location"""
        random_x = randint(SNAKE_FOOD["x"]["min"], SNAKE_FOOD["x"]["max"])
        random_y = randint(SNAKE_FOOD["y"]["min"], SNAKE_FOOD["y"]["max"])
        self.goto(random_x, random_y)
