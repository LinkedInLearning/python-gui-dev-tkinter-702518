from tkinter import *

def on_enter(event):
    lbl2.configure(text= str(event.x) + " : " + str(event.y) )

def on_leave(event):
    lbl2.configure(text="")
    
master = Tk()
lbl1=Label(
    master, bg="red", fg="yellow", font=("Times", 42), width=25,
    text="Sensitiver Bereich")
lbl1.grid(row=0, column=0)
lbl1.bind("<Enter>", on_enter)
lbl1.bind("<Leave>", on_leave)
lbl2=Label(master, bg="blue", fg="yellow", font=("Times", 42), width=25)
lbl2.grid(row=1, column=0)
master.mainloop()
