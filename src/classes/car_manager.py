"""Class to represent the car manager in the turtle crossing game"""
import time
from random import randint

from src.classes.car import Car


class CarManager:
    """Class to represent the car manager in the turtle crossing game"""

    def __init__(self):
        self.cars = []

    def add_car(self):
        car = Car()
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        self.cars.append(car)

    def move_cars_forward(self):
        for car in self.cars:
            car.forward(randint(0, 10))
