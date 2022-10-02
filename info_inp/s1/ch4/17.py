
def indice_min(L, debut):
    min_val = L[debut]
    min_indice = debut
    for i in range(debut+1, len(L)):
        if L[i]< min_val:
            min_val = L[i]
            min_indice = i
    return min_indice

def echange(l, i, j):
    l[i], l[j] = l[j], l[i]
    
def tri_selection(l):
    n = len(l)
    total_sorted = 0
    while total_sorted < n:
        print(l)
        to_sort = indice_min(l, total_sorted)
        echange(l, total_sorted,  to_sort)
        total_sorted += 1

L = [6, 5, 3, 6, 5, 99, -6, 56]
tri_selection(L)
print(L)