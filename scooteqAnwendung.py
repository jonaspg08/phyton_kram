kilometer = 1
zeit = 6


while True:
    wahl = input("Welche Variable soll verwendet werden? (kilometer oder zeit, 'stop' zum Beenden): ")

    if wahl == "kilometer":
        # Benutzer gibt eine Zahl ein, die mit kilometer multipliziert wird
        zahl = float(input("Gib deine gefahrene Kilometerzahl ein: "))
        ergebnis = kilometer * zahl
        print(f"Dein Endbetrag beträgt: {ergebnis}€")

    elif wahl == "zeit":
        # Benutzer gibt eine Zahl ein, die mit zeit multipliziert wird
        zahl = float(input("Gib deine gefahrene Zeit in Minuten ein: "))
        ergebnis = zeit * zahl
        print(f"Dein Endbetrag beträgt: {ergebnis}€")

    elif wahl == "stop":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Eingabe! Bitte 'kilometer', 'zeit' oder 'exit' eingeben.")