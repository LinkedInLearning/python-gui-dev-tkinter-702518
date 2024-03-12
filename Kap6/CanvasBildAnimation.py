from tkinter import *
gp=None
i=0
master = Tk()
def ani1():
    global i
    global gp
    w.delete(gp)
    i+=1
    if i < 2500:
        gp = w.create_image(-i,0, image=bild1, anchor="nw")
        w.after(3, ani1)
 
        
        
master.title("Canvas")
w = Canvas(master, width=500, height=500)
bild1=PhotoImage(file="img/b.png")
gp = w.create_image(0,0, image=bild1, anchor="nw")
w.grid(row=0, column=0)
Button(text="Animation", command=ani1).grid(row=1,column=0)
master.mainloop()
