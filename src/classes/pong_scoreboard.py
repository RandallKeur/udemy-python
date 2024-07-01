"""Class to represent the scoreboard in the pong game"""
from turtle import Turtle

from src.constants.values import SCOREBOARD_SETTINGS


class PongScoreboard(Turtle):
    """Class to represent the scoreboard in the pong game"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_SETTINGS["locations"]["pong"])
        self.color("white")
        self.score = {
            "1": 0,
            "2": 0
        }
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"{self.score["1"]}     {self.score["2"]}",
                   align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"],
                         SCOREBOARD_SETTINGS["font"]["size"]["x-large"],
                         SCOREBOARD_SETTINGS["font"]["weight"]))
