""" Day 27 of Coding Challenges for GUI"""
import tkinter


def play():
    """ Play the game """
    window = tkinter.Tk()
    window.title("GUI")
    window.minsize(width=500, height=300)

    my_label = tkinter.Label(text="Label", font=("Helvetica", 24, "bold"))


    window.mainloop()

