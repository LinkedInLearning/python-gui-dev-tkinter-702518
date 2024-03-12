from tkinter import *
def aktion1():
    lbl2.config(text=v1.get())
def aktion2():
    lbl3.config(text=v2.get())
def aktion3():
    lbl4.config(text=v3.get())
   
master = Tk()
lbl1=Label(master, padx=5, pady=5, font=("Times",18), bg="red", fg="white", text="Auswahl der Programmiersprache.")
lbl1.grid(row=0, columnspan=2, sticky=W+E+N+S)

v1 = IntVar() 
r1=Radiobutton(master, text="Python", font=("Arial",12), 
               padx = 20, value=1, variable=v1, command=aktion1)
r2=Radiobutton(master, text="JavaScript", font=("Arial",12), 
               padx = 20, value=2, variable=v1, command=aktion1)
r1.grid(row=1, column=0, sticky=W)
r2.grid(row=1, column=1, sticky=W)

v2 = IntVar()
c1=Checkbutton(master, text="Prozedural", font=("Arial",12),variable=v2,
               command=aktion2)
c1.grid(row=2,column=0, sticky=W)

v3 = IntVar()
c2=Checkbutton(master, text="Objektorientiert", font=("Arial",12), variable=v3,
               command=aktion3)
c2.grid(row=2,column=1, sticky=W)

lbl2=Label(master,  padx=5, pady=5, font=("Times",18), bg="white", fg="red")
lbl2.grid(row=3, columnspan=2, sticky=W+E+N+S)
lbl3=Label(master,  padx=5, pady=5, font=("Times",18), bg="white", fg="red")
lbl3.grid(row=4, columnspan=2, sticky=W+E+N+S)
lbl4=Label(master,  padx=5, pady=5, font=("Times",18), bg="white", fg="red")
lbl4.grid(row=5, columnspan=2, sticky=W+E+N+S)

master.mainloop()
