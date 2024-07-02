""" Day 21 of Coding Challenges for fully implemented Snake"""
import time

from src.classes.snake.snake_game import SnakeGame
from src.constants.values import GAME_SPEED


def snake() -> None:
    """Play a snake game"""
    snake_game = SnakeGame()
    speed = snake_game.screen.textinput(title="Snake Difficulty",
                                        prompt=f"How difficult do you want? "
                                               f"{", ".join(GAME_SPEED.keys())}: ")
    snake_game.capture_keypress()

    while snake_game.game_on():
        snake_game.screen.update()
        time.sleep(GAME_SPEED[speed])
        snake_game.snake.move()
        snake_game.eat_food()

    snake_game.screen.exitonclick()
