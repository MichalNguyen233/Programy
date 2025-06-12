import time

print("Sledování času u PC")
print("Stiskni Enter, když začneš, a zase Enter, až skončíš.")
print("Napiš 'konec', až budeš chtít ukončit.")

celkovy_cas = 0

while True:
    start = input("Stiskni Enter pro start nebo 'konec' pro ukončení: ")
    if start.lower() == "konec":
        break
    start_cas = time.time()
    input("Stiskni Enter pro zastavení měření: ")
    end_cas = time.time()
    rozdil = end_cas - start_cas
    celkovy_cas += rozdil
    print(f"Čas této seance: {rozdil:.2f} sekund\n")

print(f"Celkový čas strávený u PC: {celkovy_cas:.2f} sekund")