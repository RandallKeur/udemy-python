""" Day 19 of Coding Challenges for Turtle Etch-a-Sketch"""
# pylint: disable=no-member
from random import randint
from turtle import Screen, Turtle

from src.classes.sketching_turtle import SketchingTurtle
from src.constants.values import TURTLE_COLORS, MIN_VALUES, Y_SPACING, MAX_VALUES, RACE_DIMENSIONS


def move_turtle(screen: Screen, turtle: SketchingTurtle) -> None:
    """Listen to keys and move the turtle as specified by the user"""
    screen.listen()
    screen.onkey(key="w", fun=turtle.move_forward)
    screen.onkey(key="s", fun=turtle.move_backward)
    screen.onkey(key="a", fun=turtle.turn_counter_clockwise)
    screen.onkey(key="d", fun=turtle.turn_clockwise)
    screen.onkey(key="c", fun=turtle.restart_sketch)


def sketch(screen: Screen) -> None:
    """Sketching using the turtle graphics"""
    turtle = SketchingTurtle()
    turtle.shape("turtle")
    move_turtle(screen, turtle)


def build_turtle(index: int) -> Turtle:
    """Create a new turtle and return it"""
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(TURTLE_COLORS[index])
    new_turtle.penup()
    return new_turtle


def turtle_to_the_starting_gate(all_turtles: list[Turtle], index: int) -> None:
    """Move the turtle to their starting position"""
    new_turtle = build_turtle(index)
    all_turtles.append(new_turtle)
    new_turtle.goto(x=MIN_VALUES["x"], y=MIN_VALUES["y"] + Y_SPACING * index)


def setup_race() -> list[Turtle]:
    """Set up the turtle race"""
    racing_turtles = []
    for index in range(0, len(TURTLE_COLORS)):
        turtle_to_the_starting_gate(racing_turtles, index)
    return racing_turtles


def run_race(racing_turtles: list[Turtle], is_race_on: bool) -> str:
    """Run the race and return the winning color"""
    winning_color = ""
    while is_race_on:
        for racer in racing_turtles:
            if racer.xcor() > MAX_VALUES["x"]:
                is_race_on = False
                winning_color = racer.pencolor()
            racer.forward(randint(0, 10))
    return winning_color


def determine_winner(winning_color: str, bet: str) -> None:
    """Determine the winner of the race"""
    if winning_color == bet:
        print(f"You won! The {winning_color} turtle won!")
    else:
        print(f"You lost! The {winning_color} turtle won!")


def race(screen: Screen) -> None:
    """Racing turtles game"""
    is_race_on = False
    screen.setup(width=RACE_DIMENSIONS["x"], height=RACE_DIMENSIONS["y"])
    racing_turtles = setup_race()
    bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race?"
                                                         f" Enter a color: {TURTLE_COLORS}: ")
    if bet:
        is_race_on = True
    winning_color = run_race(racing_turtles, is_race_on)
    determine_winner(winning_color, bet)


def play() -> None:
    """Play either etch-a-sketch or race"""
    screen = Screen()
    response = screen.textinput(title="Make your choice", prompt="Choose a game "
                                                                 "\'sketch\' or \'race\': ")
    match response:
        case "sketch":
            sketch(screen)
        case "race":
            race(screen)
        case _:
            print("Invalid input")
    screen.exitonclick()
