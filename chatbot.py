import time

def odpovez(vstup):
    vstup = vstup.lower()

    if "ahoj" in vstup or "čau" in vstup:
        return "Ahoj! Jak ti mohu pomoci?"
    elif "jak se máš" in vstup:
        return "Mám se skvěle, díky za optání!"
    elif "kolik je hodin" in vstup:
        return "Je právě " + time.strftime("%H:%M")
    elif "kdo jsi" in vstup:
        return "Jsem jednoduchý chatbot v Pythonu 🙂"
    elif "dík" in vstup or "děkuju" in vstup:
        return "Není zač!"
    else:
        return "To zatím neumím pochopit."

print("🤖 Ahoj! Jsem chatbot. Piš mi, nebo napiš 'konec' pro ukončení.")

while True:
    user = input("Ty: ")
    if user.lower() == "konec":
        print("Chatbot: Měj se hezky! 👋")
        break
    print("Chatbot:", odpovez(user))