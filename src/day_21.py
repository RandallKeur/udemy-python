""" Day 21 of Coding Challenges for fully implemented Snake"""
import time

from src.classes.snake_game import SnakeGame
from src.classes.scoreboard import Scoreboard
from src.classes.food import Food
from src.constants.values import SNAKE_SPEED, SNAKE_FOOD
from src.classes.snake import Snake


def on_map(new_snake: Snake, new_scoreboard: Scoreboard) -> bool:
    """Detect if the snake is still on the map"""
    if new_snake.head.xcor() > SNAKE_FOOD["x"]["max"] \
            or new_snake.head.xcor() < SNAKE_FOOD["x"]["min"] \
            or new_snake.head.ycor() > SNAKE_FOOD["y"]["max"] \
            or new_snake.head.ycor() < SNAKE_FOOD["y"]["min"]:
        new_scoreboard.game_over()
        return False
    return True


def no_collision(new_snake: Snake, new_scoreboard: Scoreboard) -> bool:
    """Detect is there is no collision with the end of the snake"""
    for segment in new_snake.segments[1:len(new_snake.segments) - 1]:
        if new_snake.head.distance(segment) < 10:
            new_scoreboard.game_over()
            return False
    return True


def eat_food(new_snake: Snake, new_food: Food, new_scoreboard: Scoreboard):
    """Eat the food when the snake is close enough"""
    if new_snake.head.distance(new_food) < 15:
        new_snake.extend()
        new_food.move_to_new_location()
        new_scoreboard.increase_score()


def snake() -> None:
    """Play a snake game"""
    snake_game = SnakeGame()
    speed = snake_game.screen.textinput(title="Snake Difficulty",
                                        prompt=f"How difficult do you want?"
                                               f"{SNAKE_SPEED.keys()}: ")
    snake_game.capture_keypress()

    while on_map(snake_game.snake, snake_game.scoreboard) \
            and no_collision(snake_game.snake, snake_game.scoreboard):
        snake_game.screen.update()
        time.sleep(SNAKE_SPEED[speed])
        snake_game.snake.move()
        eat_food(snake_game.snake, snake_game.food, snake_game.scoreboard)

    snake_game.screen.exitonclick()
