from tkinter import *
def aktion():
    pass

master = Tk()
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command = aktion)
filemenu.add_command(label = "Open", command = aktion)
filemenu.add_command(label = "Save", command = aktion)
filemenu.add_command(label = "Save as...", command = aktion)
filemenu.add_command(label = "Close", command = aktion)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = master.quit)
menubar.add_cascade(label = "File", menu = filemenu)
editmenu = Menu(menubar)
editmenu.add_command(label = "Undo", command = aktion)

editmenu.add_separator()

editmenu.add_command(label = "Cut", command = aktion)
editmenu.add_command(label = "Copy", command = aktion)
editmenu.add_command(label = "Paste", command = aktion)
editmenu.add_command(label = "Delete", command = aktion)
editmenu.add_command(label = "Select All", command = aktion)

menubar.add_cascade(label = "Edit", menu = editmenu)

helpmenu = Menu(menubar, tearoff=1)
helpmenu.add_command(label = "About...", command = aktion)
menubar.add_cascade(label = "Help", menu = helpmenu)

master.geometry("500x300")
master.title("Menü")
master.config(menu = menubar)
master.mainloop()
