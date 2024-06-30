""" Day 20 of Coding Challenges for Snake"""
import time

from src.classes.snake_game import SnakeGame


def snake() -> None:
    """Play a snake game"""
    snake_game = SnakeGame()
    snake_game.scoreboard.hideturtle()
    snake_game.food.hideturtle()

    game_is_on = True
    while game_is_on:
        snake_game.screen.update()
        time.sleep(0.1)
        snake_game.snake.move()

    snake_game.screen.exitonclick()
