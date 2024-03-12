from tkinter import *
from tkinter.colorchooser import *

def getColor():
    color = askcolor() 
    lbl1.config(text=color)
master = Tk()
lbl1 = Label(master, width=50)

lbl1.pack()
Button(text='Select Color', command=getColor).pack()

master.mainloop()



