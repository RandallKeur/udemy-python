""" Day 22 of Coding Challenges for turtle crossing"""
import time

from src.classes.turtle_crossing.game import TurtleCrossing


def turtle_crossing():
    """Turtle crossing game"""
    turtle_crossing_game = TurtleCrossing()
    turtle_crossing_game.capture_keypress()
    while turtle_crossing_game.game_on():
        time.sleep(0.1)
        turtle_crossing_game.screen.update()
        turtle_crossing_game.car_manager.add_car()
        turtle_crossing_game.car_manager.move_cars_forward()
        turtle_crossing_game.detect_collisions()
        turtle_crossing_game.level_up()

    turtle_crossing_game.screen.exitonclick()
