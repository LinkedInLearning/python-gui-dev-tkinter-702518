from tkinter import *
def aktion1(event):
   lbl1.config(text=s1.get())

def aktion2(event):
   lbl2.config(text=s2.get())
   
master = Tk()
lbl1 = Label(master, width=20)
lbl1.grid(row=0,column=0)

s1 = Scale(master, from_=0, to=100,
           showvalue=0, command=aktion1)
s1.grid(row=0,column=1)

lbl2 = Label(master, width=20)
lbl2.grid(row=1,column=0)

s2 = Scale(master, from_=-100, to=200, orient=HORIZONTAL,
           length=150, command=aktion2)
s2.grid(row=1,column=1)
master.mainloop()
