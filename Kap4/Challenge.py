import tkinter as tk

# Hauptfenster
fenster = tk.Tk()
fenster.title("Anmeldung")

# Sprachvariablen
sprache = tk.StringVar(value="de")

# Funktion zum Umschalten der Sprache
def sprache_wechseln():
    pass

# Funktion zur Anmeldung
def anmelden():
    benutzername = benutzer_eingabe.get()
    passwort = passwort_eingabe.get()
    if sprache.get() == "de":
        print(f"Angemeldet als: {benutzername}")
    else:
        print(f"Logged in as: {benutzername}")

# Labels und Eingabefelder
benutzer_label = tk.Label(width=20, text="Benutzername:",anchor="w")
benutzer_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

benutzer_eingabe = tk.Entry(width=25)
benutzer_eingabe.grid(row=0, column=1, padx=5, pady=5)

passwort_label = tk.Label(width=20, text="Passwort:",anchor="w")
passwort_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

passwort_eingabe = tk.Entry(width=25, show="*")
passwort_eingabe.grid(row=1, column=1, padx=5, pady=5)

# Anmelde-Button
anmelden_button = tk.Button(text="Anmelden", command=anmelden, width=20)
anmelden_button.grid(row=2, column=0, columnspan=2, pady=10)

# Checkbox zum Umschalten der Sprache


fenster.mainloop()