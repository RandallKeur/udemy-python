""" Class to represent the Pomodoro timer"""
from tkinter import Tk, Canvas, PhotoImage, Label, Button

from src.constants.values import YELLOW, FONT_NAME, GREEN


class PomodoroTimer:
    """ Class to represent the Pomodoro timer"""

    def __init__(self):
        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        self.text = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
        self.canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
        self.background = PhotoImage(file="src/constants/tomato.png")
        self.canvas.create_image(100, 125, image=self.background)
        self.time_remaining = 0
        self.timer = self.canvas.create_text(100, 145, text=self.format_time(), fill="white",
                                             font=(FONT_NAME, 25, "bold"))
        self.start_button = Button(text="Start", command=self.start_timer, highlightbackground=YELLOW)
        self.reset_button = Button(text="Reset", command=self.reset_timer, highlightbackground=YELLOW)
        self.check_marks = Label(text="", font=FONT_NAME, bg=YELLOW, fg=GREEN)
        self.current_stage = 0
        self.organize_grid()

    def organize_grid(self):
        """ Organize the grid layout of the screen"""
        self.text.grid(row=0, column=1)
        self.canvas.grid(row=1, column=1)
        self.start_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2)
        self.check_marks.grid(row=3, column=1)

    def format_time(self) -> str:
        """ Get a formatted time in 00:00 format"""
        minute, second = divmod(self.time_remaining, 60)
        return '{:01d}:{:02d}'.format(minute, second)

    def complete_stage(self):
        """ Complete the stage of the Pomodoro"""
        self.current_stage += 1

    def count_down(self):
        """ Count down the timer by 1 second"""
        self.canvas.itemconfig(self.timer, text=self.format_time())
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.window.after(1000, self.count_down)
        else:
            self.complete_stage()

    def start_timer(self):
        """ Start the timer"""
        self.time_remaining = 5 * 60
        self.count_down()

    def reset_timer(self):
        """ Reset the timer"""
        self.time_remaining = 0
        self.canvas.itemconfig(self.timer, text=self.format_time())
        self.text.config(text="Timer")
        self.check_marks.config(text="")

    def start_mainloop(self):
        """ Start the Tkinter main loop """
        self.window.mainloop()
