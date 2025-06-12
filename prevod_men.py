kurzy = {"Kč":1, "EUR":24.5, "USD":22.3}
print("Převodník měn (Kč, EUR, USD), 'konec' pro ukončení.")

while True:
    zdroj = input("Zdrojová měna: ").strip()
    if zdroj.lower() == "konec": break
    cil = input("Cílová měna: ").strip()
    if cil.lower() == "konec": break
    if zdroj not in kurzy or cil not in kurzy:
        print("Neznámá měna, zkus znovu."); continue
    try:
        castka = float(input("Částka: "))
    except:
        print("Neplatná částka."); continue
    vysledek = castka * kurzy[zdroj] / kurzy[cil]
    print(f"{castka} {zdroj} = {vysledek:.2f} {cil}\n")