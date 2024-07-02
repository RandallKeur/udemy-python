"""Class to represent the scoreboard of the turtle crossing game"""
from turtle import Turtle

from src.constants.values import SCOREBOARD_SETTINGS


class TurtleCrossingScoreboard(Turtle):
    """Class to represent the scoreboard of the turtle crossing game"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_SETTINGS["locations"]["turtle_crossing"])
        self.color("black")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """Update the scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}",
                   align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["courier"],
                         SCOREBOARD_SETTINGS["font"]["size"]["large"],
                         SCOREBOARD_SETTINGS["font"]["weight"]))

    def game_over(self) -> None:
        """End the game"""
        self.goto(0, 0)
        self.write(SCOREBOARD_SETTINGS["game_over"], align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["arial"],
                         SCOREBOARD_SETTINGS["font"]["size"]["x-large"],
                         SCOREBOARD_SETTINGS["font"]["weight"])
                   )

    def level_up(self):
        """Update the scoreboard with the next level"""
        self.level += 1
        self.update_scoreboard()
