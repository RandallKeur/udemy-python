""" Day 22 of Coding Challenges for turtle crossing"""
import time

from src.classes.turtle_crossing import TurtleCrossing


def turtle_crossing():
    """Turtle crossing game"""
    turtle_crossing_game = TurtleCrossing()
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        turtle_crossing_game.screen.update()
        turtle_crossing_game.car_manager.move_cars_forward()
