import tkinter as tk

root = tk.Tk()
root.title("Hello World")
tk.Label(root, text="Scooteq GmbH Kostenberechner v1.0").pack()

def rechnung():
    try:
        text = eingabeKM.get().strip().replace(",", ".")  # Komma zulassen
        wert = float(text)
        betrag = wert * 1.5 + 1.5
        ausgabe_label.config(text=f"---------------- Quittung ---------------- \n Dein Betrag lautet: {betrag:.2f} € \n Vielen Dank für deine Fahrt mit Scooteq! \n ---------------------------------------------")

        # Nach erfolgreicher Quittung: Eingabefeld leeren
        eingabeKM.delete(0, tk.END)
        eingabeKM.focus_set()

    except ValueError:
        ausgabe_label.config(text="Bitte eine gültige Zahl eingeben!")
        # Optional: Eingabe markieren, damit man direkt überschreiben kann
        eingabeKM.focus_set()
        eingabeKM.selection_range(0, tk.END)

# Fenstergröße setzen
root.geometry("850x500")

bild = tk.PhotoImage(file=r"C:\Users\KA3254\IdeaProjects\pythenEinstieg\assets\scooTec3.png")
label_bild = tk.Label(root, image=bild)
label_bild.pack()

label_info = tk.Label(root, text="Hallo, Max Mustermann! Bitte gib deine Kilometerzahl ein:")
label_info.pack()

eingabeKM = tk.Entry(root)
eingabeKM.pack(pady=10)

button_berechnen = tk.Button(root, text="Quittung ausgeben", command=rechnung)
button_berechnen.pack(pady=10)

ausgabe_label = tk.Label(root, text="")
ausgabe_label.pack(ipadx=15)

root.mainloop()