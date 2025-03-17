import tkinter as tk
from tkinter import filedialog

# Hauptfenster
fenster = tk.Tk()
fenster.title("Grafik Viewer mit diskretem Zoom")

# Globale Variablen
original_bild = None
anzeige_bild = None
bild_objekt = None
zoom_factor = tk.IntVar(value=1)  # Standard-Zoom: 1x

# Canvas zur Darstellung des Bildes
canvas = tk.Canvas(fenster, bg='gray')
canvas.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Funktion zum Laden des Bildes
def bild_laden():
    pass

# Funktion für die Zoom-Radiobuttons
def zoom_ändern():
    pass
    
# Menüleiste für Bild 

# Radiobuttons für Zoom-Stufen

# Scrollbalken hinzufügen

# Grid-Konfiguration für Responsivität
fenster.columnconfigure(0, weight=1)
fenster.columnconfigure(1, weight=1)
fenster.rowconfigure(0, weight=1)

fenster.mainloop()
