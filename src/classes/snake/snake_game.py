""" Class for the entire snake game"""
from turtle import Screen

from src.classes.snake.food import Food
from src.classes.snake.snake_scoreboard import SnakeScoreboard
from src.classes.snake.snake import Snake
from src.constants.values import SNAKE_SCREEN, SNAKE_SCREEN_SIZE, SNAKE_SPACING


class SnakeGame:
    """ Class for the entire snake game"""

    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.snake = Snake()
        self.capture_keypress()
        self.food = Food()
        self.scoreboard = SnakeScoreboard()

    def capture_keypress(self) -> None:
        """ Capture the key pressed and move the snake"""
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.snake.up)
        self.screen.onkey(key="Down", fun=self.snake.down)
        self.screen.onkey(key="Left", fun=self.snake.left)
        self.screen.onkey(key="Right", fun=self.snake.right)

    def setup_screen(self) -> None:
        """ Set up the screen for the snake game"""
        self.screen.setup(width=SNAKE_SCREEN_SIZE, height=SNAKE_SCREEN_SIZE)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

    def on_map(self) -> bool:
        """ Detect if the snake is still on the map"""
        if self.snake.head.xcor() > SNAKE_SCREEN["x"]["max"] \
                or self.snake.head.xcor() < SNAKE_SCREEN["x"]["min"] \
                or self.snake.head.ycor() > SNAKE_SCREEN["y"]["max"] \
                or self.snake.head.ycor() < SNAKE_SCREEN["y"]["min"]:
            return False
        return True

    def collision(self) -> bool:
        """ Detect is there is no collision with the end of the snake"""
        for segment in self.snake.segments[1:len(self.snake.segments) - 1]:
            if self.snake.head.distance(segment) < SNAKE_SPACING / 2:
                return True
        return False

    def play_again(self) -> bool:
        """ Detect if the player wants to play again"""
        response = self.screen.textinput("Snake Game", "Do you want to play again? (y/n)")
        if response == 'y':
            return True
        self.scoreboard.game_over()
        return False

    def round_over(self) -> bool:
        """ Detect if the round has ended"""
        if self.on_map() and not self.collision():
            return False
        self.scoreboard.reset()
        self.snake.reset()
        return True

    def eat_food(self) -> None:
        """ Eat the food when the snake is close enough"""
        if self.snake.head.distance(self.food) < 15:
            self.snake.extend()
            self.food.move_to_new_location()
            self.scoreboard.increase_score()
