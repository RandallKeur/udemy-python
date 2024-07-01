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
            "left": 0,
            "right": 0
        }
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"{self.score["left"]}    {self.score["right"]}",
                   align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["courier"],
                         SCOREBOARD_SETTINGS["font"]["size"]["xx-large"],
                         SCOREBOARD_SETTINGS["font"]["weight"]))
