""" Day 21 of Coding Challenges for fully implemented Snake"""
import time
from turtle import Screen

from src.classes.scoreboard import Scoreboard
from src.classes.food import Food
from src.constants.values import SNAKE_SPEED, SNAKE_FOOD, SNAKE_SCREEN
from src.classes.snake import Snake


def setup_screen() -> Screen:
    """Set up the screen for the snake game"""
    screen = Screen()
    screen.setup(width=SNAKE_SCREEN['x'], height=SNAKE_SCREEN['y'])
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


def on_map(new_snake: Snake, new_scoreboard: Scoreboard) -> bool:
    """Detect if the snake is still on the map"""
    if new_snake.head.xcor() > SNAKE_FOOD['x']['max'] or new_snake.head.xcor() < SNAKE_FOOD['x']['min'] \
            or new_snake.head.ycor() > SNAKE_FOOD['y']['max'] or new_snake.head.ycor() < SNAKE_FOOD['y']['min']:
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
    screen = setup_screen()
    speed = screen.textinput(title='Snake Difficulty', prompt=f'How difficult do you want?'
                                                              f'{SNAKE_SPEED.keys()}: ')
    new_snake = Snake()
    new_food = Food()
    new_scoreboard = Scoreboard()
    capture_keypress(screen, new_snake)

    while on_map(new_snake, new_scoreboard) and no_collision(new_snake, new_scoreboard):
        screen.update()
        time.sleep(SNAKE_SPEED[speed])
        new_snake.move()
        eat_food(new_snake, new_food, new_scoreboard)

    screen.exitonclick()
