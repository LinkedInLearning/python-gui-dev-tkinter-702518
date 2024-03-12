from tkinter import *

def action():
    lbl.config(text=w.get())
   
master = Tk()
w = Spinbox(master, from_=-10, to=10, command=action)
w.pack()
lbl=Label(master, text=w.get())
lbl.pack(expand=1)
master.mainloop()
