import time

print("Stopky - ovládání: 'start', 'pauza', 'reset', 'konec'")

start_time = 0
elapsed = 0
running = False

while True:
    cmd = input("Zadej příkaz: ").lower()
    if cmd == "start":
        if not running:
            start_time = time.time() - elapsed
            running = True
            print("Stopky spuštěny.")
        else:
            print("Stopky už běží.")
    elif cmd == "pauza":
        if running:
            elapsed = time.time() - start_time
            running = False
            print(f"Stopky pozastaveny na {elapsed:.2f} sekundách.")
        else:
            print("Stopky nejsou spuštěny.")
    elif cmd == "reset":
        start_time = time.time()
        elapsed = 0
        if running:
            print("Stopky resetovány a běží dál.")
        else:
            print("Stopky resetovány.")
    elif cmd == "konec":
        print("Stopky ukončeny.")
        break
    else:
        print("Neznámý příkaz.")
    
    if running:
        current = time.time() - start_time
    else:
        current = elapsed
    print(f"Čas: {current:.2f} sekund")