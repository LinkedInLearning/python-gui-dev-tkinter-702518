from tkinter import *

def aktion():
    master.destroy()
    
master = Tk()
Button(master, text="Ende", width="40", command=aktion).pack()
master.mainloop()
