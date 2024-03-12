from tkinter import *


def openFrame():
    t="Also, nun kommt der Sinn des Lebens. Nun, es ist wirklich nichts Besonderes. Versuch einfach, nett zu den Leuten zu sein, vermeide fettes Essen, lies ab und zu ein gutes Buch, lass Dich mal besuchen und versuch mit allen Rassen und Nationen in Frieden und Harmonie zu leben."
    top = Toplevel()
    top.title("Toplevel-Fenster...")

    msg = Message(top, text=t, bg="green", fg="white", font=("Times",32))
    msg.pack()

    button = Button(top, text="Schließen", command=top.destroy)
    button.pack()

master = Tk()

Button(text='Neues Fenster',  bg="white", fg="green", font=("Times",42), command=openFrame).pack(fill=BOTH)


master.mainloop()



