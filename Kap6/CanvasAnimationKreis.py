from tkinter import *
i=0
gp=None
def init():
    global gp
    global i
    gp=w.create_oval(50,50,80,80, outline="blue", width=1)
    i=0
master = Tk()
def ani1():
    global i
    global gp
    w.delete(gp)
    i+=1
    if i < 450:
        gp = w.create_oval(50,50,80+i,80+i, outline="blue", width=1)
        w.after(3, ani1)
    else:
        init()
 
def ani2():
    global i
    global gp
    
    i+=1
    if i < 450:
        gp = w.create_oval(50,50,80+i,80+i, outline="blue", width=1)
        w.after(3, ani2)
    else:
        w.delete(ALL)
        init()
 
         
        
master.title("Canvas")
w = Canvas(master, width=500, height=500)
init()
w.grid(row=0, columnspan=2)
Button(text="Animation 1", command=ani1).grid(row=1,column=0)
Button(text="Animation 2", command=ani2).grid(row=1,column=1)

master.mainloop()
