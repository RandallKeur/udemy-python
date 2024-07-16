"""Class to represent the distance converter"""
from tkinter import Tk, Label, Button, Entry, Radiobutton, IntVar

from src.constants.values import MILES_TO_KM


class DistanceConverter:
    """Class to represent the distance converter"""
    # pylint: disable=too-many-instance-attributes

    def __init__(self):
        self.window = Tk()
        self.user_input = Entry(width=15)
        self.from_radio_state = IntVar()
        self.from_miles = Radiobutton(self.window, text="Miles", value=1,
                                      variable=self.from_radio_state,
                                      command=self.from_radio_state.get)
        self.from_kilometers = Radiobutton(self.window, text="Kilometers", value=2,
                                           variable=self.from_radio_state,
                                           command=self.from_radio_state.get)
        self.text = Label(text="is equal to ")
        self.result = Label(text="0", font=("Helvetica", 12))
        self.to_radio_state = IntVar()
        self.to_miles = Radiobutton(self.window, text="Miles", value=1,
                                    variable=self.to_radio_state,
                                    command=self.to_radio_state.get)
        self.to_kilometers = Radiobutton(self.window, text="Kilometers", value=2,
                                         variable=self.to_radio_state,
                                         command=self.to_radio_state.get)
        self.button = Button(text="Calculate", command=self.convert)
        self.configure_screen()

    def configure_screen(self):
        """Configure the screen for the converter"""
        self.window.title("Distance Converter")
        self.window.minsize(width=400, height=200)
        self.user_input.grid(row=0, column=1)
        self.from_miles.grid(column=2, row=0)
        self.from_kilometers.grid(column=3, row=0)
        self.text.grid(column=0, row=1)
        self.result.grid(column=1, row=1)
        self.to_miles.grid(column=2, row=1)
        self.to_kilometers.grid(column=3, row=1)
        self.button.grid(column=1, row=2)

    def convert(self):
        """Convert the distance"""
        if self.from_radio_state.get() == self.to_radio_state.get():
            self.result.config(text=f"{self.user_input.get()}")
        elif self.from_radio_state.get() == 1 and self.to_radio_state.get() == 2:
            self.miles_to_kilometers()
        elif self.from_radio_state.get() == 2 and self.to_radio_state.get() == 1:
            self.kilometers_to_miles()

    def kilometers_to_miles(self):
        """Convert kilometers to miles"""
        km = float(self.user_input.get())
        miles = round(km / MILES_TO_KM, 2)
        self.result.config(text=f"{miles}")

    def miles_to_kilometers(self):
        """Converts miles to kilometers"""
        miles = float(self.user_input.get())
        km = round(miles * MILES_TO_KM, 2)
        self.result.config(text=f"{km}")
