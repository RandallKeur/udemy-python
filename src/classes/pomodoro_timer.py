""" Class to represent the Pomodoro timer"""
from tkinter import Tk, Canvas, PhotoImage

from src.constants.values import YELLOW, FONT_NAME


class PomodoroTimer:
    """ Class to represent the Pomodoro timer"""

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.background = PhotoImage(file="src/constants/tomato.png")
        self.configure_screen()

    def configure_screen(self):
        """ Configure the screen for the Pomodoro timer"""
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        self.canvas.create_image(100, 100, image=self.background)
        self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
        self.canvas.pack()

    def start(self):
        """ Start the Tkinter main loop """
        self.window.mainloop()
