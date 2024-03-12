from tkinter import *

def aktion1(event):
    print(listbox.get(ACTIVE))
    print(listbox.curselection()[0])
   
master = Tk()
listbox = Listbox(master)
listbox.pack()

for item in ["Python", "JavaScript", "PHP", "Perl"]:
    listbox.insert(END, item)
listbox.bind("<Double-Button-1>",aktion1)
master.mainloop()
