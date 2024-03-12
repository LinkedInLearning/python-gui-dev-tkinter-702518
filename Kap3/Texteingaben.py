from tkinter import *

def aktion():
    lbl.configure(text="Hallo " + eingabe.get())
    
master = Tk()

Button(master, text="Verwenden", 
       font=("Arial",20), bg="red", fg="white", command=aktion).grid(row=1,sticky=W+E)
lbl=Label(master, font=("Arial",20), bg="white", fg="red", pady=15)
lbl.grid(row=2,sticky=W+E)
eingabe=Entry(master, font=("Arial",20), bg="white", fg="red")
eingabe.grid(row=0,sticky=W+E)
master.mainloop()
