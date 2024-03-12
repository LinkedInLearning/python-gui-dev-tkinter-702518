from tkinter import *
from tkinter import ttk
   
master = Tk()
pg = ttk.Progressbar(master)
pg.pack()
Button(master,text="OK", command=pg.start).pack()
master.mainloop()
