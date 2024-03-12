from tkinter import *

master = Tk()

master.geometry("500x300")
master.title("Nachrichten")
w = Message(master, text="And now for something completely different.")
w.pack()
master.mainloop()
