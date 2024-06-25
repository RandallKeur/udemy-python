""" Day 19 of Coding Challenges for Turtle Etch-a-Sketch"""
import turtle
from random import randint
from turtle import Turtle, Screen

timmy = Turtle(shape="turtle")
timmy.hideturtle()
TURTLE_COLORS = ['red', 'orange', 'green', 'blue', 'purple', 'black']
TURTLE_SIZE = 40
RACE_DIMENSIONS = {
    'x': 500,
    'y': 400
}
MAX_VALUES = {
    'x': RACE_DIMENSIONS['x'] / 2 - TURTLE_SIZE / 2,
    'y': RACE_DIMENSIONS['y'] / 2 - 50
}
MIN_VALUES = {
    'x': - MAX_VALUES['x'],
    'y': - MAX_VALUES['y']
}
Y_SPACING = (MAX_VALUES['y'] - MIN_VALUES['y']) / (len(TURTLE_COLORS) - 1)


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_counter_clockwise():
    timmy.left(15)


def turn_clockwise():
    timmy.right(15)


def restart():
    timmy.home()
    timmy.clear()


def draw():
    timmy.showturtle()
    screen = Screen()
    screen.listen()
    screen.onkey(key='w', fun=move_forward)
    screen.onkey(key='s', fun=move_backward)
    screen.onkey(key='a', fun=turn_counter_clockwise)
    screen.onkey(key='d', fun=turn_clockwise)
    screen.onkey(key='c', fun=restart)
    screen.exitonclick()


def turtle_to_the_starting_gate(all_turtles: list[Turtle], index: int) -> None:
    new_turtle = build_turtle(index)
    all_turtles.append(new_turtle)
    go_to_starting_gate(new_turtle, index)


def build_turtle(index: int) -> Turtle:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(TURTLE_COLORS[index])
    new_turtle.penup()
    return new_turtle


def go_to_starting_gate(new_turtle: Turtle, index: int) -> None:
    new_turtle.goto(x=MIN_VALUES['x'], y=MIN_VALUES['y'] + Y_SPACING * index)


def setup_race() -> list[Turtle]:
    racing_turtles = []
    for index in range(0, len(TURTLE_COLORS)):
        turtle_to_the_starting_gate(racing_turtles, index)
    return racing_turtles


def run_race(racing_turtles: list[Turtle], is_race_on: bool) -> str:
    winning_color = ''
    while is_race_on:
        for racer in racing_turtles:
            if racer.xcor() > MAX_VALUES['x']:
                is_race_on = False
                winning_color = racer.pencolor()
            racer.forward(randint(0, 10))
    return winning_color


def determine_winner(winning_color: str, bet: str) -> None:
    if winning_color == bet:
        print(f'You won! The {winning_color} turtle won!')
    else:
        print(f'You lost! The {winning_color} turtle won!')


def race():
    turtle.clearscreen()
    screen = Screen()
    is_race_on = False
    screen.setup(width=RACE_DIMENSIONS['x'], height=RACE_DIMENSIONS['y'])
    racing_turtles = setup_race()
    bet = screen.textinput(title='Make your bet', prompt=f'Which turtle will win the race? Enter a color: {TURTLE_COLORS}: ')
    if bet:
        is_race_on = True
    winning_color = run_race(racing_turtles, is_race_on)
    determine_winner(winning_color, bet)


def play():
    response = input(f'Choose a game \'sketch\' or \'race\': ')
    match response:
        case 'sketch':
            draw()
        case 'race':
            race()
        case _:
            print('Invalid input')
