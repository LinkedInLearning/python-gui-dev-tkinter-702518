from tkinter import *
from tkinter import filedialog

def getDir():
    vz = filedialog.askdirectory(
        initialdir = "/",title = "Verzeichnisauswahl")
    lbl1.config(text=vz)

master = Tk()
lbl1 = Label(master, width=50)

lbl1.pack()
Button(text='Auswahl Verzeichnis', command=getDir).pack(fill=BOTH)


master.mainloop()



