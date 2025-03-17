import tkinter as tk
from tkinter import colorchooser

# Hauptfenster
fenster = tk.Tk()
fenster.title("Farbwähler")
fenster.geometry("600x250")

# Standardfarben
hintergrundfarbe = "#ffffff"  # Weiß
textfarbe = "#000000"         # Schwarz

# Funktion zum Ändern der Hintergrundfarbe
def hintergrundfarbe_waehlen():
    global hintergrundfarbe
    farbe = colorchooser.askcolor(
        title="Auswahl Hintergrundfarbe")[1] # [1] steht für hexadezimaler Wert
    if farbe:
        hintergrundfarbe = farbe
        fenster.config(bg=hintergrundfarbe)

# Funktion zum Ändern der Textfarbe
def textfarbe_waehlen():
    global textfarbe
    farbe = colorchooser.askcolor(title="Auswahl Textfarbe")[1]
    if farbe:
        textfarbe = farbe
        text_label.config(fg=textfarbe)

# Label zur Anzeige der ausgewählten Farben
text_label = tk.Label(text="Text, dessen Farbe gewählt werden kann", font=("Arial", 20), fg=textfarbe, bg=hintergrundfarbe)
text_label.pack(pady=50)

# Buttons zur Farbauswahl
hintergrund_button = tk.Button(text="Hintergrundfarbe",
                               command=hintergrundfarbe_waehlen)
hintergrund_button.pack(pady=10)

text_button = tk.Button(text="Textfarbe", command=textfarbe_waehlen)
text_button.pack(pady=10)

fenster.mainloop()
