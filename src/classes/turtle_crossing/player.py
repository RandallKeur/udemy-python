"""Class to represent a player in the turtle crossing game"""
from turtle import Turtle

from src.constants.values import UP, PLAYER_MOVEMENT, PLAYER_STARTING_POSITION, PLAYER_FINISH_LINE


class Player(Turtle):
    """Class to represent a player in the turtle crossing game"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(PLAYER_STARTING_POSITION)
        self.setheading(UP)

    def go_up(self):
        """Move the player upwards"""
        self.forward(PLAYER_MOVEMENT)

    def go_to_start(self):
        """Move the player to the starting position"""
        self.goto(PLAYER_STARTING_POSITION)

    def is_at_finish_line(self):
        """Checks if the player has reached the finish line"""
        if self.ycor() > PLAYER_FINISH_LINE:
            return True
        return False
