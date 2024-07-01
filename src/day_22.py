""" Day 22 of Coding Challenges for pong"""

from src.classes.pong_game import PongGame


def pong() -> None:
    """Play the pong game"""
    pong_game = PongGame()
    pong_game.capture_keypress()
    while True:
        pong_game.screen.update()

