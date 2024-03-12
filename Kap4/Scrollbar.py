from tkinter import *


   
master = Tk()
textfeld1 = Text(master,  wrap='word', width=30, height=10)
textfeld1.pack(fill='both',side=LEFT)
scrollbar1 = Scrollbar(master)
scrollbar1.pack(expand=1, fill='both')
textfeld1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=textfeld1.yview)
master.mainloop()
