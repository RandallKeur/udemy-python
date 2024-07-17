""" Class to represent a password manager"""
from tkinter import Tk, Canvas, PhotoImage

from src.constants.values import PASSWORD_CANVAS


class PasswordManager:
    """ Class to represent a password manager"""

    def __init__(self):
        self.window = Tk()
        self.configure_window()
        self.canvas = Canvas(width=PASSWORD_CANVAS["width"], height=PASSWORD_CANVAS["height"],
                             bg="white", highlightthickness=0)
        self.background = PhotoImage(file="src/constants/password_manager.png")
        self.set_background()
        self.organize_grid()

    def configure_window(self):
        """ Configure the window"""
        self.window.title("Password Manager")
        self.window.config(padx=20, pady=20, bg="white")

    def set_background(self):
        """ Set the background of the canvas"""
        self.canvas.create_image(PASSWORD_CANVAS["width"] / 2,
                                 PASSWORD_CANVAS["height"] / 2, image=self.background)

    def organize_grid(self):
        """ Organize the grid layout of the screen"""
        self.canvas.grid(row=0, column=0)

    def start_mainloop(self):
        """ Start the Tkinter main loop """
        self.window.mainloop()
