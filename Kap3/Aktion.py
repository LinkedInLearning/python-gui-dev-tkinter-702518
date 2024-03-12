from tkinter import *

def aktion():
    lbl.config(text="Auf den Button geklickt")
master = Tk()
Button(master, text="Klick mich an",
       bg="yellow", fg="blue", font=("Times", 30), command=aktion).grid(row=0, column=0)
lbl=Label(master, bg="blue", fg="yellow", font=("Times", 42), width=25)
lbl.grid(row=1, column=0)
master.mainloop()
