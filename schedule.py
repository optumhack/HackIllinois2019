import tkinter as tk
from tkinter import *
from tkinter import messagebox

LARGE_FONT = ("Verdana", 12)


class Schedule(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Manager, History, Nurse):
            page_name = F.__name__
            frame = F(master=container, controller=self)

            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Manager")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class Manager(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="Manager", font=LARGE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button2 = tk.Button(self, text="Go To Nurse",
                            command=lambda: controller.show_frame("Nurse"))
        
        button3 = tk.Button(self, text="Go To History",
                            command=lambda: controller.show_frame("History"))
        
        button2.pack()
        button3.pack()

class History(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="History", font=LARGE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("Manager"))
        button1.pack()



class Nurse(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="For the Nurse", font=LARGE_FONT)
        label.pack(side="top", fill="x", pady=10)
        self.master = master
        self.validateId = 0

        #nurse id
        self.idLabel = Label(master, text='Nurse ID')
        vcmdId = master.register(self.validateId) # we have to wrap the command
        self.idEntry = Entry(master, validate="key", validatecommand=(vcmdId, '%P'))

        #layout
        # button1.pack()
        goBack = tk.messagebox.showwarning("Warning", "Are You Sure you Want to go back?", icon="warning")
        if goBack == "ok":
            print("hi")
            controller.show_frame("Manager")
        
        #idLabel.pack()
        #idEntry.pack()

        def validateId(self, new_text):
            if not new_text:
                self.id = 0
                return True

            try:
                self.id = int(new_text)
                return True
            except ValueError:
                return False


app = Schedule()
app.mainloop()