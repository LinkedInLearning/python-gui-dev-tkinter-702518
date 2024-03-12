from tkinter import *
master = Tk()
t1="Da ist das Untier"
t2="Wo?"
t3="Na da!"
t4="Wo? Hinter dem Karnickel?"
t5="Es IST das Karnickel!"
Label(master,text=t1, bg="yellow", fg="blue").grid(column=0)
Label(master,text=t2, bg="green", fg="white").grid(column=1)
Label(master,text=t1, bg="red", fg="blue").grid(column=2)
Label(master,text=t2, bg="black", fg="white").grid(column=3)
Label(master,text=t1, bg="yellow", fg="red").grid(column=4)
master.mainloop()
