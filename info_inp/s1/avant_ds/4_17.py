def indice_min(L, debut):
    indice = debut
    valeur_min = L[debut]
    for i in range(debut +1, len(L)):
        if L[i] < valeur_min:
            valeur_min = L[i]
            indice = i
    return indice

def echange(L, i, j):
    L[i], L[j] = L[j], L[i]
    return None

def tri_selection(L):
    i = 0
    while i < len(L):
        j = indice_min(L, i)
        echange(L, i, j)
        i += 1
    return None

L = [5,8,2,5,4,9,3,0]
tri_selection(L)
print(L)

print(int(int(input())*(1.1**int(input()))))
print(int(int(input())*1.1**int(input())))
