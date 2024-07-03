"""Class to represent the states quiz game"""
from turtle import Screen, Turtle

from pandas import read_csv

from src.constants.values import STATES_IMAGE, STATES_FILE, STATES_SCREEN_SIZE


class StatesQuizGame():
    """Class to represent the states quiz game"""

    def __init__(self):
        self.screen = self.setup_screen()
        self.data = self.build_states_dictionary()
        self.answer = None
        self.correct_answers = 0
        self.writer = self.setup_writer()

    @staticmethod
    def setup_screen() -> Screen:
        """Set up the screen for the states quiz game"""
        screen = Screen()
        screen.setup(width=STATES_SCREEN_SIZE["x"], height=STATES_SCREEN_SIZE["y"])
        screen.title("U.S. States Game")
        screen.bgpic(f"{STATES_IMAGE}")
        return screen

    @staticmethod
    def build_states_dictionary():
        """Create a dictionary with states"""
        data = read_csv(f"{STATES_FILE}")
        data['state'] = data['state'].str.lower()
        return data.set_index('state').T.to_dict()

    @staticmethod
    def setup_writer() -> Turtle:
        """Create a writer object for the states quiz game"""
        writer = Turtle()
        writer.penup()
        writer.hideturtle()
        return writer

    def collect_guess(self) -> None:
        """Collects the name of the state guessed"""
        self.answer = (self.screen.textinput(title=f"{self.correct_answers}/50 States correct",
                                             prompt="What's a state\'s name?").lower())

    def game_on(self) -> bool:
        """Detects if the game is over and displays game over"""
        if len(self.data) == 0:
            return False
        return True

    def check_guess(self) -> None:
        """Checks if the guess is correct"""
        self.collect_guess()
        if self.data.get(self.answer) is not None:
            self.write_state()
            self.data.pop(self.answer)
            self.correct_answers += 1

    def write_state(self) -> None:
        """Writes the state in the specified location"""
        self.writer.goto(self.data.get(self.answer)["x"],
                         self.data.get(self.answer)["y"])
        self.writer.write(self.answer)
