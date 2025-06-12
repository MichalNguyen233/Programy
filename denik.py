from datetime import datetime

print("=== Jednoduchý deník ===")
print("Napiš 'konec' pro ukončení.")

while True:
    poznamka = input("Napiš poznámku: ")
    if poznamka.lower() == "konec":
        print("Deník ukončen.")
        break
    
    cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("denik.txt", "a", encoding="utf-8") as soubor:
        soubor.write(f"[{cas}] {poznamka}\n")
    print("Poznámka uložena.\n")