from tkinter import *
gp=None
def da():
    global gp
    gp= w.create_rectangle(50, 25, 150, 75, fill="blue")
def weg():
    w.delete(gp)
def verschiebe():
    global gp
    w.move(gp,150, 125)
def konfig():
    global gp
    w.itemconfig(gp, fill="red")
def koord():
    global gp
    w.coords(gp, 20,20,400,100)

master = Tk()

master.title("Canvas")
w = Canvas(master, width=500, height=500)
w.grid(row=0, columnspan=5)

da()
Button(text="Löschen", command=weg).grid(row=1,column=0)
Button(text="Zeichnen", command=da).grid(row=1,column=1)
Button(text="Verschieben", command=verschiebe).grid(row=1,column=2)
Button(text="Färben", command=konfig).grid(row=1,column=3)
Button(text="Abmessung ändern", command=koord).grid(row=1,column=4)

master.mainloop()
