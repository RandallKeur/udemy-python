""" Class to represent the scoreboard in the pong game"""
from turtle import Turtle

from src.constants.values import SCOREBOARD_SETTINGS


class PongScoreboard(Turtle):
    """ Class to represent the scoreboard in the pong game"""

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

    def update_scoreboard(self) -> None:
        """ Update the scoreboard"""
        self.clear()
        self.write(f"P1: {self.score["left"]}   P2: {self.score["right"]}",
                   align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["courier"],
                         SCOREBOARD_SETTINGS["font"]["size"]["xx-large"],
                         SCOREBOARD_SETTINGS["font"]["weight"]))

    def determine_winner(self) -> str:
        """ Determine the winner of the game"""
        if self.score["left"] > self.score["right"]:
            return "Player 1"
        return "Player 2"

    def game_over(self) -> None:
        """ End the game"""
        self.goto(0, 0)
        self.write(f"GAME OVER\n{self.determine_winner()} won!",
                   align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["arial"],
                         SCOREBOARD_SETTINGS["font"]["size"]["large"],
                         SCOREBOARD_SETTINGS["font"]["weight"])
                   )
