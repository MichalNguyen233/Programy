# Proměnné
#### součet = a + b - (**sčítání**)
#### rozdíl = a - b - (**odčítání**)
#### součín = a * b - (**násobení**)
#### dělení = a / b - (**dělení**)
#### mocnina = a ** b - (**Umocnění**)
### x = 10 # _celá čísla_
### y = 3.14 # _desetinná čísla_
### name = "petr" # _text (string)_
# Aritmetické operace 
### () - **závorky**
### ** - **Mocnina**
### *, /, //, % - **násobení a dělení**
### +, - - sčítání a odčítání 
| Operace |  příklad  | výsledek |
| ------- | --------- | -------- |
|sčítání  |   5 += 3  |     8    |
|odčítání |   5 -= 3  |     2    |
|násobení |   5 *= 3  |    15    |
|dělení   |   5 /= 3  |  1.6667  |
|celé dělení| 5 //= 3 |     1    |
|zbytek po dělení| 5 %= 3 | 2    |
|mocnina| 5 **= 3     |    125   |
# Podmínky a logické operace
### x = 10
### y = 5
#### if x > y: 
    print ("x je větší než y")
#### elif x == y:
    print("x je rovno y")
#### else:
    print("x je větší než y")
+ and (a zároveň)
+ or (nebo)
+ not (negace)
### a = true
### b = false
#### if a and b:
    print("obě podmínky jsou pravdivé")
#### if a or b:
    print("alespoň jedna podmínka je pravdivá")
#### id not b:
    print("b je nepravdivé")
+ == (rovnost)
+ != (nerovnost)
+ (>) (větší než)
+ (<) (menší než)
+ (>=) (větší nebo rovno)
+ (<=) (menší nebo rovno)
### x = 15
### y = 20
#### if x != y:
    print("x a y nejsou stejná čísla")
# Cykly
#### for i in range(5): # 0, 1, 2, 3, 4
    print(i) # 0, 1, 2, 3, 4
### x = 0
#### while x < 5:
    print(x)
    x+= 1 
# Funkce
#### print("hello world")
#### seznam = [1, 2, 3,]
    print(len(seznam)) # výstup: 3
#### text = "hello"
    print(text.upper()) # výstup: HELLO
#### text = "hello"
    print(text.strip()) # výstup: hello
#### text = "hello world"
    print(text.replace("world, Python)) # výstup: hello Python
#### text = "hello world" 
#### seznam = text.split(" ")
    print(seznam) # výstup: ['hello, world']
#### seznam = [3, 2, 1]
#### seznam.sort()
    print(seznam) # výstup: [1, 2, 3,]
#### for i in range(5)
    print(i) # výstup: 0, 1, 2, 3, 4,
### i = 0
#### while i < 3:
    print(i)
    i += 1 # výstup: 0, 1, 2 
#### def pozdrav(jméno)
    print(f"ahoj, {jméno}!")
    pozdrav("Petr") # výstup: ahoj Petr!
# Výstupy
#### jméno = input("zadejte své jméno: ")
    print(f"ahoj, {jméno}!")
#### věk = int(input("zadejte svůj věk: "))
    print(f"za rok vám bude {věk + 1}.")
#### print("Text")
#### print("Více, položek", sep=",")
#### print("Bez nového řádku", end="")
    # výstup: text
              Text
              Více, položek
              Bez nového řádku
# Vstupy
#### proměnná = input("zadejte hodnotu")
    # výstup: závisí na uživatelském vstupu
#### jméno = input("Alice")
#### print = ("Ahoj,", Alice)
#### věk = int(input("25"))
#### print(f"za 5 let vám bude {věk + 5} let")
    # výstup: Ahoj, Alice
            věk 25
            za 5 let vám bude 30