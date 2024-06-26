"""Class to represent a snake in the snake game"""
from turtle import Turtle

from src.constants.values import SNAKE_SPACING, UP, DOWN, LEFT, RIGHT


class Snake:
    """Class to represent a snake in the snake game"""
    def __init__(self):
        self.segments = []
        self.starting_positions = [(0, 0), (-SNAKE_SPACING, 0), (-2 * SNAKE_SPACING, 0)]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the snake"""
        for position in self.starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def up(self):
        """Turn the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        """Move the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(SNAKE_SPACING)
