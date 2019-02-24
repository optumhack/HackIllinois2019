import tkinter as tk
from tkinter import *

class Frontend:

    def __init__(self, master):
        self.master = master
        master.title("Check schedule")
        self.id = 0

        # widgets here
        self.label = Label(master, text='Your Nurse ID')

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.button = Button(master, text="Enter", command=lambda: self.run())

        #layout
        self.label.grid(row=0)
        self.entry.grid(row=0, column=1)
        self.button.grid(row=1, column=1)

    def validate(self, new_text):
        if not new_text:
            self.id = 0
            return True

        try:
            self.id = int(new_text)
            return True
        except ValueError:
            return False

    def run(self):
        Label(self.master, text = "Hi").pack()

t = Tk()
# runs it
run_frontend = Frontend(t)
t.mainloop()
