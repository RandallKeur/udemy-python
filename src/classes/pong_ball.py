"""Class to represent the ball for the pong game"""
from turtle import Turtle

from src.constants.values import PONG_BALL_MOVEMENT


class PongBall(Turtle):
    """Class to represent the ball for the pong game"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("slow")
        self.setheading(45)

    def move(self):
        self.forward(PONG_BALL_MOVEMENT)

    def bounce(self):
        self.setheading(-self.heading())
