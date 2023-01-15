def insert_sort(L):
    last_sorted = 0
    long = len(L)
    while last_sorted < long - 1:
        n = last_sorted
        while L[n+1] < L[n] and n >= 0: # Tq n+1 est plus grand et qu'on est ds la liste
            L[n+1], L[n] = L[n], L[n+1] # On 'amène' n+1 vers le début
            n-=1
            
        last_sorted += 1

L = [5, 2, 1, 4 ,0 ,-9 , 5 ,8]
insert_sort(L)
print(L)