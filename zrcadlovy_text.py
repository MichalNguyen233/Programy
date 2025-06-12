print("Zrcadlový text (napiš 'konec' pro ukončení)\n")

while True:
    text = input("Zadej text: ")
    if text.lower() == "konec":
        break
    zrcadlo = text[::-1]
    print("→", zrcadlo)
    
    if input("Uložit do souboru? (ano/ne): ").lower() == "ano":
        with open("zrcadlo.txt", "a", encoding="utf-8") as f:
            f.write(f"{text} -> {zrcadlo}\n")
        print("Uloženo.\n")
    else:
        print()