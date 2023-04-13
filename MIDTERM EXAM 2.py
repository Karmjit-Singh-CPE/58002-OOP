from tkinter import *

class FullNameGUI:
    def __init__(self, master):
        self.master = master
        master.title("My Full Name")
        master.config(bg="white")
        master.geometry("400x250")

        # Labels
        self.label1 = Label(master, text="Enter Given Name:", fg="red", font=("Calibri", 10), bg="white")
        self.label1.place(x=30, y=20)

        self.label2 = Label(master, text="Enter Middle Name:", fg="red", font=("Calibri", 10), bg="white")
        self.label2.place(x=30, y=60)

        self.label3 = Label(master, text="Enter Last Name:", fg="red", font=("Calibri", 10), bg="white")
        self.label3.place(x=30, y=100)

        self.label4 = Label(master, text="My Full Name is:", fg="red", font=("Calibri", 10), bg="white")
        self.label4.place(x=30, y=160)

        # Entry widgets
        self.entry1 = Entry(master, width=30, font=("Verdana", 10))
        self.entry1.place(x=170, y=20)

        self.entry2 = Entry(master, width=30, font=("Verdana", 10))
        self.entry2.place(x=170, y=60)

        self.entry3 = Entry(master, width=30, font=("Verdana", 10))
        self.entry3.place(x=170, y=100)

        self.entry4 = Entry(master, width=40, font=("Verdana", 10))
        self.entry4.place(x=170, y=160)

        # Buttons
        self.show_button = Button(master, text="Show Full Name", font=("Verdana", 10), bg="red", fg="white", command=self.show_fullname)
        self.show_button.place(x=80, y=200, width=120)

        self.clear_button = Button(master, text="Clear All", font=("Verdana", 10), bg="red", fg="white", command=self.clear_entries)
        self.clear_button.place(x=200, y=200, width=120)

    def show_fullname(self):
        given_name = self.entry1.get()
        middle_name = self.entry2.get()
        last_name = self.entry3.get()
        full_name = last_name + ", " + given_name + " " + middle_name
        self.entry4.delete(0, END)
        self.entry4.insert(0, full_name)

    def clear_entries(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)

root = Tk()
gui = FullNameGUI(root)
root.mainloop()
