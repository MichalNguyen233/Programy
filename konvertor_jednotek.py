print("Vyber převod:\n1) km → míle\n2) míle → km\n3) kg → libry\n4) libry → kg\n5) °C → °F\n6) °F → °C")
v = input("Zadej číslo (1–6): ")

x = float(input("Zadej hodnotu: "))

if v == "1": print(f"{x} km = {x * 0.621371:.2f} mil")
elif v == "2": print(f"{x} mil = {x / 0.621371:.2f} km")
elif v == "3": print(f"{x} kg = {x * 2.20462:.2f} lb")
elif v == "4": print(f"{x} lb = {x / 2.20462:.2f} kg")
elif v == "5": print(f"{x} °C = {(x * 9/5) + 32:.2f} °F")
elif v == "6": print(f"{x} °F = {(x - 32) * 5/9:.2f} °C")
else: print("Neplatná volba.")