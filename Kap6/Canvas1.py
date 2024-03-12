from tkinter import *

master = Tk()

master.title("Canvas")
w = Canvas(master, width=500, height=500)
w.pack()
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")
w.create_arc(100,100,300,200, fill="orange")
w.create_text(200, 170, text="Monty Python", font=("Times",32), fill="green")
w.create_polygon(200, 200, 310,210,320,250, 330,400,fill="yellow")
w.create_oval(450,450,40,30, dash=(5,5))
w.create_oval(450,50,480,95, fill="purple",outline="green", width=3)
master.mainloop()
