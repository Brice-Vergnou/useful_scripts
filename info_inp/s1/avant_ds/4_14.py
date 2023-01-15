nb_ligne = 1
ligne = [1, 1]

n = int(input("Ligne à afficher : "))
while nb_ligne < n :
    print(ligne)
    new_line = []
    for i in range(len(ligne) - 1):
        new_line.append(ligne[i] + ligne[i+1])
    ligne = [1] + new_line + [1]
    nb_ligne += 1
print(ligne)