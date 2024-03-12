from tkinter import *
from tkinter import messagebox

def getMessage1():
    wert=messagebox.askokcancel('Frage','Ja oder Nein?')
    lbl1.config(text=wert)
def getMessage2():
    wert=messagebox.showwarning('Uffbasse','Die Lage könnte kritisch werden')
    lbl1.config(text=wert)
def getMessage3():
    wert=messagebox.showerror('Fehler','Die Lage ist ernst')
    lbl1.config(text=wert)
def getMessage4():
    wert=messagebox.showinfo('Keine Frage','Alternativlos')
    lbl1.config(text=wert)
def getMessage5():
    wert=messagebox.askquestion('Doch eine Frage','Alternativlos?')
    lbl1.config(text=wert)    
master = Tk()
lbl1 = Label(master, width=50)

lbl1.pack()
Button(text='Einverstanden', command=getMessage1).pack(fill=BOTH)
Button(text='Achtung', command=getMessage2).pack(fill=BOTH)
Button(text='Problem', command=getMessage3).pack(fill=BOTH)
Button(text='Information', command=getMessage4).pack(fill=BOTH)
Button(text='Hab da mal eine Frage', command=getMessage5).pack(fill=BOTH)

master.mainloop()



