from tkinter import *
master = Tk()
Label(master,text="Da ist das Untier", bg="yellow", fg="blue",
      font=("Helvetica", 16)).pack(ipadx=20, ipady=10)
Label(master,text="Wo? Hinter dem Karnickel?", bg="green",
      font=("Times", 36)).pack(fill=X)
Label(master,text="Es IST das Karnickel!", bg="gray",
      font=("Arial", 22)).pack(fill=X)
master.mainloop()
