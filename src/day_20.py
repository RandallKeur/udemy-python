""" Day 20 of Coding Challenges for Snake"""
import time
from turtle import Screen

from src.classes.snake import Snake


def setup_screen() -> Screen:
    """Setup the screen for the snake game"""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


def capture_keypress(screen: Screen, new_snake: Snake) -> None:
    """Capture the key pressed and move the snake"""
    screen.listen()
    screen.onkey(key="Up", fun=new_snake.up)
    screen.onkey(key="Down", fun=new_snake.down)
    screen.onkey(key="Left", fun=new_snake.left)
    screen.onkey(key="Right", fun=new_snake.right)


def snake() -> None:
    """Play a snake game"""
    screen = setup_screen()
    new_snake = Snake()
    capture_keypress(screen, new_snake)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        new_snake.move()

    screen.exitonclick()
