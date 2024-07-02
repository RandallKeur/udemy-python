"""Class to represent the car manager in the turtle crossing game"""
from random import randint

from src.constants.values import CAR_MOVE_DISTANCE
from src.classes.turtle_crossing.car import Car


class CarManager:
    """Class to represent the car manager in the turtle crossing game"""

    def __init__(self):
        self.cars = []
        self.difficulty = {
            "probability": 8,
            "distance": CAR_MOVE_DISTANCE
            }

    def add_car(self) -> None:
        """Add a car to the list of cars"""
        random_chance = randint(1, self.difficulty["probability"])
        if random_chance == 1:
            car = Car()
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(car)

    def move_cars_forward(self) -> None:
        """Move the cars forward a random amount"""
        for car in self.cars:
            car.backward(self.difficulty["distance"])
