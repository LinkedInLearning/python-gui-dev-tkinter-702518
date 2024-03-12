from tkinter import *
gp=None
master = Tk()

master.title("Canvas")
w = Canvas(master, width=500, height=500)
bild1=PhotoImage(file="img/b.png")
b = w.create_image(0,0, image=bild1, anchor="nw")
w.pack()
master.mainloop()
