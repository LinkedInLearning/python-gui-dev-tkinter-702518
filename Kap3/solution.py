import tkinter as tk

# Funktion zur Berechnung des Ausdrucks
def berechne():
    try:
        ausdruck = eingabe.get()
        ergebnis = eval(ausdruck)  # Achtung: eval kann bei unsicherer Eingabe ein Sicherheitsrisiko sein!
        eingabe.delete(0, tk.END)
        eingabe.insert(tk.END, str(ergebnis))
    except Exception as e:
        eingabe.delete(0, tk.END)
        eingabe.insert(tk.END, "Fehler")

# Funktion zum Hinzufügen von Zeichen zur Eingabe
def taste_druecken(zeichen):
    eingabe.insert(tk.END, zeichen)

# Funktion zum Löschen der Eingabe
def loeschen():
    eingabe.delete(0, tk.END)

# Hauptfenster
fenster = tk.Tk()
fenster.title("Taschenrechner")

# Eingabefeld
eingabe = tk.Entry(fenster, width=20, font=('Arial', 18), justify='right')
eingabe.grid(row=0, column=0, columnspan=4, pady=5)

# Tasten
tasten = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, zeile, spalte) in tasten:
    if text == '=':
        tk.Button(fenster, text=text, width=5, height=2, font=('Arial', 14),
                  command=berechne).grid(row=5, column=0,
                                         columnspan=4,sticky="nsew")
    else:
        tk.Button(fenster, text=text, width=5, height=2, font=('Arial', 14),
                  command=lambda t=text: taste_druecken(t)).
        grid(row=zeile, column=spalte, sticky="nsew")

# Löschen-Taste
tk.Button(fenster, text='C', width=5, height=2, font=('Arial', 14),
          command=loeschen).grid(row=4, column=3, sticky="nsew")



fenster.mainloop()
