from random import randint , random

print("Question 1 \n")

n = randint(0,100)
compteur = 1
print("Vous devez deviner un entier entre 0 et 100")
juste = False
while not juste:
    proposition = int(input("Votre proposition : "))
    if proposition == n:
        juste = True
        print(f"Bravo, vous avez trouvé en {compteur} questions.\n")
    elif proposition > n :
        print("-")
    else :
        print("+")
    compteur += 1
    
    
    
    
    
    
    
print("Question 2 \n")

x = random()
compteur = 1
print("Vous devez deviner un réel entre 0 et 1 à 10**-2 près")
juste = False
while not juste:
    proposition = float(input("Votre proposition : "))
    if x-1e-2 <= proposition <= x+1e-2:
        juste = True
        print(f"Bravo, vous avez trouvé en {compteur} questions.\n")
    elif proposition > x + 1e-2 :
        print("-")
    else :
        print("+")
    compteur += 1