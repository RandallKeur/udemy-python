""" Class to represent a password manager"""
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END, messagebox

import pyperclip

from src.classes.file_manager import FileManager
from src.classes.password_generator import PasswordGenerator
from src.constants.values import PASSWORD_CANVAS, COURIER, PASSWORD_FILE


def copy_to_clipboard(password):
    """ Copy the password text field to the clipboard"""
    pyperclip.copy(password)


class PasswordManager:
    """ Class to represent a password manager"""
    # pylint: disable=too-many-instance-attributes

    def __init__(self):
        self.window = Tk()
        self.configure_window()
        self.canvas = Canvas(width=PASSWORD_CANVAS["width"], height=PASSWORD_CANVAS["height"],
                             bg="white", highlightthickness=0)
        self.background = PhotoImage(file="src/constants/password_manager.png")
        self.set_background()
        self.website_label = Label(text="Website:", font=(COURIER, 15), bg="white", fg="black")
        self.email_label = Label(text="Email/Username:", font=(COURIER, 15), bg="white", fg="black")
        self.password_label = Label(text="Password:", font=(COURIER, 15), bg="white", fg="black")
        self.website_text = Entry(width=37, bg="white", fg="black", highlightbackground="white")
        self.email_text = Entry(width=37, bg="white", fg="black", highlightbackground="white")
        self.password_text = Entry(width=20, bg="white", fg="black", highlightbackground="white")
        self.text_fields = [self.website_text, self.email_text, self.password_text]
        self.password_generator = PasswordGenerator()
        self.generate_password_button = Button(text="Generate Password",
                                               command=self.generate_password,
                                               highlightbackground="white")
        self.add_button = Button(width=35, text="Add",
                                 command=self.collect_text_field_values,
                                 highlightbackground="white")
        self.organize_grid()
        self.file_manager = FileManager(write_file=PASSWORD_FILE)

    def configure_window(self):
        """ Configure the window"""
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, bg="white")

    def set_background(self):
        """ Set the background of the canvas"""
        self.canvas.create_image(PASSWORD_CANVAS["width"] / 2,
                                 PASSWORD_CANVAS["height"] / 2, image=self.background)

    def organize_grid(self):
        """ Organize the grid layout of the screen"""
        self.canvas.grid(row=0, column=1)
        self.website_label.grid(row=1, column=0)
        self.email_label.grid(row=2, column=0)
        self.password_label.grid(row=3, column=0)
        self.website_text.grid(row=1, column=1, columnspan=2)
        self.email_text.grid(row=2, column=1, columnspan=2)
        self.password_text.grid(row=3, column=1)
        self.generate_password_button.grid(row=3, column=2)
        self.add_button.grid(row=4, column=1, columnspan=2)

    def clear_password(self):
        """ Clear the password text field value"""
        self.password_text.delete(0, END)

    def generate_password(self):
        """ Generate a password from the website"""
        self.clear_password()
        password = self.password_generator.generate_password()
        copy_to_clipboard(password)
        self.password_text.insert(0, password)

    def reset_text_fields(self):
        """ Reset the text fields of the UI"""
        for field in self.text_fields:
            field.delete(0, END)

    @staticmethod
    def valid_text_fields(fields_to_check) -> bool:
        """ Validate the text fields of the UI"""
        for field in fields_to_check:
            if len(field) == 0:
                messagebox.showerror(title="Invalid input",
                                     message="Please make sure you haven't left any fields empty")
                return False
        return True

    def add_password_to_vault(self, website, email, password):
        """ Add a website to the grid"""
        save = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                             f"Email: {email}, \n"
                                                             f"Password: {password}\n"
                                                             "Is it ok to save?")
        if save:
            self.file_manager.write_to_file(f"{website} | {email} | {password}")
            self.reset_text_fields()

    def collect_text_field_values(self):
        """ Collect the text fields of the UI"""
        website = self.website_text.get().strip()
        email = self.email_text.get().strip()
        password = self.password_text.get().strip()
        if self.valid_text_fields([website, email, password]):
            self.add_password_to_vault(website, email, password)

    def start_mainloop(self):
        """ Start the Tkinter main loop """
        self.website_text.focus()
        self.window.mainloop()
