""" Class to represent the Pomodoro timer"""
from math import ceil
from tkinter import Tk, Canvas, PhotoImage, Label, Button

from src.constants.fonts import COURIER
from src.constants.values import YELLOW, GREEN, CYCLE, POMODORO_CANVAS, CONSTANTS_FILEPATH


class PomodoroTimer:
    """ Class to represent the Pomodoro timer"""
    # pylint: disable=too-many-instance-attributes

    def __init__(self):
        self.window = Tk()
        self.configure_window()
        self.text = Label(text="Timer", font=(COURIER, 50), bg=YELLOW, fg=GREEN)
        self.canvas = Canvas(width=POMODORO_CANVAS["width"], height=POMODORO_CANVAS["height"],
                             bg=YELLOW, highlightthickness=0)
        self.background = PhotoImage(file=f"{CONSTANTS_FILEPATH}tomato.png")
        self.set_background()
        self.time_remaining = 0
        self.timer = self.create_timer()
        self.start_button = Button(text="Start", command=self.start_timer,
                                   highlightbackground=YELLOW)
        self.reset_button = Button(text="Reset", command=self.reset_timer,
                                   highlightbackground=YELLOW)
        self.check_marks = Label(text="", font=(COURIER, 35), bg=YELLOW, fg=GREEN)
        self.current_stage = 0
        self.completed_steps = 0
        self.organize_grid()

    def configure_window(self):
        """ Configure the window"""
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)

    def set_background(self):
        """ Set the background of the canvas"""
        self.canvas.create_image(POMODORO_CANVAS["width"] / 2,
                                 POMODORO_CANVAS["height"] / 2, image=self.background)

    def create_timer(self):
        """ Create the timer"""
        return self.canvas.create_text(POMODORO_CANVAS["width"] / 2,
                                       POMODORO_CANVAS["height"] / 2 + 20,
                                       text=self.format_time(), fill="white",
                                       font=(COURIER, 35, "bold"))

    def place_buttons(self):
        """ Place the buttons"""
        self.start_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2)

    def organize_grid(self):
        """ Organize the grid layout of the screen"""
        self.text.grid(row=0, column=1)
        self.canvas.grid(row=1, column=1)
        self.place_buttons()
        self.check_marks.grid(row=3, column=1)

    def format_timer(self):
        """ Format the timer to the correct format"""
        self.canvas.itemconfig(self.timer, text=self.format_time())

    def format_time(self) -> str:
        """ Get a formatted time in 00:00 format"""
        minute, second = divmod(self.time_remaining, 60)
        return f"{minute:01d}:{second:02d}"

    def update_pomodoro_stage(self):
        """ Update the stage of the pomodoro"""
        self.text.config(text=CYCLE[self.current_stage]["text"])
        self.time_remaining = CYCLE[self.current_stage]["time"] * 60

    def update_check_marks(self):
        """ Update the check_marks label"""
        pomodoros = ceil(self.completed_steps / 2)
        self.check_marks.config(text="".join("✔" for i in range(pomodoros)))

    def determine_pomodoro_stage(self):
        """ Determine the stage of the pomodoro"""
        if self.current_stage == len(CYCLE) - 1:
            self.current_stage = 0
        else:
            self.current_stage += 1
            self.completed_steps += 1

    def complete_stage(self):
        """ Complete the stage of the Pomodoro"""
        self.determine_pomodoro_stage()
        self.update_check_marks()
        self.update_pomodoro_stage()
        self.format_timer()

    def count_down(self):
        """ Count down the timer by 1 second"""
        self.format_timer()
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.window.after(1000, self.count_down)
        else:
            self.place_buttons()
            self.complete_stage()

    def hide_buttons(self):
        """ Hide the buttons"""
        self.start_button.grid_forget()
        self.reset_button.grid_forget()

    def start_timer(self):
        """ Start the timer"""
        self.hide_buttons()
        self.update_pomodoro_stage()
        self.count_down()

    def reset_timer(self):
        """ Reset the timer"""
        self.time_remaining = 0
        self.completed_steps = 0
        self.current_stage = 0
        self.format_timer()
        self.text.config(text="Timer")
        self.check_marks.config(text="")

    def start_mainloop(self):
        """ Start the Tkinter main loop """
        self.window.mainloop()
