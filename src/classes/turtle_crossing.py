"""Class to represent the turtle crossing game"""
from turtle import Screen

from src.classes.turtle_crossing_scoreboard import TurtleCrossingScoreboard
from src.classes.car_manager import CarManager
from src.constants.values import TURTLE_CROSSING_SCREEN_SIZE


class TurtleCrossing:
    """Class to represent the turtle crossing game"""

    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.car_manager = CarManager()
        self.scoreboard = TurtleCrossingScoreboard()

    def setup_screen(self) -> None:
        """Set up the screen for the turtle crossing game"""
        self.screen.setup(width=TURTLE_CROSSING_SCREEN_SIZE, height=TURTLE_CROSSING_SCREEN_SIZE)
        self.screen.bgcolor("white")
        self.screen.title("Turtle Crossing Game")
        self.screen.tracer(0)

