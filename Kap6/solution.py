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
    global original_bild, anzeige_bild, bild_objekt
    dateipfad = filedialog.askopenfilename(
        filetypes=[("Bilddateien", "*.png;*.gif;*.ppm;*.pgm")])
    if dateipfad:
        original_bild = tk.PhotoImage(file=dateipfad)
        canvas.delete("all")  # Vorherige Bilder löschen

        # Bild initial mit Zoom 1x anzeigen
        anzeige_bild = original_bild
        bild_objekt = canvas.create_image(0, 0, anchor="nw",
                                          image=anzeige_bild)
        canvas.config(scrollregion=(0, 0, original_bild.width(), original_bild.height()))
        zoom_ändern()  # Setzt die aktuelle Zoom-Stufe

# Funktion für die Zoom-Radiobuttons
def zoom_ändern():
    global anzeige_bild, bild_objekt
    faktor = zoom_factor.get()
    
    if original_bild:
        if faktor == 1:
            anzeige_bild = original_bild  # Originalgröße
        else:
            anzeige_bild = original_bild.zoom(faktor, faktor)  # Zoom um Faktor x

        # Neues Bild setzen
        canvas.itemconfig(bild_objekt, image=anzeige_bild)
        canvas.config(scrollregion=(0, 0,
                                    anzeige_bild.width(),
                                    anzeige_bild.height()))

# Menüleiste für Bild laden
menueleiste = tk.Menu(fenster)
fenster.config(menu=menueleiste)
datei_menu = tk.Menu(menueleiste, tearoff=0)
datei_menu.add_command(label="Bild laden", command=bild_laden)
menueleiste.add_cascade(label="Datei", menu=datei_menu)

# Radiobuttons für Zoom-Stufen
zoom_frame = tk.Frame(fenster)
zoom_frame.grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(zoom_frame, text="Zoom:").pack(side="left")
for faktor in [1, 2, 3, 4]:  # Zoom-Faktoren
    tk.Radiobutton(zoom_frame, text=f"{faktor}x", variable=zoom_factor, value=faktor, command=zoom_ändern).pack(side="left")

# Scrollbalken hinzufügen
x_scroll = tk.Scrollbar(orient='horizontal',
                        command=canvas.xview)
x_scroll.grid(row=2, column=0, columnspan=2, sticky='ew')
y_scroll = tk.Scrollbar(orient='vertical', command=canvas.yview)
y_scroll.grid(row=0, column=2, sticky='ns')
canvas.config(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

# Grid-Konfiguration für Responsivität
fenster.columnconfigure(0, weight=1)
fenster.columnconfigure(1, weight=1)
fenster.rowconfigure(0, weight=1)

fenster.mainloop()
