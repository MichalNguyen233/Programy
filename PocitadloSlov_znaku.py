text = input("Zadej text: ")

znaky = len(text)
slova = len(text.split())
mezery = text.count(" ")

samohlasky = 0
souhlasky = 0
ceske_samohlasky = "aeiouyáéíóúůýě"

for znak in text.lower():
    if znak.isalpha():
        if znak in ceske_samohlasky:
            samohlasky += 1
        else:
            souhlasky += 1

print("\n--- Výsledky ---")
print(f"Počet znaků: {znaky}")
print(f"Počet slov: {slova}")
print(f"Počet mezer: {mezery}")
print(f"Počet samohlásek: {samohlasky}")
print(f"Počet souhlásek: {souhlasky}")