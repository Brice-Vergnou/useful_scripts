def bin2int(mot_bin):
    s = 0
    for i, digit in enumerate(mot_bin[::-1]):
        s+= int(digit) * 2**i
    return s

def int2bin(entier):
    mot_bin = ""
    continuer = True
    while entier != 0:
        entier,r = entier//2, entier%2
        mot_bin = str(r) + mot_bin
    return mot_bin
        