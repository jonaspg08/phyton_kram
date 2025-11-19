kilometer = 1
zeit = 0.16
grundgebühr = 1.5


while True:
    wahl = input("Wie willst du deine Rechnung berechnen? (km für Kilometer, Time für Zeit oder 'stop' zum Beenden): ")

    if wahl.lower() == "km":
        # Benutzer gibt eine Zahl ein, die mit kilometer multipliziert wird
        zahl = float(input("Gib deine gefahrene Kilometerzahl ein: "))
        ergebnis = kilometer * zahl + grundgebühr
        print(f"Dein Endbetrag beträgt: {round(ergebnis, 2)}€")

    elif wahl.lower() == "time":
        # Benutzer gibt eine Zahl ein, die mit zeit multipliziert wird
        zahl = float(input("Gib deine gefahrene Zeit in Minuten ein: "))
        ergebnis = zeit * zahl + grundgebühr
        print(f"Dein Endbetrag beträgt: {round(ergebnis, 2)}€")

    elif wahl.lower() == "stop":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Eingabe! Bitte 'km', 'time' oder 'stop' eingeben.")