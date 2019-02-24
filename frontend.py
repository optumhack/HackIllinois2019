import tkinter
from tkinter import *

class Manager:

    def __init__(self, master):

        self.master = master
        master.title("Manager")
        self.id = 0
        self.hours = 0

        #making nurse hour list
        nurseHourList = []
        self.nurseHourList = nurseHourList

        # WIDGETS HERE

        #nurse id
        self.idLabel = Label(master, text='Nurse ID')
        vcmdId = master.register(self.validateId) # we have to wrap the command
        self.idEntry = Entry(master, validate="key", validatecommand=(vcmdId, '%P'))

        #nurse hours
        self.nurseLabel = Label(master, text='How Many Hours')
        vcmdHours = master.register(self.validateHours)  # we have to wrap the command
        self.nurseEntry = Entry(master, validate="key", validatecommand=(vcmdHours, '%P'))

        #exit button
        self.exitButton = Button(master, text="Exit", command=master.quit)

        #enter button
        self.enterButton = Button(master, text="Enter", command=lambda: self.enter())

        #generate button
        self.generateButton = Button(master, text="Generate", command=lambda: self.generate())

        #layout
        self.idLabel.grid(row=0, column=0)
        self.idEntry.grid(row=0, column=1)
        self.nurseLabel.grid(row=1, column=0)
        self.nurseEntry.grid(row=1, column=1)
        self.exitButton.grid(row=2, column=0)
        self.enterButton.grid(row=2, column=1)

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

    def enter(self):
        #adds id/hours to nursehourlist
        i = {id, hours}
        self.nurseHourList.append(i)
        tkinter.Label(self.master, text="Hello World").grid(row=3)

class History:
    def __init__(self, master):
        self.master = master
        master.title = "Past"

        count = 0

        for i in len(Manager.nurseHourList):
            text = Manager.nurseHourList(i)
            count++
        
        #back button button
        self.exitButton = Button(master, text="Back", command=lambda: self.show_frame(History))

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()



class Nurse:
    def __init__(self, master):
        self.master = master
        master.title = "Nurse"

t = Tk()
# runs it
run_frontend = Manager(t)
t.mainloop()