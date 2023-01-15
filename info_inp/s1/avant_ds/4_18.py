def tri(L):
    to_sort = 1
    while to_sort < len(L):
        i = to_sort
        while i > 0:
            if L[i -1] > L[i]:
                L[i-1], L[i] = L[i],L[i-1]
            i -=1
        to_sort +=1

L = [ 5, 2, 1, 4, 8]
tri(L)
print(L)