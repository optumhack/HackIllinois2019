import tkinter
from tkinter import *

class Frontend:

    def __init__(self, master):
        self.master = master
        master.title("Check schedule")
        self.id = 0
        self.hours = 0

        # WIDGETS HERE

        #nurse id
        self.idLabel = Label(master, text='Nurse ID')
        vcmdId = master.register(self.validateId) # we have to wrap the command
        self.idEntry = Entry(master, validate="key", validatecommand=(vcmdId, '%P'))

        #nurse hours
        self.nurseLabel = Label(master, text='How Many Hours')
        vcmdHours = master.register(self.validateHours)  # we have to wrap the command
        self.nurseEntry = Entry(master, validate="key", validatecommand=(vcmdHours, '%P'))

        #enter button
        self.button = Button(master, text="Enter", command=lambda: self.run())

        #layout
        self.idLabel.grid(row=0, column=0)
        self.idEntry.grid(row=0, column=1)
        self.nurseLabel.grid(row=1, column=0)
        self.nurseEntry.grid(row=1, column=1)
        self.button.grid(row=2, column=1)

    def validateId(self, new_text):
        if not new_text:
            self.id = 0
            return True

        try:
            self.id = int(new_text)
            return True
        except ValueError:
            return False

    def validateHours(self, new_text):
        if not new_text:
            self.hours = 0
            return True

        try:
            self.hours = int(new_text)
            return True
        except ValueError:
            return False

    def run(self):

        tkinter.Label(self.master, text="Hi").grid(row=3)

t = tkinter.Tk()
# runs it
run_frontend = Frontend(t)
t.mainloop()