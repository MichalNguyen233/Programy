import calendar

print("=== Kalendář ===")

while True:
    try:
        rok = int(input("Zadej rok (např. 2025): "))
        mesic = int(input("Zadej měsíc (1-12): "))
        if 1 <= mesic <= 12:
            break
        else:
            print("Měsíc musí být mezi 1 a 12.")
    except ValueError:
        print("Zadej platné číslo.")

print(f"\nKalendář pro {mesic}.{rok}:\n")
print(calendar.month(rok, mesic))

# Další informace
pocet_dnu = calendar.monthrange(rok, mesic)[1]
print(f"Měsíc má {pocet_dnu} dní.")
den_v_tydnu = calendar.monthrange(rok, mesic)[0]
dny = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']
print(f"První den měsíce je: {dny[den_v_tydnu]}")