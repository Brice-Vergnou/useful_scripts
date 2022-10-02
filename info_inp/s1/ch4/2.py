def vabsolue(liste):
    for i in range(len(liste)):
        liste[i]= abs(liste[i])
        
def permutation(liste):
    liste[0], liste[-1] = liste[-1], liste[0]

ma_liste = [-1,45,-56,55,-45,-6345,-5,-9,-6,52145]
vabsolue(ma_liste)
permutation(ma_liste)
print(ma_liste)