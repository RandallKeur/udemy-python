"""Class to represent the turtle crossing game"""
from turtle import Screen

from src.classes.turtle_crossing.player import Player
from src.classes.turtle_crossing.scoreboard import TurtleCrossingScoreboard
from src.classes.turtle_crossing.car_manager import CarManager
from src.constants.values import TURTLE_CROSSING_SCREEN_SIZE


class TurtleCrossing:
    """Class to represent the turtle crossing game"""

    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.car_manager = CarManager()
        self.scoreboard = TurtleCrossingScoreboard()
        self.player = Player()

    def setup_screen(self) -> None:
        """Set up the screen for the turtle crossing game"""
        self.screen.setup(width=TURTLE_CROSSING_SCREEN_SIZE, height=TURTLE_CROSSING_SCREEN_SIZE)
        self.screen.bgcolor("white")
        self.screen.title("Turtle Crossing Game")
        self.screen.tracer(0)

    def capture_keypress(self) -> None:
        """Capture the key pressed and move the turtle"""
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.player.go_up)

    def detect_collisions(self) -> bool:
        """Detects collisions with any cars"""
        for car in self.car_manager.cars:
            if car.distance(self.player) < 20:
                return True
        return False

    def game_on(self) -> bool:
        """Detects if the game is over and display game over"""
        if self.detect_collisions():
            self.scoreboard.game_over()
            return False
        return True

    def level_up(self):
        """Updates to next level of the crossing game"""
        if self.player.is_at_finish_line():
            self.scoreboard.level_up()
            self.player.go_to_start()
            self.increase_difficulty()

    def increase_difficulty(self):
        """Increases the difficulty of the game"""
        if self.scoreboard.level % 2 == 0:
            self.car_manager.difficulty["distance"] += 1
        if self.scoreboard.level % 5 == 0:
            self.car_manager.difficulty["probability"] -= 1
