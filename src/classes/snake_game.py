"""Class for the entire snake game"""
from turtle import Screen

from src.classes.food import Food
from src.classes.scoreboard import Scoreboard
from src.classes.snake import Snake
from src.constants.values import SNAKE_SCREEN


class SnakeGame:
    """Class for the entire snake game"""

    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.snake = Snake()
        self.capture_keypress()
        self.food = Food()
        self.scoreboard = Scoreboard()

    def capture_keypress(self):
        """Capture the key pressed and move the snake"""
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.snake.up)
        self.screen.onkey(key="Down", fun=self.snake.down)
        self.screen.onkey(key="Left", fun=self.snake.left)
        self.screen.onkey(key="Right", fun=self.snake.right)

    def setup_screen(self):
        """Set up the screen for the snake game"""
        self.screen = Screen()
        self.screen.setup(width=SNAKE_SCREEN['x'], height=SNAKE_SCREEN['y'])
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
