import random

možnosti = ["kámen", "nůžky", "papír"]

print("=== Kámen, nůžky, papír ===")

while True:
    uzivatel = input("Zadej kámen, nůžky nebo papír (nebo 'konec' pro ukončení): ").lower()
    if uzivatel == "konec":
        break
    if uzivatel not in možnosti:
        print("Neplatná volba.")
        continue

    pocitac = random.choice(možnosti)
    print(f"Počítač vybral: {pocitac}")

    if uzivatel == pocitac:
        print("Remíza!")
    elif (uzivatel == "kámen" and pocitac == "nůžky") or (uzivatel == "nůžky" and pocitac == "papír") or (uzivatel == "papír" and pocitac == "kámen"):
        print("Vyhrál(a) jsi")
    else:
        print("Prohrál(a) jsi")

    if input("\nChceš hrát znovu? (ano/ne): ").lower() != "ano":
        break

print("Díky za hru")