from random import randint, random

number = randint(0,100)
print("Vous devez deviner un nombre entre 0 et 100")
guess_count = 1


guess = None
while guess != number:
    guess = int(input("Votre proposition : "))
    if guess > number :
        print("-")
        guess_count += 1
    elif guess < number :
        print("+")
        guess_count += 1
    else :
        print(f"Bravo, vous avez trouvé en {guess_count} questions.")


number = random()
guess_count = 1
guess = 2
print("Vous devez deviner un réel entre 0 et 1 à 10**-2 près")
while abs(number - guess) > 10**-2:
    guess = float(input("Votre proposition : "))
    if guess > number :
        print("-")
        guess_count += 1
    elif guess < number :
        print("+")
        guess_count += 1
print(f"Bravo, vous avez trouvé en {guess_count} questions.")
