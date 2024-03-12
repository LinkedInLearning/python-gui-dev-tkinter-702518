from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        t1="Da ist das Untier"
        t2="Wo?"
        t3="Na da!"
        t4="Wo? Hinter dem Karnickel?"
        t5="Es IST das Karnickel!"
        self.lb1=Label(master,text=t1, bg="yellow", fg="blue")
        self.lb1.grid(row=0,column=0)
        self.lb2=Label(master,text=t2, bg="green", fg="white")
        self.lb2.grid(row=0,column=1)
        self.lb3=Label(master,text=t3, bg="red", fg="blue")
        self.lb3.grid(row=0,column=2)
        self.lb4=Label(master,text=t4, bg="black", fg="white")
        self.lb4.grid(row=1,column=0)
        self.lb5=Label(master,text=t5, bg="yellow", fg="red")
        self.lb5.grid(row=1,column=1)

        self.lb1.configure(text=t5, bg="red")
        
root = Tk()
app = Application(master=root)
app.mainloop()
