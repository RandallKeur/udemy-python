from turtle import Turtle


class SketchingTurtle(Turtle):
    """Models a turtle that can do sketching"""

    def __init__(self):
        super().__init__()

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)

    def turn_counter_clockwise(self):
        self.left(15)

    def turn_clockwise(self):
        self.right(15)

    def restart_sketch(self):
        self.home()
        self.clear()
