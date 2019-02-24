import tkinter
from tkinter import *
from tkinter import messagebox

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

        #back button 
        self.backButton = Button(master, text="Back", command=lambda: self.back())

        #history button 
        self.historyButton = Button(master, text="History", command=lambda: self.history())
        

        #layout
        self.idLabel.grid(row=1, column=0)
        self.idEntry.grid(row=1, column=1)
        self.nurseLabel.grid(row=2, column=0)
        self.nurseEntry.grid(row=2, column=1)
        self.exitButton.grid(row=3, column=0)
        self.enterButton.grid(row=3, column=1)
        self.historyButton.grid(row=0, column=0)

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
        i = {id}
        self.nurseHourList.append(i)
        tkinter.Label(self.master, text="Hello World").grid(row=3)
    
    #page1=Tk()
    #Label1=Label(page1, text="Manager")
    #label1.pack()

    #def topage2():
        #page2=Tk()
        #label2=Label(page2, text="History")
        #label2.pack()


    def back(self):
        #creates warning messagebox
        tkinter.messagebox.showwarning("Warning", "Are You Sure You Want To Go Back?")

class History:
    def __init__(self, master):
        self.master = master
        master.title = "Past"

class Nurse:
    def __init__(self, master):
        self.master = master
        master.title = "Nurse"
    #nurse hours
    #self.nurseLabel = Label(master, text='How Many Hours')
    #vcmdHours = master.register(self.validateHours)  # we have to wrap the command
    #self.nurseEntry = Entry(master, validate="key", validatecommand=(vcmdHours, '%P'))

t = tkinter.Tk()
# runs it
run_frontend = Manager(t)
t.mainloop()