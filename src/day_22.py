""" Day 22 of Coding Challenges for pong"""
import time

from src.constants.values import GAME_SPEED
from src.classes.pong.pong_game import PongGame


def pong() -> None:
    """Play the pong game"""
    pong_game = PongGame()
    speed = pong_game.screen.textinput(title="Snake Difficulty",
                                       prompt=f"How difficult do you want? "
                                              f"{", ".join(GAME_SPEED.keys())}: ")
    pong_game.capture_keypress()
    while pong_game.game_on():
        pong_game.screen.update()
        time.sleep(GAME_SPEED[speed])
        pong_game.ball.move()
        pong_game.detect_collisions()
        pong_game.detect_goal()

    pong_game.screen.exitonclick()
