"""Class to represent the scoreboard in the snake game"""
from turtle import Turtle

from src.constants.values import SCOREBOARD_SETTINGS


class SnakeScoreboard(Turtle):
    """Class to represent the scoreboard in the snake game"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_SETTINGS["locations"]["snake"])
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1"""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}", align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["arial"],
                         SCOREBOARD_SETTINGS["font"]["size"]["small"],
                         SCOREBOARD_SETTINGS["font"]["weight"]))

    def game_over(self):
        """End the game"""
        self.goto(0, 0)
        self.write(SCOREBOARD_SETTINGS["game_over"], align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["arial"],
                         SCOREBOARD_SETTINGS["font"]["size"]["large"],
                         SCOREBOARD_SETTINGS["font"]["weight"])
                   )
