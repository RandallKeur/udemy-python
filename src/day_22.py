""" Day 22 of Coding Challenges for pong"""
import time

from src.constants.values import PONG_SCREEN, PONG_OFFSETS
from src.classes.pong_game import PongGame


def pong() -> None:
    """Play the pong game"""
    pong_game = PongGame()
    pong_game.capture_keypress()
    while True:
        pong_game.screen.update()
        time.sleep(0.05)
        pong_game.ball.move()
        if pong_game.ball.ycor() >= PONG_SCREEN["y"]["max"] - PONG_OFFSETS["ball"] \
                or pong_game.ball.ycor() <= PONG_SCREEN["y"]["min"] - PONG_OFFSETS["ball"]:
            pong_game.ball.bounce()

