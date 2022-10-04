def ppcm(a,b):
    n = 1
    while True: # Pas joli mais on sait qu'on va tomber sur a*b
        if n/a == int(n/a) and n/b == int(n/b):
            return n
        n += 1

print(ppcm(3,6))