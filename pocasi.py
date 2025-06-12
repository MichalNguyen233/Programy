počasí = {
    "Praha": {"teplota": 22, "stav": "slunečno"},
    "Brno": {"teplota": 20, "stav": "polojasno"},
    "Ostrava": {"teplota": 18, "stav": "déšť"},
    "Plzeň": {"teplota": 21, "stav": "oblačno"},
}

print("=== Jednoduchý počasí program ===")
print("Města:", ", ".join(počasí.keys()))

while True:
    mesto = input("Zadej město (nebo 'konec' pro ukončení): ")
    if mesto.lower() == "konec":
        break
    if mesto in počasí:
        info = počasí[mesto]
        print(f"Počasí v {mesto}: {info['teplota']}°C, {info['stav']}\n")
    else:
        print("Město není v databázi.\n")