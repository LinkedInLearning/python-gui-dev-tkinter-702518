from tkinter import *
from tkinter import filedialog

def getFile():
    dat = filedialog.askopenfilename(
        initialdir = "/",title = "Dateiauswahl",
        filetypes = (("Textdateien","*.txt"),("Alle Dateien","*.*")))
    lbl1.config(text=dat)
master = Tk()
lbl1 = Label(master, width=50)

lbl1.pack()
Button(text='Auswahl Verzeichnis', command=getFile).pack()

master.mainloop()



