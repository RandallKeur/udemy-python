"""Class to represent that paddle in the pong game"""
from turtle import Turtle

from src.constants.values import UP, DOWN, PONG_PADDLE_MOVEMENT


class PongPaddle(Turtle):
    """Class to represent the paddle in the pong game"""

    def __init__(self, starting_position: int):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.move_to_starting_position(starting_position)

    def move_to_starting_position(self, starting_position: int) -> None:
        """Moves the paddle to its starting position"""
        self.penup()
        self.hideturtle()
        self.goto(starting_position, 0)
        self.setheading(UP)
        self.showturtle()

    def move(self) -> None:
        """Move the paddle"""
        self.forward(PONG_PADDLE_MOVEMENT)

    def move_up(self) -> None:
        """Move the paddle up"""
        self.setheading(UP)
        self.move()

    def move_down(self) -> None:
        """Move the paddle down"""
        self.setheading(DOWN)
        self.move()
