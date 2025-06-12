import time

sekundy = int(input("Zadej počet sekund k odpočítání: "))

while sekundy > 0:
    print(f"Zbývá {sekundy} sekund...")
    time.sleep(1)  # počkej 1 sekundu
    sekundy -= 1

print("Čas vypršel!")