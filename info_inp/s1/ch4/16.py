from random import randint

n = 10000
resultats = []
for _ in range(n):
    resultats.append(randint(1,6) + randint(1,6))

loi = [] # représente les lois de X allant de 2 à 12, on aurait pu utiliser un dict
for i in range(2,13):
    loi.append(resultats.count(i) / len(resultats))
    
print(loi)
print(f"L'espérance de la loi de X est d'environ {sum([(n+2)*prob for n, prob in enumerate(loi)])}")