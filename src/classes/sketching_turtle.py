"""Class that inherits base turtle class and provides additional
functionality for sketching"""
from turtle import Turtle


class SketchingTurtle(Turtle):
    """Models a turtle that can do sketching"""

    def __init__(self):
        super().__init__()

    def move_forward(self):
        """Move the turtle forward"""
        self.forward(10)

    def move_backward(self):
        """Move the turtle backwards"""
        self.backward(10)

    def turn_counter_clockwise(self):
        """Turn the turtle counter-clockwise by 15 degrees"""
        self.left(15)

    def turn_clockwise(self):
        """Turn the turtle clockwise by 15 degrees"""
        self.right(15)

    def restart_sketch(self):
        """Restarts the sketch"""
        self.home()
        self.clear()
