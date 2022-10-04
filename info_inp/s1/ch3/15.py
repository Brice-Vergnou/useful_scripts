def somme_f(n,f):
    s = 0
    for i in range(1,n+1):
        s+= f(i)
    return s

def indice_somme(m,f):
    n = 1
    while somme_f(n, f)< m:
        n+=1
    return n




f = lambda x:x
print(somme_f(3,f))
print(indice_somme(7, f))
