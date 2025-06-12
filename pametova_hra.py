import random, time

print("Paměťová hra - napiš 'konec' pro ukončení.")

while True:
    d = input("Délka sekvence: ")
    if d.lower() == "konec":
        break
    if not d.isdigit() or int(d) < 1:
        print("Zadej kladné číslo.")
        continue

    d = int(d)
    seq = [str(random.randint(0,9)) for _ in range(d)]
    print("Zapamatuj si:", ' '.join(seq))
    time.sleep(d+1)
    print("\n" * 30)

    pokus = input("Napiš sekvenci: ")
    if pokus.lower() == "konec":
        break

    if pokus.split() == seq:
        print("Správně! 🎉\n")
    else:
        print("Špatně, bylo to:", ' '.join(seq), "\n")