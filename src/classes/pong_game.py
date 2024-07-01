"""Class for the pong game"""
from turtle import Screen

from src.classes.pong_ball import PongBall
from src.classes.pong_scoreboard import PongScoreboard
from src.classes.pong_paddle import PongPaddle
from src.constants.values import PONG_SCREEN_SIZE, PONG_PADDLE_LOCATION, PONG_SCREEN


class PongGame:
    """Class for the pong game"""

    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.scoreboard = PongScoreboard()
        self.left_paddle = PongPaddle(PONG_PADDLE_LOCATION["left"])
        self.right_paddle = PongPaddle(PONG_PADDLE_LOCATION["right"])
        self.ball = PongBall()

    def setup_screen(self):
        """Set up the screen for the pong game"""
        self.screen = Screen()
        self.screen.setup(width=PONG_SCREEN_SIZE["x"], height=PONG_SCREEN_SIZE["y"])
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

    def capture_keypress(self):
        """Capture the key pressed and move the paddle"""
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.right_paddle.move_up)
        self.screen.onkey(key="Down", fun=self.right_paddle.move_down)
        self.screen.onkey(key="w", fun=self.left_paddle.move_up)
        self.screen.onkey(key="s", fun=self.left_paddle.move_down)

    def detect_bounce_off_wall(self):
        if self.ball.ycor() >= PONG_SCREEN["y"]["max"] or self.ball.ycor() <= PONG_SCREEN["y"]["min"]:
            self.ball.bounce()

