""" Day 21 of Coding Challenges for fully implemented Snake"""
import time

from src.classes.snake.snake_game import SnakeGame
from src.constants.values import GAME_SPEED


def play_round(snake_game: SnakeGame, ) -> None:
    """Play a round of the snake game"""
    speed = snake_game.screen.textinput(title="Snake Difficulty",
                                        prompt=f"How difficult do you want? "
                                               f"{", ".join(GAME_SPEED.keys())}: ")
    snake_game.capture_keypress()
    while not snake_game.round_over():
        snake_game.screen.update()
        time.sleep(GAME_SPEED[speed])
        snake_game.snake.move()
        snake_game.eat_food()


def snake() -> None:
    """Play a snake game"""
    snake_game = SnakeGame()
    is_game_on = True
    while is_game_on:
        play_round(snake_game)
        is_game_on = snake_game.play_again()
    snake_game.screen.exitonclick()
