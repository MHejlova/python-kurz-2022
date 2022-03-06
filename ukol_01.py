baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input ("Jaky je kod baliku?")

if kod_baliku in baliky:
    print(f"Balik {kod_baliku} byl predan kuryrovi {baliky[kod_baliku]}.")
else:
    print(f"Balik {kod_baliku} zatim nebyl predan kuryrovi.")