def tri_bulles(L):
    a_ete_trie = True
    while a_ete_trie:
        i=0
        a_ete_trie = False
        while i+1< len(L):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1],L[i]
                a_ete_trie = True
            i+=1
            
L = [5, 2, 4, 1, 8, 3, 10, 1, 0]
tri_bulles(L)
print(L)
            