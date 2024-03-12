from tkinter import *

    
master = Tk()

lbl1=Label(master, font=("Times",28), bg="red", fg="white", text="Wir kommen aus dem Nichts.")
lbl1.grid(row=0, column=0, sticky=W+E+N+S)
lbl2=Label(master, font=("Times",26), bg="red", fg="white", text="Wir werden zu Nichts.")
lbl2.grid(row=1, column=0, sticky=W+E+N+S)
lbl3=Label(master, font=("Times",38), bg="white", fg="red", text="Also was haben wir zu verlieren?")
lbl3.grid(row=0, column=1, sticky=W+E+N+S)
lbl4=Label(master, font=("Times",18), bg="white", fg="red", text="Nichts!")
lbl4.grid(row=1, column=1, sticky=W+E+N+S)
master.mainloop()
