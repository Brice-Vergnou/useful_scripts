def bin2int(mot_bin):
    i = 0
    somme = 0
    for c in mot_bin[::-1]:
        if int(c) == 1:
            somme += 2**i
        i+=1
    return somme

def int2bin(entier):
    chaine = ""
    while entier > 0:
        entier, r = entier //2, entier%2
        chaine = str(r) + chaine
    return chaine



print(bin2int('10011101'))
print(int2bin(6))