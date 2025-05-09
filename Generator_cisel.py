import random

print("=== Generátor náhodných čísel ===")

while True:
    od = int(input("Z jakého čísla (od): "))
    do = int(input("Do jakého čísla (do): "))
    pocet = int(input("Kolik čísel chceš: "))

    cisla = [random.randint(od, do) for _ in range(pocet)]
    print("Vygenerovaná čísla:", cisla)
    print("Nejmenší:", min(cisla), "| Největší:", max(cisla), "| Průměr:", round(sum(cisla)/len(cisla), 2))

    if input("Chceš pokračovat? (ano/ne): ").lower() != "ano":
        break