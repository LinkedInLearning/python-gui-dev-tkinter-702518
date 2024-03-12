from tkinter import *
from tkinter import ttk

def action(event):
    lbl.config(text=cb.get())
master = Tk()
master.geometry("500x500")
pg = ttk.Progressbar(master)
pg.pack(fill=BOTH)
Button(master,text="Start", command=pg.start).pack(fill=BOTH)
Button(master,text="Stopp", command=pg.stop).pack(fill=BOTH)
cb=ttk.Combobox(master, values=[1,2,3])
cb.pack(fill=BOTH)
cb.bind( "<<ComboboxSelected>>",action)
lbl=Label(master)
lbl.pack(fill=BOTH)

nb = ttk.Notebook(master)
nb.pack(fill=BOTH)
 
page1 = ttk.Frame(nb)
nb.add(page1, text='Tab1')
Label(page1, text="Auf dem ersten Tab").pack()
 
page2 = ttk.Frame(nb)
nb.add(page2, text='Tab2')
Label(page2, text="Auf dem zweiten Tab").pack()
master.mainloop()
