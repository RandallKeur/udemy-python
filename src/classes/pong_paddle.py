"""Class to represent that paddle in the pong game"""
from turtle import Turtle

from src.constants.values import UP, DOWN


class PongPaddle(Turtle):
    """Class to represent the paddle in the pong game"""

    def __init__(self, starting_position: int):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.move_to_starting_position(starting_position)

    def move_to_starting_position(self, starting_position: int):
        """Moves the paddle to its starting position"""
        self.penup()
        self.hideturtle()
        self.goto(starting_position, 0)
        self.setheading(UP)
        self.showturtle()

    def move(self):
        """Move the paddle"""
        self.forward(10)

    def move_up(self):
        self.setheading(UP)
        self.move()

    def move_down(self):
        self.setheading(DOWN)
        self.move()


