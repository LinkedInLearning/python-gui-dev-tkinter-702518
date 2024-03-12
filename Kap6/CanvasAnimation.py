from tkinter import *


i=0
gp=None
def init():
    global gp
    global i
    gp=w.create_oval(50,50,80,80, fill="yellow",outline="blue", width=2)
    i=0


def ani1():
    global i
    i+=1
    if i < 200:
        w.move(gp,1, 0)
        w.after(10, ani1)
    else:
        w.delete(gp)
        init()
def ani2():
    global i
    i+=1
    if i < 200:
        w.move(gp,1, 0)
        w.after(10, ani2)
    elif i < 400:
        w.move(gp,-1, 0)
        w.after(10, ani2)
    else:
        w.delete(gp)
        init()
def ani3():
    global i
    i+=1
    if i < 200:
        w.move(gp,1, 2)
        w.after(15, ani3)
    elif i < 400:
        w.move(gp,-1, -2)
        w.after(15, ani3)
    else:
        w.delete(gp)
        init()


def ani4():
    
    global i
    i+=1
    if i < 200:
        w.coords(gp, 50,50,80+i,80)
        w.after(15, ani4)
    else:
        w.delete(gp)
        init()
   


def ani5():
    global i
    i+=1
    if i < 200:
        w.coords(gp, 50,50+i,80+i,80+i)
        w.after(15, ani5)
    else:
        w.delete(gp)
        init()

def ani6():
    global i
    i+=1
    if i < 200:
        if i%3==0:
            w.itemconfig(gp, fill="red")
            
        elif i%3==1:
            w.itemconfig(gp, fill="yellow")
        else:
            w.itemconfig(gp, fill="blue")
 
        w.after(50, ani6)
    else:
        w.delete(gp)
        init()





master = Tk()

master.title("Canvas")
w = Canvas(master, width=500, height=500)
w.grid(row=0, columnspan=6)
init()
Button(text="Animation 1", command=ani1).grid(row=1,column=0)
Button(text="Animation 2", command=ani2).grid(row=1,column=1)
Button(text="Animation 3", command=ani3).grid(row=1,column=2)
Button(text="Animation 4", command=ani4).grid(row=1,column=3)
Button(text="Animation 5", command=ani5).grid(row=1,column=4)
Button(text="Animation 6", command=ani6).grid(row=1,column=5)
master.mainloop()
