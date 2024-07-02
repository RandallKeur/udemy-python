"""Class for the pong game"""
from turtle import Screen

from src.classes.pong.pong_ball import PongBall
from src.classes.pong.pong_scoreboard import PongScoreboard
from src.classes.pong.pong_paddle import PongPaddle
from src.constants.values import PONG_SCREEN_SIZE, PONG_PADDLE_LOCATION, PONG_SCREEN, PONG_OFFSETS


class PongGame:
    """Class for the pong game"""

    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.scoreboard = PongScoreboard()
        self.left_paddle = PongPaddle(PONG_PADDLE_LOCATION["left"])
        self.right_paddle = PongPaddle(PONG_PADDLE_LOCATION["right"])
        self.ball = PongBall()
        self.winning_score = self.set_winning_score()

    def setup_screen(self):
        """Set up the screen for the pong game"""
        self.screen.setup(width=PONG_SCREEN_SIZE["x"], height=PONG_SCREEN_SIZE["y"])
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

    def set_winning_score(self) -> int:
        """Set the winning score to be played to"""
        response = self.screen.textinput(title="Snake Game",
                                         prompt="What score do you want to play to?: ")
        return int(response)

    def capture_keypress(self):
        """Capture the key pressed and move the paddle"""
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.right_paddle.move_up)
        self.screen.onkey(key="Down", fun=self.right_paddle.move_down)
        self.screen.onkey(key="r", fun=self.left_paddle.move_up)
        self.screen.onkey(key="f", fun=self.left_paddle.move_down)

    def detect_collision_with_paddle(self):
        """Detect a collision with either paddle"""
        if self.right_paddle.ycor() - 50 <= self.ball.ycor() <= self.right_paddle.ycor() + 50\
                and self.ball.xcor() > PONG_PADDLE_LOCATION["right"] - PONG_OFFSETS["paddle"]\
                or self.left_paddle.ycor() - 50 <= self.ball.ycor() <= self.left_paddle.ycor() + 50\
                and self.ball.xcor() < PONG_PADDLE_LOCATION["left"] + PONG_OFFSETS["paddle"]:
            self.ball.bounce()

    def detect_collision_with_wall(self):
        """Detect a collision with the wall"""
        if self.ball.ycor() > PONG_SCREEN["y"]["max"] - PONG_OFFSETS["ball"] \
                or self.ball.ycor() < PONG_SCREEN["y"]["min"] + PONG_OFFSETS["ball"]:
            self.ball.bounce()

    def detect_collisions(self):
        """Detect if there is a collision"""
        self.detect_collision_with_paddle()
        self.detect_collision_with_wall()

    def score_left(self):
        """Score a goal for the left player"""
        self.scoreboard.score["left"] += 1
        self.scoreboard.update_scoreboard()
        self.ball.reset_position()

    def score_right(self):
        """Score a goal for the right player"""
        self.scoreboard.score["right"] += 1
        self.scoreboard.update_scoreboard()
        self.ball.reset_position()

    def detect_goal(self):
        """Detect if a goal has been scored"""
        if self.ball.xcor() > PONG_PADDLE_LOCATION["right"]:
            self.score_left()
        if self.ball.xcor() < PONG_PADDLE_LOCATION["left"]:
            self.score_right()

    def game_on(self):
        """Determine if the game is still going"""
        if self.scoreboard.score["left"] >= self.winning_score \
                or self.scoreboard.score["right"] >= self.winning_score:
            self.scoreboard.game_over()
            return False
        return True
