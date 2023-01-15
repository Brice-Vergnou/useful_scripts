# -*- coding: utf-8 -*-

"""
print("Question 1 \n")
print('Je vais deviner l\'entier entre 0 et 100 auquel vous pensez')

feedback = None
guess = 50
compteur = 1
sup = 101
inf = 0

while feedback != "=":
    feedback = input(f"Est-ce {guess} ? ")
    if feedback == "-":
        sup = guess
        guess = (guess + inf) //2
        compteur += 1
    elif feedback == "+":
        inf = guess
        guess = (guess + sup) //2
        compteur += 1

        
print(f"J'ai trouvé en {compteur} questions.")
"""

print("Question 2 \n")
print('Je vais deviner un réel entre 0 et 1 auquel vous pensez\ (à 10**-2 près)')

feedback = None
guess = 0.5
compteur = 1
sup = 1.01
inf = 0

while feedback != "=":
    feedback = input(f"Est-ce {guess} ? ")
    if feedback == "-":
        sup = guess
        guess = round((guess + inf) /2,2)
        compteur += 1
    elif feedback == "+":
        inf = guess
        guess = round((guess + sup) /2,2)
        compteur += 1

        
print(f"J'ai trouvé en {compteur} questions.")