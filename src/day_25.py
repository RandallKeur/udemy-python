""" Day 25 of Coding Challenges for US states game"""
from src.classes.states_quiz_game import StatesQuizGame


def play():
    """ Plays the game"""
    states_quiz_game = StatesQuizGame()
    while states_quiz_game.game_on():
        states_quiz_game.check_guess()
