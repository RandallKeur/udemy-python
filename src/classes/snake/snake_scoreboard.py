"""Class to represent the scoreboard in the snake game"""
import os
from turtle import Turtle

from src.constants.values import SCOREBOARD_SETTINGS, HIGH_SCORE_FILE


class SnakeScoreboard(Turtle):
    """Class to represent the scoreboard in the snake game"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_SETTINGS["locations"]["snake"])
        self.color("white")
        self.high_score = self.get_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self) -> None:
        """Increase the score by 1"""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """Update the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",
                   align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["arial"],
                         SCOREBOARD_SETTINGS["font"]["size"]["small"],
                         SCOREBOARD_SETTINGS["font"]["weight"]))

    def reset(self):
        """Reset the scoreboard on the screen with new high score"""
        self.high_score = max(self.high_score, self.score)
        self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def game_over(self) -> None:
        """End the game"""
        self.goto(0, 0)
        self.write(SCOREBOARD_SETTINGS["game_over"], align=SCOREBOARD_SETTINGS["alignment"],
                   font=(SCOREBOARD_SETTINGS["font"]["family"]["arial"],
                         SCOREBOARD_SETTINGS["font"]["size"]["large"],
                         SCOREBOARD_SETTINGS["font"]["weight"])
                   )

    def save_high_score(self) -> None:
        """Save the high score to a local text file"""
        if os.path.exists(f"{HIGH_SCORE_FILE}"):
            os.remove(f"{HIGH_SCORE_FILE}")
        with open(f"{HIGH_SCORE_FILE}", "w", encoding="utf-8") as file:
            file.write("high_score: " + str(self.high_score) + "\n")

    @staticmethod
    def get_file_high_score() -> int:
        """Get the high score from the local file"""
        mydict = {}
        with open(f"{HIGH_SCORE_FILE}", "r", encoding="utf-8") as file:
            for line in file:
                key, value = line.partition(":")[::2]
                mydict[key.strip()] = int(value)
        return mydict["high_score"]

    def get_high_score(self) -> int:
        """Return the high score from the file or default to 0"""
        if os.path.exists(f"{HIGH_SCORE_FILE}"):
            self.get_file_high_score()
        return 0
