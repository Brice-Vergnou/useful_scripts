def tri_a_bulle(L):
    changed = True
    while changed:
        changed = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                changed = True
    
L = [5, 2, 1, 4 ,0 ,-9 , 5 ,8]
tri_a_bulle(L)
print(L)