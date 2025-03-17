import tkinter as tk

# Hauptfenster
fenster = tk.Tk()
fenster.title("Navigation mit Bild und Text")

# Bilder laden (nur PNG, GIF, PPM/PGM mit Tkinter)
pfeil_links = tk.PhotoImage(file="img/links.png")
pfeil_rechts = tk.PhotoImage(file="img/rechts.png")


# 2 Buttons mit Bild und Text
button_zurueck = tk.Button(
    fenster, 
    image=pfeil_links, 
    text="Zurück", 
    compound="top" 
    
)
button_zurueck.grid(row=0, column=0, padx=20, pady=20)

button_vorwaerts = tk.Button(
    fenster, 
    image=pfeil_rechts, 
    text="Vorwärts", 
    compound="top" 
)
button_vorwaerts.grid(row=0, column=1, padx=2, pady=2)

fenster.mainloop()
