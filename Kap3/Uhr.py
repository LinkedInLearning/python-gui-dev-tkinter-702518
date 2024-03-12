from tkinter import *
import time

master = Tk()
clock=Label(master, font=("Times", 42), bg="green", fg="yellow", text="1")
clock.pack(fill=BOTH)
def ticken():
    zeit=time.strftime("%H:%M:%S")
    clock.config(text=zeit)
    clock.after(1000, ticken)
ticken()    
master.mainloop()
