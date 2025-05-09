print("=== Kalkulačka ===")
a = float(input("První číslo: "))
b = float(input("Druhé číslo: "))
op = input("Zadej operaci (+, -, *, /): ")

if op == "+":
    print("Výsledek:", a + b)
elif op == "-":
    print("Výsledek:", a - b)
elif op == "*":
    print("Výsledek:", a * b)
elif op == "/":
    if b != 0:
        print("Výsledek:", a / b)
    else:
        print("Chyba: dělení nulou!")
else:
    print("Neplatná operace.")
