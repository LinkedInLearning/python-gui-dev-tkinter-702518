from tkinter import *
master = Tk()

fr1=Frame(master, width=300, height=100, bg="red")
Label(fr1, text="Das soll auf Frame1 sein").place(
    x=10, y = 10, width=200, height=30)
fr1.pack()

fr2=Frame(master, width=200, height=100, bg="blue")
fr2.pack()
master.mainloop()
